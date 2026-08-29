"""Constitue le corpus brut du challenge CIFRE, sans extraire de triples.

Lancement (depuis la racine du projet) :
    .venv/bin/python build_corpus.py

Le script ne tente jamais de contourner un paywall ou une authentification. Chaque
réponse insuffisante ou erreur réseau est conservée dans corpus/failed_sources.json.

Pipeline par source HTML : requests+trafilatura, puis en repli (page trop courte,
squelette de SPA, erreur réseau/HTTP) Playwright (rendu JS réel). Pour S12
(Medium), si même Playwright échoue, un remplacement peut être configuré dans
S12_REPLACEMENT après une recherche web manuelle — jamais de remplacement
silencieux (voir "fallback_used" dans le JSON de sortie).
"""

import json
import re
import time
from datetime import datetime, timezone
from html import unescape
from io import BytesIO
from pathlib import Path
from urllib.parse import urljoin

import pdfplumber
import requests
import trafilatura
from playwright.sync_api import sync_playwright
from readability import Document


OUTPUT_DIR = Path("corpus")
RAW_DIR = OUTPUT_DIR / "raw"
TIMEOUT_SECONDS = 15
PAUSE_SECONDS = 1.5
RETRY_DELAYS = [0, 5, 15, 30]  # 1re tentative immédiate, puis 5s/15s/30s
MIN_TEXT_LENGTH = 200
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0 Safari/537.36"
    ),
    "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
}

# Rempli seulement après une recherche web manuelle (voir plan de correction) et
# validation humaine. Tant qu'il vaut None, un échec S12 reste un échec explicite.
S12_REPLACEMENT = None
# Exemple de structure attendue si un remplacement est retenu :
# S12_REPLACEMENT = {
#     "replacement_url": "https://...",
#     "replacement_reason": "Couvre la même donnée (361 IP / 47 pays) que la source Medium bloquée.",
#     "search_query_used": "CVE-2026-59310 361 victim IPs 47 countries",
# }


# La liste est volontairement fermée : le corpus est celui défini pour le challenge.
# S26 (DTIC, cadre SSVC v2.0) a été retirée : le site source redirige systématiquement
# vers une page de maintenance (vérifié manuellement, indépendant du bac à sable).
SOURCES = [
    ("S01", "CISA KEV Alert 2026-08-18", "https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog", ["CVE-2026-33824", "CVE-2026-55040", "CVE-2026-59310", "CVE-2026-65400"], "primary", "official", "html"),
    ("S02", "NVD: CVE-2026-33824", "https://nvd.nist.gov/vuln/detail/CVE-2026-33824", ["CVE-2026-33824"], "primary", "official", "nvd_api"),
    ("S03", "NVD: CVE-2026-55040", "https://nvd.nist.gov/vuln/detail/CVE-2026-55040", ["CVE-2026-55040"], "primary", "official", "nvd_api"),
    ("S04", "NVD: CVE-2026-59310", "https://nvd.nist.gov/vuln/detail/CVE-2026-59310", ["CVE-2026-59310"], "primary", "official", "nvd_api"),
    ("S05", "NVD: CVE-2026-65400", "https://nvd.nist.gov/vuln/detail/CVE-2026-65400", ["CVE-2026-65400"], "primary", "official", "nvd_api"),
    ("S06", "NVD: CVE-2026-63520", "https://nvd.nist.gov/vuln/detail/CVE-2026-63520", ["CVE-2026-63520"], "primary", "official", "nvd_api"),
    ("S07", "Microsoft Security Response Center: CVE-2026-33824", "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33824", ["CVE-2026-33824"], "primary", "publisher", "html"),
    ("S08", "Rapid7: SharePoint JWT authentication bypass CVE-2026-55040", "https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-jwt-token-authentication-bypass-cve-2026-55040/", ["CVE-2026-55040"], "primary", "researcher", "html"),
    ("S09", "Rapid7: SharePoint RCE CVE-2026-63520", "https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-remote-code-execution-cve-2026-63520/", ["CVE-2026-63520"], "primary", "researcher", "html"),
    ("S10", "VulnCheck: SharePoint unsafe type RCE CVE-2026-63520", "https://www.vulncheck.com/blog/cve-2026-63520-sharepoint-unsafe-type-rce", ["CVE-2026-63520"], "primary", "researcher", "html"),
    ("S11", "BleepingComputer: VMware vCenter RCE exploitation", "https://www.bleepingcomputer.com/news/security/critical-vmware-vcenter-rce-flaw-exploited-for-reverse-ssh-access/", ["CVE-2026-59310"], "secondary", "journalistic", "html"),
    ("S12", "Medium: active exploitation of CVE-2026-59310", "https://medium.com/@quirso_de/active-exploitation-of-cve-2026-59310-361-victim-ips-across-47-countries-9783187cc6ff", ["CVE-2026-59310"], "secondary", "researcher", "html"),
    ("S13", "Malwarebytes: macOS Screen Sharing vulnerability", "https://www.malwarebytes.com/blog/bugs/2026/08/update-your-mac-screen-sharing-vulnerability-exploited-in-the-wild", ["CVE-2026-65400"], "secondary", "journalistic", "html"),
    ("S14", "NCSC Netherlands advisory 2026-0280", "https://advisories.ncsc.nl/2026/ncsc-2026-0280.html", ["CVE-2026-65400"], "primary", "official", "html"),
    ("S15", "Apple security update 148170", "https://support.apple.com/en-us/148170", ["CVE-2026-65400"], "primary", "publisher", "html"),
    ("S16", "Unit 42: autonomous AI cyber attack campaign", "https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/", ["CVE-2026-33824"], "secondary", "researcher", "html"),
    ("S17", "DIESEC: cybersecurity news, August 21 2026", "https://diesec.com/2026/08/top-5-cybersecurity-news-stories-august-21-2026/", ["CVE-2026-55040", "CVE-2026-59310", "CVE-2026-65400"], "secondary", "commercial", "html"),
    ("S18", "Help Net Security: SharePoint CVE-2026-55040 PoC", "https://www.helpnetsecurity.com/2026/08/13/microsoft-sharepoint-cve-2026-55040-poc-exploit/", ["CVE-2026-55040"], "secondary", "journalistic", "html"),
    ("S19", "CISA BOD 26-04: prioritizing security updates", "https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk", [], "primary", "official", "html"),
    ("S20", "MITRE ATT&CK T1190: Exploit Public-Facing Application", "https://attack.mitre.org/techniques/T1190/", [], "primary", "official_framework", "html"),
    ("S21", "FIRST EPSS: CVE-2026-33824", "https://api.first.org/data/v1/epss?cve=CVE-2026-33824", ["CVE-2026-33824"], "primary", "official", "api"),
    ("S22", "FIRST EPSS: CVE-2026-55040", "https://api.first.org/data/v1/epss?cve=CVE-2026-55040", ["CVE-2026-55040"], "primary", "official", "api"),
    ("S23", "FIRST EPSS: CVE-2026-59310", "https://api.first.org/data/v1/epss?cve=CVE-2026-59310", ["CVE-2026-59310"], "primary", "official", "api"),
    ("S24", "FIRST EPSS: CVE-2026-65400", "https://api.first.org/data/v1/epss?cve=CVE-2026-65400", ["CVE-2026-65400"], "primary", "official", "api"),
    ("S25", "FIRST EPSS: CVE-2026-63520", "https://api.first.org/data/v1/epss?cve=CVE-2026-63520", ["CVE-2026-63520"], "primary", "official", "api"),
    ("S27", "Broadcom VMSA-2026-0006", "https://support.broadcom.com/", [], "primary", "publisher", "unavailable"),
    # Ajoutées pour affiner l'interprétation des métriques (CVSS/EPSS/SSVC) et
    # croiser les statuts KEV/CNA/ADP. Union avec S01-S25/S27 : les doublons
    # stricts (même CVE, même page NVD/MSRC/ATT&CK/Apple déjà listée) ont été
    # écartés ; les liens ?utm_source=chatgpt.com ont été nettoyés.
    ("S28", "CISA GovDelivery bulletin 2026-08-18", "https://content.govdelivery.com/accounts/USDHSCISA/bulletins/425854d", ["CVE-2026-33824", "CVE-2026-55040", "CVE-2026-59310", "CVE-2026-65400"], "primary", "official", "html"),
    ("S29", "CISA KEV catalog entry: CVE-2026-33824", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-33824", ["CVE-2026-33824"], "primary", "official", "html"),
    ("S30", "CISA KEV catalog entry: CVE-2026-55040", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-55040", ["CVE-2026-55040"], "primary", "official", "html"),
    ("S31", "CISA KEV catalog entry: CVE-2026-59310", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-59310", ["CVE-2026-59310"], "primary", "official", "html"),
    ("S32", "CISA KEV catalog entry: CVE-2026-65400", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-65400", ["CVE-2026-65400"], "primary", "official", "html"),
    ("S33", "CVE.org record: CVE-2026-33824", "https://www.cve.org/CVERecord?id=CVE-2026-33824", ["CVE-2026-33824"], "primary", "official", "html"),
    ("S34", "CVE.org record: CVE-2026-55040", "https://www.cve.org/CVERecord?id=CVE-2026-55040", ["CVE-2026-55040"], "primary", "official", "html"),
    ("S35", "CVE.org record: CVE-2026-63520", "https://www.cve.org/CVERecord?id=CVE-2026-63520", ["CVE-2026-63520"], "primary", "official", "html"),
    ("S36", "CVE.org record: CVE-2026-59310", "https://www.cve.org/CVERecord?id=CVE-2026-59310", ["CVE-2026-59310"], "primary", "official", "html"),
    ("S37", "CVE.org record: CVE-2026-65400", "https://www.cve.org/CVERecord?id=CVE-2026-65400", ["CVE-2026-65400"], "primary", "official", "html"),
    ("S38", "CVE.org: Authorized Data Publishers (ADP program)", "https://www.cve.org/ProgramOrganization/ADPs", [], "primary", "official_framework", "html"),
    ("S39", "MSRC: CVE-2026-55040", "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-55040", ["CVE-2026-55040"], "primary", "publisher", "html"),
    ("S40", "Rapid7: SharePoint JWT bypass CVE-2026-55040 (fixed)", "https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed/", ["CVE-2026-55040"], "primary", "researcher", "html"),
    ("S41", "Rapid7: SharePoint RCE CVE-2026-63520 (fixed)", "https://www.rapid7.com/blog/post/etr-cve-2026-63520-microsoft-sharepoint-remote-code-execution-fixed/", ["CVE-2026-63520"], "primary", "researcher", "html"),
    ("S42", "MSRC: CVE-2026-63520", "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-63520", ["CVE-2026-63520"], "primary", "publisher", "html"),
    ("S43", "Broadcom VMSA advisory (contenu spécifique)", "https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017", ["CVE-2026-59310"], "primary", "publisher", "html"),
    ("S44", "DIESEC: VMware vCenter CVE-2026-59310", "https://diesec.com/2026/08/vmware-vcenter-cve-2026-59310/", ["CVE-2026-59310"], "secondary", "commercial", "html"),
    ("S45", "BleepingComputer: Windows IKE CVE-2026-33824", "https://www.bleepingcomputer.com/news/security/cisa-critical-windows-ike-extension-flaw-now-exploited-in-attacks/", ["CVE-2026-33824"], "secondary", "journalistic", "html"),
    ("S46", "Sentrium Security: Windows IKE CVE-2026-33824", "https://www.sentrium.co.uk/labs/windows-ike-service-extensions-vulnerability-enables-remote-code-execution-cve-2026-33824", ["CVE-2026-33824"], "secondary", "researcher", "html"),
    ("S47", "FIRST EPSS: présentation", "https://www.first.org/epss/", [], "primary", "official_framework", "html"),
    ("S48", "FIRST EPSS: data", "https://www.first.org/epss/data.html", [], "primary", "official_framework", "html"),
    ("S49", "FIRST CVSS v4.0: page principale", "https://www.first.org/cvss/v4.0/", [], "primary", "official_framework", "html"),
    ("S50", "FIRST CVSS v4.0: specification", "https://www.first.org/cvss/v4.0/specification-document", [], "primary", "official_framework", "html"),
    ("S51", "FIRST CVSS v4.0: user guide", "https://www.first.org/cvss/v4.0/user-guide", [], "primary", "official_framework", "html"),
    ("S52", "FIRST CVSS v3.1: specification", "https://www.first.org/cvss/v3.1/specification-document", [], "primary", "official_framework", "html"),
    ("S53", "CISA: Stakeholder-Specific Vulnerability Categorization (SSVC)", "https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc", [], "primary", "official_framework", "html"),
    ("S54", "CISA: SSVC Guide (PDF)", "https://www.cisa.gov/sites/default/files/publications/cisa-ssvc-guide%20508c.pdf", [], "primary", "official_framework", "pdf_direct"),
    ("S55", "Apple security update 148171 (macOS Sequoia 15.7.9)", "https://support.apple.com/en-us/148171", ["CVE-2026-65400"], "primary", "publisher", "html"),
    ("S56", "Apple security update 148172 (macOS Sonoma 14.8.9)", "https://support.apple.com/en-us/148172", ["CVE-2026-65400"], "primary", "publisher", "html"),
    ("S57", "MITRE ATT&CK: Detection Strategy DET0080", "https://attack.mitre.org/detectionstrategies/DET0080/", [], "primary", "official_framework", "html"),
    ("S58", "CISA KEV catalog entry: CVE-2026-63520", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-63520", ["CVE-2026-63520"], "primary", "official", "html"),
]


def make_record(source, accessed_at):
    source_id, name, url, cves, level, category, kind = source
    methods = {
        "html": "html_trafilatura",
        "api": "api_json",
        "nvd_api": "api_json",
        "pdf_page": "pdf_pdfplumber",
        "pdf_direct": "pdf_pdfplumber",
        "unavailable": "not_attempted",
    }
    return {
        "source_id": source_id,
        "cve_ids": cves,
        "source_name": name,
        "url": url,
        "source_type": {"primary_secondary": level, "category": category},
        "date_accessed": accessed_at,
        "extraction_method": methods[kind],
        "extraction_method_used": "not_attempted" if kind == "unavailable" else "requests_trafilatura",
        "extraction_status": "failed",
        "raw_text": "",
        "http_status": None,
        "fallback_used": False,
        "original_url": None,
        "replacement_url": None,
        "replacement_reason": None,
        "search_query_used": None,
        "notes": "",
    }


def request_with_retry(session, url):
    """GET avec retry (5s/15s/30s) sur erreur réseau/5xx ; timeout 15s par tentative.

    Reste poli : PAUSE_SECONDS après chaque tentative, réussie ou non.
    """
    last_error = None
    for delay in RETRY_DELAYS:
        if delay:
            time.sleep(delay)
        try:
            response = session.get(url, timeout=TIMEOUT_SECONDS, allow_redirects=True)
        except (requests.ConnectionError, requests.Timeout) as error:
            last_error = f"{type(error).__name__}: {error}"
            time.sleep(PAUSE_SECONDS)
            continue
        time.sleep(PAUSE_SECONDS)
        if response.status_code >= 500:
            last_error = f"HTTP {response.status_code}"
            continue
        return response
    raise requests.RequestException(f"Échec après {len(RETRY_DELAYS)} tentatives : {last_error}")


def html_to_text(html, url):
    """Extrait l'article principal, avec readability-lxml comme repli."""
    text = trafilatura.extract(html, url=url, include_comments=False, include_tables=True)
    if text and text.strip():
        return text.strip(), "html_trafilatura"

    # readability produit encore du HTML : trafilatura le transforme ensuite en texte.
    article_html = Document(html).summary()
    text = trafilatura.extract(article_html, include_comments=False, include_tables=True)
    if text and text.strip():
        return text.strip(), "html_readability_lxml"
    return "", "html_trafilatura+readability_lxml"


SYSTEM_CHROMIUM = "/usr/bin/chromium"


def fetch_via_playwright(url):
    """Repli pour les pages qui nécessitent du JS (SPA) : rendu réel avant extraction.

    Utilise le Chromium système (SYSTEM_CHROMIUM) plutôt que le binaire géré par
    Playwright : son téléchargement automatique est bloqué dans cet environnement
    (CDN playwright.download.prss.microsoft.com injoignable).

    Une tentative unique confond un vrai squelette SPA avec un blip réseau
    transitoire du bac à sable (déjà observé côté requests, voir
    request_with_retry) : deux essais avec une courte pause suffisent à absorber
    ce cas sans masquer un échec réel.
    """
    last_error = None
    for attempt in range(2):
        if attempt:
            time.sleep(5)
        try:
            with sync_playwright() as pw:
                browser = pw.chromium.launch(executable_path=SYSTEM_CHROMIUM)
                page = browser.new_page(user_agent=HEADERS["User-Agent"])
                page.goto(url, timeout=30000, wait_until="networkidle")
                html = page.content()
                final_url = page.url
                browser.close()
            return html, final_url, None
        except Exception as error:
            last_error = f"{type(error).__name__}: {error}"
    return None, None, last_error


KEV_CATALOG_MARKER = "known-exploited-vulnerabilities-catalog"
KEV_PER_CVE_FIELDS = ("Due Date", "Required Action", "Date Added")


def isolate_kev_teasers(html):
    """Isole les blocs <article class="c-teaser"> (résultats du catalogue KEV filtré).

    Diagnostic : ces données sont bien rendues côté serveur (présentes dans le HTML
    brut de `requests`, pas besoin de JS/Playwright) mais `trafilatura` les élimine
    en les confondant avec le bruit de navigation/facettes du reste de la page quand
    on lui donne la page entière. Isoler le fragment avant extraction règle le
    problème (vérifié manuellement sur S29-S32).
    """
    teasers = re.findall(r'<article[^>]*class="[^"]*c-teaser[^"]*"[^>]*>.*?</article>', html, re.S)
    if not teasers:
        return html
    return "<html><body>" + "".join(teasers) + "</body></html>"


def prepare_html(html, url):
    if KEV_CATALOG_MARKER in url and "field_cve=" in url:
        return isolate_kev_teasers(html)
    return html


def is_suspect(text, url=""):
    lowered = text.lower()
    reasons = []
    if len(text) < MIN_TEXT_LENGTH:
        reasons.append(f"texte extrait trop court ({len(text)} caractères, seuil {MIN_TEXT_LENGTH})")
    if "enable javascript" in lowered or "javascript is required" in lowered:
        reasons.append("la page demande JavaScript")
    if KEV_CATALOG_MARKER in url and "field_cve=" in url:
        if not any(field in text for field in KEV_PER_CVE_FIELDS):
            reasons.append(
                "page KEV filtrée sans données par-CVE "
                f"({'/'.join(KEV_PER_CVE_FIELDS)} absents)"
            )
    return reasons


def find_pdf_url(page_html, page_url):
    """Trouve le lien Open PDF d'une page DTIC-like, sans supposer son URL."""
    matches = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', page_html, re.I | re.S)
    for href, label in matches:
        clean_label = re.sub(r"<[^>]+>", " ", unescape(label)).lower()
        if "open pdf" in clean_label or href.lower().split("?")[0].endswith(".pdf"):
            return urljoin(page_url, unescape(href))
    return None


def extract_pdf(pdf_bytes):
    with pdfplumber.open(BytesIO(pdf_bytes)) as pdf:
        return "\n\n".join(page.extract_text() or "" for page in pdf.pages).strip()


def failure_entry(record, error, kind="failed"):
    return {
        "source_id": record["source_id"],
        "url": record["url"],
        "http_status": record["http_status"],
        "extraction_status": record["extraction_status"],
        "kind": kind,
        "error": error,
    }


def save_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def medium_search_fallback(session, record, primary_error, pw_error):
    """S12 uniquement : remplacement web manuel si requests et Playwright échouent tous les deux.

    Ne remplace jamais silencieusement — S12_REPLACEMENT doit être rempli à la main
    après une recherche explicite (voir en tête de fichier).
    """
    if S12_REPLACEMENT is None:
        record["extraction_status"] = "failed"
        record["notes"] = (
            f"Échec requests ({primary_error}) ; échec Playwright ({pw_error}) ; "
            "aucun remplacement web configuré pour l'instant (S12_REPLACEMENT vide)."
        )
        return record, failure_entry(record, record["notes"])

    record["fallback_used"] = True
    record["original_url"] = record["url"]
    record["replacement_url"] = S12_REPLACEMENT["replacement_url"]
    record["replacement_reason"] = S12_REPLACEMENT["replacement_reason"]
    record["search_query_used"] = S12_REPLACEMENT["search_query_used"]
    record["url"] = S12_REPLACEMENT["replacement_url"]

    try:
        response = request_with_retry(session, S12_REPLACEMENT["replacement_url"])
    except Exception as error:
        record["extraction_status"] = "failed"
        record["notes"] = f"Remplacement web configuré mais inaccessible : {type(error).__name__}: {error}"
        return record, failure_entry(record, record["notes"])

    record["http_status"] = response.status_code
    if response.status_code != 200:
        record["extraction_status"] = "failed"
        record["notes"] = f"Remplacement web : HTTP {response.status_code}."
        return record, failure_entry(record, record["notes"])

    text, method = html_to_text(response.text, response.url)
    reasons = is_suspect(text)
    record["raw_text"] = text
    record["extraction_method"] = method
    record["extraction_method_used"] = "search_fallback"
    if reasons:
        record["extraction_status"] = "partial_suspect"
        record["notes"] = "; ".join(reasons)
        return record, failure_entry(record, record["notes"], kind="manual_review")
    record["extraction_status"] = "success"
    return record, None


def fallback_or_fail_html(session, record, source_id, url, primary_error, partial_text=""):
    """Deuxième essai en Playwright (rendu JS réel) pour toute page HTML suspecte ou en échec."""
    html, final_url, pw_error = fetch_via_playwright(url)
    if html is not None:
        text, method = html_to_text(prepare_html(html, final_url or url), final_url or url)
        reasons = is_suspect(text, url)
        if not reasons:
            record["raw_text"] = text
            record["extraction_method"] = f"playwright+{method}"
            record["extraction_method_used"] = "playwright"
            record["extraction_status"] = "success"
            record["notes"] = f"Extraction directe insuffisante ({primary_error}) ; réussie via Playwright."
            return record, None
        pw_error = "; ".join(reasons)

    # Playwright n'a pas suffi non plus (ou a levé une exception).
    if source_id == "S12":
        return medium_search_fallback(session, record, primary_error, pw_error)

    record["raw_text"] = partial_text
    record["extraction_status"] = "partial_suspect" if partial_text else "failed"
    record["notes"] = f"Échec requests ({primary_error}) ; échec Playwright ({pw_error})."
    kind = "manual_review" if partial_text else "failed"
    return record, failure_entry(record, record["notes"], kind=kind)


def process_html_source(session, record, url, source_id):
    try:
        response = request_with_retry(session, url)
    except requests.RequestException as error:
        return fallback_or_fail_html(session, record, source_id, url, primary_error=str(error))

    record["http_status"] = response.status_code
    if response.status_code != 200:
        return fallback_or_fail_html(session, record, source_id, url, primary_error=f"HTTP {response.status_code}")

    text, method = html_to_text(prepare_html(response.text, response.url), response.url)
    reasons = is_suspect(text, url)
    if not reasons:
        record["raw_text"] = text
        record["extraction_method"] = method
        record["extraction_method_used"] = "requests_trafilatura"
        record["extraction_status"] = "success"
        return record, None

    return fallback_or_fail_html(session, record, source_id, url, primary_error="; ".join(reasons), partial_text=text)


def process_api_source(session, record, url):
    response = request_with_retry(session, url)
    record["http_status"] = response.status_code
    record["extraction_method_used"] = "api_json"
    if response.status_code != 200:
        record["notes"] = f"HTTP {response.status_code} : aucun contenu utilisé."
        return record, failure_entry(record, record["notes"])

    payload = response.json()
    record["raw_text"] = json.dumps(payload, ensure_ascii=False, indent=2)
    if not isinstance(payload, dict) or not payload.get("data"):
        record["extraction_status"] = "partial_suspect"
        record["notes"] = "API EPSS : réponse JSON sans donnée CVE exploitable."
        return record, failure_entry(record, record["notes"], kind="manual_review")

    record["extraction_status"] = "success"
    return record, None


def process_nvd_api_source(session, record, source):
    """NVD sert une SPA vide côté HTML (diagnostic confirmé) : on interroge l'API officielle."""
    _, _, page_url, cves, _, _, _ = source
    cve_id = cves[0]
    api_url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"

    response = request_with_retry(session, api_url)
    record["http_status"] = response.status_code
    record["extraction_method_used"] = "api_json"
    if response.status_code != 200:
        record["notes"] = f"HTTP {response.status_code} sur l'API NVD : aucun contenu utilisé."
        return record, failure_entry(record, record["notes"])

    payload = response.json()
    record["raw_text"] = json.dumps(payload, ensure_ascii=False, indent=2)
    record["notes"] = (
        f"Page NVD ({page_url}) est une SPA sans contenu serveur (diagnostic confirmé) ; "
        f"données récupérées via l'API officielle ({api_url})."
    )
    if not payload.get("vulnerabilities"):
        record["extraction_status"] = "partial_suspect"
        record["notes"] += " Réponse JSON sans CVE exploitable."
        return record, failure_entry(record, record["notes"], kind="manual_review")

    record["extraction_status"] = "success"
    return record, None


def process_pdf_source(session, record, url):
    response = request_with_retry(session, url)
    record["http_status"] = response.status_code
    if response.status_code != 200:
        record["notes"] = f"HTTP {response.status_code} : aucun contenu utilisé."
        return record, failure_entry(record, record["notes"])

    pdf_url = find_pdf_url(response.text, response.url)
    if not pdf_url:
        record["notes"] = "Lien « Open PDF » introuvable sur la page."
        return record, failure_entry(record, record["notes"])

    pdf_response = request_with_retry(session, pdf_url)
    record["http_status"] = pdf_response.status_code
    if pdf_response.status_code != 200:
        record["notes"] = f"Téléchargement du PDF : HTTP {pdf_response.status_code}."
        return record, failure_entry(record, record["notes"])

    record["url"] = pdf_response.url
    record["raw_text"] = extract_pdf(pdf_response.content)
    record["extraction_method_used"] = "requests_trafilatura"
    record["notes"] = f"PDF téléchargé depuis {pdf_response.url}"

    reasons = is_suspect(record["raw_text"])
    if reasons:
        record["extraction_status"] = "partial_suspect"
        record["notes"] += " ; " + "; ".join(reasons)
        return record, failure_entry(record, record["notes"], kind="manual_review")

    record["extraction_status"] = "success"
    return record, None


def process_pdf_direct_source(session, record, url):
    """PDF téléchargeable directement (URL déjà connue), sans page intermédiaire à parser."""
    response = request_with_retry(session, url)
    record["http_status"] = response.status_code
    if response.status_code != 200:
        record["notes"] = f"HTTP {response.status_code} : aucun contenu utilisé."
        return record, failure_entry(record, record["notes"])

    record["raw_text"] = extract_pdf(response.content)
    record["notes"] = f"PDF téléchargé depuis {response.url}"

    reasons = is_suspect(record["raw_text"])
    if reasons:
        record["extraction_status"] = "partial_suspect"
        record["notes"] += " ; " + "; ".join(reasons)
        return record, failure_entry(record, record["notes"], kind="manual_review")

    record["extraction_status"] = "success"
    return record, None


def process_source(session, source, accessed_at):
    record = make_record(source, accessed_at)
    source_id, _, url, _, _, _, kind = source

    if kind == "unavailable":
        record["notes"] = "Accès non disponible : source volontairement non tentée (login Broadcom requis)."
        return record, failure_entry(record, record["notes"])

    try:
        if kind == "api":
            return process_api_source(session, record, url)
        if kind == "nvd_api":
            return process_nvd_api_source(session, record, source)
        if kind == "pdf_page":
            return process_pdf_source(session, record, url)
        if kind == "pdf_direct":
            return process_pdf_direct_source(session, record, url)
        return process_html_source(session, record, url, source_id)
    # Une erreur de parsing imprévue ne doit jamais interrompre la collecte suivante.
    except Exception as error:
        record["notes"] = f"{type(error).__name__}: {error}"
        return record, failure_entry(record, record["notes"])


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    # Nettoie tout résidu d'une source retirée du corpus (ex. S26).
    for stale in RAW_DIR.glob("*.json"):
        if stale.stem not in {source[0] for source in SOURCES}:
            stale.unlink()

    accessed_at = datetime.now(timezone.utc).isoformat()
    failures = []
    records = []

    with requests.Session() as session:
        session.headers.update(HEADERS)
        for source in SOURCES:
            record, issue = process_source(session, source, accessed_at)
            save_json(RAW_DIR / f"{record['source_id']}.json", record)
            records.append(record)
            if issue:
                failures.append(issue)
            print(f"{record['source_id']}: {record['extraction_status']} ({len(record['raw_text'])} caractères)")

    save_json(OUTPUT_DIR / "failed_sources.json", failures)
    summary_lines = ["# Résumé de collecte", "", "| Source | Statut | Caractères extraits |", "|---|---|---:|"]
    summary_lines.extend(
        f"| {record['source_id']} | {record['extraction_status']} | {len(record['raw_text'])} |"
        for record in records
    )
    (OUTPUT_DIR / "summary.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    print(f"\nCorpus écrit dans {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
