#!/usr/bin/env python3
"""Ingest user-supplied URLs and files into a separate live workspace.

Nothing here re-implements scraping or cleaning. The HTML/PDF fetch path is
`build_corpus.py`'s (`request_with_retry`, `prepare_html`, `html_to_text`,
`extract_pdf`, `is_suspect`, `fetch_via_playwright`) and the cleaning path is
`preprocess_corpus.py`'s (`filter_noise`, `normalize_whitespace`, `chunk_text`). Those
modules live at the project root, so they are imported, not copied.

Isolation is the point: everything lands in `live_corpus/`, never in `corpus/` and never
in `demo_corpus/`. Sources are numbered from S901 so they can never be confused with the
frozen corpus (S01-S58) while still matching the `S*.json` glob that
`pipeline_lib.discover_sources()` uses.

Every failure is captured and returned as a per-source status. A dead URL, a corrupt PDF
or a scrape timeout degrades that one source and leaves the rest of the batch intact.
"""
from __future__ import annotations

import json
import re
import sys
import traceback
import concurrent.futures
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build_corpus as bc          # noqa: E402  scraping methods, reused as-is
import preprocess_corpus as pc     # noqa: E402  cleaning methods, reused as-is

LIVE_CORPUS = ROOT / "live_corpus"
CLEAN_DIR = LIVE_CORPUS / "clean"
RAW_DIR = LIVE_CORPUS / "raw"
FIRST_ID = 901

TEXT_SUFFIXES = {".txt", ".md", ".text"}
HTML_SUFFIXES = {".html", ".htm", ".xhtml"}
PDF_SUFFIXES = {".pdf"}


def reset_workspace() -> None:
    """Each ingestion run starts from an empty workspace, so the graph shown is exactly
    what the user just submitted -- not an accumulation across runs."""
    for directory in (CLEAN_DIR, RAW_DIR):
        directory.mkdir(parents=True, exist_ok=True)
        for path in directory.glob("S*.json"):
            path.unlink()


def _next_id(counter: list[int]) -> str:
    source_id = f"S{FIRST_ID + counter[0]}"
    counter[0] += 1
    return source_id


def _clean_and_store(source_id: str, name: str, origin: str, raw_text: str,
                     method: str) -> dict:
    """Apply the corpus cleaning chain and write a record in corpus/clean's schema."""
    filtered, dropped = pc.filter_noise(raw_text)
    clean_text = pc.normalize_whitespace(filtered)
    chunks = pc.chunk_text(clean_text) if len(clean_text) > pc.SEGMENT_THRESHOLD else None

    record = {
        "source_id": source_id,
        "source_name": name,
        "cve_ids": sorted(set(re.findall(r"CVE-\d{4}-\d{4,7}", clean_text))),
        "url": origin,
        "extraction_status": "success",
        "relevance": "cve-specific" if re.search(r"CVE-\d{4}-\d{4,7}", clean_text) else "framework",
        "char_count_raw": len(raw_text),
        "char_count_clean": len(clean_text),
        "filtered_lines": dropped,
        "clean_text": clean_text,
        "chunks": chunks,
        "extraction_method": method,
        "ingested_at": datetime.now(timezone.utc).isoformat(),
    }
    (CLEAN_DIR / f"{source_id}.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    return record


def ingest_url(url: str, counter: list[int]) -> dict:
    """Fetch one URL through build_corpus.py's own path. Never raises."""
    source_id = _next_id(counter)
    status = {"source_id": source_id, "origin": url, "kind": "url"}
    try:
        session = requests.Session()
        session.headers.update(bc.HEADERS)
        response = bc.request_with_retry(session, url)

        content_type = (response.headers.get("Content-Type") or "").lower()
        if "pdf" in content_type or url.lower().split("?")[0].endswith(".pdf"):
            text, method = bc.extract_pdf(response.content), "pdf_pdfplumber"
        else:
            html = bc.prepare_html(response.text, url)
            text, method = bc.html_to_text(html, url)

        suspects = bc.is_suspect(text or "", url)
        if suspects:
            # Same escalation as the corpus builder: try a real browser render. On this
            # machine there is no system Chromium, so it fails -- reported, not hidden.
            try:
                # build_corpus.fetch_via_playwright returns (html, final_url, error).
                rendered, _final_url, pw_error = bc.fetch_via_playwright(url)
                if rendered:
                    text2, method2 = bc.html_to_text(bc.prepare_html(rendered, url), url)
                    if not bc.is_suspect(text2 or "", url):
                        text, method = text2, f"playwright+{method2}"
                        suspects = []
                else:
                    status["playwright_fallback"] = f"indisponible ({pw_error})"
            except Exception as exc:  # noqa: BLE001
                status["playwright_fallback"] = f"indisponible ({type(exc).__name__})"

        if not (text or "").strip():
            status.update(status="failed", error="aucun texte extrait")
            return status
        if suspects:
            status["warning"] = " ; ".join(suspects)

        record = _clean_and_store(source_id, url.split("//")[-1][:70], url, text, method)
        status.update(status="ok", method=method, chars=record["char_count_clean"],
                      cves=record["cve_ids"])
    except requests.RequestException as exc:
        status.update(status="failed", error=f"réseau : {exc}")
    except Exception as exc:  # noqa: BLE001
        status.update(status="failed", error=f"{type(exc).__name__}: {exc}",
                      trace=traceback.format_exc(limit=2))
    return status


def ingest_file(filename: str, payload: bytes, counter: list[int]) -> dict:
    """Read one uploaded file. Never raises."""
    source_id = _next_id(counter)
    status = {"source_id": source_id, "origin": filename, "kind": "file"}
    suffix = Path(filename).suffix.lower()
    try:
        if suffix in PDF_SUFFIXES:
            text, method = bc.extract_pdf(payload), "pdf_pdfplumber"
        elif suffix in HTML_SUFFIXES:
            text, method = bc.html_to_text(payload.decode("utf-8", "replace"), filename)
        elif suffix in TEXT_SUFFIXES or not suffix:
            text, method = payload.decode("utf-8", "replace"), "text_direct"
        else:
            status.update(status="failed", error=f"extension non prise en charge : {suffix}")
            return status

        if not (text or "").strip():
            status.update(status="failed", error="fichier vide ou illisible")
            return status

        record = _clean_and_store(source_id, filename, f"file://{filename}", text, method)
        status.update(status="ok", method=method, chars=record["char_count_clean"],
                      cves=record["cve_ids"])
    except Exception as exc:  # noqa: BLE001
        status.update(status="failed", error=f"{type(exc).__name__}: {exc}")
    return status


def ingest(urls: list[str], files: list[tuple[str, bytes]]) -> list[dict]:
    """Ingest everything. URLs run concurrently -- build_corpus retries a failing host for
    up to ~55 s, and doing that serially would make a batch with one dead link feel hung.
    Source ids are pre-assigned so concurrency cannot make them race."""
    reset_workspace()
    clean_urls = [u.strip() for u in urls if u.strip()]
    ids = [f"S{FIRST_ID + i}" for i in range(len(clean_urls) + len(files))]

    statuses: list[dict] = [None] * len(ids)  # type: ignore[list-item]
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(4, max(1, len(clean_urls)))) as pool:
        futures = {pool.submit(ingest_url, url, [int(ids[i][1:]) - FIRST_ID]): i
                   for i, url in enumerate(clean_urls)}
        for future in concurrent.futures.as_completed(futures):
            statuses[futures[future]] = future.result()

    for offset, (name, data) in enumerate(files):
        index = len(clean_urls) + offset
        statuses[index] = ingest_file(name, data, [int(ids[index][1:]) - FIRST_ID])
    return [s for s in statuses if s]
