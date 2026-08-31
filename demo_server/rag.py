#!/usr/bin/env python3
"""Documentary RAG over the demo corpus, using real embeddings.

This is a genuine addition to the protocol, not a cosmetic column. The §13 list of
configurations includes "RAG documentaire simple" at position 2; the 45 recorded cells
never ran it, because the experiment had no retrieval component. Here it does retrieve:
passages are cut from `demo_corpus/clean/`, embedded with a dedicated embedding model,
and the top-k by cosine similarity are injected as context. If retrieval returned
nothing, the column would be indistinguishable from "LLM seul" and saying otherwise out
loud would be false -- so an empty retrieval is reported as such rather than silently
falling through.

The passage index is built once and cached on disk (`demo_server/rag_index.json`),
because embedding 10 sources on every request would make the demo unusable.
"""
from __future__ import annotations

import json
import math
import re
from pathlib import Path

from model_client import embed

ROOT = Path(__file__).resolve().parent.parent
DEMO_CLEAN = ROOT / "demo_corpus" / "clean"
INDEX_PATH = Path(__file__).resolve().parent / "rag_index.json"

# Passage sizing: long enough to carry a fact with its qualifiers, short enough that
# top-k stays readable next to the KG columns.
TARGET_CHARS = 700
MIN_CHARS = 120
TOP_K = 5


def split_passages(text: str) -> list[str]:
    """Cut clean_text into paragraph-ish passages of roughly TARGET_CHARS."""
    blocks = [b.strip() for b in re.split(r"\n\s*\n|\n(?=[A-Z])", text) if b.strip()]
    passages, current = [], ""
    for block in blocks:
        if len(current) + len(block) + 1 <= TARGET_CHARS:
            current = f"{current}\n{block}".strip()
        else:
            if len(current) >= MIN_CHARS:
                passages.append(current)
            current = block[:TARGET_CHARS * 2]
    if len(current) >= MIN_CHARS:
        passages.append(current)
    return passages


def build_index(force: bool = False) -> dict:
    """Embed every passage of the demo corpus once, cache to disk."""
    if INDEX_PATH.exists() and not force:
        with INDEX_PATH.open(encoding="utf-8") as handle:
            return json.load(handle)

    records = []
    for path in sorted(DEMO_CLEAN.glob("S*.json")):
        with path.open(encoding="utf-8") as handle:
            source = json.load(handle)
        for i, passage in enumerate(split_passages(source.get("clean_text", ""))):
            records.append({"source_id": source["source_id"],
                            "source_name": source.get("source_name", ""),
                            "passage_index": i, "text": passage})

    # Batch to keep each request modest.
    vectors = []
    for start in range(0, len(records), 32):
        vectors.extend(embed([r["text"] for r in records[start:start + 32]]))
    for record, vector in zip(records, vectors):
        record["embedding"] = vector

    index = {"model": "liquid/lfm-2.5-embedding-350m:free",
             "passages": len(records),
             "sources": sorted({r["source_id"] for r in records}),
             "records": records}
    INDEX_PATH.write_text(json.dumps(index), encoding="utf-8")
    return index


def _cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


def retrieve(question: str, top_k: int = TOP_K) -> list[dict]:
    """Top-k passages for a question, by cosine similarity on real embeddings."""
    index = build_index()
    query_vector = embed([question])[0]
    scored = [
        {"source_id": r["source_id"], "source_name": r["source_name"],
         "text": r["text"], "score": _cosine(query_vector, r["embedding"])}
        for r in index["records"]
    ]
    scored.sort(key=lambda r: -r["score"])
    return scored[:top_k]


def build_context(question: str, top_k: int = TOP_K) -> tuple[str, list[dict]]:
    """Render retrieved passages as a context block, in the same citation style as the KG."""
    hits = retrieve(question, top_k)
    if not hits:
        return "", []
    lines = ["Passages documentaires les plus proches de la question :", ""]
    for hit in hits:
        lines.append(f"[source: {hit['source_id']}] (similarité {hit['score']:.3f}) {hit['text']}")
        lines.append("")
    return "\n".join(lines).strip(), hits


if __name__ == "__main__":
    idx = build_index(force=True)
    print(f"indexed {idx['passages']} passages from {len(idx['sources'])} sources")
    print(f"sources: {', '.join(idx['sources'])}")
