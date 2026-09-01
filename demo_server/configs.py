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

import graph_view

ROOT = Path(__file__).resolve().parent.parent
DEMO_KG = ROOT / "demo_kg"
LIVE_CANONICAL = ROOT / "live_kg" / "canonical_kg"

# Two selectable graphs. demo_kg is the frozen, validated projection whose behaviour is
# documented in resultats.md; live_kg is whatever the current session just built and
# validated, at heuristic extraction quality.
GRAPH_SOURCES = {
    "demo_kg": {"dir": DEMO_KG, "label": "demo_kg — projection validée du graphe figé"},
    "live_kg": {"dir": LIVE_CANONICAL, "label": "live_kg — session en cours, qualité heuristique"},
}
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


def graph_dir(source: str) -> Path:
    return GRAPH_SOURCES.get(source, GRAPH_SOURCES["demo_kg"])["dir"]


def graph_available(source: str) -> bool:
    return (graph_dir(source) / "edges.json").exists()


def load_graph(source: str = "demo_kg"):
    directory = graph_dir(source)
    edges_path = directory / "edges.json"
    if not edges_path.exists():
        raise FileNotFoundError(
            f"{source} n'a pas encore de graphe canonique — ingérez des sources puis "
            f"validez les relations sur /live avant d'interroger ce graphe.")
    edges = load_json(edges_path)
    nodes = load_json(directory / "nodes.json")
    # open_kg and canonical_kg name the label field differently in places; accept both.
    labels = {n.get("id") or n.get("entity_id"):
              n.get("label") or n.get("canonical_label", "") for n in nodes}
    return edges, labels


def vis_payload(source: str = "demo_kg", pivots: list | None = None,
                max_edges: int = 400) -> dict:
    """Shape a whole graph -- or the subgraph around `pivots` -- for the graph viewer.

    Same `subgraph()` filter the context builder uses, so what you see drawn is exactly
    the edge set a KG-aware configuration would have been given for those pivots. Reusing
    the filter is the point: a viewer with its own selection rule would show a graph the
    experiment never used.
    """
    directory = graph_dir(source)
    if not (directory / "edges.json").exists():
        return {"nodes": [], "edges": [], "stage": source, "truncated": False,
                "total_edges": 0,
                "note": f"{source} n'a pas encore de graphe — ingérez des sources sur /live."}
    edges = load_json(directory / "edges.json")
    nodes = load_json(directory / "nodes.json")
    total_before_filter = len(edges)
    if pivots:
        labels = {n.get("id") or n.get("entity_id"):
                  n.get("label") or n.get("canonical_label", "") for n in nodes}
        edges = subgraph(edges, labels, pivots)
    payload = graph_view.shape(edges, nodes, max_edges=max_edges, stage=source)
    payload["pivots"] = pivots or []
    payload["graph_total_edges"] = total_before_filter
    return payload


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


MAX_ENTITY_PIVOTS = 12


def available_pivots(source: str = "demo_kg") -> list[dict]:
    """Entities worth offering as a pivot.

    CVE identifiers come first, which keeps the frozen graph's choices exactly as before.
    But an ingested corpus need not mention a single CVE -- the XZ backdoor thread names
    none in any extracted triple -- so the highest-degree entity labels are appended.
    Without that, `live_kg` would offer nothing to pivot on and the column would be
    unusable on precisely the sources the user just supplied.
    """
    if not graph_available(source):
        return []
    edges, labels = load_graph(source)

    cve_counts: dict[str, int] = {}
    degree: dict[str, int] = {}
    for edge in edges:
        for endpoint_id in (edge["source"], edge["target"]):
            label = labels.get(endpoint_id, "")
            degree[label] = degree.get(label, 0) + 1
            for cve in re.findall(r"CVE-\d{4}-\d{4,7}", label):
                cve_counts[cve] = cve_counts.get(cve, 0) + 1

    pivots = [{"id": k, "edges": v, "kind": "CVE"}
              for k, v in sorted(cve_counts.items(), key=lambda kv: -kv[1])]

    if len(pivots) < MAX_ENTITY_PIVOTS:
        seen = {p["id"] for p in pivots}
        for label, count in sorted(degree.items(), key=lambda kv: -kv[1]):
            if len(pivots) >= MAX_ENTITY_PIVOTS:
                break
            if not label or label in seen or any(c in label for c in seen):
                continue
            pivots.append({"id": label, "edges": count, "kind": "entité"})
            seen.add(label)
    return pivots


def principal_carrier_lines(pivots: list, anchors: list,
                            source: str = "demo_kg") -> tuple[list[str], dict]:
    """Ask carrier_check which edges carry the anchored fact; ablate the Tier-1 set.

    This is the point of the checkbox: the removed edges are computed, never designated
    by hand -- the same guarantee the 45 recorded cells rely on.
    """
    edges, labels = load_graph(source)
    if not anchors:
        return [], {"tier1": [], "tier2": [], "note": "aucun ancrage fourni"}
    result = carrier_check.find_carriers(edges, labels, anchors, pivots)
    return [c["line"] for c in result["tier1"]], result


def build_context(config: str, question: str, pivots: list, ablate: bool,
                  anchors: list, source: str = "demo_kg") -> tuple[str, dict]:
    """Return (context_text, diagnostics). Empty context for config 1."""
    if config == "c1":
        return "", {"kind": "aucun contexte"}

    if config == "c2":
        import rag
        context, hits = rag.build_context(question, source=source)
        return context, {"kind": "RAG", "passages": len(hits),
                         "sources": sorted({h["source_id"] for h in hits}),
                         "hits": [{"source_id": h["source_id"], "score": round(h["score"], 3),
                                   "excerpt": h["text"][:180]} for h in hits]}

    edges, labels = load_graph(source)
    selected = subgraph(edges, labels, pivots)
    lines = [render_edge(e, labels) for e in selected]
    diagnostics = {"kind": "KG", "triples": len(lines), "removed": [], "carriers": None}

    if config in ("c5", "c8") and ablate:
        removed, carriers = principal_carrier_lines(pivots, anchors, source)
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


# ONE template, used verbatim by all five configurations -- there is deliberately no
# per-configuration branch. A configuration with no context simply gets an empty
# information block, and the citation requirement then yields "aucun" on its own: that is
# the demonstration, not a special case coded for it.
#
# NOTE: this template is stricter than the one used for the 45 recorded cells (it demands
# a structured decision / justification / citation triplet). It applies ONLY to this
# interactive tool; `experiments/` and `deliverables/resultats.md` are untouched, and the
# divergence is recorded in the AI Usage Log.
PROMPT_TEMPLATE = """{information}

Question : {question}

Réponds exactement dans ce format, en français, sans montrer ton raisonnement interne :

DÉCISION : <ta décision en une phrase>
JUSTIFICATION : <2 à 4 phrases expliquant sur quoi tu t'appuies>
ÉLÉMENTS CITÉS : <les éléments ci-dessus sur lesquels repose ta décision, avec leur identifiant [source: Sxx] ; écris exactement « aucun » si les informations fournies ne contiennent rien de citable>

Ne fonde ta décision que sur les informations fournies ci-dessus."""

NO_INFORMATION = "(aucune information fournie)"

# The heading is "ÉLÉMENTS CITÉS :" -- the lookaheads must allow the word between
# ÉLÉMENTS and the colon, otherwise the justification swallows the citation block.
_CITED_HEAD = r"[ÉE]L[ÉE]MENTS\s+CIT[ÉE]S\s*:"
_FIELDS = {
    "decision": rf"D[ÉE]CISION\s*:\s*(.+?)(?=\n\s*(?:JUSTIFICATION\s*:|{_CITED_HEAD})|\Z)",
    "justification": rf"JUSTIFICATION\s*:\s*(.+?)(?=\n\s*{_CITED_HEAD}|\Z)",
    "cited": rf"{_CITED_HEAD}\s*(.+?)\Z",
}


def build_prompt(question: str, context: str) -> str:
    """Identical template for every configuration; only `information` differs."""
    return PROMPT_TEMPLATE.format(information=context or NO_INFORMATION,
                                  question=question)


def parse_answer(text: str) -> dict:
    """Split the structured answer. Falls back to the raw text rather than losing it."""
    out = {}
    for name, pattern in _FIELDS.items():
        match = re.search(pattern, text, re.S | re.I)
        out[name] = match.group(1).strip() if match else ""
    out["structured"] = bool(out["decision"])
    if not out["structured"]:
        # The model ignored the format. Show everything rather than nothing.
        out["decision"] = text.strip().split("\n")[0][:200]
        out["justification"] = text.strip()
    # "aucun" is a meaningful answer, not a missing one -- it is the config-1 result.
    out["cites_nothing"] = out["cited"].strip().lower().startswith("aucun")
    return out


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
