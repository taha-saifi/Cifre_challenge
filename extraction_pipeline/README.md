# Auditable non-LLM open-KG extraction

This standalone pipeline reads only `../corpus/clean/S*.json`; it never reads or
modifies the legacy extractor or `kg/` directory.

Run the complete workflow from the repository root:

```bash
python3 extraction_pipeline/scripts/run_pipeline.py
```

The workflow is `corpus → structured/OpenIE assertions → open KG → relation
inventory → deterministic clustering → human validation → canonical KG`.

Structured NVD and EPSS records are read directly from their JSON paths. Every
assertion retains its source, evidence, extraction method, JSON path or chunk
ID, polarity, and modality. EPSS observations are separate entities, so EPSS
probability is never treated as severity.

## MinIE setup and test

The official GPL-3.0 MinIE source is vendored in `vendor/minie`; its Maven
repository is isolated at `.m2`. Java and Maven are required. Build once:

```bash
cd extraction_pipeline/vendor/minie
mvn -ntp -Dmaven.repo.local=../../.m2 -DskipTests package
```

The vendored `.mvn/jvm.config` supplies the one Java 21 module-opening option
needed by MinIE's Java 8-era JAXB dependency; no system-wide Java change is
required.

Start the local HTTP service in a separate terminal:

```bash
python3 extraction_pipeline/scripts/start_minie_service.py
```

After updating this repository, stop a running service with `Ctrl+C` and start
it again so it loads the rebuilt MinIE JAR. The launcher refuses to start a
second service on the same port.

It binds only to `127.0.0.1:8080`, and the configured endpoint is
`http://127.0.0.1:8080/minie/query`. Verify the adapter before a full corpus
run:

```bash
python3 extraction_pipeline/scripts/test_minie.py
```

The expected response is written to `data/minie_smoke_test.json`. The pipeline
calls this local service when `config.OPENIE_BACKEND = "minie"`; its metadata
will then show `"minie"` as the actual backend. If the service is not running,
the run explicitly records the `heuristic` non-LLM fallback instead. An
alternative TSV stdin adapter can still be configured through `MINIE_COMMAND`.

MinIE is called once per eligible sentence, not once per source chunk. This
preserves exact sentence evidence and lets the pipeline discard table rows,
navigation fragments, and malformed MinIE triples before graph construction.
`data/openie_audit.json` records every extracted, skipped, empty, or failed
sentence with its source and chunk context.

Review `relation_clustering/clusters_review.md`, then edit
`relation_clustering/clusters_validation.json`. Set each reviewed cluster's
`decision` to `accept`, `reject`, or `split`. The pipeline automatically uses
the cluster heading (its representative relation in the review file) as the
canonical label for accepted clusters. `canonical_relation` is optional and
only needed to override that default. Then run:

```bash
python3 extraction_pipeline/scripts/apply_cluster_validation.py
python3 extraction_pipeline/scripts/build_canonical_kg.py
python3 extraction_pipeline/scripts/evaluate_pipeline.py
```

The canonical KG is deliberately empty until human review accepts clusters.
Optional gold triples in `evaluation/gold/*.json` use objects with `source`,
`predicate`, and `target` IDs to obtain precision and recall.
