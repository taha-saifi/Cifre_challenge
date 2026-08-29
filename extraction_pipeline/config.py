"""Configuration for the auditable, non-LLM extraction pipeline."""
from pathlib import Path

PIPELINE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PIPELINE_ROOT.parent
CORPUS_DIR = PROJECT_ROOT / "corpus" / "clean"
DATA_DIR = PIPELINE_ROOT / "data"
OPEN_KG_DIR = PIPELINE_ROOT / "open_kg"
CLUSTER_DIR = PIPELINE_ROOT / "relation_clustering"
CANONICAL_KG_DIR = PIPELINE_ROOT / "canonical_kg"
EVALUATION_DIR = PIPELINE_ROOT / "evaluation"
REPORTS_DIR = PIPELINE_ROOT / "reports"
LOG_DIR = PIPELINE_ROOT / "logs"

# "minie" tries MINIE_COMMAND first and records a deterministic fallback when it
# is unavailable.  This prevents silently claiming that MinIE was used.
OPENIE_BACKEND = "minie"  # minie | stanford | heuristic
# The official MinIE service is vendored at vendor/minie and listens locally.
# Keep this loopback-only endpoint; no corpus text leaves the machine.
MINIE_SERVICE_URL = "http://127.0.0.1:8080/minie/query"
MINIE_SERVICE_TIMEOUT_SECONDS = 120
MINIE_RETRY_COUNT = 1
MINIE_COMMAND = None      # Optional TSV-stdin command adapter, if preferred.
STANFORD_OPENIE_COMMAND = None
OPENIE_MAX_CHARS_PER_CHUNK = 12000
OPENIE_MAX_CHARS_PER_SENTENCE = 600
# Batches reduce MinIE overhead; every returned triple is aligned back to one
# source sentence before it becomes an assertion.
OPENIE_GRANULARITY = "sentence_evidence_batched"
MINIE_BATCH_SIZE = 8
MINIE_MIN_ALIGNMENT_SCORE = 0.55
FALLBACK_ON_MINIE_FAILURE = True

# These are surface-form aliases, not a relation ontology. Add reviewed aliases
# here only when they are useful for entity resolution in a new corpus.
ENTITY_ALIASES = {
    "microsoft sharepoint": "Microsoft SharePoint",
    "sharepoint server": "Microsoft SharePoint",
    "microsoft sharepoint server": "Microsoft SharePoint",
}
RELATION_JACCARD_THRESHOLD = 0.80
