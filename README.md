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

## The result in one paragraph

We built a knowledge graph from 56 real sources **without presupposing any relation
schema** — relations are discovered from the corpus, clustered, and validated by a human
before becoming canonical. We then measured how the graph's completeness changes an AI's
decisions, by removing specific facts and re-asking the same question across 45
experimental cells. The finding that organises everything else: **you cannot measure the
impact of a missing relation until you count how many edges carry that fact.** Our first
ablation removed a relation and nothing changed — not because the relation was
unimportant, but because nine other edges still carried the same information under
different labels. Removing a *singly*-carried fact does change the decision, cleanly.

## What's here

1. **`corpus/`** — 56 cleaned sources with provenance. Nothing is invented: anything that
   could not be scraped is recorded in `corpus/failed_sources.json`.
2. **`extraction_pipeline/`** — the KG builder. Auditable, non-LLM, rule/statistical
   extraction (MinIE OpenIE + deterministic structured field mapping), full provenance on
   every assertion, and a human-reviewed relation-clustering gate before anything becomes
   canonical. See [`extraction_pipeline/README.md`](extraction_pipeline/README.md) to run
   it and [`CLAUDE.md`](CLAUDE.md) for architecture.
3. **`experiments/`** — the experimental protocol run on top of the frozen graph: 9 tasks
   × 5 configurations, a reproducible context builder, carrier analysis, and scoring that
   uses **no LLM judge**. Stdlib only.
4. **`deliverables/`** — the three required artefacts (4-page note, 8-slide deck,
   demonstrator) plus generated tables. In French; the code stays in English.
5. **`demo_server/`** — the interactive demonstrator: a local Flask app that runs the five
   configurations in parallel on a question you type, over `demo_kg/` (a filtered
   projection of the frozen graph, never a re-extraction) or over `live_kg/` (sources
   ingested during the session, kept isolated and clearly marked heuristic-quality).

An earlier regex-vs-LLM mini-experiment (`kg/`) has been removed — only its regex half was
ever finished and it fed nothing. Its generator `extract_regex.py` remains at the root as
dead code, writing to a directory that no longer exists.

## Key numbers

| | |
|---|---|
| Sources (cleaned / declared) | 56 / 57, in **9 principal source families** |
| Assertions | 4122 OpenIE + 279 structured |
| Canonical graph | **2123 edges**, 1867 distinct nodes |
| Relation clusters | 2111 — 944 accepted, 11 rejected, 2 split, **1154 still pending** |
| Experiment | 9 tasks × 5 configs = **45 cells**, one call each, no retries |
| Exactitude (LLM alone → full KG) | **3/9 → 9/9** |
| Verifiable facts produced (LLM alone → KG-aware) | **16 → 556** |

## The experimental protocol

Five configurations per task: LLM alone · full KG · ablated KG · pre-validation KG ·
ablated KG with an explicit uncertainty notice. The decision prompt is **identical across
all five**; only the context varies. Every cell was run by an isolated agent with no
knowledge of the protocol.

Three properties make the results defensible rather than merely plausible:

- **The ablation target is computed, not chosen.** `carrier_check.py` finds every edge
  carrying the fact and removes the whole set.
- **The answer key is pre-registered.** `experiments/decision_key.json` was frozen before
  any cell ran, derived only from structured fields.
- **No LLM grades anything** — an explicitly eliminating criterion in the brief. Grounding
  and citation validity are computed by string matching against each cell's exact context.

```bash
.venv/Scripts/python experiments/build_contexts.py --verify   # must print PASS 10/10
```

This is the tripwire: it rebuilds the original contexts from the current graph and
compares them byte-for-byte. **The KG is frozen at 2123 edges** — the 45 cells were
produced against exactly that state, and rebuilding it invalidates all of them.

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

## Setup — exact steps

Requires **Python 3.11+** (developed on 3.14.2). Paths below use the Windows layout
(`.venv/Scripts/`); on Linux/macOS substitute `.venv/bin/`.

### Step 1 — virtual environment

```bash
python -m venv .venv
```

### Step 2 — install what you actually need

There are four dependency sets, deliberately separate. Install only the ones for the
task at hand; none of them is required to *read* the results.

```bash
.venv/Scripts/python -m pip install -r requirements-deliverables.txt
```

| File | Needed for | Contents |
|---|---|---|
| `requirements-deliverables.txt` | exporting the note/deck, presentation subgraph | python-docx, python-pptx, pdfplumber, networkx |
| `demo_server/requirements.txt` | the interactive demonstrator | flask, requests, python-dotenv |
| `requirements.txt` | re-scraping the corpus, and live ingestion in the demo | trafilatura, playwright, requests, pdfplumber, readability-lxml |
| `extraction_pipeline/requirements.txt` | nothing | **empty by design** — the pipeline is standard library only, and so is `experiments/` |

Playwright also needs its browser binary once, and only if you re-scrape or ingest live
sources (10 sources of the frozen corpus required a browser after a 403):

```bash
.venv/Scripts/python -m playwright install chromium
```

### Step 3 — MinIE (only to re-extract)

The OpenIE backend needs **Java 21 + Maven**, built once:

```bash
cd extraction_pipeline/vendor/minie && mvn -ntp -Dmaven.repo.local=../../.m2 -DskipTests package
```

Then start the service in a separate terminal before any extraction run — it binds
`127.0.0.1:8080` only, so no corpus text leaves the machine:

```bash
python extraction_pipeline/scripts/start_minie_service.py
```

Without MinIE the pipeline falls back to a heuristic extractor **and records that it
did** (`data/openie_run_metadata.json`) — it never silently pretends to have run MinIE.

### Step 4 — model API key (only for the interactive demonstrator)

The demonstrator calls OpenRouter. Create a local `.env` at the repo root — it is
gitignored and must never be committed:

```
OPENROUTER_API_KEY=<your key>
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

Nothing else in the repo needs a key. The extraction pipeline never calls a model, and
the 45 experiment cells are already recorded.

## Running things — exact steps

### A. Read the results (no install, no key)

`deliverables/` and `experiments/scores.json` are committed. Nothing needs to run.

### B. Verify and re-score the experiment (safe)

Reads the frozen graph; writes only under `experiments/` and `deliverables/`.
**Run the tripwire first, every time.**

```bash
.venv/Scripts/python experiments/build_contexts.py --verify   # must print PASS 10/10
```

```bash
.venv/Scripts/python experiments/carrier_check.py             # carrier profile per task
.venv/Scripts/python experiments/score.py                     # -> experiments/scores.json
.venv/Scripts/python experiments/build_report.py              # -> deliverables/resultats.md
.venv/Scripts/python experiments/build_source_quality.py      # -> deliverables/sources.md
.venv/Scripts/python experiments/build_presentation_view.py   # -> presentation_view.json
.venv/Scripts/python experiments/build_docx.py                # -> note.docx (+ measures pages)
.venv/Scripts/python experiments/build_pptx.py                # -> deck.pptx
```

`carrier_check.py --apply` additionally rewrites the ablation targets in `tasks.json`;
run it that way only if an upstream change should move them.

### C. The interactive demonstrator

```bash
.venv/Scripts/python -m pip install -r demo_server/requirements.txt
.venv/Scripts/python demo_server/app.py       # http://127.0.0.1:5000
```

Ask a question against `demo_kg` (a filtered projection of the frozen graph) or against
`live_kg` (sources you ingest in the session), and the five configurations answer side by
side. Live ingestion also needs `requirements.txt` installed. `demo_kg/` is regenerated
by `.venv/Scripts/python demo_server/build_demo_kg.py`; `deliverables/demo.html` is the
separate scripted 2-case demo and needs no server.

### D. Rebuilding the corpus or the KG — read this first

**Rebuilding the KG invalidates the 45 experiment cells**, which were produced against the
current 2123-edge graph and cannot be cheaply re-run. In dependency order:

```bash
.venv/Scripts/python build_corpus.py                          # -> corpus/raw/
.venv/Scripts/python preprocess_corpus.py                     # -> corpus/clean/
python extraction_pipeline/scripts/run_pipeline.py            # -> canonical_kg/
```

Between clustering and the canonical graph there is a **human gate**: after hand-editing
`extraction_pipeline/relation_clustering/clusters_validation.json`, re-run

```bash
python extraction_pipeline/scripts/apply_cluster_validation.py
python extraction_pipeline/scripts/build_canonical_kg.py
python extraction_pipeline/scripts/evaluate_pipeline.py
```

Then run `experiments/build_contexts.py --verify` again: if it stops passing, the graph
moved under the protocol and the recorded results are no longer comparable.

`preprocess_corpus.py` also copies each source's declared category, primary/secondary
rank, collection method and **authority score** into `corpus/clean/`, and
`build_canonical_kg()` joins that score onto every edge as `source_authority` (inherited
by `demo_kg/` for free, since it is a projection). The score itself is computed in one
place only — `score_source()` in `experiments/build_source_quality.py`, which
`preprocess_corpus.py` imports rather than restates. It is exposed on the graph but
**not yet used** by the 45-cell protocol or by answer generation; that is declared
roadmap work, not a retroactive reweighting of recorded results.

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

The same rule governs the experiment: results are recorded before they are interpreted,
and a conclusion that turns out to be unsupported is **withdrawn rather than rewritten**.
Known defects are written down instead of quietly fixed — see
[`experiments/data_quality_notes.md`](experiments/data_quality_notes.md), which records
among other things that the canonical graph has 1956 node rows but only **1867 distinct
node ids** (87 case-collision duplicates), and that entity resolution merges almost
nothing (3699 mentions → 3697 entities).
