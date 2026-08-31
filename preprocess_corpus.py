"""Prétraite le corpus brut (corpus/raw/) pour l'étape d'extraction de triples.

Lancement (depuis la racine du projet) :
    .venv/bin/python preprocess_corpus.py

Ne touche jamais à corpus/raw/ : la sortie va dans corpus/clean/. Chaque étape
est traçable (rien n'est supprimé silencieusement) :
  1. Déduplication par contenu (Jaccard sur shingles de mots, calculée sur le
     clean_text final, pas sur le JSON brut échappé) — rapport seulement,
     aucune suppression automatique.
  2. Filtrage du bruit résiduel pour les sources HTML (motifs explicites :
     cookies, newsletter, partage, articles similaires, copyright) — chaque
     ligne retirée est loguée. Sans objet pour les sources api_json (voir 6).
  3. Normalisation des espaces/caractères de contrôle.
  4. Segmentation des sources longues (> SEGMENT_THRESHOLD) en chunks.
  5. Marquage de pertinence (cve-specific vs framework) d'après cve_ids.
  6. Sources api_json (NVD, EPSS) : le JSON est parsé et reformaté en prose
     lisible (format_nvd_cve/format_epss) plutôt que traité comme du texte
     libre — le filtrage de bruit ligne-à-ligne n'a pas de sens sur du JSON.
     Le JSON d'origine est conservé tel quel (objet, pas string échappée)
     dans le champ "raw_json" pour rester la source de vérité structurée.
  7. Propagation des métadonnées de fiabilité : catégorie, rang primaire/
     secondaire, méthode de collecte et score d'autorité sont COPIÉS de raw/
     vers clean/ (champ "source_authority"), avec la règle unique de
     experiments/build_source_quality.py. C'est ce qui permet à
     build_canonical_kg() de joindre le score sur chaque arête par source_id.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW_DIR = Path("corpus/raw")
CLEAN_DIR = Path("corpus/clean")

# La règle de scoring d'autorité vit dans experiments/build_source_quality.py et n'est
# écrite qu'une seule fois. On l'importe pour COPIER son résultat dans clean/ ; on ne la
# réécrit pas ici, sinon la table §14.1 et le graphe pourraient diverger sur une même
# source sans que rien ne le signale.
sys.path.insert(0, str(ROOT / "experiments"))
from build_source_quality import score_source  # noqa: E402

SHINGLE_SIZE = 8
DEDUP_THRESHOLD = 0.5
SEGMENT_THRESHOLD = 8000
CHUNK_TARGET = 3000
CHUNK_OVERLAP = 200

# Motifs de bruit résiduel : liste courte et explicite (pas de filtre par longueur
# de ligne, pour ne jamais supprimer une vector string CVSS ou une ligne de tableau).
NOISE_PATTERNS = [
    re.compile(r"accept\s*(all)?\s*cookies?", re.I),
    re.compile(r"cookie\s*(policy|settings|consent)", re.I),
    re.compile(r"we use cookies", re.I),
    re.compile(r"subscribe (to (our)?\s*newsletter)?", re.I),
    re.compile(r"sign up for (our)?\s*newsletter", re.I),
    re.compile(r"share this (article|post)", re.I),
    re.compile(r"related (posts|articles)", re.I),
    re.compile(r"articles? similaires?", re.I),
    re.compile(r"you might also like", re.I),
    re.compile(r"^\s*©\s*\d{4}", re.I),
    re.compile(r"all rights reserved", re.I),
    re.compile(r"follow us on (twitter|x|linkedin|facebook|instagram)", re.I),
    re.compile(r"^\s*(advertisement|sponsored)\s*$", re.I),
]


def load_records():
    records = []
    for path in sorted(RAW_DIR.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record["raw_text"].strip():
            records.append(record)
    return records


def shingles(text, n=SHINGLE_SIZE):
    words = re.findall(r"\w+", text.lower())
    if len(words) < n:
        return {tuple(words)} if words else set()
    return {tuple(words[i : i + n]) for i in range(len(words) - n + 1)}


def jaccard(set_a, set_b):
    if not set_a or not set_b:
        return 0.0
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return inter / union if union else 0.0


def find_dedup_pairs(clean_records):
    """clean_records : dict source_id -> clean_record (utilise clean_text, jamais
    le JSON brut échappé des sources api_json)."""
    shingle_sets = {sid: shingles(cr["clean_text"]) for sid, cr in clean_records.items()}
    pairs = []
    ids = list(shingle_sets)
    for i, sid_a in enumerate(ids):
        for sid_b in ids[i + 1 :]:
            score = jaccard(shingle_sets[sid_a], shingle_sets[sid_b])
            if score > DEDUP_THRESHOLD:
                pairs.append((sid_a, sid_b, score))
    pairs.sort(key=lambda p: -p[2])
    return pairs


def filter_noise(text):
    kept_lines = []
    filtered = []
    for line in text.split("\n"):
        stripped = line.strip()
        matched_pattern = None
        if stripped:
            for pattern in NOISE_PATTERNS:
                if pattern.search(stripped):
                    matched_pattern = pattern.pattern
                    break
        if matched_pattern:
            filtered.append({"line": stripped, "pattern": matched_pattern})
        else:
            kept_lines.append(line)
    return "\n".join(kept_lines), filtered


def normalize_whitespace(text):
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def chunk_text(text, target=CHUNK_TARGET, overlap=CHUNK_OVERLAP):
    # trafilatura sépare ses paragraphes par un simple "\n" (pas "\n\n") ; pdfplumber
    # produit les deux selon la mise en page. On découpe sur "\n" pour couvrir les
    # deux cas sans dépendre du format d'une source en particulier.
    paragraphs = [p for p in text.split("\n") if p.strip()]
    chunks = []
    current = ""
    for para in paragraphs:
        if current and len(current) + len(para) + 1 > target:
            chunks.append(current.strip())
            # current[-overlap:] is a raw character slice and can land mid-word
            # (e.g. "knowledge" -> "edge"); drop any partial leading word so the
            # next chunk always starts on a real word boundary.
            tail = current[-overlap:]
            if len(tail) < len(current):
                space_idx = tail.find(" ")
                if space_idx != -1:
                    tail = tail[space_idx + 1:]
            current = f"{tail}\n{para}" if tail else para
        else:
            current = f"{current}\n{para}" if current else para
    if current.strip():
        chunks.append(current.strip())
    return chunks


def relevance_of(record):
    return "cve-specific" if record["cve_ids"] else "framework"


def _join_fields(pairs):
    """Joint des paires (label, valeur) en 'label: valeur | label: valeur', en
    sautant les valeurs absentes — évite d'écrire "Attack Vector: None"."""
    parts = [f"{label}: {value}" for label, value in pairs if value not in (None, "")]
    return " | ".join(parts)


def detect_json_kind(payload):
    """Distingue une réponse NVD (vulnerabilities[]) d'une réponse EPSS (data[].epss),
    sans dépendre du source_id — vaut aussi pour une future source du même type."""
    if isinstance(payload, dict) and payload.get("vulnerabilities"):
        return "nvd"
    if isinstance(payload, dict) and isinstance(payload.get("data"), list) and payload["data"]:
        if "epss" in payload["data"][0]:
            return "epss"
    return None


def format_nvd_cve(payload):
    """Reformate une réponse de l'API NVD (CVE unique) en prose lisible."""
    vulns = payload.get("vulnerabilities") or []
    if not vulns:
        return ""
    cve = vulns[0]["cve"]
    lines = []

    cve_id = cve.get("id", "")
    vuln_name = cve.get("cisaVulnerabilityName")
    lines.append(f"{cve_id} — {vuln_name}" if vuln_name else cve_id)

    published = (cve.get("published") or "")[:10]
    modified = (cve.get("lastModified") or "")[:10]
    lines.append(f"Publiée le {published}, dernière modification le {modified}, statut: {cve.get('vulnStatus', '')}.")

    for d in cve.get("descriptions", []):
        if d.get("lang") == "en":
            lines.append(f"Description: {d['value']}")
            break

    metrics = cve.get("metrics", {})
    for version_key in ("cvssMetricV40", "cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
        for entry in metrics.get(version_key, []):
            cvss = entry.get("cvssData", {})
            lines.append(
                f"CVSS {cvss.get('version', '')} (source: {entry.get('source', '')}, "
                f"{entry.get('type', '')}): {cvss.get('baseScore', '')} {cvss.get('baseSeverity', '')}"
            )
            if cvss.get("vectorString"):
                lines.append(f"Vector: {cvss['vectorString']}")
            row = _join_fields([
                ("Attack Vector", cvss.get("attackVector")),
                ("Attack Complexity", cvss.get("attackComplexity")),
                ("Privileges Required", cvss.get("privilegesRequired")),
            ])
            if row:
                lines.append(row)
            row = _join_fields([
                ("User Interaction", cvss.get("userInteraction")),
                ("Scope", cvss.get("scope")),
            ])
            if row:
                lines.append(row)
            impact = _join_fields([
                ("Confidentiality", cvss.get("confidentialityImpact")),
                ("Integrity", cvss.get("integrityImpact")),
                ("Availability", cvss.get("availabilityImpact")),
            ])
            if impact:
                lines.append(f"Impact: {impact}")
            scores = _join_fields([
                ("Exploitability score", entry.get("exploitabilityScore")),
                ("Impact score", entry.get("impactScore")),
            ])
            if scores:
                lines.append(scores)

    for entry in metrics.get("ssvcV203", []):
        ssvc = entry.get("ssvcData", {})
        options = {}
        for opt in ssvc.get("options", []):
            options.update(opt)
        opt_str = " | ".join(f"{k[0].upper()}{k[1:]}: {v}" for k, v in options.items())
        lines.append(f"SSVC ({ssvc.get('role', '')}, {(ssvc.get('timestamp') or '')[:10]}): {opt_str}")

    cwe_values = []
    for w in cve.get("weaknesses", []):
        for d in w.get("description", []):
            if d.get("lang") == "en":
                cwe_values.append(d["value"])
    if cwe_values:
        lines.append(", ".join(cwe_values))

    if cve.get("cisaExploitAdd"):
        lines.append(f"Statut CISA KEV: ajoutée le {cve['cisaExploitAdd']}, échéance {cve.get('cisaActionDue', '')}.")
        if cve.get("cisaRequiredAction"):
            lines.append(f"Action requise CISA: {cve['cisaRequiredAction']}")

    affected_lines = []
    for aff in cve.get("affected", []):
        for ad in aff.get("affectedData", []):
            vendor, product = ad.get("vendor") or "", ad.get("product") or ""
            # Le nom de produit répète parfois déjà le vendeur (ex. "Microsoft SharePoint
            # Server") : ne pas le préfixer une deuxième fois dans ce cas.
            if product.lower().startswith(vendor.lower()) and vendor:
                label = product
            else:
                label = " ".join(part for part in (vendor, product) if part)
            platforms = ad.get("platforms") or []
            if platforms:
                label += f" ({', '.join(platforms)})"
            version_bits = []
            for v in ad.get("versions", []):
                if v.get("lessThan"):
                    version_bits.append(f"versions < {v['lessThan']}")
                elif v.get("version"):
                    version_bits.append(v["version"])
            version_str = ", ".join(version_bits)
            affected_lines.append(f"- {label}" + (f" — {version_str}" if version_str else ""))
    if affected_lines:
        lines.append("Produits affectés:")
        lines.extend(affected_lines)

    ref_lines = []
    for ref in cve.get("references", []):
        tag_str = f" [{', '.join(ref.get('tags', []))}]" if ref.get("tags") else ""
        ref_lines.append(f"- {ref.get('url', '')}{tag_str}")
    if ref_lines:
        lines.append("Références:")
        lines.extend(ref_lines)

    return "\n".join(lines)


def format_epss(payload):
    """Reformate une réponse de l'API EPSS (FIRST.org) en prose lisible."""
    lines = []
    for entry in payload.get("data") or []:
        try:
            epss_val = f"{float(entry.get('epss')):.4f}"
        except (TypeError, ValueError):
            epss_val = entry.get("epss", "")
        try:
            pct_val = f"{float(entry.get('percentile')):.3f}"
        except (TypeError, ValueError):
            pct_val = entry.get("percentile", "")
        lines.append(f"{entry.get('cve', '')} — score EPSS {epss_val} (percentile {pct_val}) au {entry.get('date', '')}.")
    return "\n".join(lines)


def build_clean_record(record):
    """Construit l'enregistrement corpus/clean/{id}.json pour une source brute.

    Deux chemins : les sources api_json (NVD/EPSS) sont parsées et reformatées en
    prose (le filtrage de bruit ligne-à-ligne n'a pas de sens sur du JSON) ; les
    sources HTML/PDF suivent le pipeline texte libre habituel (filtrage + normalisation).
    """
    raw_json = None
    if record.get("extraction_method") == "api_json":
        payload = json.loads(record["raw_text"])
        kind = detect_json_kind(payload)
        if kind == "nvd":
            clean_text = format_nvd_cve(payload)
        elif kind == "epss":
            clean_text = format_epss(payload)
        else:
            # Structure JSON non reconnue : pas de prose inventée sur un format inconnu.
            clean_text = ""
        clean_text = normalize_whitespace(clean_text)
        filtered_lines = []
        raw_json = payload
    else:
        clean_text, filtered_lines = filter_noise(record["raw_text"])
        clean_text = normalize_whitespace(clean_text)

    needs_chunks = len(clean_text) > SEGMENT_THRESHOLD
    chunks = chunk_text(clean_text) if needs_chunks else None

    clean_record = {
        "source_id": record["source_id"],
        "source_name": record["source_name"],
        "cve_ids": record["cve_ids"],
        "url": record["url"],
        "extraction_status": record["extraction_status"],
        "extraction_method": record.get("extraction_method"),
        # Copié depuis raw/, jamais recalculé ici : catégorie, rang primaire/secondaire,
        # méthode de collecte et score d'autorité, tels que score_source() les produit.
        # Une source atteint clean/ par construction, d'où in_corpus=True.
        "source_authority": score_source(record, in_corpus=True),
        "relevance": relevance_of(record),
        "char_count_raw": len(record["raw_text"]),
        "char_count_clean": len(clean_text),
        "filtered_lines": filtered_lines,
        "clean_text": clean_text,
        "chunks": chunks,
    }
    if raw_json is not None:
        clean_record["raw_json"] = raw_json
    return clean_record


def main():
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    records = load_records()

    clean_records = {r["source_id"]: build_clean_record(r) for r in records}
    dedup_pairs = find_dedup_pairs(clean_records)

    for source_id, clean_record in clean_records.items():
        (CLEAN_DIR / f"{source_id}.json").write_text(
            json.dumps(clean_record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    noise_summary = [(sid, len(cr["filtered_lines"])) for sid, cr in clean_records.items()]

    dedup_lines = ["# Paires détectées comme doublons probables (Jaccard > 0.5)", ""]
    if dedup_pairs:
        dedup_lines += ["| Source A | Source B | Jaccard |", "|---|---|---:|"]
        dedup_lines += [f"| {a} | {b} | {score:.3f} |" for a, b, score in dedup_pairs]
    else:
        dedup_lines.append("Aucune paire au-dessus du seuil.")
    (CLEAN_DIR / "dedup_report.md").write_text("\n".join(dedup_lines) + "\n", encoding="utf-8")

    noise_lines = ["# Lignes filtrées comme bruit, par source", "", "| Source | Lignes filtrées |", "|---|---:|"]
    noise_lines += [f"| {sid} | {count} |" for sid, count in noise_summary]
    (CLEAN_DIR / "noise_filter_report.md").write_text("\n".join(noise_lines) + "\n", encoding="utf-8")

    print(f"{len(records)} sources prétraitées -> {CLEAN_DIR.resolve()}")
    print(f"Paires de doublons probables (Jaccard > {DEDUP_THRESHOLD}) : {len(dedup_pairs)}")
    print(f"Total de lignes filtrées comme bruit : {sum(c for _, c in noise_summary)}")


if __name__ == "__main__":
    main()
