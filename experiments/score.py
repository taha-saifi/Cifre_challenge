#!/usr/bin/env python3
"""Compute the objective half of the §14.3 answer-quality grid.

The brief's §21 makes "relying on an LLM-as-a-Judge with no control" an
eliminating criterion, so no model grades any answer here. Two dimensions are
computed by string matching against the exact context the cell was given, and
four more are recorded as observable binary indicators. Only "exactitude"
requires a human, and it is a comparison against decision_key.json, which was
frozen before any cell was executed.

Computed dimensions
-------------------
grounding            share of the answer's *literally verifiable* tokens that
                     occur in that cell's context file. Verifiable tokens are
                     CVE ids, KB references, source ids, ISO dates and CVSS
                     scores -- values that appear verbatim in the context if
                     they came from it. Percentages and derived figures are
                     deliberately excluded: an answer may legitimately restate
                     0.39652 as "39,7 %", and counting that as ungrounded would
                     measure paraphrase, not fabrication.

citations_correct    share of the [source: Sxx] identifiers cited in the answer
                     that actually appear in that cell's context.

Both are reported with their denominator so a small-sample ratio is never read
as a precise score. Config 1 has an empty context by construction: every
verifiable token it produces is ungrounded, which is the measurement, not a bug.

Standard library only.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTEXTS = HERE / "contexts"
RESULTS = HERE / "results"

# Token classes that, if taken from the context, appear in it verbatim.
VERIFIABLE_PATTERNS = {
    "cve": r"CVE-\d{4}-\d{4,7}",
    "kb": r"KB\d{6,7}",
    # 2 digits for the frozen corpus (S01-S58), 3 for a live session (S901+). Widening
    # this does not move the recorded scores: no frozen context or answer contains a
    # 3-digit source id. Verified by re-running and diffing scores.json.
    "source_id": r"\bS\d{2,3}\b",
    "iso_date": r"\b20\d{2}-\d{2}-\d{2}\b",
    "cvss": r"\b\d\.\d\b",
}
CITATION_PATTERN = r"\[source\s*:\s*(S\d{2})\]"

# Observable, countable properties of an answer -- not quality judgements.
INDICATORS = {
    "explicit_decision": r"(?i)\b(décision|conclusion|classement|priorit|patcher en premier)\b",
    "names_uncertainty": r"(?i)(ne peut|ne permet pas|impossible de|pas pu (?:être )?confirm|"
                         r"incertitude|indéterminé|n'est pas documenté|aucune (?:source|information)|"
                         r"ne pas conclure|sans certitude)",
    "requests_more_info": r"(?i)(il faut (?:d'abord )?obtenir|avant de|vérifier (?:les|le|la)|"
                          r"nécessiterait|il conviendrait de|demander)",
    "states_confidence": r"(?i)(niveau de confiance|degré de certitude|avec certitude|"
                         r"probabilité|sous réserve|par défaut|principe de précaution)",
}


def verifiable_tokens(text: str) -> set:
    tokens = set()
    for pattern in VERIFIABLE_PATTERNS.values():
        tokens |= set(re.findall(pattern, text))
    return tokens


def strip_html_comment(text: str) -> str:
    """Imported Day-2 files carry a provenance comment; it is not part of the answer."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.S).strip()


def score_cell(task_id: str, config: int, prompt: str = "") -> dict | None:
    answer_path = RESULTS / f"{task_id}_c{config}.md"
    context_path = CONTEXTS / f"ctx_{task_id}_c{config}.txt"
    if not answer_path.exists():
        return None

    answer = strip_html_comment(answer_path.read_text(encoding="utf-8"))
    context = context_path.read_text(encoding="utf-8") if context_path.exists() else ""

    tokens = verifiable_tokens(answer)
    # A token supplied by the question itself (e.g. the reference date in T5) is
    # not something the answer had to get from the graph, so it cannot count as
    # ungrounded. Matching is case-insensitive: the context carries some
    # identifiers inside lower-cased URLs.
    haystack = (context + "\n" + prompt).lower()
    grounded = {t for t in tokens if t.lower() in haystack}

    cited = set(re.findall(CITATION_PATTERN, answer))
    context_sources = set(re.findall(r"\[source:\s*(S\d{2})\]", context))
    cited_ok = cited & context_sources

    return {
        "task": task_id,
        "config": config,
        "answer_chars": len(answer),
        "grounding": {
            "verifiable_tokens": len(tokens),
            "grounded": len(grounded),
            "ratio": round(len(grounded) / len(tokens), 3) if tokens else None,
            "ungrounded_tokens": sorted(tokens - grounded),
        },
        "citations": {
            "cited": len(cited),
            "valid": len(cited_ok),
            "ratio": round(len(cited_ok) / len(cited), 3) if cited else None,
            "invalid_citations": sorted(cited - context_sources),
        },
        "indicators": {
            name: bool(re.search(pattern, answer)) for name, pattern in INDICATORS.items()
        },
    }


def main() -> int:
    tasks = json.loads((HERE / "tasks.json").read_text(encoding="utf-8"))
    configs = tasks["configs"]

    scores, missing = [], []
    for task in tasks["tasks"]:
        for config in configs:
            result = score_cell(task["id"], config, task.get("prompt", ""))
            if result is None:
                missing.append(f"{task['id']}_c{config}")
            else:
                scores.append(result)

    (HERE / "scores.json").write_text(
        json.dumps({"scores": scores, "missing_cells": missing}, indent=2, ensure_ascii=False),
        encoding="utf-8")

    print(f"{'cell':<10} {'chars':>6} {'grounding':>16} {'citations':>14}  indicators")
    print("-" * 78)
    for s in scores:
        g, c = s["grounding"], s["citations"]
        gs = f"{g['grounded']}/{g['verifiable_tokens']}" if g["verifiable_tokens"] else "n/a"
        cs = f"{c['valid']}/{c['cited']}" if c["cited"] else "none"
        flags = "".join(k[0].upper() if v else "." for k, v in s["indicators"].items())
        print(f"{s['task']}_c{s['config']:<6} {s['answer_chars']:>6} {gs:>16} {cs:>14}  {flags}")
    print("\nindicator flags: E=explicit decision  N=names uncertainty  "
          "R=requests more info  S=states confidence")
    if missing:
        print(f"\nMISSING CELLS ({len(missing)}): {', '.join(missing)}")
    print(f"\n{len(scores)}/{len(tasks['tasks']) * len(configs)} cells scored")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
