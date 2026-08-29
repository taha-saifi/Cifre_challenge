"""Shared implementation for an auditable open-KG extraction workflow.

This module deliberately has no relation ontology and no model/API dependency.
It keeps original predicates, evidence, source paths, polarity and modality at
every stage.  The lightweight extractor is a runnable fallback for MinIE.
"""
from __future__ import annotations

import hashlib
import html
import json
import logging
import re
import subprocess
import sys
from urllib import error as urlerror
from urllib import request as urlrequest
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from xml.etree.ElementTree import Element, SubElement, ElementTree

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config

URL_RE = re.compile(r"https?://[^\s\]\[\)>,\"']+", re.I)
CVE_RE = re.compile(r"\bCVE[\s_-]?(\d{4})[\s_-]?(\d{4,7})\b", re.I)
CWE_RE = re.compile(r"\bCWE[\s_-]?(\d+)\b", re.I)
KB_RE = re.compile(r"\bKB\s?(\d{4,})\b", re.I)
DATE_RE = re.compile(r"\b(?:19|20)\d{2}-\d{2}-\d{2}\b")


def ensure_dirs() -> None:
    for path in (config.DATA_DIR, config.OPEN_KG_DIR, config.CLUSTER_DIR,
                 config.CANONICAL_KG_DIR, config.EVALUATION_DIR,
                 config.EVALUATION_DIR / "gold", config.REPORTS_DIR, config.LOG_DIR):
        path.mkdir(parents=True, exist_ok=True)


def configure_logging() -> None:
    ensure_dirs()
    logging.basicConfig(filename=config.LOG_DIR / "pipeline.log", level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s", force=True)


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, value: Any) -> None:
    ensure_dirs()
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def stable_id(prefix: str, *parts: object) -> str:
    text = "\x1f".join(str(part) for part in parts)
    return f"{prefix}_{hashlib.sha256(text.encode()).hexdigest()[:16]}"


def meaningful_raw(value: Any) -> bool:
    return value is not None and value != {} and value != [] and value != ""


def discover_sources() -> list[dict[str, Any]]:
    sources = []
    for path in sorted(config.CORPUS_DIR.glob("S*.json")):
        try:
            source = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            logging.warning("Skipping invalid source %s: %s", path, exc)
            continue
        if not isinstance(source, dict):
            logging.warning("Skipping non-object source %s", path)
            continue
        source["_path"] = str(path)
        source.setdefault("source_id", path.stem)
        source["source_kind"] = "structured" if meaningful_raw(source.get("raw_json")) else "free_text"
        sources.append(source)
    return sources


def inspect_corpus() -> dict[str, Any]:
    configure_logging()
    sources = discover_sources()
    rows = [{
        "source_id": s["source_id"], "source_name": s.get("source_name"), "url": s.get("url"),
        "kind": s["source_kind"], "has_clean_text": bool(s.get("clean_text")),
        "chunk_count": len(s.get("chunks") or []), "raw_json_type": type(s.get("raw_json")).__name__,
        "file": s["_path"],
    } for s in sources]
    result = {"generated_at": now(), "source_count": len(rows),
              "structured_count": sum(r["kind"] == "structured" for r in rows),
              "free_text_count": sum(r["kind"] == "free_text" for r in rows), "sources": rows}
    write_json(config.DATA_DIR / "corpus_inventory.json", result)
    lines = ["# Corpus inventory", "", f"Discovered **{len(rows)}** valid `S*.json` files.", "",
             "| Source | Class | Chunks | Name |", "|---|---|---:|---|"]
    lines += [f"| {r['source_id']} | {r['kind']} | {r['chunk_count']} | {r['source_name'] or ''} |" for r in rows]
    write_text(config.REPORTS_DIR / "corpus_inventory.md", "\n".join(lines) + "\n")
    return result


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_text(path: Path, text: str) -> None:
    ensure_dirs()
    path.write_text(text, encoding="utf-8")


def assertion(source: dict[str, Any], subject: str, predicate: str, obj: str,
              subject_type: str, object_type: str, json_path: str | None,
              evidence: str, method: str = "structured", polarity: str = "positive",
              modality: str = "asserted", chunk_id: str | None = None) -> dict[str, Any]:
    return {
        "assertion_id": stable_id("a", source["source_id"], json_path or chunk_id, subject, predicate, obj, evidence),
        "subject_raw": clean_surface(subject), "predicate_raw": clean_surface(predicate), "object_raw": clean_surface(obj),
        "subject_type_hint": subject_type, "object_type_hint": object_type,
        "source_id": source["source_id"], "source_url": source.get("url"), "chunk_id": chunk_id,
        "extraction_method": method, "json_path": json_path, "evidence": evidence,
        "polarity": polarity, "modality": modality,
    }


def clean_surface(value: object) -> str:
    return re.sub(r"\s+", " ", str(value)).strip(" \t\n.;")


def nvd_assertions(source: dict[str, Any]) -> list[dict[str, Any]]:
    raw, out = source["raw_json"], []
    for vi, vulnerability in enumerate(raw.get("vulnerabilities", [])):
        cve = vulnerability.get("cve", {})
        cve_id = cve.get("id")
        if not cve_id:
            continue
        base = f"raw_json.vulnerabilities[{vi}].cve"
        for field, label in (("published", "has published date"), ("lastModified", "has last modified date"),
                             ("vulnStatus", "has vulnerability status"), ("sourceIdentifier", "has source identifier")):
            if cve.get(field) is not None:
                out.append(assertion(source, cve_id, label, str(cve[field]), "CVE", "Date" if "date" in label else "Value",
                                     f"{base}.{field}", f"{field}: {cve[field]}"))
        for di, desc in enumerate(cve.get("descriptions", [])):
            if desc.get("value"):
                out.append(assertion(source, cve_id, "has description", desc["value"], "CVE", "Description",
                    f"{base}.descriptions[{di}].value", desc["value"]))
        for ai, affected in enumerate(cve.get("affected", [])):
            for pi, product in enumerate(affected.get("affectedData", [])):
                name = product.get("product")
                pbase = f"{base}.affected[{ai}].affectedData[{pi}]"
                if name:
                    out.append(assertion(source, cve_id, "has affected product", name, "CVE", "Product", f"{pbase}.product", name))
                if product.get("vendor") and name:
                    out.append(assertion(source, name, "has vendor", product["vendor"], "Product", "Vendor", f"{pbase}.vendor", product["vendor"]))
                for xi, version in enumerate(product.get("versions", [])):
                    val = version.get("lessThan") or version.get("version")
                    if name and val:
                        path = f"{pbase}.versions[{xi}]"
                        out.append(assertion(source, name, "has affected version bound", val, "Product", "Version",
                            f"{path}.lessThan" if version.get("lessThan") else f"{path}.version", json.dumps(version, ensure_ascii=False)))
        for wi, weakness in enumerate(cve.get("weaknesses", [])):
            for di, desc in enumerate(weakness.get("description", [])):
                if desc.get("value"):
                    out.append(assertion(source, cve_id, "has weakness", desc["value"], "CVE", "CWE",
                        f"{base}.weaknesses[{wi}].description[{di}].value", desc["value"]))
        for ri, ref in enumerate(cve.get("references", [])):
            url = ref.get("url")
            if url:
                out.append(assertion(source, cve_id, "references", url, "CVE", "URL", f"{base}.references[{ri}].url", url))
        for metric_name, metrics in cve.get("metrics", {}).items():
            for mi, metric in enumerate(metrics):
                data = metric.get("cvssData", {})
                mbase = f"{base}.metrics.{metric_name}[{mi}]"
                for field in ("baseScore", "baseSeverity", "vectorString", "attackVector", "attackComplexity",
                              "privilegesRequired", "userInteraction", "scope", "confidentialityImpact", "integrityImpact", "availabilityImpact"):
                    if data.get(field) is not None:
                        out.append(assertion(source, cve_id, f"has {field}", str(data[field]), "CVE", "Metric",
                            f"{mbase}.cvssData.{field}", f"{field}: {data[field]}"))
                for field in ("exploitabilityScore", "impactScore"):
                    if metric.get(field) is not None:
                        out.append(assertion(source, cve_id, f"has {field}", str(metric[field]), "CVE", "Metric",
                            f"{mbase}.{field}", f"{field}: {metric[field]}"))
                for oi, option in enumerate(metric.get("ssvcData", {}).get("options", [])):
                    for key, val in option.items():
                        out.append(assertion(source, cve_id, f"has SSVC {key}", str(val), "CVE", "Observation",
                            f"{mbase}.ssvcData.options[{oi}].{key}", f"{key}: {val}"))
        for field, label in (("cisaExploitAdd", "has CISA exploit addition date"), ("cisaActionDue", "has CISA action due date"),
                             ("cisaRequiredAction", "has CISA required action")):
            if cve.get(field):
                out.append(assertion(source, cve_id, label, str(cve[field]), "CVE", "Date" if "date" in label else "Mitigation",
                    f"{base}.{field}", str(cve[field])))
    return out


def epss_assertions(source: dict[str, Any]) -> list[dict[str, Any]]:
    raw, out = source["raw_json"], []
    for i, observation in enumerate(raw.get("data", [])):
        cve, date = observation.get("cve"), observation.get("date")
        if not cve:
            continue
        observation_id = f"EPSS observation for {cve} on {date or 'undated'}"
        base = f"raw_json.data[{i}]"
        out.append(assertion(source, observation_id, "observes", cve, "EPSS observation", "CVE", f"{base}.cve", json.dumps(observation, ensure_ascii=False)))
        for field, predicate in (("epss", "has EPSS probability"), ("percentile", "has EPSS percentile"), ("date", "has observation date")):
            if observation.get(field) is not None:
                out.append(assertion(source, observation_id, predicate, str(observation[field]), "EPSS observation",
                    "Date" if field == "date" else "Probability", f"{base}.{field}", f"{field}: {observation[field]}"))
    return out


def generic_structured_assertions(source: dict[str, Any]) -> list[dict[str, Any]]:
    """Schema-preserving last-resort adapter for unknown structured sources."""
    out, raw = [], source["raw_json"]
    subject = source.get("source_id", "structured record")
    def walk(value: Any, path: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items(): walk(child, f"{path}.{key}")
        elif isinstance(value, list):
            for idx, child in enumerate(value): walk(child, f"{path}[{idx}]")
        elif value is not None:
            out.append(assertion(source, subject, f"has {path.rsplit('.', 1)[-1]}", str(value), "Structured record", "Value", path, f"{path}: {value}"))
    walk(raw, "raw_json")
    return out


# MSRC vulnerability pages render a small "Exploitability assessment" table as
# isolated one-word/one-phrase lines: "Publicly disclosed" / "Yes"|"No" /
# "Exploited" / "Yes"|"No" / optionally "Exploitability assessment" / <text>.
# These fields are MSRC-specific (not CVSS sub-fields -- Attack Vector, Attack
# Complexity etc. on the same page duplicate the CVSS vector already captured
# from the NVD JSON structured sources) and too short individually to pass
# is_extractable_sentence(), so they never reached MinIE. Scoped to
# msrc.microsoft.com pages and this exact label sequence to avoid matching
# unrelated "Exploited"/"disclosed" prose elsewhere in the corpus.
MSRC_EXPLOITABILITY_RE = re.compile(
    r"Publicly disclosed\n(Yes|No)\nExploited\n(Yes|No)(?:\nExploitability assessment\n([^\n]+))?"
)


def msrc_exploitability_assertions(source: dict[str, Any]) -> list[dict[str, Any]]:
    url = source.get("url") or ""
    if "msrc.microsoft.com" not in url:
        return []
    match = MSRC_EXPLOITABILITY_RE.search(source.get("clean_text") or "")
    if not match:
        return []
    cve_ids = source.get("cve_ids") or []
    if len(cve_ids) != 1:
        return []
    cve_id = cve_ids[0]
    disclosed, exploited, assessment = match.groups()
    out = [
        assertion(source, cve_id, "has MSRC publicly disclosed status", disclosed, "CVE", "Value",
                  "msrc_exploitability.publicly_disclosed", match.group(0)),
        assertion(source, cve_id, "has MSRC exploited status", exploited, "CVE", "Value",
                  "msrc_exploitability.exploited", match.group(0)),
    ]
    if assessment:
        out.append(assertion(source, cve_id, "has MSRC exploitability assessment", assessment.strip(), "CVE", "Value",
                             "msrc_exploitability.assessment", match.group(0)))
    return out


def msrc_exploitability_captured_lines(source: dict[str, Any]) -> set[str]:
    """Clean-text lines already covered by msrc_exploitability_assertions() for this
    source -- excluded from the OpenIE stream so MinIE is never asked to parse a bare
    table label that was never a sentence."""
    if not msrc_exploitability_assertions(source):
        return set()
    return {"Publicly disclosed", "Exploited", "Exploitability assessment"}


# Two Rapid7 disclosure posts (S40, S41 -- grepped, no other source in the corpus
# matches) list vendor KB patches for a CVE as a bare bullet list with no verb per
# item, e.g. "The vendor has provided the following updates to remediate
# CVE-2026-55040.\n- KB5002882 - Microsoft SharePoint Server Subscription Edition
# (version 16.0.19725.20434).\n...". Tested against the live MinIE service both as
# isolated bullet fragments and rejoined with the intro sentence into one sentence
# ("...to remediate CVE-X: KB... - Product (version Y)."): neither produced a usable
# has_patch(CVE, KB) triple -- MinIE either drops the KB entirely or binds it to an
# unrelated "is version" fact, because a bullet item alone has no verb to anchor a
# relation. Extracted deterministically instead, same strategy as
# msrc_exploitability_assertions().
VENDOR_REMEDIATION_RE = re.compile(
    r"vendor has provided the following updates? to remediate (CVE-\d{4}-\d{4,7})\.?\n"
    r"((?:-\s*KB\d+[^\n]*\n?)+)", re.I)
KB_LIST_ITEM_RE = re.compile(r"-\s*(KB\d+\s*-\s*[^\n]+)")


def vendor_remediation_kb_assertions(source: dict[str, Any]) -> list[dict[str, Any]]:
    text = source.get("clean_text") or ""
    out = []
    for match in VENDOR_REMEDIATION_RE.finditer(text):
        cve_id = match.group(1)
        for item in KB_LIST_ITEM_RE.finditer(match.group(2)):
            out.append(assertion(source, cve_id, "has patch", clean_surface(item.group(1)), "CVE", "Advisory",
                                 "vendor_remediation_kb_list", item.group(0).strip(), "structured"))
    return out


def vendor_remediation_captured_lines(source: dict[str, Any]) -> set[str]:
    """Clean-text lines already covered by vendor_remediation_kb_assertions()."""
    text = source.get("clean_text") or ""
    lines = set()
    for match in VENDOR_REMEDIATION_RE.finditer(text):
        for item in KB_LIST_ITEM_RE.finditer(match.group(2)):
            lines.add(clean_surface(item.group(0)))
    return lines


# Individual CVE-specific facts promoted out of the `requires`, `allows`, and `publish`
# relation clusters after exact-triple dedup + per-triple classification (see
# reports/cluster_dedup_final.md). Each of these three clusters mixed a handful of
# complete, CVE-anchored facts with duplicated CVSS/SSVC glossary boilerplate or
# truncated heuristic fragments SHARING THE SAME predicate_raw string as the good
# facts, so no relation_clustering decision (accept/reject/split) could isolate them --
# split_assignments acts per member phrase, not per individual assertion. Extracted here
# by hand instead, each under its own canonical predicate rather than the noisy
# cluster's generic label, so they never re-collide with "requires"/"allows"/"publish"
# on a future re-cluster. evidence_contains is checked against the live source text
# before emitting, so a corpus change silently invalidating one of these is caught
# (logged and skipped) rather than fabricating a stale fact.
CLUSTER_REVIEW_PROMOTED_FACTS = [
    {"source_id": "S46", "cve_id": "CVE-2026-33824", "predicate": "requires attacker capability",
     "object_type": "Description",
     "object": "ability to send specially crafted IKE traffic to a vulnerable system",
     "evidence_contains": "An attacker only requires the ability to send specially crafted IKE traffic"},
    {"source_id": "S18", "cve_id": "CVE-2026-55040", "predicate": "has technical impact",
     "object_type": "Description", "object": "impersonation",
     "evidence_contains": "this vulnerability allows impersonation"},
    {"source_id": "S10", "cve_id": "CVE-2026-55040", "predicate": "has technical impact",
     "object_type": "Description",
     "object": "a lack of proper validation in SharePoint's JWT handling allows an unauthenticated attacker to forge JWT tokens and access the web application as a privileged account",
     "evidence_contains": "allows an unauthenticated attacker to forge JWT tokens"},
    {"source_id": "S17", "cve_id": "CVE-2026-59310", "predicate": "has technical impact",
     "object_type": "Description",
     "object": "the exploit allows an unauthenticated attacker with network access to the vCenter management interface to traverse directories beyond their intended boundaries and achieve remote code execution without credentials or user interaction",
     "evidence_contains": "The exploit allows an unauthenticated attacker with network access"},
    {"source_id": "S31", "cve_id": "CVE-2026-59310", "predicate": "has technical impact",
     "object_type": "Description",
     "object": "could allow a threat actor with network access to vCenter to execute arbitrary code",
     "evidence_contains": "could allow a threat actor with network access to vCenter to execute arbitrary code"},
    {"source_id": "S12", "cve_id": "CVE-2026-59310", "predicate": "has vendor advisory",
     "object_type": "Advisory", "object": "VMSA-2026-0006",
     "evidence_contains": "Broadcom initially published VMSA-2026"},
]


def cluster_review_promoted_assertions() -> list[dict[str, Any]]:
    sources = {s["source_id"]: s for s in discover_sources()}
    out = []
    for spec in CLUSTER_REVIEW_PROMOTED_FACTS:
        source = sources.get(spec["source_id"])
        text = (source or {}).get("clean_text") or ""
        if spec["evidence_contains"] not in text:
            logging.warning("cluster_review_promoted_assertions: expected text not found in %s, skipping %r",
                            spec["source_id"], spec["predicate"])
            continue
        out.append(assertion(source, spec["cve_id"], spec["predicate"], spec["object"], "CVE", spec["object_type"],
                             "cluster_review_dedup", spec["evidence_contains"], "structured"))
    return out


def extract_structured() -> list[dict[str, Any]]:
    configure_logging()
    result = []
    for source in discover_sources():
        if source["source_kind"] == "structured":
            raw = source["raw_json"]
            if isinstance(raw, dict) and raw.get("format") == "NVD_CVE": result.extend(nvd_assertions(source))
            elif isinstance(raw, dict) and isinstance(raw.get("data"), list) and all(isinstance(x, dict) and "epss" in x for x in raw["data"]): result.extend(epss_assertions(source))
            else: result.extend(generic_structured_assertions(source))
        else:
            result.extend(msrc_exploitability_assertions(source))
            result.extend(vendor_remediation_kb_assertions(source))
    result.extend(cluster_review_promoted_assertions())
    write_json(config.DATA_DIR / "structured_assertions.json", result)
    logging.info("Extracted %s structured assertions", len(result))
    return result


def sentence_split(text: str) -> list[str]:
    text = text.replace("\u00a0", " ").replace("\u2800", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n", text).strip()
    # Keep line boundaries: they help reject table rows, headings and navigation.
    units = re.split(r"(?<=[.!?])\s+(?=[A-Z\"“])|\n+", text)
    return [clean_surface(unit) for unit in units if clean_surface(unit)]


def is_extractable_sentence(sentence: str) -> tuple[bool, str | None]:
    """Reject presentation artefacts before sending text to MinIE."""
    stripped = clean_surface(sentence)
    lower = stripped.lower()
    if len(stripped) < 12 or len(stripped) > config.OPENIE_MAX_CHARS_PER_SENTENCE:
        return False, "length"
    if "|" in stripped or "quant_" in lower or "<table" in lower:
        return False, "table_or_placeholder"
    if URL_RE.fullmatch(stripped) or re.fullmatch(r"(?:figure|table)\s+\d+[:.]?.*", stripped, re.I):
        return False, "url_or_figure"
    if lower in {"overview", "workflow", "impact", "remediation", "references", "disclosure timeline", "credit"}:
        return False, "heading"
    if re.search(r"\b(?:learn more|cookie|privacy policy|subscribe|all rights reserved)\b", lower):
        return False, "navigation"
    if len(re.findall(r"[A-Za-z]", stripped)) < 8:
        return False, "insufficient_language"
    return True, None


# Words that carry no relation content on their own (copulas, auxiliaries,
# negation). A predicate built ENTIRELY from these words is not a relation --
# it is MinIE reporting a bare "is"/"has"/"are"/"be" because it could not find
# a real verb phrase. Audit finding: these bare-auxiliary predicates formed
# the two largest relation clusters (595 and 271 assertions for "is"/"has"
# alone) and offered no analytical value once canonicalized.
AUX_ONLY_WORDS = {"can", "could", "may", "might", "will", "would", "shall", "should",
                  "does", "do", "did", "is", "are", "was", "were", "been", "being", "be",
                  "has", "have", "had", "not", "n't"}


def is_bare_auxiliary_predicate(predicate: str) -> bool:
    words = re.findall(r"[a-z']+", predicate.lower())
    return bool(words) and all(word in AUX_ONLY_WORDS for word in words)


def is_usable_triple(triple: tuple[str, str, str]) -> tuple[bool, str | None]:
    subject, predicate, obj = (clean_surface(value) for value in triple)
    joined = " ".join((subject, predicate, obj)).lower()
    if min(len(subject), len(predicate), len(obj)) < 2:
        return False, "empty_component"
    if any(marker in joined for marker in ("quant_", "|", "<table", "learn more")):
        return False, "table_or_placeholder"
    # 160 chars let 158-char run-on clauses through (MinIE mis-parsing a whole
    # sentence as one "predicate"); p99 of real predicates is 85 chars, so 100
    # keeps essentially all genuine relations while rejecting that tail.
    if len(subject) > 240 or len(predicate) > 100 or len(obj) > 320:
        return False, "overlong_component"
    if not all(re.search(r"[A-Za-z0-9]", value) for value in (subject, predicate, obj)):
        return False, "nonlexical_component"
    if is_bare_auxiliary_predicate(predicate):
        return False, "bare_auxiliary_predicate"
    return True, None


def ensure_terminal_punctuation(sentence: str) -> str:
    """Restore sentence-ending punctuation stripped by clean_surface() -- but only in
    the text handed to MinIE, never in stored evidence.

    sentence_split() strips trailing "." via clean_surface() before units are later
    newline-joined into a MinIE batch. MinIE does not treat a bare newline as a
    sentence boundary: verified directly against the running service that a
    period-stripped, newline-joined batch gets parsed as one run-on multi-sentence
    clause (subjects/objects bleeding across unrelated sentences), while restoring the
    period yields one clean triple per sentence, correctly aligned. This affected not
    only bulleted-list continuations (S40/S41 patch KB numbers) but also a fully
    self-contained sentence (S17 Broadcom patch date) that returned "no_triples" only
    because it happened to sit inside a contaminated batch. Safe to apply everywhere:
    MinIE's returned "sentence" field is itself clean_surface()'d before comparison
    (see minie_service_response), so the added period never breaks exact-match
    alignment against the (period-less) stored unit["evidence"].
    """
    return sentence if sentence.rstrip().endswith((".", "!", "?", ":")) else sentence + "."


def polarity_modality(sentence: str) -> tuple[str, str]:
    lower = sentence.lower()
    polarity = "negative" if re.search(r"\b(no|not|never|without|cannot|can't|isn't|aren't|wasn't|weren't)\b", lower) else "positive"
    if re.search(r"\b(may|might|could|can|likely|possible|potentially)\b", lower): modality = "possible"
    elif re.search(r"\b(reported|according to|said|warned|announced)\b", lower): modality = "reported"
    elif re.search(r"\b(unclear|unknown|uncertain)\b", lower): modality = "uncertain"
    else: modality = "asserted"
    return polarity, modality


def chunks_for(source: dict[str, Any]) -> Iterable[tuple[str | None, str]]:
    chunks = source.get("chunks")
    if isinstance(chunks, list) and chunks:
        for index, chunk in enumerate(chunks, 1):
            if isinstance(chunk, str) and chunk.strip(): yield f"{source['source_id']}_C{index:02d}", chunk
    elif source.get("clean_text"):
        yield None, source["clean_text"]


def heuristic_triples(sentence: str) -> list[tuple[str, str, str]]:
    """Open surface-pattern extractor; predicates are copied from each sentence.

    Cues are grammatical constructions, not a finite cybersecurity relation set.
    """
    s = clean_surface(sentence.strip('"“”'))
    triples: list[tuple[str, str, str]] = []
    # Keeps a key OpenIE construction intact, including modal/passive wording.
    for match in re.finditer(r"\b(?P<sub>CVE[- ]\d{4}[- ]\d{4,7})\s+(?P<rel>(?:can|could|may|might)?\s*be\s+chained\s+(?:to|with))(?:\s+[^.;:]{0,100}?,)?\s+(?P<obj>CVE[- ]\d{4}[- ]\d{4,7})", s, re.I):
        triples.append((match["sub"], match["rel"], match["obj"]))
    # Generic clause patterns, retaining exactly the lexical relation phrase.
    patterns = [
        r"(?P<sub>(?:CVE[- ]\d{4}[- ]\d{4,7}|CWE[- ]\d+|KB\d+|[A-Z][^,;:.]{1,90}?))\s+(?P<rel>(?:can|could|may|might|will|does|do|is|are|was|were|has|have|had)?\s*(?:not\s+)?(?:allow(?:s|ed|ing)?|affect(?:s|ed|ing)?|exploit(?:s|ed|ing)?|patch(?:es|ed|ing)?|mitigat(?:es|ed|ing)?|disclos(?:es|ed|ing)?|publish(?:es|ed|ing)?|execut(?:e|es|ed|ing)|bypass(?:es|ed|ing)?|contain(?:s|ed|ing)|include(?:s|d|ing)|provid(?:es|ed|ing)|require(?:s|d|ing)|use(?:s|d|ing)|lead(?:s|ing)?\s+to|result(?:s|ed|ing)?\s+in|cause(?:s|d|ing)?|is\s+(?:not\s+)?(?:affected|patched|vulnerable|available)))\s+(?P<obj>[^.;:]{2,180})",
        r"(?P<sub>[^.;:]{2,100}?)\s+(?P<rel>has\s+(?:a|an)?\s*[^.;:]{1,50})\s+(?P<obj>\b(?:CVE|CWE|KB)[- ]?\d[^.;:]*)",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, s, re.I):
            sub, rel, obj = (clean_surface(match[x]) for x in ("sub", "rel", "obj"))
            if len(sub) > 1 and len(obj) > 1 and len(rel) > 1: triples.append((sub, rel, obj))
    return list(dict.fromkeys(triples))


def command_openie(command: list[str] | None, text: str) -> list[tuple[str, str, str]] | None:
    """Optional adapter: command must print TSV subject<TAB>relation<TAB>object."""
    if not command: return None
    try:
        result = subprocess.run(command, input=text, text=True, capture_output=True, timeout=120, check=True)
    except (OSError, subprocess.SubprocessError) as exc:
        logging.warning("Configured OpenIE command unavailable: %s", exc)
        return None
    triples = []
    for line in result.stdout.splitlines():
        fields = line.split("\t")
        if len(fields) >= 3: triples.append(tuple(clean_surface(x) for x in fields[:3]))
    return triples


def minie_service_response(text: str) -> tuple[list[dict[str, str]] | None, str | None]:
    """Call the official local MinIE service and preserve its surface triples.

    The second return value is a short failure reason for the extraction audit.
    """
    endpoint = getattr(config, "MINIE_SERVICE_URL", None)
    if not endpoint:
        return None, "endpoint_not_configured"
    body = text.encode("utf-8")
    failure = None
    payload = None
    for _ in range(config.MINIE_RETRY_COUNT + 1):
        request = urlrequest.Request(endpoint, data=body, method="POST",
            headers={"Content-Type": "text/plain; charset=utf-8", "Accept": "application/json"})
        try:
            with urlrequest.urlopen(request, timeout=config.MINIE_SERVICE_TIMEOUT_SECONDS) as response:
                payload = json.loads(response.read().decode("utf-8"))
            failure = None
            break
        except urlerror.HTTPError as exc:
            failure = f"http_{exc.code}"
        except (urlerror.URLError, TimeoutError, OSError, ValueError) as exc:
            failure = type(exc).__name__.lower()
    if payload is None:
        logging.info("MinIE service failed at %s: %s", endpoint, failure)
        return None, failure
    payload_facts = payload.get("facts", []) if isinstance(payload, dict) else []
    facts = []
    for fact in payload_facts:
        if isinstance(fact, dict) and all(fact.get(key) for key in ("subject", "predicate", "object")):
            facts.append({"subject": clean_surface(fact["subject"]), "predicate": clean_surface(fact["predicate"]),
                          "object": clean_surface(fact["object"]), "sentence": clean_surface(fact.get("sentence") or "")})
    for sentence in payload.get("failedSentences", []) if isinstance(payload, dict) else []:
        if isinstance(sentence, str) and sentence.strip():
            facts.append({"sentence": clean_surface(sentence), "error": "minie_parse_error"})
    return facts, None


def minie_service_triples(text: str) -> list[tuple[str, str, str]] | None:
    """Compatibility helper used by the isolated MinIE smoke test."""
    facts = minie_service_response(text)[0]
    return None if facts is None else [(fact["subject"], fact["predicate"], fact["object"]) for fact in facts if "subject" in fact]


def fact_parts(fact: Any) -> tuple[tuple[str, str, str], str | None]:
    if isinstance(fact, dict):
        return (fact["subject"], fact["predicate"], fact["object"]), fact.get("sentence") or None
    return tuple(fact), None


def text_tokens(value: str) -> set[str]:
    return {token for token in re.findall(r"[a-z0-9]+", value.lower()) if len(token) > 1 and token not in {"the", "a", "an", "to", "of", "and", "or", "for", "with", "by", "in", "on", "be", "is", "are", "was", "were"}}


def align_triple_to_sentence(triple: tuple[str, str, str], units: list[dict[str, Any]]) -> int | None:
    """Return a high-confidence sentence match for a MinIE triple."""
    components = [text_tokens(value) for value in triple]
    best_index, best_score = None, 0.0
    for index, unit in enumerate(units):
        sentence_tokens = text_tokens(unit["evidence"])
        coverage = [len(component & sentence_tokens) / len(component) if component else 0.0 for component in components]
        score = 0.45 * coverage[0] + 0.15 * coverage[1] + 0.40 * coverage[2]
        if coverage[0] >= 0.5 and coverage[2] >= 0.5 and score > best_score:
            best_index, best_score = index, score
    return best_index if best_score >= config.MINIE_MIN_ALIGNMENT_SCORE else None


def batches(items: list[dict[str, Any]], size: int) -> Iterable[list[dict[str, Any]]]:
    for index in range(0, len(items), size):
        yield items[index:index + size]


def extract_openie() -> list[dict[str, Any]]:
    configure_logging()
    assertions, actual_backends, audit, request_count = [], Counter(), [], Counter()
    command = config.MINIE_COMMAND if config.OPENIE_BACKEND == "minie" else config.STANFORD_OPENIE_COMMAND
    for source in discover_sources():
        if source["source_kind"] != "free_text":
            continue
        skip_lines = msrc_exploitability_captured_lines(source) | vendor_remediation_captured_lines(source)
        units, seen_evidence = [], set()
        for chunk_id, chunk in chunks_for(source):
            for sentence_index, sentence in enumerate(sentence_split(chunk[:config.OPENIE_MAX_CHARS_PER_CHUNK]), 1):
                audit_row = {"source_id": source["source_id"], "chunk_id": chunk_id,
                             "sentence_index": sentence_index, "evidence": sentence}
                if sentence in skip_lines:
                    audit.append({**audit_row, "status": "skipped", "reason": "captured_by_structured_extraction", "triple_count": 0})
                    continue
                eligible, reason = is_extractable_sentence(sentence)
                if not eligible:
                    audit.append({**audit_row, "status": "skipped", "reason": reason, "triple_count": 0})
                elif sentence not in seen_evidence:
                    seen_evidence.add(sentence)
                    units.append(audit_row)
        for group in batches(units, config.MINIE_BATCH_SIZE):
            batch_text = "\n".join(ensure_terminal_punctuation(unit["evidence"]) for unit in group)
            external, failure = None, None
            if config.OPENIE_BACKEND == "minie":
                external, failure = minie_service_response(batch_text)
                request_count["minie_batch_requests"] += 1
                if external is None:
                    # Isolate a bad input rather than losing a whole batch.
                    for unit in group:
                        single, single_failure = minie_service_response(ensure_terminal_punctuation(unit["evidence"]))
                        request_count["minie_single_retry_requests"] += 1
                        backend = "minie" if single is not None else "heuristic"
                        triples = single if single is not None else (heuristic_triples(unit["evidence"]) if config.FALLBACK_ON_MINIE_FAILURE else [])
                        usable = [fact_parts(fact)[0] for fact in triples if is_usable_triple(fact_parts(fact)[0])[0]]
                        actual_backends[backend] += 1
                        audit.append({**unit, "status": "extracted" if usable else ("no_triples" if single is not None else "failed"),
                                      "backend": backend, "fallback_reason": single_failure or failure, "triple_count": len(usable)})
                        for sub, rel, obj in usable:
                            polarity, modality = polarity_modality(unit["evidence"])
                            assertions.append(assertion(source, sub, rel, obj, infer_type(sub), infer_type(obj), None, unit["evidence"], backend, polarity, modality, unit["chunk_id"]))
                    continue
            elif config.OPENIE_BACKEND == "stanford":
                external = command_openie(command, batch_text)
                request_count["stanford_batch_requests"] += 1
            if external is None:
                # Stanford/unconfigured backends use the same transparent fallback.
                for unit in group:
                    triples = heuristic_triples(unit["evidence"]) if config.FALLBACK_ON_MINIE_FAILURE else []
                    usable = [triple for triple in triples if is_usable_triple(triple)[0]]
                    actual_backends["heuristic"] += 1
                    audit.append({**unit, "status": "extracted" if usable else "failed", "backend": "heuristic", "fallback_reason": failure, "triple_count": len(usable)})
                    for sub, rel, obj in usable:
                        polarity, modality = polarity_modality(unit["evidence"])
                        assertions.append(assertion(source, sub, rel, obj, infer_type(sub), infer_type(obj), None, unit["evidence"], "heuristic", polarity, modality, unit["chunk_id"]))
                continue
            assigned: dict[int, list[tuple[str, str, str]]] = defaultdict(list)
            service_failures: dict[int, str] = {}
            rejected = Counter()
            for fact in external:
                if isinstance(fact, dict) and fact.get("error"):
                    failed_index = next((index for index, unit in enumerate(group) if fact.get("sentence") == unit["evidence"]), None)
                    if failed_index is not None:
                        service_failures[failed_index] = fact["error"]
                    else:
                        rejected["unmapped_service_failure"] += 1
                    continue
                triple, fact_sentence = fact_parts(fact)
                ok, reason = is_usable_triple(triple)
                if not ok:
                    rejected[reason] += 1
                    continue
                match = next((index for index, unit in enumerate(group) if fact_sentence == unit["evidence"]), None)
                if match is None:
                    match = align_triple_to_sentence(triple, group)
                if match is None:
                    rejected["no_sentence_alignment"] += 1
                else:
                    assigned[match].append(triple)
            for index, unit in enumerate(group):
                if index in service_failures:
                    usable = [triple for triple in heuristic_triples(unit["evidence"]) if is_usable_triple(triple)[0]] if config.FALLBACK_ON_MINIE_FAILURE else []
                    actual_backends["heuristic"] += 1
                    audit.append({**unit, "status": "extracted" if usable else "failed", "backend": "heuristic",
                                  "fallback_reason": service_failures[index], "triple_count": len(usable)})
                    output_backend = "heuristic"
                else:
                    usable = assigned[index]
                    actual_backends[config.OPENIE_BACKEND] += 1
                    audit.append({**unit, "status": "extracted" if usable else "no_triples", "backend": config.OPENIE_BACKEND,
                                  "triple_count": len(usable), "batch_rejected_triples": dict(rejected) if index == 0 and rejected else {}})
                    output_backend = config.OPENIE_BACKEND
                for sub, rel, obj in usable:
                    polarity, modality = polarity_modality(unit["evidence"])
                    assertions.append(assertion(source, sub, rel, obj, infer_type(sub), infer_type(obj), None, unit["evidence"], output_backend, polarity, modality, unit["chunk_id"]))
    # Sources with overlapping chunks often repeat the same sentence. Retain one
    # assertion, while exact evidence and source provenance remain unchanged.
    unique = {}
    for item in assertions:
        key = (item["source_id"], item["subject_raw"], item["predicate_raw"], item["object_raw"], item["evidence"], item["polarity"], item["modality"])
        unique.setdefault(key, item)
    assertions = list(unique.values())
    write_json(config.DATA_DIR / "openie_assertions.json", assertions)
    write_json(config.DATA_DIR / "openie_audit.json", audit)
    summary = Counter(row["status"] for row in audit)
    write_json(config.DATA_DIR / "openie_run_metadata.json", {"requested_backend": config.OPENIE_BACKEND,
        "granularity": config.OPENIE_GRANULARITY, "actual_backends": actual_backends,
        "request_count": request_count, "audit_summary": summary, "generated_at": now()})
    logging.info("Extracted %s text assertions using %s", len(assertions), dict(actual_backends))
    return assertions


def infer_type(surface: str) -> str:
    if CVE_RE.search(surface): return "CVE"
    if CWE_RE.search(surface): return "CWE"
    if KB_RE.search(surface): return "Patch/update"
    if URL_RE.search(surface): return "URL"
    if DATE_RE.search(surface): return "Date"
    if re.search(r"\b(?:Microsoft|Google|CISA|Rapid7|NVD)\b", surface, re.I): return "Organization" if len(surface.split()) <= 3 else "Product"
    return "Mention"


def entity_mentions(assertions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    found: dict[tuple[str, str], dict[str, Any]] = {}
    for a in assertions:
        for field, hint in (("subject_raw", a["subject_type_hint"]), ("object_raw", a["object_type_hint"])):
            text = a[field]
            spans = [(text, hint)]
            spans += [(m.group(0), "CVE") for m in CVE_RE.finditer(text)]
            spans += [(m.group(0), "CWE") for m in CWE_RE.finditer(text)]
            spans += [(m.group(0), "Patch/update") for m in KB_RE.finditer(text)]
            spans += [(m.group(0), "URL") for m in URL_RE.finditer(text)]
            spans += [(m.group(0), "Date") for m in DATE_RE.finditer(text)]
            for surface, typ in spans:
                surface = clean_surface(surface)
                if not surface: continue
                key = (surface, typ)
                item = found.setdefault(key, {"entity_mention_id": stable_id("em", surface, typ), "surface_form": surface,
                    "type_hint": typ, "assertion_ids": [], "source_ids": []})
                item["assertion_ids"].append(a["assertion_id"])
                item["source_ids"].append(a["source_id"])
    for item in found.values():
        item["assertion_ids"] = sorted(set(item["assertion_ids"])); item["source_ids"] = sorted(set(item["source_ids"]))
    return sorted(found.values(), key=lambda x: (x["type_hint"], x["surface_form"].lower()))


def extract_entities() -> list[dict[str, Any]]:
    assertions = load_json(config.DATA_DIR / "structured_assertions.json", []) + load_json(config.DATA_DIR / "openie_assertions.json", [])
    entities = entity_mentions(assertions)
    write_json(config.DATA_DIR / "entities_raw.json", entities)
    return entities


def evidence_identifier_aliases(assertions: list[dict[str, Any]]) -> dict[tuple[str, str], str]:
    """Resolve explicit appositives such as ``the bypass vulnerability, CVE-X``.

    This is source-scoped and evidence-backed; it does not infer aliases merely
    from lexical similarity.
    """
    aliases: dict[tuple[str, str], str] = {}
    pattern = re.compile(r"\b(?:the|an?|this|that)\s+(?P<alias>[A-Za-z][^,.;]{2,100}?),\s*(?P<cve>CVE[\s_-]?\d{4}[\s_-]?\d{4,7})", re.I)
    for item in assertions:
        for match in pattern.finditer(item["evidence"]):
            alias = clean_surface(match["alias"]).lower()
            target = canonical_label(match["cve"])
            aliases[(item["source_id"], alias)] = target
    return aliases


def canonical_label(surface: str) -> str:
    # A CVE embedded in a longer OpenIE argument is not, by itself, that CVE
    # entity. Dedicated regex spans are added separately in entity_mentions.
    if match := CVE_RE.fullmatch(clean_surface(surface)): return f"CVE-{match.group(1)}-{match.group(2)}"
    if match := CWE_RE.fullmatch(clean_surface(surface)): return f"CWE-{match.group(1)}"
    if match := KB_RE.fullmatch(clean_surface(surface)): return f"KB{match.group(1)}"
    compact = re.sub(r"\s+", " ", surface).strip()
    return config.ENTITY_ALIASES.get(compact.lower(), compact)


def resolve_entities() -> list[dict[str, Any]]:
    raw = load_json(config.DATA_DIR / "entities_raw.json", [])
    assertions = load_json(config.DATA_DIR / "structured_assertions.json", []) + load_json(config.DATA_DIR / "openie_assertions.json", [])
    identifier_aliases = evidence_identifier_aliases(assertions)
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for mention in raw:
        targets = {identifier_aliases[(source_id, mention["surface_form"].lower())] for source_id in mention["source_ids"]
                   if (source_id, mention["surface_form"].lower()) in identifier_aliases}
        # Merge only if every source containing this surface form explicitly
        # identifies it with the same CVE in local evidence.
        label = next(iter(targets)) if len(targets) == 1 and len(targets) == len(mention["source_ids"]) else canonical_label(mention["surface_form"])
        entity_type = "CVE" if CVE_RE.fullmatch(label) else mention["type_hint"]
        groups[(label, entity_type)].append(mention)
    canonical = []
    for (label, typ), mentions in sorted(groups.items()):
        canonical.append({"entity_id": stable_id("e", typ, label.lower()), "canonical_label": label, "entity_type": typ,
            "aliases": sorted({m["surface_form"] for m in mentions}), "source_ids": sorted({x for m in mentions for x in m["source_ids"]}),
            "mention_ids": sorted(m["entity_mention_id"] for m in mentions)})
    write_json(config.DATA_DIR / "entities_canonical.json", canonical)
    report = ["# Entity resolution", "", f"Raw mentions: **{len(raw)}**", f"Canonical entities: **{len(canonical)}**", f"Evidence-backed identifier aliases: **{len(identifier_aliases)}**", "",
              "Only deterministic identifiers, configured surface aliases, and source-scoped appositives are merged; ambiguous names remain separate."]
    write_text(config.REPORTS_DIR / "entity_resolution_report.md", "\n".join(report) + "\n")
    return canonical


def entity_index(entities: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    index = {}
    for entity in entities:
        for alias in entity["aliases"]: index[alias] = entity
        index[entity["canonical_label"]] = entity
    return index


def graphml(nodes: list[dict[str, Any]], edges: list[dict[str, Any]], path: Path) -> None:
    root = Element("graphml", xmlns="http://graphml.graphdrawing.org/xmlns")
    node_keys = sorted({key for node in nodes for key in node if key != "id"})
    edge_keys = sorted({key for edge in edges for key in edge if key not in {"edge_id", "source", "target"}})
    # Declare every data key so exported files conform to GraphML rather than
    # merely being XML shaped like a graph.
    for key in node_keys:
        SubElement(root, "key", id=f"node_{key}", attrib={"for": "node", "attr.name": key, "attr.type": "string"})
    for key in edge_keys:
        SubElement(root, "key", id=f"edge_{key}", attrib={"for": "edge", "attr.name": key, "attr.type": "string"})
    graph = SubElement(root, "graph", edgedefault="directed")
    for n in nodes:
        node = SubElement(graph, "node", id=n["id"])
        for key, value in n.items():
            if key != "id": SubElement(node, "data", key=f"node_{key}").text = json.dumps(value, ensure_ascii=False) if isinstance(value, (list, dict)) else str(value)
    for e in edges:
        edge = SubElement(graph, "edge", id=e["edge_id"], source=e["source"], target=e["target"])
        for key, value in e.items():
            if key not in {"edge_id", "source", "target"}: SubElement(edge, "data", key=f"edge_{key}").text = json.dumps(value, ensure_ascii=False) if isinstance(value, (list, dict)) else str(value)
    ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)


def build_open_kg() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    entities = load_json(config.DATA_DIR / "entities_canonical.json", [])
    assertions = load_json(config.DATA_DIR / "structured_assertions.json", []) + load_json(config.DATA_DIR / "openie_assertions.json", [])
    index = entity_index(entities)
    nodes = [{"id": e["entity_id"], "label": e["canonical_label"], "entity_type": e["entity_type"], "aliases": e["aliases"], "source_ids": e["source_ids"]} for e in entities]
    edges = []
    for a in assertions:
        sub, obj = index.get(a["subject_raw"]), index.get(a["object_raw"])
        if not sub or not obj: continue
        edge = {"edge_id": stable_id("oe", a["assertion_id"]), "source": sub["entity_id"], "target": obj["entity_id"],
                "predicate_raw": a["predicate_raw"], "assertion_id": a["assertion_id"], "source_id": a["source_id"],
                "source_url": a["source_url"], "chunk_id": a["chunk_id"], "json_path": a["json_path"], "evidence": a["evidence"],
                "extraction_method": a["extraction_method"], "polarity": a["polarity"], "modality": a["modality"]}
        edges.append(edge)
    write_json(config.OPEN_KG_DIR / "nodes.json", nodes); write_json(config.OPEN_KG_DIR / "edges.json", edges); graphml(nodes, edges, config.OPEN_KG_DIR / "graph.graphml")
    return nodes, edges


def normalize_relation(phrase: str) -> str:
    original = phrase.lower().strip()
    phrase = original
    phrase = re.sub(r"\b(can|could|may|might|will|does|do|is|are|was|were|has|have|had)\b", "", phrase)
    phrase = re.sub(r"\s+", " ", phrase).strip()
    # Conservative deterministic lemmatization for clustering suggestions.
    phrase = re.sub(r"\b([a-z]+)ies\b", r"\1y", phrase)
    phrase = re.sub(r"\b([a-z]+)es\b", r"\1e", phrase)
    phrase = re.sub(r"\b([a-z]+)s\b", r"\1", phrase)
    phrase = re.sub(r"\b([a-z]+?)(?:ing|ed)\b", r"\1", phrase)
    return phrase or original


def build_relation_inventory() -> list[dict[str, Any]]:
    assertions = load_json(config.DATA_DIR / "structured_assertions.json", []) + load_json(config.DATA_DIR / "openie_assertions.json", [])
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for a in assertions: grouped[a["predicate_raw"]].append(a)
    inventory = [{"relation_raw": phrase, "count": len(items), "normalized_suggestion": normalize_relation(phrase),
                  "examples": [{k: x[k] for k in ("subject_raw", "object_raw", "evidence", "source_id", "assertion_id")} for x in items[:3]]}
                 for phrase, items in sorted(grouped.items(), key=lambda kv: (-len(kv[1]), kv[0].lower()))]
    write_json(config.DATA_DIR / "relation_inventory.json", inventory)
    lines = ["# Discovered relation inventory", "", f"Distinct surface predicates: **{len(inventory)}**", "", "| Relation phrase | Count | Normalized suggestion |", "|---|---:|---|"]
    lines += [f"| {x['relation_raw']} | {x['count']} | {x['normalized_suggestion']} |" for x in inventory]
    write_text(config.REPORTS_DIR / "relation_inventory.md", "\n".join(lines) + "\n")
    return inventory


def normalize_relations() -> list[dict[str, Any]]:
    inventory = load_json(config.DATA_DIR / "relation_inventory.json", [])
    features = []
    for item in inventory:
        normalized = normalize_relation(item["relation_raw"])
        tokens = sorted(set(re.findall(r"[a-z0-9]+", normalized)))
        features.append({"relation_raw": item["relation_raw"], "normalized": normalized, "tokens": tokens, "count": item["count"]})
    write_json(config.DATA_DIR / "relation_features.json", features)
    return features


def jaccard(left: list[str], right: list[str]) -> float:
    a, b = set(left), set(right)
    return len(a & b) / len(a | b) if a and b else 0.0


def cluster_concept_key(representative: str) -> str:
    """The stable "concept anchor" for a cluster: the normalized form of its
    dominant (most frequent) raw phrase. Two clusters keep the same identity
    across reruns as long as their dominant phrase normalizes the same way,
    even if satellite members were added or removed by upstream extraction
    changes (see cluster_relations() docstring for why this replaced hashing
    the full exact membership)."""
    return normalize_relation(representative)


def cluster_relations() -> list[dict[str, Any]]:
    """Cluster relation phrases and assign each cluster a stable identity.

    cluster_id used to be stable_id("rc", *member_phrases) -- a hash of the
    EXACT membership set. That made the ID churn on every upstream extraction
    change: adding even one new phrase to a cluster produced a brand-new ID,
    silently discarding whatever accept/reject decision a human had made for
    "the same" cluster under its old ID. Concretely, the terminal-punctuation
    fix (see reports/fix_report_v2.md) added ~1800 assertions and pushed 1168
    of 2108 clusters back to "pending" this way.

    cluster_id is now derived from cluster_concept_key() of the dominant
    phrase instead, so it survives ordinary membership drift. The exact
    membership hash is kept as content_id (same formula as the old
    cluster_id) so export_clusters_for_review() can still detect *when*
    membership actually changed and react explicitly rather than either
    silently keeping a stale decision or silently discarding it.
    """
    features = load_json(config.DATA_DIR / "relation_features.json", [])
    parent = list(range(len(features)))
    def find(x: int) -> int:
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a: int, b: int) -> None:
        a, b = find(a), find(b)
        if a != b: parent[b] = a
    for i, left in enumerate(features):
        for j, right in enumerate(features[:i]):
            if left["normalized"] == right["normalized"] or jaccard(left["tokens"], right["tokens"]) >= config.RELATION_JACCARD_THRESHOLD: union(i, j)
    groups: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for i, feature in enumerate(features): groups[find(i)].append(feature)
    clusters = []
    for members in groups.values():
        members.sort(key=lambda x: (-x["count"], x["relation_raw"]))
        representative = members[0]["relation_raw"]
        clusters.append({
            "cluster_id": stable_id("rc2", cluster_concept_key(representative)),
            "content_id": stable_id("rc", *(x["relation_raw"] for x in members)),
            "representative": representative,
            "member_phrases": [x["relation_raw"] for x in members],
            "normalized_suggestions": sorted({x["normalized"] for x in members}),
            "assertion_count": sum(x["count"] for x in members), "status": "pending",
        })
    clusters.sort(key=lambda x: (-x["assertion_count"], x["representative"]))
    # Two clusters can coincidentally share a dominant-phrase concept key without
    # Jaccard ever having judged them similar (e.g. two unrelated single-word
    # clusters whose top member both normalize to the same lemma). Detected
    # explicitly rather than silently letting the second overwrite the first in
    # any cluster_id -> cluster lookup: the largest cluster keeps the plain ID,
    # every other colliding cluster gets a numbered suffix and a visible flag.
    seen: dict[str, int] = {}
    for cluster in clusters:
        base_id = cluster["cluster_id"]
        seen[base_id] = seen.get(base_id, 0) + 1
        if seen[base_id] > 1:
            cluster["cluster_id"] = f"{base_id}_dup{seen[base_id]}"
            cluster["concept_id_collision"] = True
            cluster["concept_id_collision_base"] = base_id
        else:
            cluster["concept_id_collision"] = False
    write_json(config.CLUSTER_DIR / "clusters_raw.json", clusters)
    collisions = sum(1 for c in clusters if c["concept_id_collision"])
    report = ["# Relation clustering report", "", f"Clusters: **{len(clusters)}**; threshold: `{config.RELATION_JACCARD_THRESHOLD}`.",
              f"Concept-key collisions (distinct clusters sharing a dominant-phrase ID): **{collisions}**.", "",
              "Clusters are suggestions only; no canonical label has been assigned automatically."]
    write_text(config.CLUSTER_DIR / "clustering_report.md", "\n".join(report) + "\n")
    return clusters


def export_clusters_for_review() -> list[dict[str, Any]]:
    """Merge freshly computed clusters with prior human review decisions.

    Protocol per validation record (see reports/cluster_id_stabilization.md for
    the full rationale):
      - review_status "new": no record exists yet under this cluster_id (a
        concept never reviewed before under this identity). decision=pending.
      - review_status "confirmed": a real decision (accept/reject/split) is on
        file AND membership matches the anchor recorded for that decision
        (content_id_at_last_decision). Carried over as-is.
      - review_status "needs_reconfirmation": a real decision is/was on file
        but membership has drifted since the anchor was recorded. decision is
        forced back to "pending" -- never silently kept, never silently
        dropped -- with previous_decision preserved and an explicit
        added/removed diff against the anchor membership. Clears only when a
        human sets reconfirm: true alongside the decision (see below); simply
        re-typing the same decision string is not treated as evidence of a
        fresh look, since this file format has no review timestamp to tell
        "still valid" apart from "re-saved without noticing the diff".
      - review_status "pending": ordinary, never-decided pending cluster whose
        membership happens to have changed since last export -- no prior
        decision to protect, so no downgrade to report.
    """
    clusters = load_json(config.CLUSTER_DIR / "clusters_raw.json", [])
    validation_path = config.CLUSTER_DIR / "clusters_validation.json"
    old = {x.get("cluster_id"): x for x in load_json(validation_path, [])}
    validation = []
    lines = ["# Relation clusters for human review", "",
             "Edit `clusters_validation.json`: set `decision` to `accept`, `reject`, or `split`. "
             "The canonical relation is filled automatically from the cluster representative and can be "
             "overridden only when needed. If `review_status` is `needs_reconfirmation`, check the `diff` "
             "field before deciding, then add `\"reconfirm\": true` alongside your decision to clear it -- "
             "otherwise the next export will downgrade it back to pending.", ""]
    for cluster in clusters:
        cid, content_id, current_members = cluster["cluster_id"], cluster["content_id"], cluster["member_phrases"]
        default_label = clean_surface(cluster["representative"])
        prior = old.get(cid)
        if prior is None:
            value = {"cluster_id": cid, "decision": "pending", "canonical_relation": default_label, "notes": "",
                      "content_id_at_last_decision": None, "member_phrases_at_decision": [],
                      "composition_changed_since_review": False, "diff": {"added": [], "removed": []},
                      "previous_decision": None, "review_status": "new", "split_assignments": None}
        else:
            prior_decision = prior.get("decision", "pending")
            anchor_content_id = prior.get("content_id_at_last_decision")
            anchor_members = set(prior.get("member_phrases_at_decision") or [])
            drifted = anchor_content_id is not None and anchor_content_id != content_id
            if prior_decision in ("accept", "reject", "split") and (not drifted or prior.get("reconfirm")):
                # Either membership still matches the anchor, or a human explicitly
                # reconfirmed despite the drift -- refresh the anchor either way.
                value = {"cluster_id": cid, "decision": prior_decision,
                          "canonical_relation": prior.get("canonical_relation") or default_label,
                          "notes": prior.get("notes", ""), "content_id_at_last_decision": content_id,
                          "member_phrases_at_decision": current_members,
                          "composition_changed_since_review": False, "diff": {"added": [], "removed": []},
                          "previous_decision": None, "review_status": "confirmed",
                          "split_assignments": prior.get("split_assignments")}
            elif prior_decision in ("accept", "reject", "split") and drifted:
                added, removed = sorted(set(current_members) - anchor_members), sorted(anchor_members - set(current_members))
                value = {"cluster_id": cid, "decision": "pending",
                          "canonical_relation": prior.get("canonical_relation") or default_label,
                          "notes": prior.get("notes", ""), "content_id_at_last_decision": anchor_content_id,
                          "member_phrases_at_decision": sorted(anchor_members),
                          "composition_changed_since_review": True, "diff": {"added": added, "removed": removed},
                          "previous_decision": prior_decision, "review_status": "needs_reconfirmation",
                          "split_assignments": prior.get("split_assignments")}
            elif prior.get("previous_decision") and drifted:
                # Already-downgraded cluster, still not reconfirmed, drifted further.
                added, removed = sorted(set(current_members) - anchor_members), sorted(anchor_members - set(current_members))
                value = {"cluster_id": cid, "decision": "pending",
                          "canonical_relation": prior.get("canonical_relation") or default_label,
                          "notes": prior.get("notes", ""), "content_id_at_last_decision": anchor_content_id,
                          "member_phrases_at_decision": sorted(anchor_members),
                          "composition_changed_since_review": True, "diff": {"added": added, "removed": removed},
                          "previous_decision": prior.get("previous_decision"), "review_status": "needs_reconfirmation",
                          "split_assignments": prior.get("split_assignments")}
            else:
                # Ordinary pending, never decided (or already-cleared) -- no anchor to protect.
                value = {"cluster_id": cid, "decision": "pending",
                          "canonical_relation": prior.get("canonical_relation") or default_label,
                          "notes": prior.get("notes", ""), "content_id_at_last_decision": None,
                          "member_phrases_at_decision": [], "composition_changed_since_review": False,
                          "diff": {"added": [], "removed": []}, "previous_decision": None, "review_status": "pending",
                          "split_assignments": prior.get("split_assignments")}
        if not clean_surface(value.get("canonical_relation") or ""):
            value["canonical_relation"] = default_label
        validation.append(value)
        lines += [f"## {cluster['representative']}", "", f"- Cluster ID: `{cid}`",
                  f"- Assertions: {cluster['assertion_count']}", f"- Phrases: {', '.join(cluster['member_phrases'])}",
                  f"- Suggested normal forms: {', '.join(cluster['normalized_suggestions'])}",
                  f"- Decision: {value['decision']} (review_status: {value['review_status']})"]
        if value["composition_changed_since_review"]:
            lines += [f"- Previous decision: {value['previous_decision']}",
                      f"- Added since anchor: {', '.join(value['diff']['added']) or '(none)'}",
                      f"- Removed since anchor: {', '.join(value['diff']['removed']) or '(none)'}"]
        lines.append("")
    write_json(validation_path, validation); write_text(config.CLUSTER_DIR / "clusters_review.md", "\n".join(lines))
    return validation


def split_assignment_labels(decision: dict[str, Any], cluster: dict[str, Any]) -> dict[str, str]:
    """Per-phrase canonical labels for a "split" cluster.

    A cluster-wide canonical_relation cannot represent a mixed-sense cluster
    like `added` (CISA adding a CVE to the KEV catalog vs. Microsoft adding a
    protocol capability) or `patch` (8 clean structured KB facts alongside a
    dozen heuristic-fallback mis-parses). split_assignments maps each member
    phrase individually: {"phrase": "canonical label"} to route it, or
    {"phrase": null} / an omitted phrase to reject it (excluded from the
    canonical KG, same as if the whole cluster were "reject"). Every phrase is
    reject-by-default so a partially filled-in split cannot accidentally leak
    an unreviewed phrase through with the wrong label."""
    assignments = decision.get("split_assignments") or {}
    out = {}
    for phrase in cluster["member_phrases"]:
        label = clean_surface(assignments.get(phrase) or "")
        if label:
            out[phrase] = label
    return out


def accepted_relation_map() -> dict[str, str]:
    clusters = {x["cluster_id"]: x for x in load_json(config.CLUSTER_DIR / "clusters_raw.json", [])}
    output = {}
    for decision in load_json(config.CLUSTER_DIR / "clusters_validation.json", []):
        cluster = clusters.get(decision.get("cluster_id"))
        if not cluster:
            continue
        if decision.get("decision") == "accept":
            label = clean_surface(decision.get("canonical_relation") or cluster["representative"])
            if label:
                output.update({phrase: label for phrase in cluster["member_phrases"]})
        elif decision.get("decision") == "split":
            output.update(split_assignment_labels(decision, cluster))
    return output


def apply_cluster_validation() -> dict[str, str]:
    mapping = accepted_relation_map()
    write_json(config.CLUSTER_DIR / "accepted_relation_mapping.json", mapping)
    return mapping


def derived_from_map() -> dict[str, list[str]]:
    """For every accepted relation_raw phrase, the full list of raw phrasings that
    were judged to mean the same thing -- so a canonical edge can show its full
    provenance, not just its own predicate_raw. For a "split" cluster this is the
    phrases that share its OWN split-assigned label, not the whole cluster: two
    phrases assigned to different labels within the same split are not each
    other's derivation, even though they came from the same relation cluster."""
    clusters = {c["cluster_id"]: c for c in load_json(config.CLUSTER_DIR / "clusters_raw.json", [])}
    mapping: dict[str, list[str]] = {}
    for decision in load_json(config.CLUSTER_DIR / "clusters_validation.json", []):
        cluster = clusters.get(decision.get("cluster_id"))
        if not cluster:
            continue
        if decision.get("decision") == "accept":
            for phrase in cluster["member_phrases"]:
                mapping[phrase] = cluster["member_phrases"]
        elif decision.get("decision") == "split":
            by_label: dict[str, list[str]] = defaultdict(list)
            for phrase, label in split_assignment_labels(decision, cluster).items():
                by_label[label].append(phrase)
            for phrase, label in split_assignment_labels(decision, cluster).items():
                mapping[phrase] = by_label[label]
    return mapping


def build_canonical_kg() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    mapping = apply_cluster_validation()
    derived_from = derived_from_map()
    open_nodes = load_json(config.OPEN_KG_DIR / "nodes.json", [])
    node_type = {node["id"]: node.get("entity_type") for node in open_nodes}
    edges = load_json(config.OPEN_KG_DIR / "edges.json", [])
    canonical_edges = [{
        **edge,
        "predicate_canonical": mapping[edge["predicate_raw"]],
        "domain": node_type.get(edge["source"]),
        "range": node_type.get(edge["target"]),
        "derived_from": derived_from.get(edge["predicate_raw"], [edge["predicate_raw"]]),
    } for edge in edges if edge["predicate_raw"] in mapping]
    node_ids = {edge["source"] for edge in canonical_edges} | {edge["target"] for edge in canonical_edges}
    nodes = [node for node in open_nodes if node["id"] in node_ids]
    write_json(config.CANONICAL_KG_DIR / "nodes.json", nodes); write_json(config.CANONICAL_KG_DIR / "edges.json", canonical_edges); graphml(nodes, canonical_edges, config.CANONICAL_KG_DIR / "graph.graphml")
    return nodes, canonical_edges


def prf1(predicted: set, expected: set) -> dict[str, Any]:
    tp = len(predicted & expected)
    precision = tp / len(predicted) if predicted else 0.0
    recall = tp / len(expected) if expected else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"predicted": len(predicted), "expected": len(expected), "true_positives": tp,
            "precision": precision, "recall": recall, "f1": f1}


def structural_metrics() -> dict[str, Any]:
    """Metrics computable without any gold annotation: coverage and compression
    at each stage. These do not tell you whether extractions are CORRECT, only
    how much reduction/merging happened -- useful as a sanity check on their own
    (e.g. a cluster count barely below the raw-phrase count signals clustering
    did almost nothing) but not a substitute for gold precision/recall."""
    raw_entities = load_json(config.DATA_DIR / "entities_raw.json", [])
    canonical_entities = load_json(config.DATA_DIR / "entities_canonical.json", [])
    inventory = load_json(config.DATA_DIR / "relation_inventory.json", [])
    clusters = load_json(config.CLUSTER_DIR / "clusters_raw.json", [])
    mapping = load_json(config.CLUSTER_DIR / "accepted_relation_mapping.json", {})
    sizes = sorted(len(c["member_phrases"]) for c in clusters)
    mid = sizes[len(sizes) // 2] if sizes else 0
    return {
        "entity_mentions_raw": len(raw_entities), "entities_canonical": len(canonical_entities),
        "entity_compression_ratio": len(raw_entities) / len(canonical_entities) if canonical_entities else 0.0,
        "distinct_relation_phrases_raw": len(inventory), "relation_clusters": len(clusters),
        "cluster_member_count_median": mid, "cluster_member_count_max": sizes[-1] if sizes else 0,
        "clusters_with_multiple_phrases": sum(1 for s in sizes if s > 1),
        "clusters_still_pending_review": sum(1 for c in clusters
            if next((d for d in load_json(config.CLUSTER_DIR / "clusters_validation.json", [])
                     if d.get("cluster_id") == c["cluster_id"]), {}).get("decision") == "pending"),
        "distinct_canonical_relations": len(set(mapping.values())),
        "canonical_to_raw_relation_ratio": len(set(mapping.values())) / len(inventory) if inventory else 0.0,
    }


def gold_entries() -> list[dict[str, Any]]:
    return [load_json(path, {}) for path in sorted((config.EVALUATION_DIR / "gold").glob("*.json"))]


def gold_evaluation() -> dict[str, Any] | str:
    """Precision/recall/F1 at three stages, matched on human-readable labels
    (never the internal SHA256 entity IDs, which nobody can hand-author)."""
    gold = gold_entries()
    if not gold:
        return "not run (no gold JSON files in evaluation/gold/)"
    canonical_entities = load_json(config.DATA_DIR / "entities_canonical.json", [])
    node_label = {n["id"]: n["label"] for n in load_json(config.OPEN_KG_DIR / "nodes.json", [])}
    openie = load_json(config.DATA_DIR / "openie_assertions.json", [])
    canonical_edges = load_json(config.CANONICAL_KG_DIR / "edges.json", [])
    result: dict[str, Any] = {"gold_source_count": len(gold)}
    # Every comparison is scoped to just the annotated source_ids: gold covers
    # a handful of known-correct facts per source, not every fact in the whole
    # corpus, so comparing against corpus-wide predictions would make
    # precision meaningless (thousands of true, simply un-annotated, facts
    # would count as false positives).
    gold_sources = {g.get("source_id") for g in gold}
    if any("entities" in g for g in gold):
        by_source: dict[str, set[tuple[str, str]]] = defaultdict(set)
        for e in canonical_entities:
            for sid in e["source_ids"]:
                by_source[sid].add((e["canonical_label"], e["entity_type"]))
        predicted = {(sid, label, typ) for sid in gold_sources for (label, typ) in by_source.get(sid, set())}
        expected = {(g.get("source_id"), ent["canonical_label"], ent["entity_type"])
                    for g in gold for ent in g.get("entities", [])}
        result["entity_resolution"] = prf1(predicted, expected)
    if any("openie_triples" in g for g in gold):
        predicted = {(a["source_id"], a["subject_raw"], a["predicate_raw"], a["object_raw"])
                     for a in openie if a["source_id"] in gold_sources}
        expected = {(g.get("source_id"), t["subject"], t["predicate"], t["object"])
                    for g in gold for t in g.get("openie_triples", [])}
        result["openie_triple"] = prf1(predicted, expected)
    if any("canonical_triples" in g for g in gold):
        predicted = {(e["source_id"], node_label.get(e["source"]), e["predicate_canonical"], node_label.get(e["target"]))
                     for e in canonical_edges if e["source_id"] in gold_sources}
        expected = {(g.get("source_id"), t["source"], t["predicate"], t["target"])
                    for g in gold for t in g.get("canonical_triples", [])}
        result["canonical_triple"] = prf1(predicted, expected)
    return result


def evaluate_pipeline() -> dict[str, Any]:
    sources = discover_sources(); structured = load_json(config.DATA_DIR / "structured_assertions.json", []); text = load_json(config.DATA_DIR / "openie_assertions.json", [])
    canonical_edges = load_json(config.CANONICAL_KG_DIR / "edges.json", [])
    metrics: dict[str, Any] = {"generated_at": now(), "sources": len(sources), "structured_assertions": len(structured), "openie_assertions": len(text),
        "open_kg_edges": len(load_json(config.OPEN_KG_DIR / "edges.json", [])), "canonical_kg_edges": len(canonical_edges),
        "source_coverage": len({a["source_id"] for a in structured + text}) / len(sources) if sources else 0,
        "structural": structural_metrics(), "gold_evaluation": gold_evaluation()}
    write_json(config.EVALUATION_DIR / "metrics.json", metrics)
    write_text(config.EVALUATION_DIR / "report.md", "# Pipeline evaluation\n\n```json\n" + json.dumps(metrics, indent=2) + "\n```\n")
    return metrics


def final_report() -> None:
    inventory = load_json(config.DATA_DIR / "corpus_inventory.json", {}); structured = load_json(config.DATA_DIR / "structured_assertions.json", []); text = load_json(config.DATA_DIR / "openie_assertions.json", []); clusters = load_json(config.CLUSTER_DIR / "clusters_raw.json", []); canonical = load_json(config.CANONICAL_KG_DIR / "edges.json", [])
    report = ["# Extraction summary", "", f"- Sources: {inventory.get('source_count', 0)}", f"- Structured assertions: {len(structured)}", f"- OpenIE assertions: {len(text)}", f"- Discovered relation clusters: {len(clusters)}", f"- Canonical edges: {len(canonical)}", "", "Canonical edges appear only after explicit cluster validation. All open-KG edges retain assertion-level evidence and provenance."]
    write_text(config.REPORTS_DIR / "final_summary.md", "\n".join(report) + "\n")


def extraction_report() -> None:
    structured = load_json(config.DATA_DIR / "structured_assertions.json", []); text = load_json(config.DATA_DIR / "openie_assertions.json", []); metadata = load_json(config.DATA_DIR / "openie_run_metadata.json", {})
    write_text(config.REPORTS_DIR / "extraction_report.md", "# Extraction report\n\n" + f"- Structured assertions: **{len(structured)}**\n- Text assertions: **{len(text)}**\n- OpenIE backend requested: `{metadata.get('requested_backend')}`\n- Actual backends: `{metadata.get('actual_backends')}`\n")
