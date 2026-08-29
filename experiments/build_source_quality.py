#!/usr/bin/env python3
"""Score the corpus against the §14.1 source-quality dimensions.

The scoring is derived from metadata the corpus builder already declared -- it is not
a fresh human judgement per source. Each dimension below states the rule it applies, so
a reader can disagree with the rule rather than with 57 individual opinions.

Read path matters: `source_type` (primary/secondary, category) lives in `corpus/raw/`,
NOT in `corpus/clean/`. `preprocess_corpus.py` does not propagate it, and `clean/` is
what the extraction pipeline reads -- which is itself a finding, reported at the end:
the KG was built with no notion of how credible any source was.

Standard library only.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "corpus" / "raw"
CLEAN = ROOT / "corpus" / "clean"
FAILED = ROOT / "corpus" / "failed_sources.json"
OUT = ROOT / "deliverables" / "sources.md"

# --- Scoring rules, stated once and applied uniformly ------------------------

# Authority: who is speaking, and with what standing on this fact.
AUTHORITY = {
    "official": 5,             # NVD, CISA, FIRST -- the system of record
    "official_framework": 4,   # MITRE ATT&CK, CVSS specs -- normative, not CVE-specific
    "publisher": 4,            # Microsoft MSRC, Apple -- authoritative on their product
    "researcher": 3,           # Rapid7, VulnCheck -- primary technical analysis
    "journalistic": 2,         # BleepingComputer, Help Net -- reports others' findings
    "commercial": 1,           # vendor blog -- promotional framing
}

# Evidence level: first-hand vs reporting on someone else.
TIER = {"primary": 2, "secondary": 1}

# Accessibility: how hard the source was to obtain, which bears on reproducibility.
ACCESS = {
    "api_json": 5,                      # stable, versioned, machine-readable
    "html_trafilatura": 4,              # plain fetch succeeded
    "playwright+html_trafilatura": 3,   # needed a browser (403 or JS-rendered)
    "pdf_pdfplumber": 3,                # stable but layout-fragile
    "not_attempted": 0,                 # deliberately not fetched
}

# The ~8 source families that carry the decision-relevant facts. Everything else
# corroborates. This is the answer to §9's "5 to 10 principal sources" against a
# 56-source corpus: the corpus is wide, the evidential base is narrow.
# Keyed by family, because "5 to 10 principal sources" means source families, not
# individual fetches: NVD is one system of record queried five times, not five sources.
PRINCIPAL_FAMILIES = {
    "NVD (NIST)": ("NVD:",),
    "FIRST EPSS": ("FIRST EPSS:",),
    "CISA KEV": ("CISA KEV",),
    "CISA BOD 26-04": ("CISA BOD",),
    "Microsoft MSRC": ("Microsoft Security Response", "MSRC:"),
    "Rapid7": ("Rapid7:",),
    "VulnCheck": ("VulnCheck:",),
    "Apple": ("Apple security update",),
    "Broadcom": ("Broadcom VMSA",),
}


def family_of(name: str):
    for family, prefixes in PRINCIPAL_FAMILIES.items():
        if name.startswith(prefixes):
            return family
    return None


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    raw_records = [load_json(p) for p in sorted(RAW.glob("S*.json"))]
    clean_ids = {p.stem for p in CLEAN.glob("S*.json")}
    failed = {f["source_id"]: f for f in load_json(FAILED)}

    rows = []
    for rec in raw_records:
        sid = rec["source_id"]
        stype = rec.get("source_type") or {}
        category = stype.get("category", "unknown")
        tier = stype.get("primary_secondary", "unknown")
        method = rec.get("extraction_method", "unknown")
        status = rec.get("extraction_status", "unknown")

        authority = AUTHORITY.get(category, 0)
        evidence = TIER.get(tier, 0)
        access = ACCESS.get(method, 2)
        # A source that never reached the clean corpus contributes nothing to the KG,
        # whatever its authority -- that is the point of scoring accessibility at all.
        in_corpus = sid in clean_ids
        total = authority + evidence + access if in_corpus else 0

        rows.append({
            "source_id": sid,
            "name": rec.get("source_name", ""),
            "tier": tier,
            "category": category,
            "method": method,
            "status": status,
            "in_clean_corpus": in_corpus,
            "authority": authority,
            "evidence_level": evidence,
            "accessibility": access,
            "score": total,
            "family": family_of(rec.get("source_name", "")),
            "principal": family_of(rec.get("source_name", "")) is not None,
        })

    principal = [r for r in rows if r["principal"]]
    corroborating = [r for r in rows if not r["principal"]]

    lines = []
    add = lines.append
    add("# Qualité des sources (§14.1)")
    add("")
    add("*Document généré par `experiments/build_source_quality.py`. Les scores sont "
        "dérivés de métadonnées déclarées à la collecte, par une règle unique appliquée "
        "à toutes les sources — pas par une appréciation source par source. On peut "
        "contester la règle ; on n'a pas à contester 57 jugements individuels.*")
    add("")

    add("## Règle de scoring")
    add("")
    add("| Dimension | Règle | Échelle |")
    add("|---|---|---|")
    add("| Autorité | catégorie déclarée de l'émetteur | official 5 · framework 4 · "
        "éditeur 4 · chercheur 3 · presse 2 · commercial 1 |")
    add("| Niveau de preuve | source de première main ou rapport de seconde main | "
        "primary 2 · secondary 1 |")
    add("| Accessibilité | méthode ayant permis la collecte | API 5 · HTML direct 4 · "
        "navigateur requis 3 · PDF 3 · non tentée 0 |")
    add("")
    add("**Deux dimensions du §14.1 ne sont pas instrumentées, et il faut le dire plutôt "
        "que de les simuler : la *fraîcheur* et la *stabilité dans le temps*.** Le seul "
        "champ temporel disponible est `date_accessed`, un horodatage de collecte "
        "(toutes les sources le 2026-08-28), pas une date de publication. Les scorer "
        "reviendrait à inventer une mesure.")
    add("")

    add("## Sources principales et corpus de corroboration")
    add("")
    families = {}
    for r in principal:
        families.setdefault(r["family"], []).append(r)
    add(f"Le brief (§9) recommande 5 à 10 sources principales ; le corpus compte "
        f"{len(rows)} fichiers déclarés. L'écart tient à une différence d'unité : ces "
        f"fichiers se ramènent à **{len(families)} familles de sources principales**, "
        f"interrogées plusieurs fois. Le NVD n'est pas cinq sources parce qu'on l'a "
        f"consulté pour cinq CVE : c'est un système de référence, requêté cinq fois.")
    add("")
    add(f"**{len(families)} familles principales couvrent {len(principal)} fichiers** et "
        f"portent les faits décisionnels ; les {len(corroborating)} fichiers restants "
        f"corroborent, datent, ou fournissent le cadre normatif (spécifications CVSS, "
        f"SSVC, ATT&CK). La base probante est étroite, le corpus est large — et c'est "
        f"cette distinction, pas le volume, qui répond au §9.")
    add("")
    add("### Familles principales")
    add("")
    add("| Famille | Fichiers | Rang | Catégorie | Score | Sources |")
    add("|---|---:|---|---|---:|---|")
    # Rank a family by its best-scoring member: one unreachable file (Broadcom's S27)
    # must not make the whole family look worthless when another member did land.
    for family, members in sorted(families.items(),
                                  key=lambda kv: -max(m["score"] for m in kv[1])):
        head = max(members, key=lambda m: m["score"])
        unreachable = [m["source_id"] for m in members if not m["in_clean_corpus"]]
        ids = ", ".join(m["source_id"] for m in sorted(members, key=lambda m: m["source_id"]))
        flag = f" *(dont {', '.join(unreachable)} inaccessible)*" if unreachable else ""
        add(f"| **{family}** | {len(members)} | {head['tier']} | {head['category']} | "
            f"{head['score']} | {ids[:52]}{flag} |")
    add("")

    add("## Distribution du corpus complet")
    add("")
    for field, title in (("category", "Catégorie"), ("tier", "Rang"), ("method", "Méthode de collecte")):
        counts = Counter(r[field] for r in rows)
        add(f"- **{title}** : " + " · ".join(f"{k} {v}" for k, v in counts.most_common()))
    add("")

    add("## Lacunes de source documentées (§7.1)")
    add("")
    add("Deux sources n'ont pas produit de contenu exploitable. Elles sont **enregistrées "
        "comme telles, jamais remplacées par du contenu plausible** — c'est la règle qui "
        "a gouverné toute la collecte.")
    add("")
    for sid, info in sorted(failed.items()):
        row = next((r for r in rows if r["source_id"] == sid), None)
        name = row["name"] if row else "(non déclarée)"
        add(f"- **{sid} — {name}** · statut `{info['extraction_status']}` · "
            f"{info['error']}")
    add("")
    add("Le cas S58 mérite d'être défendu explicitement : la page KEV de "
        "CVE-2026-63520 a répondu 200 mais sans données par-CVE, si bien que le graphe "
        "ne contient aucune échéance CISA pour cette vulnérabilité. On pourrait y voir "
        "une lacune de collecte qui fausserait la tâche T5. Ce n'est pas le cas : "
        "l'enregistrement NVD de cette même CVE (S06) ne contient **aucun** champ "
        "`cisa*`, alors que S02–S05 en contiennent quatre chacun. Deux sources "
        "indépendantes concordent — CVE-2026-63520 n'est pas au catalogue KEV. C'est une "
        "**preuve d'absence**, pas une **absence de preuve**.")
    add("")

    add("## Limite structurelle : la crédibilité n'atteint pas le graphe")
    add("")
    add("Les champs de rang et de catégorie utilisés ci-dessus vivent dans "
        "`corpus/raw/`. `preprocess_corpus.py` ne les propage pas vers `corpus/clean/`, "
        "qui est pourtant le seul répertoire lu par le pipeline d'extraction. "
        "**Conséquence : une affirmation issue d'un billet commercial et une affirmation "
        "issue du NVD entrent dans le KG avec exactement le même poids.** Aucune "
        "pondération par fiabilité n'existe aujourd'hui. C'est une extension naturelle "
        "de la méthode, et l'une des premières à mener.")
    add("")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"scored {len(rows)} declared sources "
          f"({sum(1 for r in rows if r['in_clean_corpus'])} in clean corpus)")
    print(f"  principal: {len(principal)}   corroborating: {len(corroborating)}")
    print(f"  documented source gaps: {sorted(failed)}")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
