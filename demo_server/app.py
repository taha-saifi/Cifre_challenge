#!/usr/bin/env python3
"""Local exploration server: one question, five configurations, answers side by side.

Scope note. This is the 40-minute discussion tool, NOT the scripted 3-minute demo.
`deliverables/demo.html` stays the scripted demonstration: it is static, offline, already
tested, and carries no live-call risk. This server exists for the case the static page
cannot handle -- a question the jury invents on the spot.

Runs on 127.0.0.1 only. The single outbound dependency is the model call itself.
"""
from __future__ import annotations

import concurrent.futures
import sys
import traceback
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import configs  # noqa: E402
import live_ingest  # noqa: E402
import live_pipeline  # noqa: E402
import live_validate  # noqa: E402
import model_client  # noqa: E402

app = Flask(__name__, static_folder=str(HERE / "static"))

# Each configuration runs in its own thread: five sequential model calls would make the
# page feel broken during a live discussion.
MAX_WORKERS = 5


@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.get("/live")
def live_page():
    """Ingestion + visualisation. Separate page: it does not touch demo_kg."""
    return send_from_directory(app.static_folder, "live.html")


@app.post("/api/ingest")
def ingest():
    """Scrape/read the submitted sources, run the pipeline, return statuses + graph.

    A failure on one source degrades that source only; the request still returns 200 with
    per-source statuses so the page can render what worked.
    """
    urls = [u for u in (request.form.get("urls") or "").splitlines() if u.strip()]
    files = []
    for storage in request.files.getlist("files"):
        if storage and storage.filename:
            files.append((storage.filename, storage.read()))
    if not urls and not files:
        return jsonify({"error": "aucune source fournie"}), 400

    statuses = live_ingest.ingest(urls, files)
    ok = [s for s in statuses if s.get("status") == "ok"]
    if not ok:
        return jsonify({"sources": statuses, "summary": None, "graph": None,
                        "error": "aucune source exploitable"}), 200

    try:
        summary = live_pipeline.run()
        graph = live_pipeline.graph_payload()
    except Exception as exc:  # noqa: BLE001 - extraction failure must not break the page
        return jsonify({"sources": statuses, "summary": None, "graph": None,
                        "error": f"extraction : {type(exc).__name__}: {exc}"}), 200

    return jsonify({"sources": statuses, "summary": summary, "graph": graph})


@app.get("/api/candidates")
def candidates():
    """Relation clusters awaiting a decision, with their evidence."""
    try:
        return jsonify(live_validate.build_candidates())
    except Exception as exc:  # noqa: BLE001
        return jsonify({"error": f"{type(exc).__name__}: {exc}", "candidates": []}), 200


@app.post("/api/validate")
def validate():
    """Apply per-cluster decisions and rebuild the session's canonical graph.

    An empty `decisions` with auto_default=true is the zero-interaction path: one call,
    no clicks, everything left to the pipeline's own guardrails.
    """
    body = request.get_json(force=True, silent=True) or {}
    decisions = body.get("decisions") or {}
    auto_default = body.get("auto_default", True)
    try:
        summary = live_validate.apply_decisions(decisions, bool(auto_default))
        return jsonify({"summary": summary, "graph": live_validate.canonical_graph()})
    except Exception as exc:  # noqa: BLE001
        return jsonify({"error": f"{type(exc).__name__}: {exc}",
                        "summary": None, "graph": None}), 200


@app.get("/api/live_graph")
def live_graph():
    return jsonify(live_pipeline.graph_payload())


@app.get("/api/pivots")
def pivots():
    """Entities that actually anchor edges in demo_kg, most connected first."""
    source = request.args.get("source", "demo_kg")
    return jsonify({"pivots": configs.available_pivots(source),
                    "configs": configs.CONFIG_LABELS,
                    "source": source,
                    "sources": {k: {"label": v["label"],
                                    "available": configs.graph_available(k)}
                                for k, v in configs.GRAPH_SOURCES.items()},
                    "model_ready": model_client.have_key()})


def run_one(config: str, question: str, pivots_list: list, ablate: bool,
            anchors: list, source: str = "demo_kg") -> dict:
    """Run a single configuration. Never raises -- failures become a displayable state."""
    result = {"config": config, "label": configs.CONFIG_LABELS.get(config, config)}
    try:
        context, diagnostics = configs.build_context(config, question, pivots_list,
                                                     ablate, anchors, source)
        result["diagnostics"] = diagnostics
        result["context_chars"] = len(context)
        prompt = configs.build_prompt(question, context)

        completion = model_client.chat(prompt)
        result["answer"] = completion["text"]
        result["raw_answer"] = completion.get("raw", completion["text"])
        result["cleaned"] = completion.get("raw") != completion["text"]
        result["model"] = completion["model"]
        result["attempts"] = completion["attempts"]
        # Both are shown, never one instead of the other: `parsed` is what the model says
        # it relied on (which can be wrong while sounding right), `grounding` is the
        # mechanical check against the exact context it was given.
        result["parsed"] = configs.parse_answer(completion["text"])
        result["grounding"] = configs.grounding(completion["text"], context)
        result["status"] = "ok"
    except model_client.ModelUnavailable as exc:
        result["status"] = "unavailable"
        result["error"] = str(exc)
    except Exception as exc:  # noqa: BLE001 - a broken config must not break the page
        result["status"] = "error"
        result["error"] = f"{type(exc).__name__}: {exc}"
        result["trace"] = traceback.format_exc(limit=3)
    return result


@app.post("/api/run")
def run():
    body = request.get_json(force=True, silent=True) or {}
    question = (body.get("question") or "").strip()
    if not question:
        return jsonify({"error": "question vide"}), 400

    selected = body.get("configs") or ["c1", "c2", "c4", "c5", "c8"]
    source = body.get("source", "demo_kg")
    pivots_list = body.get("pivots") or []
    ablate = bool(body.get("ablate"))
    # Anchors default to the pivots: the fact under test is the one relating them.
    anchors = body.get("anchors") or pivots_list

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(run_one, c, question, pivots_list, ablate, anchors, source): c
                   for c in selected}
        results = []
        for future in concurrent.futures.as_completed(futures):
            try:
                results.append(future.result())
            except Exception as exc:  # noqa: BLE001
                results.append({"config": futures[future], "status": "error",
                                "error": f"{type(exc).__name__}: {exc}"})

    order = {c: i for i, c in enumerate(selected)}
    results.sort(key=lambda r: order.get(r["config"], 99))
    return jsonify({"question": question, "pivots": pivots_list, "source": source,
                    "ablate": ablate, "results": results})


if __name__ == "__main__":
    if not model_client.have_key():
        print("ATTENTION : OPENROUTER_API_KEY absent de .env — "
              "les colonnes afficheront « configuration indisponible ».")
    print("Explorateur KG        ->  http://127.0.0.1:5000")
    print("Ingestion + graphe    ->  http://127.0.0.1:5000/live")
    app.run(host="127.0.0.1", port=5000, debug=False)
