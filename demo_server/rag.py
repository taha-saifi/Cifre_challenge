#!/usr/bin/env python3
"""Documentary RAG over a chosen corpus (demo_corpus or live_corpus), real embeddings.

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
CORPORA = {
    "demo_kg": ROOT / "demo_corpus" / "clean",
    "live_kg": ROOT / "live_corpus" / "clean",
}
HERE = Path(__file__).resolve().parent


def corpus_dir(source: str) -> Path:
    return CORPORA.get(source, CORPORA["demo_kg"])


def index_path(source: str) -> Path:
    """One cache per corpus: the live corpus changes on every ingestion."""
    return HERE / f"rag_index_{source}.json"

# Passage sizing: long enough to carry a fact with its qualifiers, short enough that
# top-k stays readable next to the KG columns.
TARGET_CHARS = 700
MIN_CHARS = 120
# Hard ceiling. The model rejects >512 tokens (HTTP 400), and a character cap cannot
# guarantee a token count: dense hex/base64 stretches in this corpus reach ~1.3 chars per
# token, so 1000 chars produced 764 tokens. 600 chars keeps the worst case near 460 tokens.
# A char cap is still only an estimate, which is why build_index also survives rejections.
MAX_CHARS = 600
TOP_K = 5


def _hard_split(block: str) -> list[str]:
    """Cut an over-long block on whitespace, never above MAX_CHARS.

    The embedding model rejects inputs over 512 tokens with HTTP 400. Dense technical prose
    runs about 2.6 chars/token, so MAX_CHARS stays well under that ceiling. Splitting is
    used rather than truncating: dropping the tail of a passage would silently remove text
    from the corpus being searched.
    """
    if len(block) <= MAX_CHARS:
        return [block]
    pieces, current = [], ""
    for word in block.split():
        # A single unbroken token can itself exceed the cap -- a long URL, a base64 blob,
        # a certificate. Whitespace splitting alone cannot help, so slice it.
        for fragment in ([word] if len(word) <= MAX_CHARS else
                         [word[i:i + MAX_CHARS] for i in range(0, len(word), MAX_CHARS)]):
            if len(current) + len(fragment) + 1 > MAX_CHARS:
                if current:
                    pieces.append(current)
                current = fragment
            else:
                current = f"{current} {fragment}".strip()
    if current:
        pieces.append(current)
    return pieces


def split_passages(text: str) -> list[str]:
    """Cut clean_text into paragraph-ish passages of roughly TARGET_CHARS, capped hard."""
    blocks = [b.strip() for b in re.split(r"\n\s*\n|\n(?=[A-Z])", text) if b.strip()]
    passages, current = [], ""
    for block in blocks:
        for piece in _hard_split(block):
            if len(current) + len(piece) + 1 <= TARGET_CHARS:
                current = f"{current}\n{piece}".strip()
            else:
                if len(current) >= MIN_CHARS:
                    passages.append(current)
                current = piece
    if len(current) >= MIN_CHARS:
        passages.append(current)
    # Belt and braces: nothing leaves this function above the cap.
    return [p for chunk in passages for p in _hard_split(chunk)]


def build_index(source: str = "demo_kg", force: bool = False) -> dict:
    """Embed every passage of the chosen corpus, cache to disk per corpus.

    The live corpus is re-ingested constantly, so its index is invalidated whenever the
    set of source files no longer matches what was indexed.
    """
    path_cache = index_path(source)
    present = sorted(p.stem for p in corpus_dir(source).glob("S*.json"))
    if path_cache.exists() and not force:
        with path_cache.open(encoding="utf-8") as handle:
            cached = json.load(handle)
        if cached.get("sources") == present:
            return cached

    records = []
    for path in sorted(corpus_dir(source).glob("S*.json")):
        with path.open(encoding="utf-8") as handle:
            doc = json.load(handle)   # not `source`: that name is the corpus selector
        for i, passage in enumerate(split_passages(doc.get("clean_text", ""))):
            records.append({"source_id": doc["source_id"],
                            "source_name": doc.get("source_name", ""),
                            "passage_index": i, "text": passage})

    # Batch to keep each request modest. A batch can still be refused if one passage is
    # denser than the character cap predicted; in that case fall back to embedding the
    # batch one passage at a time and drop only what the model actually refuses. Losing
    # the whole index because of a single dense blob would be the wrong failure mode.
    embedded, skipped = [], []
    for start in range(0, len(records), 32):
        batch = records[start:start + 32]
        try:
            for record, vector in zip(batch, embed([r["text"] for r in batch])):
                record["embedding"] = vector
                embedded.append(record)
        except Exception:  # noqa: BLE001 - retry individually to isolate the offender
            for record in batch:
                try:
                    record["embedding"] = embed([record["text"]])[0]
                    embedded.append(record)
                except Exception as exc:  # noqa: BLE001
                    skipped.append({"source_id": record["source_id"],
                                    "passage_index": record["passage_index"],
                                    "chars": len(record["text"]),
                                    "reason": str(exc)[:120]})
    records = embedded

    index = {"model": "liquid/lfm-2.5-embedding-350m:free",
             "passages": len(records),
             "sources": present,
             "skipped": skipped,
             "records": records}
    path_cache.write_text(json.dumps(index), encoding="utf-8")
    return index


def _cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


def retrieve(question: str, top_k: int = TOP_K, source: str = "demo_kg") -> list[dict]:
    """Top-k passages for a question, by cosine similarity on real embeddings."""
    index = build_index(source)
    query_vector = embed([question])[0]
    scored = [
        {"source_id": r["source_id"], "source_name": r["source_name"],
         "text": r["text"], "score": _cosine(query_vector, r["embedding"])}
        for r in index["records"]
    ]
    scored.sort(key=lambda r: -r["score"])
    return scored[:top_k]


def build_context(question: str, top_k: int = TOP_K,
                  source: str = "demo_kg") -> tuple[str, list[dict]]:
    """Render retrieved passages as a context block, in the same citation style as the KG."""
    hits = retrieve(question, top_k, source)
    if not hits:
        return "", []
    lines = ["Passages documentaires les plus proches de la question :", ""]
    for hit in hits:
        lines.append(f"[source: {hit['source_id']}] (similarité {hit['score']:.3f}) {hit['text']}")
        lines.append("")
    return "\n".join(lines).strip(), hits


if __name__ == "__main__":
    import sys
    which = sys.argv[1] if len(sys.argv) > 1 else "demo_kg"
    idx = build_index(which, force=True)
    print(f"[{which}] indexed {idx['passages']} passages from {len(idx['sources'])} sources")
    print(f"sources: {', '.join(idx['sources'])}")
    if idx.get("skipped"):
        print(f"REFUSES par le modele ({len(idx['skipped'])}) :")
        for entry in idx["skipped"][:5]:
            print(f"  {entry['source_id']}#{entry['passage_index']} "
                  f"({entry['chars']} car.) : {entry['reason'][:80]}")
