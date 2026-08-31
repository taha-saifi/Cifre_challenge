#!/usr/bin/env python3
"""Project the frozen canonical KG onto the demo corpus -- a PROJECTION, not a re-run.

Why this is a projection and not a pipeline re-run
--------------------------------------------------
Re-running `extraction_pipeline` on the 10 demo sources would be the faithful thing to
do, and it is what was originally asked for. It is not possible on this machine, and
producing it anyway would manufacture a false signal:

  * The frozen KG was built with MinIE for 3246 assertions and the heuristic fallback for
    only 405 (`data/openie_run_metadata.json`). MinIE needs Java + a built JAR; neither
    exists here and nothing listens on 127.0.0.1:8080.
  * A re-run would therefore be heuristic-only. Measured on the single most important
    sentence of the demonstration (S40):
        MinIE       : Patching CVE-2026-55040 | break   | exploit chain
        heuristic   : Patching CVE-2026-55040 will successfully break this | exploit | chain
    The predicate becomes `exploit`, which is one of the 11 clusters a human REJECTED, so
    the edge would be dropped from the canonical graph entirely and the T1/T1b
    demonstration would collapse.
  * That divergence would look like "the subset lost a carrier" while actually meaning
    "the extractor changed" -- a different diagnosis, and the wrong one to report.

So `demo_kg/` is defined as: every canonical edge whose `source_id` belongs to the demo
corpus. Deterministic, regenerable, and it preserves the two validated results exactly.
It must never be described as a re-extraction.

Standard library only.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = ROOT / "extraction_pipeline" / "canonical_kg"
DEMO_CLEAN = ROOT / "demo_corpus" / "clean"
OUT = ROOT / "demo_kg"


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    demo_sources = {p.stem for p in DEMO_CLEAN.glob("S*.json")}
    edges = load_json(CANONICAL / "edges.json")
    nodes = load_json(CANONICAL / "nodes.json")

    kept = [e for e in edges if e["source_id"] in demo_sources]
    touched = {e["source"] for e in kept} | {e["target"] for e in kept}
    # Keep node rows for touched ids only. Note the upstream defect: nodes.json holds
    # 1956 rows for 1867 distinct ids (case-collision duplicates), so we filter rows and
    # report both counts rather than pretending the two numbers are the same.
    kept_nodes = [n for n in nodes if n["id"] in touched]

    OUT.mkdir(exist_ok=True)
    (OUT / "edges.json").write_text(
        json.dumps(kept, indent=2, ensure_ascii=False), encoding="utf-8")
    (OUT / "nodes.json").write_text(
        json.dumps(kept_nodes, indent=2, ensure_ascii=False), encoding="utf-8")

    manifest = {
        "_note": "PROJECTION of extraction_pipeline/canonical_kg onto the demo corpus. "
                 "NOT a pipeline re-run -- see the module docstring of build_demo_kg.py "
                 "for why a re-run is impossible here and what it would break.",
        "demo_sources": sorted(demo_sources),
        "edges": len(kept),
        "node_rows": len(kept_nodes),
        "distinct_node_ids": len({n["id"] for n in kept_nodes}),
        "distinct_predicates": len({e["predicate_canonical"] for e in kept}),
        "edges_by_source": dict(Counter(e["source_id"] for e in kept).most_common()),
        "extraction_methods": dict(Counter(e["extraction_method"] for e in kept)),
        "full_graph_for_comparison": {"edges": len(edges), "node_rows": len(nodes)},
    }
    (OUT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"demo sources      : {len(demo_sources)}")
    print(f"edges             : {len(kept)}  (full graph: {len(edges)})")
    print(f"node rows         : {len(kept_nodes)}  distinct ids: {manifest['distinct_node_ids']}")
    print(f"distinct predicates: {manifest['distinct_predicates']}")
    print(f"extraction methods : {manifest['extraction_methods']}")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
