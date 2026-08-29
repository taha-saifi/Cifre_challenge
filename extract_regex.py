"""Extraction de triples KG par règles/regex, à partir de corpus/clean/.

Deux chemins, selon la présence de "raw_json" dans le fichier clean/{id}.json :
- Sources api_json (S02-S06 NVD, S21-S25 EPSS) : mapping direct de champs
  structurés, aucun regex nécessaire.
- Sources HTML/PDF (clean_text libre) : patterns regex ancrés sur des
  passages réels du corpus (voir plan de correction validé — chaque pattern
  documente sa source d'inspiration et ses limites connues).

Sortie : kg/regex/nodes.json, kg/regex/edges.json

Ne modifie jamais corpus/clean/ ni corpus/raw/.
"""

import json
import re
from pathlib import Path

CLEAN_DIR = Path("corpus/clean")
OUT_DIR = Path("kg/regex")

KEV_DATE_ADDED_RE = re.compile(r"Date Added:\s*\n?\s*(\d{4}-\d{2}-\d{2})")
KEV_DUE_DATE_RE = re.compile(r"Due Date:\s*\n?\s*(\d{4}-\d{2}-\d{2})")
CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}")
CWE_RE = re.compile(r"CWE-\d{1,4}")
WORKAROUND_TABLE_RE = re.compile(r"Workarounds:\s*\n?\s*None\.?")
WORKAROUND_NARRATIVE_RE = re.compile(
    r"(no supported workaround|no workaround is available|provides no workarounds?|offers no workaround)",
    re.I,
)
ADVISORY_ID_RE = re.compile(r"Advisory ID:\s*\|?\s*([\w.\-]+)")
CVE_SECTION_ANCHOR_RE = re.compile(r"\((CVE-\d{4}-\d{4,7})\)")
CHAINS_TRIGGER_RE = re.compile(r"(can be chained to\b|chained (?:to|with)\b|paired with another vulnerability)", re.I)
VICTIM_COUNTRIES_RE = re.compile(
    r"(\d+)\D{0,40}victim\D{0,20}(?:IP|IPs|address(?:es)?)\D{0,40}across\D{0,10}(\d+)\D{0,15}countr",
    re.I,
)
SUPERSEDES_RE = re.compile(r"supersedes and (?:hereby )?revokes([^.]*)\.", re.I)
BOD_TOKEN_RE = re.compile(r"BOD [\d\-]+")


class NodeStore:
    def __init__(self):
        self.nodes = {}

    def add(self, node_id, node_type, attributes=None):
        attributes = attributes or {}
        if node_id not in self.nodes:
            self.nodes[node_id] = {"id": node_id, "type": node_type, "attributes": dict(attributes)}
        else:
            existing = self.nodes[node_id]["attributes"]
            for k, v in attributes.items():
                if v is not None and existing.get(k) is None:
                    existing[k] = v

    def as_list(self):
        return list(self.nodes.values())


def make_edge(subject, subject_type, relation, obj, object_type, qualifiers, source_id, evidence):
    return {
        "subject": subject, "subject_type": subject_type,
        "relation": relation,
        "object": obj, "object_type": object_type,
        "qualifiers": qualifiers or {},
        "source_id": source_id,
        "method": "regex",
        "evidence": evidence,
    }


# ---------------------------------------------------------------------------
# Chemin api_json (S02-S06 NVD, S21-S25 EPSS)
# ---------------------------------------------------------------------------

def extract_nvd(record, payload, nodes, edges):
    vulns = payload.get("vulnerabilities") or []
    if not vulns:
        return
    cve = vulns[0]["cve"]
    cve_id = cve["id"]
    source_id = record["source_id"]

    attrs = {}
    for version_key in ("cvssMetricV40", "cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
        for entry in cve.get("metrics", {}).get(version_key, []):
            cvss = entry.get("cvssData", {})
            attrs.setdefault("cvss_score", cvss.get("baseScore"))
            attrs.setdefault("cvss_vector", cvss.get("vectorString"))
            attrs.setdefault("cvss_severity", cvss.get("baseSeverity"))

    for entry in cve.get("metrics", {}).get("ssvcV203", []):
        ssvc = entry.get("ssvcData", {})
        opts = {}
        for o in ssvc.get("options", []):
            opts.update(o)
        attrs.setdefault("ssvc_automatable", opts.get("automatable"))
        attrs.setdefault("ssvc_technical_impact", opts.get("technicalImpact"))
        if "exploitation" in opts:
            edges.append(make_edge(
                cve_id, "CVE", "exploitation_status_per", opts["exploitation"], "literal",
                {"status_source": ssvc.get("role"), "timestamp": (ssvc.get("timestamp") or "")[:10]},
                source_id, f"metrics.ssvcV203: role={ssvc.get('role')}, options={ssvc.get('options')}",
            ))

    nodes.add(cve_id, "CVE", attrs)

    for w in cve.get("weaknesses", []):
        for d in w.get("description", []):
            if d.get("lang") == "en":
                nodes.add(d["value"], "CWE")
                edges.append(make_edge(
                    cve_id, "CVE", "has_weakness", d["value"], "CWE", {},
                    source_id, f"weaknesses[].description: {d['value']}",
                ))

    for aff in cve.get("affected", []):
        for ad in aff.get("affectedData", []):
            for v in ad.get("versions", []):
                if v.get("lessThan"):
                    pid = f"{ad['product']} < {v['lessThan']}"
                    nodes.add(pid, "Product/Version", {"vendor": ad.get("vendor")})
                    edges.append(make_edge(
                        cve_id, "CVE", "affects", pid, "Product/Version", {},
                        source_id,
                        f"affected[].affectedData: {ad.get('vendor')} {ad.get('product')} lessThan={v['lessThan']}",
                    ))

    for ref in cve.get("references", []):
        if "Patch" in ref.get("tags", []) or "Vendor Advisory" in ref.get("tags", []):
            nodes.add(ref["url"], "Advisory")
            edges.append(make_edge(
                cve_id, "CVE", "has_patch", ref["url"], "Advisory", {"tags": ref.get("tags", [])},
                source_id, f"references[]: {ref['url']} tags={ref.get('tags')}",
            ))

    if cve.get("cisaExploitAdd"):
        nodes.add("CISA-KEV", "KEV")
        edges.append(make_edge(
            cve_id, "CVE", "confirmed_exploited_by", "CISA-KEV", "KEV",
            {"date_added": cve["cisaExploitAdd"], "action_due": cve.get("cisaActionDue")},
            source_id, f"cisaExploitAdd={cve['cisaExploitAdd']}, cisaActionDue={cve.get('cisaActionDue')}",
        ))


def extract_epss(record, payload, nodes, edges):
    # Pas de relation dédiée dans le schéma validé : traité comme attribut du
    # nœud CVE, par analogie directe avec cvss_score/cvss_vector.
    for entry in payload.get("data") or []:
        cve_id = entry.get("cve")
        if not cve_id:
            continue
        try:
            epss_score = float(entry["epss"])
        except (TypeError, ValueError, KeyError):
            epss_score = None
        try:
            epss_percentile = float(entry["percentile"])
        except (TypeError, ValueError, KeyError):
            epss_percentile = None
        nodes.add(cve_id, "CVE", {
            "epss_score": epss_score, "epss_percentile": epss_percentile, "epss_date": entry.get("date"),
        })


def extract_from_api_json(record, nodes, edges):
    payload = record["raw_json"]
    if payload.get("vulnerabilities"):
        extract_nvd(record, payload, nodes, edges)
    elif isinstance(payload.get("data"), list):
        extract_epss(record, payload, nodes, edges)


# ---------------------------------------------------------------------------
# Chemin HTML/PDF (texte libre)
# ---------------------------------------------------------------------------

def context(text, start, end, radius=60):
    return text[max(0, start - radius):min(len(text), end + radius)].replace("\n", " ").strip()


def extract_has_weakness(record, text, nodes, edges):
    if len(record["cve_ids"]) != 1:
        return
    cve_id = record["cve_ids"][0]
    seen = set()
    for m in CWE_RE.finditer(text):
        if m.group() in seen:
            continue
        seen.add(m.group())
        nodes.add(m.group(), "CWE")
        edges.append(make_edge(
            cve_id, "CVE", "has_weakness", m.group(), "CWE", {},
            record["source_id"], context(text, m.start(), m.end()),
        ))


def extract_kev_teaser(record, text, nodes, edges):
    if len(record["cve_ids"]) != 1:
        return
    added = KEV_DATE_ADDED_RE.search(text)
    due = KEV_DUE_DATE_RE.search(text)
    if not added or not due:
        return
    cve_id = record["cve_ids"][0]
    nodes.add("CISA-KEV", "KEV")
    edges.append(make_edge(
        cve_id, "CVE", "confirmed_exploited_by", "CISA-KEV", "KEV",
        {"date_added": added.group(1), "action_due": due.group(1)},
        record["source_id"], f"Date Added: {added.group(1)} / Due Date: {due.group(1)}",
    ))


def _preceding_cve_anchor(text, pos):
    """CVE le plus proche AVANT `pos`, pour associer un fait à la bonne CVE
    dans une source multi-CVE structurée en sections (ex. avis Broadcom)."""
    best = None
    for m in CVE_SECTION_ANCHOR_RE.finditer(text, 0, pos):
        best = m.group(1)
    return best


def extract_vendor_workaround(record, text, nodes, edges):
    source_id = record["source_id"]

    # Cas structuré multi-CVE : "(CVE-XXXX-YYYYY)" comme ancre de section,
    # "Workarounds:\nNone" plus loin dans la même section (avis Broadcom-like).
    if CVE_SECTION_ANCHOR_RE.search(text):
        for m in WORKAROUND_TABLE_RE.finditer(text):
            cve_id = _preceding_cve_anchor(text, m.start())
            if cve_id:
                edges.append(make_edge(
                    cve_id, "CVE", "has_vendor_workaround", "false", "literal", {},
                    source_id, context(text, m.start(), m.end(), radius=100),
                ))
        return

    # Cas mono-CVE : formulation narrative, seulement sur les sources cve-specific
    # (les sources "framework" définissent le mot "workaround" en général, ce
    # n'est pas un statut par-CVE).
    if record["relevance"] != "cve-specific" or len(record["cve_ids"]) != 1:
        return
    cve_id = record["cve_ids"][0]
    m = WORKAROUND_TABLE_RE.search(text) or WORKAROUND_NARRATIVE_RE.search(text)
    if m:
        edges.append(make_edge(
            cve_id, "CVE", "has_vendor_workaround", "false", "literal", {},
            source_id, context(text, m.start(), m.end(), radius=100),
        ))


def extract_advisory_id_patch(record, text, nodes, edges):
    m = ADVISORY_ID_RE.search(text)
    if not m:
        return
    advisory_id = m.group(1)
    nodes.add(advisory_id, "Advisory")
    cve_ids = sorted(set(CVE_RE.findall(text)))
    for cve_id in cve_ids:
        edges.append(make_edge(
            cve_id, "CVE", "has_patch", advisory_id, "Advisory", {},
            record["source_id"], context(text, m.start(), m.end(), radius=150),
        ))


def extract_chains_with(record, text, nodes, edges):
    for m in CHAINS_TRIGGER_RE.finditer(text):
        window_start = max(0, m.start() - 200)
        window_end = min(len(text), m.end() + 200)
        window = text[window_start:window_end]
        found = list(dict.fromkeys(CVE_RE.findall(window)))  # unique, ordre préservé
        if len(found) == 2:
            edges.append(make_edge(
                found[0], "CVE", "chains_with", found[1], "CVE", {},
                record["source_id"], context(text, m.start(), m.end(), radius=200),
            ))


def extract_exploitation_signal(record, text, nodes, edges):
    for m in VICTIM_COUNTRIES_RE.finditer(text):
        cve_id = _preceding_cve_anchor(text, m.start())
        if not cve_id:
            # Repli : recherche la CVE la plus proche avant le match, hors format
            # "(CVE-...)" (ex. mention en prose libre).
            preceding = list(CVE_RE.finditer(text, 0, m.start()))
            cve_id = preceding[-1].group() if preceding else None
        if not cve_id:
            continue
        victim_count, countries = int(m.group(1)), int(m.group(2))
        signal_id = f"signal-{record['source_id']}-{cve_id}"
        nodes.add(signal_id, "Exploitation Signal", {
            "reported_by": record["source_name"], "victim_count": victim_count, "countries": countries,
        })
        edges.append(make_edge(
            cve_id, "CVE", "has_exploitation_signal", signal_id, "Exploitation Signal", {},
            record["source_id"], context(text, m.start(), m.end(), radius=100),
        ))


def extract_supersedes(record, text, nodes, edges):
    m = SUPERSEDES_RE.search(text)
    if not m:
        return
    subject_match = BOD_TOKEN_RE.search(record["source_name"])
    if not subject_match:
        return
    subject = subject_match.group()
    nodes.add(subject, "Advisory")
    for obj in BOD_TOKEN_RE.findall(m.group(1)):
        nodes.add(obj, "Advisory")
        edges.append(make_edge(
            subject, "Advisory", "supersedes", obj, "Advisory", {},
            record["source_id"], context(text, m.start(), m.end(), radius=50),
        ))


def extract_from_html(record, nodes, edges):
    text = record["clean_text"]
    extract_has_weakness(record, text, nodes, edges)
    extract_kev_teaser(record, text, nodes, edges)
    extract_vendor_workaround(record, text, nodes, edges)
    extract_advisory_id_patch(record, text, nodes, edges)
    extract_chains_with(record, text, nodes, edges)
    extract_exploitation_signal(record, text, nodes, edges)
    extract_supersedes(record, text, nodes, edges)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    nodes = NodeStore()
    edges = []

    for path in sorted(CLEAN_DIR.glob("S*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if "raw_json" in record:
            extract_from_api_json(record, nodes, edges)
        else:
            extract_from_html(record, nodes, edges)

    (OUT_DIR / "nodes.json").write_text(
        json.dumps(nodes.as_list(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (OUT_DIR / "edges.json").write_text(
        json.dumps(edges, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"{len(nodes.as_list())} nœuds, {len(edges)} edges -> {OUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
