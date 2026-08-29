"""Smoke-test the configured local MinIE service without changing KG outputs."""
import json
import re
from pathlib import Path
from pipeline_lib import minie_service_triples, write_json

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    source = json.loads((ROOT.parent / "corpus" / "clean" / "S41.json").read_text(encoding="utf-8"))
    sentence = next(item for item in re.split(r"(?<=[.!?])\s+", source["clean_text"])
                    if "CVE-2026-63520 can be chained to" in item)
    triples = minie_service_triples(sentence)
    if triples is None:
        raise SystemExit("MinIE is not reachable. Start scripts/start_minie_service.py first.")
    result = {"backend": "minie", "source_id": source["source_id"], "source_url": source.get("url"),
              "chunk_id": "S41_C03", "evidence": sentence, "sentence": sentence,
              "triples": [{"subject_raw": s, "predicate_raw": p, "object_raw": o} for s, p, o in triples]}
    write_json(ROOT / "data" / "minie_smoke_test.json", result)
    print(json.dumps(result, indent=2, ensure_ascii=False))
