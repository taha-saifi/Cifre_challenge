#!/usr/bin/env python3
"""Relation-cluster validation for the live session: by hand, or left to the system.

Reuses the existing clustering and validation machinery, applied to the relations of
`live_corpus/` instead of the 2111 clusters of the frozen graph:
`build_relation_inventory` → `normalize_relations` → `cluster_relations` (Jaccard 0.80,
`config.RELATION_JACCARD_THRESHOLD`) → `export_clusters_for_review` →
`apply_cluster_validation` → `build_canonical_kg`.

What "leave it to the system" means -- stated precisely, because it matters
--------------------------------------------------------------------------
There is no pre-existing automatic *acceptance* policy in this project, and inventing a
second decision logic was explicitly out of bounds. So auto mode does exactly one thing:
it marks a cluster `accept` and lets the guardrails that are already coded do the filtering
they already do. Those guardrails are:

  * `is_bare_auxiliary_predicate()`, applied inside `is_usable_triple()` *before*
    clustering -- so bare copulas (`is`, `has`, `be`, …) never reach a candidate cluster at
    all. This is the filter that was added after the historical incident where ~940 clusters
    were bulk-accepted and the two largest "relations" in the graph turned out to be empty
    copulas.
  * `split_assignment_labels()`'s reject-by-default: an unassigned phrase in a split
    contributes nothing.
  * `accepted_relation_map()`: only `accept` and `split` produce a canonical label;
    `reject` and `pending` produce nothing.

Consequence to keep visible: an auto-validated graph is **machine-validated, not
human-validated**. The project's claim that no edge becomes canonical without a human
accepting it holds for the frozen graph, not for a live session run in auto mode. Every
decision therefore records its origin, and the counts are returned to the UI.
"""
from __future__ import annotations

import json
from pathlib import Path

import live_pipeline
from live_pipeline import LIVE_KG, config, pipeline_lib, redirected_config, _LOCK

MAX_EXAMPLES = 3
MAX_CANDIDATES = 300


def _load(path: Path, default):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def build_candidates() -> dict:
    """Cluster the live relations and return candidates enriched with evidence."""
    with _LOCK, redirected_config():
        pipeline_lib.build_relation_inventory()
        pipeline_lib.normalize_relations()
        clusters = pipeline_lib.cluster_relations()
        pipeline_lib.export_clusters_for_review()
        inventory = _load(config.DATA_DIR / "relation_inventory.json", [])

    # Evidence lives in the inventory, keyed by the raw predicate phrase.
    by_phrase = {row["relation_raw"]: row for row in inventory}

    candidates = []
    for cluster in clusters[:MAX_CANDIDATES]:
        examples = []
        for phrase in cluster["member_phrases"]:
            for sample in (by_phrase.get(phrase, {}).get("examples") or [])[:MAX_EXAMPLES]:
                examples.append({
                    "phrase": phrase,
                    "subject": sample.get("subject_raw", ""),
                    "object": sample.get("object_raw", ""),
                    "evidence": sample.get("evidence", ""),
                    "source_id": sample.get("source_id", ""),
                })
            if len(examples) >= MAX_EXAMPLES:
                break
        candidates.append({
            "cluster_id": cluster["cluster_id"],
            "representative": cluster["representative"],
            "member_phrases": cluster["member_phrases"],
            "assertion_count": cluster.get("assertion_count", 0),
            "examples": examples[:MAX_EXAMPLES],
        })

    candidates.sort(key=lambda c: (-c["assertion_count"], c["representative"]))
    return {
        "candidates": candidates,
        "total_clusters": len(clusters),
        "shown": len(candidates),
        "jaccard_threshold": config.RELATION_JACCARD_THRESHOLD,
    }


def apply_decisions(decisions: dict[str, str], auto_default: bool = True) -> dict:
    """Write the decisions and rebuild the session's canonical graph.

    `decisions` maps cluster_id -> "accept" | "reject" | "auto". Anything absent is treated
    as "auto" when `auto_default` is true (the zero-interaction path), otherwise left
    `pending` -- and a pending cluster contributes no canonical edge, by the existing rule.
    """
    with _LOCK, redirected_config():
        validation_path = config.CLUSTER_DIR / "clusters_validation.json"
        records = _load(validation_path, [])
        clusters = {c["cluster_id"]: c for c in _load(config.CLUSTER_DIR / "clusters_raw.json", [])}

        counts = {"human_accept": 0, "human_reject": 0, "auto_accept": 0, "pending": 0}
        for record in records:
            cluster_id = record.get("cluster_id")
            choice = decisions.get(cluster_id, "auto" if auto_default else "pending")

            if choice == "accept":
                record["decision"] = "accept"
                record["notes"] = "validation humaine (session live)"
                counts["human_accept"] += 1
            elif choice == "reject":
                record["decision"] = "reject"
                record["notes"] = "rejet humain (session live)"
                counts["human_reject"] += 1
            elif choice == "auto":
                # Accept and let the already-coded guardrails filter. No second decision
                # logic -- see the module docstring.
                record["decision"] = "accept"
                record["notes"] = ("auto : garde-fous du pipeline seuls "
                                   "(is_bare_auxiliary_predicate en amont du clustering, "
                                   "rejet-par-defaut sur split)")
                counts["auto_accept"] += 1
            else:
                record["decision"] = "pending"
                record["notes"] = "laisse en attente : aucune arete canonique"
                counts["pending"] += 1
            # A live session has no drift history to protect.
            record["review_status"] = "confirmed" if record["decision"] != "pending" else "pending"

        validation_path.write_text(
            json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")

        mapping = pipeline_lib.apply_cluster_validation()
        nodes, edges = pipeline_lib.build_canonical_kg()

    return {
        "counts": counts,
        "accepted_phrases": len(mapping),
        "canonical_nodes": len(nodes),
        "canonical_edges": len(edges),
        "clusters_total": len(clusters),
        # True only when every contributing decision came from a human.
        "fully_human_validated": counts["auto_accept"] == 0 and counts["human_accept"] > 0,
    }


def canonical_graph() -> dict:
    return live_pipeline.graph_payload(stage="canonical_kg")
