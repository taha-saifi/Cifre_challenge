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

Individual stage scripts under `extraction_pipeline/scripts/` (`extract_structured.py`,
`extract_openie.py`, `extract_entities.py`, `resolve_entities.py`, `build_open_kg.py`,
`build_relation_inventory.py`, `normalize_relations.py`, `cluster_relations.py`,
`export_clusters_for_review.py`) each run one stage in isolation for debugging — all
logic lives in `pipeline_lib.py`, these are thin entry points.

No automated test suite. Correctness is verified per change with targeted before/after
comparisons (see `extraction_pipeline/reports/` and the `archive/` snapshots below) —
follow that pattern rather than adding an ad hoc test file.

## Architecture

### Two independent KG efforts — do not conflate them

- **`extraction_pipeline/`** is the active pipeline: rule/statistical extraction only
  (MinIE OpenIE + deterministic structured-field mapping), never an LLM call. This is
  what `run_pipeline.py` builds.
- **`kg/` + `extract_regex.py`** (project root) is a separate, paused mini-experiment
  comparing regex-rules extraction against direct LLM extraction, for the thesis
  report's methodology section. Only the regex half (`kg/regex/`) finished; nothing
  here feeds `extraction_pipeline/`, and `extraction_pipeline/README.md` states
  explicitly that it never reads `kg/`. Don't wire them together without being asked.

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

### Corpus structure

`corpus/clean/*.json` sources fall into two kinds, both handled by
`discover_sources()`: `source_kind: "structured"` (has `raw_json` — NVD CVE records
S02–S06, EPSS observations S21–S25) goes through direct field mapping with no OpenIE
involved; `"free_text"` (everything else, `clean_text` + optional `chunks`) goes
through sentence-splitting and MinIE. A source can have zero output from either path
if — and only if — its content genuinely doesn't support the schema; check
`data/corpus_inventory.json` / `data/openie_audit.json` before assuming a gap is a bug.

### Audit trail discipline — keep it

Every non-trivial pipeline change in this repo's history was made with: a
before-state snapshot copied under `extraction_pipeline/archive/<name>_<timestamp>/`,
the code change, a targeted re-run, and a written comparison in
`extraction_pipeline/reports/<name>.md` with concrete before/after numbers (not just
"it's fixed now"). Follow this pattern for any change to the extraction or clustering
logic — it's how prior regressions in this exact codebase were caught (see the
`export_clusters_for_review()` bug that silently dropped `split_assignments` on
every re-export, found only because the before/after edge counts didn't match).
