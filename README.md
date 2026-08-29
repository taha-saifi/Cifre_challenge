# CIFRE Challenge — Impact of Knowledge Graph Quality on Trustworthy AI Systems

Mini documentary corpus and Knowledge Graph built for a CIFRE PhD thesis selection
challenge (SpotworkAI / LIPADE) on *"Impact of Knowledge Graph Quality on Trustworthy
AI Systems."* The use case is security-patch prioritization: five CVEs added to the
CISA Known Exploited Vulnerabilities (KEV) catalog in August 2026 —

- **CVE-2026-55040** / **CVE-2026-63520** — Microsoft SharePoint auth-bypass + RCE
  exploit chain
- **CVE-2026-33824** — Windows IKE Extensions double-free
- **CVE-2026-59310** — Broadcom VMware vCenter path traversal
- **CVE-2026-65400** — Apple macOS Screen Sharing auth bypass

The challenge brief is in `files/CIFRE_Challenge_SpotworkAI_LIPADE_*.pdf`.

## What's here

Two independent KG-building efforts over the same corpus, kept deliberately separate:

1. **`extraction_pipeline/`** — the main, currently active pipeline. Auditable,
   non-LLM, rule/statistical extraction (MinIE OpenIE + deterministic structured
   field mapping), with full provenance on every assertion and a human-reviewed
   relation-clustering step before anything becomes canonical. See
   [`extraction_pipeline/README.md`](extraction_pipeline/README.md) for how to run it
   and [`CLAUDE.md`](CLAUDE.md) for its architecture.
2. **`kg/` + `extract_regex.py`** — an earlier, paused mini-experiment comparing a
   regex-rules extractor against direct LLM extraction, for the thesis report's
   methodology section. Only the regex side (`kg/regex/`) was completed; the LLM
   side was interrupted mid-run and never finished. Kept as-is, not part of the
   current pipeline.

### Corpus pipeline (feeds both KG efforts)

```
build_corpus.py        # scrape ~57 real sources -> corpus/raw/  (never invents content)
preprocess_corpus.py   # dedup, noise filtering, chunking       -> corpus/clean/
```

Both scripts refuse to fabricate content on failure — anything that couldn't be
scraped is recorded in `corpus/failed_sources.json`, never silently skipped or
replaced with placeholder text.

### `exercices/`

Two small standalone warm-up scripts (toy KG triple store, toy TF-IDF RAG) — not
part of the deliverable, kept for reference.

## Setup

Requires Python 3.11+ and, only for `extraction_pipeline`'s MinIE backend, Java 21 +
Maven.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt   # trafilatura, playwright, requests, pdfplumber...
.venv/bin/playwright install chromium
```

`extraction_pipeline/` itself has **no external Python dependencies** (standard
library only) — its own `requirements.txt` documents that. See
[`extraction_pipeline/README.md`](extraction_pipeline/README.md) for the MinIE
build/run steps.

## Running the corpus pipeline

```bash
.venv/bin/python build_corpus.py       # -> corpus/raw/
.venv/bin/python preprocess_corpus.py  # -> corpus/clean/
```

## Running the KG pipeline

```bash
python3 extraction_pipeline/scripts/run_pipeline.py
```

See [`extraction_pipeline/README.md`](extraction_pipeline/README.md) for the full
workflow (including starting the local MinIE service first) and
[`extraction_pipeline/reports/`](extraction_pipeline/reports/) for the audit trail —
every correction made to the pipeline is documented there with before/after evidence,
not just applied silently.

## Working with Claude Code on this repo

[`CLAUDE.md`](CLAUDE.md) has the architecture notes and common commands for an agent
picking this up cold. The short version of the working style this project has kept
throughout: **never invent a fact** — every assertion in the KG traces back to a
`source_id` and exact evidence text from `corpus/clean/`; every non-trivial pipeline
change is applied with a before/after archive under `extraction_pipeline/archive/`
and written up in `extraction_pipeline/reports/`, not just applied and forgotten.
