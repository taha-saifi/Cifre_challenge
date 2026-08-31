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
import model_client  # noqa: E402

app = Flask(__name__, static_folder=str(HERE / "static"))

# Each configuration runs in its own thread: five sequential model calls would make the
# page feel broken during a live discussion.
MAX_WORKERS = 5


@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.get("/api/pivots")
def pivots():
    """Entities that actually anchor edges in demo_kg, most connected first."""
    return jsonify({"pivots": configs.available_pivots(),
                    "configs": configs.CONFIG_LABELS,
                    "model_ready": model_client.have_key()})


def run_one(config: str, question: str, pivots_list: list, ablate: bool,
            anchors: list) -> dict:
    """Run a single configuration. Never raises -- failures become a displayable state."""
    result = {"config": config, "label": configs.CONFIG_LABELS.get(config, config)}
    try:
        context, diagnostics = configs.build_context(config, question, pivots_list,
                                                     ablate, anchors)
        result["diagnostics"] = diagnostics
        result["context_chars"] = len(context)
        prompt = configs.build_prompt(question, context)

        completion = model_client.chat(prompt)
        result["answer"] = completion["text"]
        result["raw_answer"] = completion.get("raw", completion["text"])
        result["cleaned"] = completion.get("raw") != completion["text"]
        result["model"] = completion["model"]
        result["attempts"] = completion["attempts"]
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
    pivots_list = body.get("pivots") or []
    ablate = bool(body.get("ablate"))
    # Anchors default to the pivots: the fact under test is the one relating them.
    anchors = body.get("anchors") or pivots_list

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(run_one, c, question, pivots_list, ablate, anchors): c
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
    return jsonify({"question": question, "pivots": pivots_list,
                    "ablate": ablate, "results": results})


if __name__ == "__main__":
    if not model_client.have_key():
        print("ATTENTION : OPENROUTER_API_KEY absent de .env — "
              "les colonnes afficheront « configuration indisponible ».")
    print("Explorateur KG  ->  http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)
