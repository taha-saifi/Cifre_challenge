#!/usr/bin/env python3
"""Deterministic builder for the §13 experiment contexts.

One context file per (task, configuration) cell. Nothing here is hand-written:
a cell's context is a pure function of the task definition in `tasks.json` and
the canonical KG on disk. This is what makes the protocol reproducible and the
config-4 vs config-5 contrast auditable.

Standard library only, like `extraction_pipeline/`.

Usage:
    python experiments/build_contexts.py --verify   # reproduce the 10 Day-2 files
    python experiments/build_contexts.py            # write experiments/contexts/
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPELINE = ROOT / "extraction_pipeline"
CANONICAL = PIPELINE / "canonical_kg"
PREVALIDATION = PIPELINE / "archive" / "pre_final_dedup_20260829T011315"
DAY2_CONTEXTS = PIPELINE / "reports" / "experiment_contexts"

# Header line per configuration. Config 1 gets no context file content at all.
HEADERS = {
    4: "Informations disponibles (sous-graphe canonical KG actuel) :",
    5: "Informations disponibles (sous-graphe canonical KG actuel, incomplet) :",
    7: "Informations disponibles (sous-graphe canonical KG, etat pre-validation) :",
    8: "Informations disponibles (sous-graphe canonical KG actuel, incomplet) :",
}
CONFIGS = (1, 4, 5, 7, 8)


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_graph(directory: Path):
    """Return (edges, node_id -> label) for a canonical_kg directory."""
    edges = load_json(directory / "edges.json")
    labels = {node["id"]: node["label"] for node in load_json(directory / "nodes.json")}
    return edges, labels


def render_edge(edge: dict, labels: dict) -> str:
    """One context line: `subject predicate object [source: Sxx]`.

    The predicate is underscore-joined so a multi-word canonical relation stays
    visually one token; subject and object labels keep their spaces.
    """
    subject = labels.get(edge["source"], "")
    obj = labels.get(edge["target"], "")
    predicate = "_".join(edge["predicate_canonical"].split())
    return f"{subject} {predicate} {obj} [source: {edge['source_id']}]"


def subgraph(edges: list, labels: dict, pivots: list) -> list:
    """Every edge with a pivot string in its subject or object label.

    Edge order is preserved from edges.json, so the context is a stable function
    of the graph rather than of the traversal.
    """
    selected = []
    for edge in edges:
        endpoints = labels.get(edge["source"], "") + " " + labels.get(edge["target"], "")
        if any(pivot in endpoints for pivot in pivots):
            selected.append(edge)
    return selected


def build_context(task: dict, config: int) -> str:
    """Render the full context text for one cell. Empty string for config 1."""
    if config == 1:
        return ""

    directory = PREVALIDATION if config == 7 else CANONICAL
    edges, labels = load_graph(directory)
    selected = subgraph(edges, labels, task["pivots"])

    lines = [render_edge(edge, labels) for edge in selected]

    # Configs 5 and 8 ablate the targeted fact; 4 and 7 keep it.
    if config in (5, 8):
        removed = set(task.get("ablation_lines", []))
        lines = [line for line in lines if line not in removed]

    # A scenario sentence is corpus-external and always marked as such.
    scenario = task.get("scenario")
    if scenario and config in (4, 7):
        lines.append(scenario)

    if config == 8 and task.get("gap_notice"):
        lines.append(task["gap_notice"])

    return HEADERS[config] + "\n\n" + "\n".join(lines)


def verify() -> int:
    """Reproduce the 10 Day-2 context files byte for byte.

    If this fails, the harness does not reproduce the Day-2 run and the new
    cells are not comparable with the existing ones.
    """
    tasks = {task["id"]: task for task in load_json(Path(__file__).parent / "tasks.json")["tasks"]}
    failures = 0
    for legacy_id, task_id in (("A", "T1"), ("B", "T2")):
        for config in CONFIGS:
            expected_path = DAY2_CONTEXTS / f"ctx_{legacy_id}{config}.txt"
            expected = expected_path.read_text(encoding="utf-8")
            actual = build_context(tasks[task_id], config)
            status = "OK  " if actual == expected else "FAIL"
            if actual != expected:
                failures += 1
                exp_lines, act_lines = expected.split("\n"), actual.split("\n")
                detail = f"  expected {len(exp_lines)} lines, got {len(act_lines)}"
                for i, (e, a) in enumerate(zip(exp_lines, act_lines)):
                    if e != a:
                        detail += f"\n  first diff at line {i + 1}:\n    exp: {e!r}\n    got: {a!r}"
                        break
                print(f"{status} ctx_{legacy_id}{config}.txt\n{detail}")
            else:
                print(f"{status} ctx_{legacy_id}{config}.txt ({len(actual)} bytes)")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true",
                        help="reproduce the 10 Day-2 contexts and report any drift")
    args = parser.parse_args()

    if args.verify:
        failures = verify()
        print(f"\n{'PASS' if not failures else 'FAIL'}: {failures} mismatch(es)")
        return 1 if failures else 0

    tasks = load_json(Path(__file__).parent / "tasks.json")["tasks"]
    out_dir = Path(__file__).parent / "contexts"
    out_dir.mkdir(exist_ok=True)
    for task in tasks:
        for config in CONFIGS:
            text = build_context(task, config)
            path = out_dir / f"ctx_{task['id']}_c{config}.txt"
            path.write_text(text, encoding="utf-8", newline="\n")
            print(f"wrote {path.name} ({len(text)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
