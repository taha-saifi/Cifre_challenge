#!/usr/bin/env python3
"""The five configurations, built by reusing the experiment code rather than reimplementing it.

Reused, not rewritten:
  * the sub-graph filter and the `sujet prédicat objet [source: Sxx]` rendering are the
    same logic as `experiments/build_contexts.py`;
  * carrier detection is `experiments/carrier_check.py:find_carriers` verbatim -- the
    "remove the principal carrier" checkbox calls it instead of naming an edge by hand;
  * the grounding metric is `experiments/score.py:verifiable_tokens` verbatim.

The decision prompt is assembled identically for all five configurations. Only the
context block changes -- that is the whole methodological contract, and it is enforced
here by construction: `build_prompt()` has one template and every configuration goes
through it.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEMO_KG = ROOT / "demo_kg"
sys.path.insert(0, str(ROOT / "experiments"))

import carrier_check  # noqa: E402  (experiments/carrier_check.py)
import score as score_module  # noqa: E402  (experiments/score.py)

CONFIG_LABELS = {
    "c1": "1 — LLM seul",
    "c2": "2 — RAG documentaire",
    "c4": "4 — KG-aware complet",
    "c5": "5 — KG incomplet",
    "c8": "8 — KG incomplet + signalement",
}

GAP_NOTICE = ("Note : une information potentiellement pertinente n'a pas pu être "
              "confirmée avec certitude dans les sources disponibles.")

HEADERS = {
    "c4": "Informations disponibles (sous-graphe canonical KG actuel) :",
    "c5": "Informations disponibles (sous-graphe canonical KG actuel, incomplet) :",
    "c8": "Informations disponibles (sous-graphe canonical KG actuel, incomplet) :",
}


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_graph():
    edges = load_json(DEMO_KG / "edges.json")
    labels = {n["id"]: n["label"] for n in load_json(DEMO_KG / "nodes.json")}
    return edges, labels


def render_edge(edge: dict, labels: dict) -> str:
    """Identical rendering to experiments/build_contexts.py."""
    predicate = "_".join(edge["predicate_canonical"].split())
    return (f"{labels.get(edge['source'], '')} {predicate} "
            f"{labels.get(edge['target'], '')} [source: {edge['source_id']}]")


def subgraph(edges: list, labels: dict, pivots: list) -> list:
    """Identical filter to experiments/build_contexts.py. Edge order preserved."""
    selected = []
    for edge in edges:
        endpoints = labels.get(edge["source"], "") + " " + labels.get(edge["target"], "")
        if any(pivot in endpoints for pivot in pivots):
            selected.append(edge)
    return selected


def available_pivots() -> list[dict]:
    """Entities worth offering as a pivot: those that actually anchor edges in demo_kg."""
    edges, labels = load_graph()
    counts: dict[str, int] = {}
    for edge in edges:
        for endpoint in (labels.get(edge["source"], ""), labels.get(edge["target"], "")):
            for cve in re.findall(r"CVE-\d{4}-\d{4,7}", endpoint):
                counts[cve] = counts.get(cve, 0) + 1
    return [{"id": k, "edges": v} for k, v in sorted(counts.items(), key=lambda kv: -kv[1])]


def principal_carrier_lines(pivots: list, anchors: list) -> tuple[list[str], dict]:
    """Ask carrier_check which edges carry the anchored fact; ablate the Tier-1 set.

    This is the point of the checkbox: the removed edges are computed, never designated
    by hand -- the same guarantee the 45 recorded cells rely on.
    """
    edges, labels = load_graph()
    if not anchors:
        return [], {"tier1": [], "tier2": [], "note": "aucun ancrage fourni"}
    result = carrier_check.find_carriers(edges, labels, anchors, pivots)
    return [c["line"] for c in result["tier1"]], result


def build_context(config: str, question: str, pivots: list, ablate: bool,
                  anchors: list) -> tuple[str, dict]:
    """Return (context_text, diagnostics). Empty context for config 1."""
    if config == "c1":
        return "", {"kind": "aucun contexte"}

    if config == "c2":
        import rag
        context, hits = rag.build_context(question)
        return context, {"kind": "RAG", "passages": len(hits),
                         "sources": sorted({h["source_id"] for h in hits}),
                         "hits": [{"source_id": h["source_id"], "score": round(h["score"], 3),
                                   "excerpt": h["text"][:180]} for h in hits]}

    edges, labels = load_graph()
    selected = subgraph(edges, labels, pivots)
    lines = [render_edge(e, labels) for e in selected]
    diagnostics = {"kind": "KG", "triples": len(lines), "removed": [], "carriers": None}

    if config in ("c5", "c8") and ablate:
        removed, carriers = principal_carrier_lines(pivots, anchors)
        removed_set = set(removed)
        lines = [l for l in lines if l not in removed_set]
        diagnostics["removed"] = removed
        diagnostics["carriers"] = {"tier1": len(carriers["tier1"]),
                                   "tier2": len(carriers["tier2"])}
        diagnostics["triples"] = len(lines)

    context = HEADERS[config] + "\n\n" + "\n".join(lines)
    if config == "c8":
        context += "\n" + GAP_NOTICE
    return context, diagnostics


def build_prompt(question: str, context: str) -> str:
    """One template for every configuration. Only `context` differs."""
    if not context:
        return (f"{question}\n\n"
                "Formule ta réponse en une décision claire suivie de ta justification.")
    return (f"{context}\n\n"
            f"Question : {question}\n\n"
            "Formule ta réponse en une décision claire suivie de ta justification, "
            "en te fondant uniquement sur les informations ci-dessus.")


def grounding(answer: str, context: str) -> dict | None:
    """Reuse score.py's verifiable-token rule. None when nothing checkable was asserted."""
    tokens = score_module.verifiable_tokens(answer)
    if not tokens:
        return None
    haystack = context.lower()
    grounded = {t for t in tokens if t.lower() in haystack}
    return {"grounded": len(grounded), "total": len(tokens),
            "ratio": round(len(grounded) / len(tokens), 2),
            "ungrounded": sorted(tokens - grounded)[:6]}
