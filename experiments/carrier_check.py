#!/usr/bin/env python3
"""Redundancy-aware ablation: count how many canonical edges carry a given fact.

Why this exists
---------------
The Day-2 run ablated the two edges that *literally* expressed the SharePoint
chaining relation, and the decision did not move. The reason was not that the
relation was unimportant: the same information survived under other relation
labels. An ablation that does not first measure redundancy measures nothing.

So before ablating, we count the *carriers* of a fact. A fact is identified by
its `anchors` -- the entity labels it relates. Two carrier tiers, both mechanical:

  Tier 1 (explicit)  an edge whose `evidence` sentence mentions **every** anchor.
                     Such a sentence is, by construction, capable of expressing
                     the relation between them.

  Tier 2 (partial)   an edge whose evidence mentions **at least one** anchor and
                     at least MIN_SHARED_TERMS content words that also occur in
                     the Tier-1 evidence sentences. The term list is *derived
                     from the Tier-1 evidence*, never hand-authored -- that is
                     what keeps the tier reproducible rather than a judgement.

A complete ablation must remove every Tier-1 carrier. Tier-2 carriers are
reported, not removed: they are the measurement of how redundantly the graph
encodes the fact, which is the §14.2 "densité relationnelle" metric and the
explanation of the Day-2 non-result.

Standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = ROOT / "extraction_pipeline" / "canonical_kg"

# Declared parameters. Fixed in advance, reported with the results -- in the
# same spirit as the pipeline's existing RELATION_JACCARD_THRESHOLD = 0.80.
MIN_SHARED_TERMS = 2
MIN_TERM_LENGTH = 4

# Function words carry no topical signal; excluded from the derived term list.
STOPWORDS = {
    "with", "that", "this", "when", "from", "into", "such", "than", "then",
    "they", "them", "their", "there", "these", "those", "which", "while",
    "have", "has", "had", "been", "being", "will", "would", "could", "should",
    "can", "may", "might", "must", "does", "did", "done", "also", "just",
    "another", "other", "some", "each", "both", "more", "most", "very",
    "according", "using", "used", "full", "here", "what", "were", "was",
}


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_graph():
    edges = load_json(CANONICAL / "edges.json")
    labels = {node["id"]: node["label"] for node in load_json(CANONICAL / "nodes.json")}
    return edges, labels


def render_edge(edge: dict, labels: dict) -> str:
    predicate = "_".join(edge["predicate_canonical"].split())
    return (f"{labels.get(edge['source'], '')} {predicate} "
            f"{labels.get(edge['target'], '')} [source: {edge['source_id']}]")


def content_terms(text: str, anchors: list) -> set:
    """Lower-cased content words of `text`, minus stopwords and anchor tokens."""
    anchor_tokens = {tok for anchor in anchors for tok in re.findall(r"\w+", anchor.lower())}
    return {
        word for word in re.findall(r"[a-zA-Z]+", text.lower())
        if len(word) >= MIN_TERM_LENGTH and word not in STOPWORDS and word not in anchor_tokens
    }


def find_carriers(edges: list, labels: dict, anchors: list, pivots: list,
                  min_shared: int = MIN_SHARED_TERMS) -> dict:
    """Split the task subgraph into Tier-1 and Tier-2 carriers of the anchored fact."""
    # Restrict to the task's own subgraph: an edge outside it was never in the
    # context, so it cannot have carried the fact to the model.
    scope = []
    for edge in edges:
        endpoints = labels.get(edge["source"], "") + " " + labels.get(edge["target"], "")
        if any(pivot in endpoints for pivot in pivots):
            scope.append(edge)

    tier1 = [e for e in scope if all(a.lower() in e["evidence"].lower() for a in anchors)]

    # The Tier-2 vocabulary is derived from Tier-1 evidence, not authored here.
    derived_terms = set()
    for edge in tier1:
        derived_terms |= content_terms(edge["evidence"], anchors)

    tier1_ids = {e["edge_id"] for e in tier1}
    tier2 = []
    for edge in scope:
        if edge["edge_id"] in tier1_ids:
            continue
        evidence = edge["evidence"].lower()
        if not any(a.lower() in evidence for a in anchors):
            continue
        shared = content_terms(edge["evidence"], anchors) & derived_terms
        if len(shared) >= min_shared:
            tier2.append((edge, sorted(shared)))

    return {
        "scope_edges": len(scope),
        "derived_term_count": len(derived_terms),
        "tier1": [
            {"edge_id": e["edge_id"], "source_id": e["source_id"],
             "line": render_edge(e, labels), "evidence": e["evidence"],
             # The context shows the rendered triple, not the evidence sentence.
             # An edge can therefore carry the fact in the graph (evidence names
             # every anchor) while the model only sees a partial rendering.
             "anchors_visible_in_line": all(
                 a.lower() in render_edge(e, labels).lower() for a in anchors)}
            for e in tier1
        ],
        "tier2": [
            {"edge_id": e["edge_id"], "source_id": e["source_id"],
             "line": render_edge(e, labels), "evidence": e["evidence"],
             "shared_terms": shared}
            for e, shared in tier2
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Count carriers; optionally set ablation targets.")
    parser.add_argument("--apply", action="store_true",
                        help="write the computed Tier-1 carrier set into tasks.json "
                             "for every task with ablation_mode=auto")
    args = parser.parse_args()

    tasks_file = Path(__file__).parent / "tasks.json"
    tasks_doc = load_json(tasks_file)
    tasks = tasks_doc["tasks"]
    edges, labels = load_graph()

    report = {
        "parameters": {
            "MIN_SHARED_TERMS": MIN_SHARED_TERMS,
            "MIN_TERM_LENGTH": MIN_TERM_LENGTH,
        },
        "tasks": {},
    }

    for task in tasks:
        anchors = task.get("anchors")
        if not anchors:
            report["tasks"][task["id"]] = {"skipped": "no anchors declared (no relational ablation)"}
            continue

        result = find_carriers(edges, labels, anchors, task["pivots"])
        result["tier2_sensitivity"] = {
            str(k): len(find_carriers(edges, labels, anchors, task["pivots"], k)["tier2"])
            for k in (2, 3, 4, 5)
        }
        # For auto tasks the ablation IS the full Tier-1 carrier set: computed,
        # never chosen. Historical and scenario tasks keep their frozen ablation.
        if args.apply and task.get("ablation_mode") == "auto":
            task["ablation_lines"] = [c["line"] for c in result["tier1"]]

        ablated = set(task.get("ablation_lines", []))
        tier1_lines = {c["line"] for c in result["tier1"]}
        missed = sorted(tier1_lines - ablated)

        result["ablation_declared"] = sorted(ablated)
        result["tier1_carriers_not_ablated"] = missed
        result["ablation_complete"] = not missed
        result["carrier_count"] = len(result["tier1"]) + len(result["tier2"])
        report["tasks"][task["id"]] = result

        print(f"\n=== {task['id']} — anchors: {anchors}")
        print(f"  subgraph edges          : {result['scope_edges']}")
        print(f"  Tier-1 explicit carriers: {len(result['tier1'])}")
        for c in result["tier1"]:
            mark = "ABLATED" if c["line"] in ablated else "SURVIVED"
            vis = "anchors visible in line" if c["anchors_visible_in_line"] else "anchors only in evidence"
            print(f"    [{mark}] {c['line'][:100]}")
            print(f"              ({vis})")
        print(f"  Tier-2 partial carriers : {len(result['tier2'])}")
        for c in result["tier2"]:
            print(f"    [SURVIVED] {c['line'][:100]}")
            print(f"               shared: {c['shared_terms'][:6]}")
        print(f"  Tier-2 sensitivity (K -> count): {result['tier2_sensitivity']}")
        verdict = "COMPLETE" if result["ablation_complete"] else "INCOMPLETE"
        print(f"  --> ablation is {verdict}; total carriers = {result['carrier_count']}")

    if args.apply:
        tasks_file.write_text(
            json.dumps(tasks_doc, indent=2, ensure_ascii=False) + chr(10), encoding="utf-8")
        print(f"applied computed ablations to {tasks_file.name}")

    out = Path(__file__).parent / "carriers.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
