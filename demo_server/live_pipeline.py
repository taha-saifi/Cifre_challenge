#!/usr/bin/env python3
"""Run the existing extraction pipeline over the live workspace, writing to live_kg/.

Reuse, not reimplementation: the stage functions called here are exactly the ones
`extraction_pipeline/scripts/run_pipeline.py` calls. They take no arguments and read every
path from `config`, so the only way to retarget them is to rebind those paths -- which is
done under a lock and always restored, so a live run can never write into
`extraction_pipeline/`.

What is displayed is the OPEN KG, not the canonical one, and that is a deliberate
consequence of the project's own rule: nothing becomes canonical without a human accepting
its relation cluster. Human validation is out of scope here, so the canonical graph would
be empty by construction. Showing the open graph and labelling it *pre-validation* is the
honest option; silently relabelling it "canonical" would contradict the whole method.
"""
from __future__ import annotations

import contextlib
import json
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPELINE_SCRIPTS = ROOT / "extraction_pipeline" / "scripts"
sys.path.insert(0, str(PIPELINE_SCRIPTS))

# pipeline_lib puts extraction_pipeline/ on sys.path itself, so it must be imported
# before `config` becomes resolvable.
import pipeline_lib  # noqa: E402
import config  # noqa: E402

LIVE_KG = ROOT / "live_kg"
LIVE_CORPUS_CLEAN = ROOT / "live_corpus" / "clean"

# config is process-global; serialise live runs so two requests cannot interleave.
_LOCK = threading.Lock()

REDIRECTED = ("CORPUS_DIR", "DATA_DIR", "OPEN_KG_DIR", "CLUSTER_DIR",
              "CANONICAL_KG_DIR", "EVALUATION_DIR", "REPORTS_DIR", "LOG_DIR")
# Saved and restored alongside the paths.
ALSO_SAVED = ("OPENIE_BACKEND",)


def minie_available() -> bool:
    """One cheap probe. Left as `minie` when the service is down, extract_openie retries
    MinIE once per batch AND once per sentence -- hundreds of socket attempts for a single
    long page, which is what makes an ingestion look hung. Probing once and configuring the
    backend to what actually exists is the correct setup, not a shortcut."""
    response, _failure = pipeline_lib.minie_service_response("Test sentence.")
    return response is not None


@contextlib.contextmanager
def redirected_config():
    """Point every pipeline output at live_kg/ for the duration of the run."""
    original = {name: getattr(config, name) for name in REDIRECTED + ALSO_SAVED}
    try:
        config.CORPUS_DIR = LIVE_CORPUS_CLEAN
        for name in REDIRECTED:
            if name == "CORPUS_DIR":
                continue
            target = LIVE_KG / name.replace("_DIR", "").lower()
            target.mkdir(parents=True, exist_ok=True)
            setattr(config, name, target)
        config.OPENIE_BACKEND = "minie" if minie_available() else "heuristic"
        yield
    finally:
        for name, value in original.items():
            setattr(config, name, value)


def run() -> dict:
    """Extract → resolve → build open KG over the live corpus. Returns a summary."""
    with _LOCK, redirected_config():
        backend_used = config.OPENIE_BACKEND
        # Same order as run_pipeline.py, stopping before clustering: the stages after
        # build_open_kg exist to feed the human validation gate, which is out of scope.
        structured = pipeline_lib.extract_structured()
        openie = pipeline_lib.extract_openie()
        pipeline_lib.extract_entities()
        entities = pipeline_lib.resolve_entities()
        nodes, edges = pipeline_lib.build_open_kg()

        metadata_path = config.DATA_DIR / "openie_run_metadata.json"
        backends = {}
        if metadata_path.exists():
            with metadata_path.open(encoding="utf-8") as handle:
                backends = json.load(handle).get("actual_backends", {})

    return {
        "sources": len(list(LIVE_CORPUS_CLEAN.glob("S*.json"))),
        "structured_assertions": len(structured),
        "openie_assertions": len(openie),
        "entities": len(entities),
        "nodes": len(nodes),
        "edges": len(edges),
        "backends": backends,
        "openie_backend": backend_used,
        "minie_available": backend_used == "minie",
        # The visualised graph is pre-validation by construction -- see module docstring.
        "graph_stage": "open_kg (pré-validation, aucune validation humaine appliquée)",
    }


def graph_payload(max_edges: int = 400, stage: str = "open_kg") -> dict:
    """Shape a live_kg stage for vis-network, keeping provenance on every edge.

    stage="open_kg"      -> everything extracted, pre-validation
    stage="canonical_kg" -> only what survived cluster validation
    """
    edges_path = LIVE_KG / stage / "edges.json"
    nodes_path = LIVE_KG / stage / "nodes.json"
    if not edges_path.exists():
        return {"nodes": [], "edges": [], "truncated": False, "total_edges": 0,
                "stage": stage}

    with edges_path.open(encoding="utf-8") as handle:
        raw_edges = json.load(handle)
    with nodes_path.open(encoding="utf-8") as handle:
        raw_nodes = json.load(handle)

    labels = {n["entity_id"] if "entity_id" in n else n["id"]:
              n.get("canonical_label") or n.get("label", "") for n in raw_nodes}
    types = {n["entity_id"] if "entity_id" in n else n["id"]:
             n.get("entity_type", "") for n in raw_nodes}

    kept = raw_edges[:max_edges]
    used = {e["source"] for e in kept} | {e["target"] for e in kept}
    degree: dict[str, int] = {}
    for edge in kept:
        for endpoint in (edge["source"], edge["target"]):
            degree[endpoint] = degree.get(endpoint, 0) + 1

    nodes = [{
        "id": node_id,
        "label": (labels.get(node_id) or "")[:42],
        "title": f"{labels.get(node_id, '')}\n[{types.get(node_id, '')}]",
        "value": degree.get(node_id, 1),
        "group": types.get(node_id, "Mention"),
    } for node_id in used]

    edges = [{
        "id": edge["edge_id"],
        "from": edge["source"],
        "to": edge["target"],
        "label": (edge.get("predicate_canonical") or edge["predicate_raw"])[:34],
        # Provenance travels to the click handler: source id, method and evidence text.
        "source_id": edge["source_id"],
        "source_url": edge.get("source_url") or "",
        "method": edge.get("extraction_method", ""),
        "evidence": edge.get("evidence", ""),
        "predicate": edge.get("predicate_canonical") or edge["predicate_raw"],
        "predicate_raw": edge["predicate_raw"],
        "subject": labels.get(edge["source"], ""),
        "object": labels.get(edge["target"], ""),
    } for edge in kept]

    return {"nodes": nodes, "edges": edges, "stage": stage,
            "truncated": len(raw_edges) > max_edges, "total_edges": len(raw_edges)}
