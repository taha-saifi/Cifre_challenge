# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Corpus pipeline (project root, needs `.venv` from `requirements.txt`):
```bash
.venv/bin/python build_corpus.py       # scrape -> corpus/raw/  (never fabricates on failure; see corpus/failed_sources.json)
.venv/bin/python preprocess_corpus.py  # clean/dedup/chunk -> corpus/clean/
```

KG pipeline (`extraction_pipeline/`, stdlib-only, no venv needed):
```bash
# One-time MinIE build (Java 21 + Maven required):
cd extraction_pipeline/vendor/minie && mvn -ntp -Dmaven.repo.local=../../.m2 -DskipTests package

# Start the local OpenIE service before any run that needs it (separate terminal):
python3 extraction_pipeline/scripts/start_minie_service.py   # binds 127.0.0.1:8080 only

# Full pipeline, in dependency order:
python3 extraction_pipeline/scripts/run_pipeline.py

# After hand-editing relation_clustering/clusters_validation.json:
python3 extraction_pipeline/scripts/apply_cluster_validation.py
python3 extraction_pipeline/scripts/build_canonical_kg.py
python3 extraction_pipeline/scripts/evaluate_pipeline.py
```

Experiment harness and deliverables (`experiments/`, stdlib-only; needs `.venv` only for
the document exports):
```bash
python -m venv .venv && .venv/Scripts/python -m pip install -r requirements-deliverables.txt

# ALWAYS run this first after touching anything upstream of the protocol:
.venv/Scripts/python experiments/build_contexts.py --verify   # must print PASS 10/10

.venv/Scripts/python experiments/carrier_check.py --apply     # recompute ablation targets
.venv/Scripts/python experiments/build_contexts.py            # -> experiments/contexts/
.venv/Scripts/python experiments/score.py                     # -> experiments/scores.json
.venv/Scripts/python experiments/build_report.py              # -> deliverables/resultats.md
.venv/Scripts/python experiments/build_presentation_view.py   # -> presentation_view.json
.venv/Scripts/python experiments/build_source_quality.py      # -> deliverables/sources.md
.venv/Scripts/python experiments/build_docx.py                # -> note.docx, measures real pages
.venv/Scripts/python experiments/build_pptx.py                # -> deck.pptx
```

Interactive demonstrator (`demo_server/`; needs `demo_server/requirements.txt`, plus
`requirements.txt` for live ingestion, plus a gitignored root `.env` carrying
`OPENROUTER_API_KEY`):
```bash
.venv/Scripts/python -m pip install -r demo_server/requirements.txt
.venv/Scripts/python demo_server/app.py            # 127.0.0.1:5000
.venv/Scripts/python demo_server/build_demo_kg.py  # regenerate the demo_kg/ projection
.venv/Scripts/python demo_server/rag.py demo_kg    # rebuild one RAG embedding index
```

On this machine the interpreter is `python` (3.14.x), not `python3`, and the console is
cp1252 — always pass `encoding="utf-8"` explicitly when reading repo JSON.

Individual stage scripts under `extraction_pipeline/scripts/` (`extract_structured.py`,
`extract_openie.py`, `extract_entities.py`, `resolve_entities.py`, `build_open_kg.py`,
`build_relation_inventory.py`, `normalize_relations.py`, `cluster_relations.py`,
`export_clusters_for_review.py`) each run one stage in isolation for debugging — all
logic lives in `pipeline_lib.py`, these are thin entry points.

No automated test suite. Correctness is verified per change with targeted before/after
comparisons (see `extraction_pipeline/reports/` and the `archive/` snapshots below) —
follow that pattern rather than adding an ad hoc test file.

## Architecture

### Five top-level areas — do not conflate them

- **`corpus/`** — 56 cleaned sources with provenance. Frozen.
- **`extraction_pipeline/`** — the KG builder: rule/statistical extraction only (MinIE
  OpenIE + deterministic structured-field mapping), never an LLM call. This is what
  `run_pipeline.py` builds. Frozen at 2123 canonical edges (see above).
- **`experiments/`** — the §13 experimental protocol run *on top of* the frozen KG:
  task definitions, context builder, carrier analysis, scoring. Reads
  `extraction_pipeline/` and never writes to it.
- **`deliverables/`** — the three artefacts the challenge actually asks for (note, deck,
  demonstrator) plus generated supporting tables. Written in **French**; the code, its
  comments and the commit messages stay in English.
- **`demo_server/`** — the interactive demonstrator (Flask, 127.0.0.1 only). It is an
  *exploration tool built on the same prompt contract*, not a replay of the 45 cells: same
  template across the five configurations, different transport and different model. It
  reads `demo_kg/` (a `source_id` projection of the frozen graph — never a re-extraction,
  see the docstring of `build_demo_kg.py` for why a re-run would manufacture a false gap
  signal) and `live_kg/` (session-ingested sources, isolated, marked heuristic-quality and
  never merged into `demo_kg/`). `live_corpus/` and `live_kg/` are gitignored working
  state. Nothing here may write into `extraction_pipeline/` — that is what
  `redirected_config()` in `live_pipeline.py` enforces, under a lock.

**`kg/` has been deleted.** It held an abandoned mini-experiment comparing regex
extraction against direct LLM extraction; only the regex half finished and it fed nothing.
Its generator `extract_regex.py` is still at the project root and is now **dead code** —
it writes to `kg/regex/`, which no longer exists. Don't run it, don't build on it. Older
reports under `extraction_pipeline/reports/` still mention `kg/`; those are historical
audit records describing a past state and are deliberately left unedited.

### `extraction_pipeline/` staged flow

```
corpus/clean/*.json
  -> extract_structured()  (NVD/EPSS JSON field mapping + a few hand-scoped regex
                             extractors for HTML pages with a fixed field layout,
                             e.g. MSRC's Exploitability table)
  -> extract_openie()      (MinIE, sentence-batched, with a heuristic regex fallback
                             when MinIE is unavailable — never silently "no data")
  -> extract_entities() / resolve_entities()
  -> build_open_kg()       (every resolved edge, unfiltered)
  -> build_relation_inventory() / normalize_relations() / cluster_relations()
  -> export_clusters_for_review()   (human gate, see below)
  -> build_canonical_kg()  (only clusters marked "accept"/"split" in
                             clusters_validation.json become canonical edges)
  -> evaluate_pipeline()
```

Every assertion at every stage carries `source_id` + verbatim `evidence` text back to
`corpus/clean/`. A source that yields nothing gets an explicit audit status
(`skipped` / `no_triples` / `failed` in `data/openie_audit.json`) with a reason —
never a silent gap. Preserve this on any change to `pipeline_lib.py`.

### Relation clustering has a human-review gate — never bulk-accept

`cluster_relations()` groups raw predicate phrases (e.g. "add"/"added"/"adds") by
Jaccard similarity on normalized tokens. `export_clusters_for_review()` writes
`relation_clustering/clusters_validation.json`, and only clusters a human has marked
`"decision": "accept"` (or `"split"`, see below) flow into `canonical_kg/` via
`build_canonical_kg()`. **Do not accept clusters in bulk to raise coverage numbers** —
an early rubber-stamp pass (1419/1423 clusters auto-accepted) produced two of the
largest "relations" in the graph being bare copulas ("is", "has") with zero semantic
content; see `extraction_pipeline/reports/audit_report.md` for the full incident and
fix (`is_bare_auxiliary_predicate` filter in `pipeline_lib.py`).

**Cluster IDs are concept-stable, not content-hashed.** `cluster_id` is derived from
the normalized *dominant* member phrase (`cluster_concept_key()`), not a hash of the
full membership — hashing full membership meant any upstream extraction change (e.g.
a fix that surfaces new phrasings) silently invalidated hundreds of prior accept/
reject decisions with no trace. The exact-membership hash is kept as `content_id`
purely to detect drift: when a cluster's membership changes under a stable
`cluster_id`, `export_clusters_for_review()` downgrades it back to `pending`,
preserves the old decision in `previous_decision`, and writes an explicit
`diff: {added, removed}` — it never silently keeps a stale accept or silently drops
it. Clearing that state requires a human to add `"reconfirm": true` alongside the
decision; merely re-saving the same `"decision"` string is not treated as a fresh
look (this file format has no review timestamp to prove that it was). See
`extraction_pipeline/reports/cluster_id_stabilization.md`.

**Some clusters are polysemous, not just noisy** — the same surface predicate (e.g.
"added") can carry both a real, dated fact (`CISA added CVE-X to the KEV catalog`)
and an unrelated sense (`Microsoft added capabilities to the IKE protocol`) that no
Jaccard threshold will separate. For these, `"decision": "split"` plus a per-phrase
`split_assignments: {"phrase": "canonical label" | null}` map routes each raw phrase
individually (default is reject-by-null, so a partially filled split never leaks an
unreviewed phrase through). See `split_assignment_labels()` in `pipeline_lib.py` and
`extraction_pipeline/reports/cluster_dedup_final.md` for worked examples.

### MinIE batching needs restored sentence punctuation

`sentence_split()` strips trailing punctuation via `clean_surface()`. MinIE does
**not** treat a bare newline as a sentence boundary — a period-stripped,
newline-joined batch gets parsed as one run-on multi-clause sentence, silently
corrupting unrelated triples in the same batch. `ensure_terminal_punctuation()` in
`pipeline_lib.py` restores a period before building `batch_text`, but never touches
the stored `evidence` field (MinIE's own returned `sentence` is re-`clean_surface()`'d
before alignment, so this doesn't break exact-match alignment). If you touch the
MinIE batching path, keep this — removing it silently reintroduces cross-sentence
contamination across the whole corpus, not just an isolated bug.

### `build_canonical_kg()` reads `open_kg/`, not the raw assertion files

Adding new facts to `structured_assertions.json` or `openie_assertions.json` has no
effect on `canonical_kg/` until `extract_entities → resolve_entities → build_open_kg`
runs again — `build_canonical_kg()` never reads assertions directly. This has bitten
this exact pipeline before (a promoted fact stayed invisible in canonical output
despite a correct `"accept"` decision until `build_open_kg()` was rerun).

### Source authority is copied, never recomputed

There is exactly **one** source-scoring rule: `score_source()` in
`experiments/build_source_quality.py` (authority by declared category + primary/secondary
tier + accessibility by collection method, 0–12). It flows one way and is only ever
copied:

```
corpus/raw/S*.json  (source_type, extraction_method declared at collection)
  -> score_source()                       # the only place the score is computed
  -> preprocess_corpus.py                 # copies it into corpus/clean/ as source_authority
  -> build_canonical_kg()                 # source_authority_map(), a JOIN on source_id
  -> canonical_kg/edges.json              # every edge carries source_authority
  -> demo_kg/edges.json                   # inherited: demo_kg is a projection, no separate logic
```

Do **not** add a second scoring rule anywhere — `preprocess_corpus.py` imports the
function (via `sys.path` on `experiments/`) precisely so the §14.1 table in
`deliverables/sources.md` and the graph cannot disagree about the same source. A source
with no declared metadata (a `live_corpus/` session) joins to `None`, which is an explicit
"unknown" and must never be defaulted to a numeric score.

Two consequences to keep in mind:

- Adding the field to `clean/` does nothing until `build_canonical_kg()` runs again — the
  same staleness trap as everything else downstream of `open_kg/`.
- The score is **exposed, not used**: it is absent from the 45-cell protocol (pre-registered
  before it existed) and from context selection in `demo_server/`. Reweighting the recorded
  results with it is roadmap work and explicitly out of bounds — see
  `deliverables/note.md` §16.4. `build_contexts.py --verify` still passes 10/10 with the
  field present, because context rendering never reads edge metadata.

### Corpus structure

`corpus/clean/*.json` sources fall into two kinds, both handled by
`discover_sources()`: `source_kind: "structured"` (has `raw_json` — NVD CVE records
S02–S06, EPSS observations S21–S25) goes through direct field mapping with no OpenIE
involved; `"free_text"` (everything else, `clean_text` + optional `chunks`) goes
through sentence-splitting and MinIE. A source can have zero output from either path
if — and only if — its content genuinely doesn't support the schema; check
`data/corpus_inventory.json` / `data/openie_audit.json` before assuming a gap is a bug.

### The KG is FROZEN — do not rebuild it

`canonical_kg/` is pinned at **2123 edges** and the 45 experiment cells in
`experiments/results/` were produced against exactly that state. Rebuilding the graph
invalidates every one of them, and they cannot be cheaply re-run (each was a separate
isolated agent call, one shot, no retry). Two consequences:

- Treat `extraction_pipeline/` and `corpus/` as read-only unless the task is explicitly
  to re-open the extraction work. `evaluate_pipeline.py` is safe to re-run — it only
  rewrites `metrics.json` with an identical body and a new timestamp.
- `experiments/build_contexts.py --verify` is the tripwire: it rebuilds the 10 original
  Day-2 contexts from the current graph and compares them byte-for-byte to the frozen
  copies in `reports/experiment_contexts/`. If it stops printing `PASS: 0 mismatch(es)`,
  the graph moved under the protocol and the results are no longer comparable.

MinIE cannot run on the current machine anyway (no Java, no built JAR), so a rebuild
would silently fall back to the heuristic extractor and produce a different graph.

### `experiments/` — the §13 protocol, and why ablation needs carrier counting

Nine tasks × five configurations = 45 cells. The load-bearing idea is **carrier
counting**: before removing a fact to measure its impact, count how many canonical edges
carry it. The Day-2 run removed two edges believing it had removed a relation; a third
explicit carrier survived, along with nine partial ones, and the decision predictably did
not move. `carrier_check.py` exists so that never happens silently again.

- A **Tier-1 carrier** is an edge whose `evidence` mentions every anchor of the fact. A
  **Tier-2 carrier** mentions at least one anchor plus `MIN_SHARED_TERMS` content words
  drawn *from the Tier-1 evidence* — the vocabulary is derived from data, never
  hand-authored, and the threshold is swept (2→5) and reported rather than tuned.
- `carrier_check.py --apply` **writes** the computed Tier-1 set into `tasks.json` as the
  ablation target for every task with `ablation_mode: "auto"`. Do not hand-edit
  `ablation_lines`. T1 (`historical`) and T2 (`scenario`) are deliberately exempt: T1 is
  frozen to reproduce Day 2, T2's fact is corpus-external.
- `decision_key.json` is **pre-registered** — written before any cell ran, derived only
  from structured fields. Do not amend it to match observed answers; that would destroy
  the one thing that makes "exactitude" a measurement.

Scoring never uses an LLM judge (§21 makes that an eliminating criterion). `score.py`
computes grounding and citation validity by string matching against each cell's exact
context; prudence and calibration are recorded as observable binary indicators, counted
not graded.

`deliverables/resultats.md` and `deliverables/sources.md` are **generated** by
`build_report.py` / `build_source_quality.py`. Fix numbers in the data and regenerate;
never edit those two files by hand.

### Known data defects — recorded, deliberately not fixed

See `experiments/data_quality_notes.md`. The two that will bite a reader first:

- **`canonical_kg/nodes.json` has 1956 entries but only 1867 distinct ids.** 87 ids are
  duplicated because the id is computed case-insensitively while the label is not
  ("Active" from S51 and "active" from S16 collide). Building a `{id: label}` dict — as
  every consumer here does — silently keeps whichever came last. **The correct node count
  is 1867**; older reports say 1956 and are counting rows, not entities.
- **Entity resolution is effectively inert**: 3699 mentions → 3697 canonical entities.
  This is why carrier detection works off `evidence` text rather than graph structure.

Both are fixable, neither is fixed, because fixing them means rebuilding the frozen KG.

### Audit trail discipline — keep it

Every non-trivial pipeline change in this repo's history was made with: a
before-state snapshot copied under `extraction_pipeline/archive/<name>_<timestamp>/`,
the code change, a targeted re-run, and a written comparison in
`extraction_pipeline/reports/<name>.md` with concrete before/after numbers (not just
"it's fixed now"). Follow this pattern for any change to the extraction or clustering
logic — it's how prior regressions in this exact codebase were caught (see the
`export_clusters_for_review()` bug that silently dropped `split_assignments` on
every re-export, found only because the before/after edge counts didn't match).
