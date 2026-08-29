"""One-off migration: seed the new concept-stable clusters_validation.json from
the old exact-hash-keyed clusters_validation.json, so accept/reject decisions
made under the old ID scheme are not silently discarded.

Run once, before the first cluster_relations() + export_clusters_for_review()
call under the new ID scheme. Safe to re-run: it only ever reads the
*current* clusters_raw.json/clusters_validation.json (whatever scheme they are
currently in) and writes a seed dict keyed by the new concept-id scheme;
running it again after the new scheme is already live is a no-op in practice
because old-scheme records will no longer be found where migrated ones aren't
already newer, but there is no reason to run it more than once.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config
import pipeline_lib as pl


def main() -> None:
    old_clusters = pl.load_json(config.CLUSTER_DIR / "clusters_raw.json", [])
    old_validation = pl.load_json(config.CLUSTER_DIR / "clusters_validation.json", [])
    old_cluster_by_id = {c["cluster_id"]: c for c in old_clusters}

    # concept_key -> list of (assertion_count, old_cluster, old_validation_record)
    # for every OLD cluster that carried a real decision.
    by_concept: dict[str, list[tuple[int, dict, dict]]] = defaultdict(list)
    for record in old_validation:
        if record.get("decision") not in ("accept", "reject", "split"):
            continue
        cluster = old_cluster_by_id.get(record.get("cluster_id"))
        if cluster is None:
            continue
        concept_key = pl.cluster_concept_key(cluster["representative"])
        by_concept[concept_key].append((cluster["assertion_count"], cluster, record))

    collisions = {k: v for k, v in by_concept.items() if len(v) > 1}
    seed: dict[str, dict] = {}
    conflict_report = []
    for concept_key, entries in by_concept.items():
        entries.sort(key=lambda e: -e[0])
        count, cluster, record = entries[0]
        new_cluster_id = pl.stable_id("rc2", concept_key)
        content_id = pl.stable_id("rc", *cluster["member_phrases"])
        seed[new_cluster_id] = {
            "cluster_id": new_cluster_id,
            "decision": record["decision"],
            "canonical_relation": record.get("canonical_relation") or cluster["representative"],
            "notes": record.get("notes", ""),
            "content_id_at_last_decision": content_id,
            "member_phrases_at_decision": cluster["member_phrases"],
            "composition_changed_since_review": False,
            "diff": {"added": [], "removed": []},
            "previous_decision": None,
            "review_status": "confirmed",
        }
        if len(entries) > 1:
            conflict_report.append({
                "concept_key": concept_key,
                "kept": {"old_cluster_id": cluster["cluster_id"], "representative": cluster["representative"],
                         "assertion_count": count, "decision": record["decision"]},
                "dropped": [{"old_cluster_id": c["cluster_id"], "representative": c["representative"],
                             "assertion_count": ac, "decision": r["decision"]}
                            for ac, c, r in entries[1:]],
            })

    pl.write_json(config.CLUSTER_DIR / "clusters_validation.json", list(seed.values()))
    pl.write_json(config.REPORTS_DIR / "cluster_id_migration_conflicts.json", conflict_report)
    print(f"Migrated {len(seed)} decisions from {sum(1 for r in old_validation if r.get('decision') in ('accept','reject','split'))} "
          f"old accept/reject/split records ({len(old_validation)} total old records).")
    print(f"Concept-key collisions among old decided clusters: {len(collisions)} "
          f"(kept the highest-volume cluster's decision for each, see reports/cluster_id_migration_conflicts.json)")


if __name__ == "__main__":
    main()
