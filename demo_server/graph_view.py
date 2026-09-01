#!/usr/bin/env python3
"""One shaping rule turning a KG stage into a vis-network payload.

Why this lives in its own module
--------------------------------
Two callers need the same shape: `live_pipeline.graph_payload()` (a live session's
open_kg / canonical_kg) and `configs.vis_payload()` (the frozen projection demo_kg, or a
validated live_kg). Copying the shaping into both would let the two views drift apart and
show the same graph differently -- the same failure this repo already refuses for source
scoring, where `score_source()` is the single rule everything else copies.

Provenance travels with every edge (source_id, evidence, extraction method, and the
source_authority joined by build_canonical_kg) so a click can always answer "where does
this come from?" without a second request.

Standard library only.
"""
from __future__ import annotations

from typing import Any


def node_key(node: dict) -> str:
    """open_kg and canonical_kg disagree on the id field name; accept both."""
    return node["entity_id"] if "entity_id" in node else node["id"]


def shape(raw_edges: list[dict], raw_nodes: list[dict],
          max_edges: int = 400, stage: str = "") -> dict[str, Any]:
    """Return {nodes, edges, stage, truncated, total_edges} for vis-network.

    `max_edges` truncates rather than samples, and the result says so: a silently
    thinned graph would look like a sparser graph, which is a different claim.
    """
    labels = {node_key(n): n.get("label") or n.get("canonical_label", "") for n in raw_nodes}
    types = {node_key(n): n.get("entity_type", "") for n in raw_nodes}

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

    edges = []
    for edge in kept:
        authority = edge.get("source_authority") or {}
        edges.append({
            "id": edge["edge_id"],
            "from": edge["source"],
            "to": edge["target"],
            "label": (edge.get("predicate_canonical") or edge["predicate_raw"])[:34],
            "source_id": edge["source_id"],
            "source_url": edge.get("source_url") or "",
            "method": edge.get("extraction_method", ""),
            "evidence": edge.get("evidence", ""),
            "predicate": edge.get("predicate_canonical") or edge["predicate_raw"],
            "predicate_raw": edge["predicate_raw"],
            "subject": labels.get(edge["source"], ""),
            "object": labels.get(edge["target"], ""),
            # None for a source with no declared metadata (a live session). Kept as None
            # rather than defaulted to a number: "unknown" is not "low".
            "authority_score": authority.get("score"),
            "authority_category": authority.get("category"),
            "authority_tier": authority.get("tier"),
        })

    return {"nodes": nodes, "edges": edges, "stage": stage,
            "truncated": len(raw_edges) > max_edges, "total_edges": len(raw_edges)}
