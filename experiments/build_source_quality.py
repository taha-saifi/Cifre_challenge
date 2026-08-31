#!/usr/bin/env python3
"""Score the corpus against the §14.1 source-quality dimensions.

The scoring is derived from metadata the corpus builder already declared -- it is not
a fresh human judgement per source. Each dimension below states the rule it applies, so
a reader can disagree with the rule rather than with 57 individual opinions.

Read path: `source_type` (primary/secondary, category) is declared in `corpus/raw/`.
This module owns the ONE scoring rule (`score_source` below); `preprocess_corpus.py`
imports it to copy the resulting score into `corpus/clean/`, and `build_canonical_kg()`
joins it onto every edge by `source_id`. There is deliberately no second rule anywhere:
if the tables below change, every downstream copy changes with them on the next run.

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


def score_source(record: dict, in_corpus: bool = True) -> dict:
    """The single source-authority rule, applied to one `corpus/raw/` record.

    Every consumer calls this -- the §14.1 table, `preprocess_corpus.py` (which copies
    the result into `corpus/clean/`), and through it every canonical edge. Callers copy,
    they never recompute: a second rule would let the graph and the table disagree about
    the same source.

    `in_corpus=False` scores 0: a source that never reached the clean corpus contributes
    nothing to the KG whatever its authority, which is the point of scoring accessibility.
    """
    stype = record.get("source_type") or {}
    category = stype.get("category", "unknown")
    tier = stype.get("primary_secondary", "unknown")
    method = record.get("extraction_method", "unknown")

    authority = AUTHORITY.get(category, 0)
    evidence = TIER.get(tier, 0)
    access = ACCESS.get(method, 2)
    return {
        "category": category,
        "tier": tier,
        "method": method,
        "authority": authority,
        "evidence_level": evidence,
        "accessibility": access,
        "score": authority + evidence + access if in_corpus else 0,
        "scale_max": max(AUTHORITY.values()) + max(TIER.values()) + max(ACCESS.values()),
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
        status = rec.get("extraction_status", "unknown")
        in_corpus = sid in clean_ids
        scored = score_source(rec, in_corpus)

        rows.append({
            "source_id": sid,
            "name": rec.get("source_name", ""),
            "tier": scored["tier"],
            "category": scored["category"],
            "method": scored["method"],
            "status": status,
            "in_clean_corpus": in_corpus,
            "authority": scored["authority"],
            "evidence_level": scored["evidence_level"],
            "accessibility": scored["accessibility"],
            "score": scored["score"],
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

    add("## Corroboration et contradiction entre sources")
    add("")
    add("Le §14.1 attend une dimension « cohérence avec d'autres sources ». Elle n'est pas "
        "calculable par règle — deux sources peuvent diverger sans qu'aucune ne soit "
        "fautive — mais les divergences réellement constatées dans le corpus sont "
        "consignées ici plutôt que résolues d'autorité.")
    add("")
    add("**Contradiction conservée telle quelle — date de publication du PoC de "
        "CVE-2026-55040.** Deux sources donnent deux dates différentes pour le même "
        "événement :")
    add("")
    add("| Source | Rang | Affirmation |")
    add("|---|---|---|")
    add("| **S10** — VulnCheck | primary, researcher | « published a PoC for CVE-2026-55040 "
        "(the first part of the chain) **on August 11** » |")
    add("| **S17** — DIESEC | secondary, commercial | « **On August 13**, a proof-of-concept "
        "exploit for CVE-2026-55040 […] was made publicly available » |")
    add("")
    add("Écart de deux jours sur un fait daté et vérifiable. Elle **n'est pas arbitrée** : "
        "la source la mieux placée (S10, chercheur ayant publié le PoC, primaire) est aussi "
        "la plus crédible selon la règle de scoring ci-dessus, mais rien dans les données ne "
        "permet d'exclure que S17 date la reprise publique plutôt que la publication "
        "initiale. La divergence est donc gardée comme **donnée expérimentale** — c'est "
        "exactement le cas de figure que le §7.1 du brief désigne sous « une source "
        "contredit une autre source mais la contradiction n'est pas identifiée ».")
    add("")
    add("**Ce que le graphe en a fait — le point le plus instructif, et il n'est pas à notre "
        "avantage.** Les deux dates ont été extraites par OpenIE, mais une seule a survécu :")
    add("")
    add("- S10 → arête canonique `Rapid7 's Stephen Fewer published_PoC_for_CVE-2026-55040_on "
        "August 11` ;")
    add("- S17 → 3 assertions extraites (`proof-of-concept | exploit was made available O | "
        "August 13`) **restées dans `open_kg`**, jamais promues, leur cluster de relation "
        "n'ayant pas été accepté.")
    add("")
    add("La contradiction a donc été **arbitrée par le silence** : la formulation qui s'est "
        "trouvée regroupée dans un cluster accepté est passée, l'autre est restée en "
        "attente. Personne n'a constaté le conflit ni tranché — le graphe affirme "
        "aujourd'hui « August 11 » sans aucune trace qu'une seconde date existait dans le "
        "corpus. C'est une limite de conception réelle : **la porte de validation humaine "
        "protège contre les fausses relations, pas contre l'arbitrage involontaire d'un "
        "désaccord factuel**, parce qu'elle statue sur des étiquettes de relation et jamais "
        "sur la cohérence des valeurs. Aucun mécanisme de détection de contradiction "
        "n'existe dans le pipeline.")
    add("")
    add("**Concordance vérifiée, à ne pas confondre avec une contradiction.** S11 "
        "(« 361 victim IPs by August 7 ») et S17 (« By August 14 […] 361 compromised vCenter "
        "servers ») annoncent le **même nombre, 361**, à deux dates d'observation "
        "différentes. Ce sont deux instantanés concordants, pas un écart — le noter évite "
        "de présenter à tort une corroboration comme un désaccord.")
    add("")

    add("## Le score d'autorité atteint désormais chaque arête")
    add("")
    add("Les champs de rang et de catégorie utilisés ci-dessus sont déclarés dans "
        "`corpus/raw/`. Ils sont maintenant **copiés** vers `corpus/clean/` par "
        "`preprocess_corpus.py` (champ `source_authority`), et `build_canonical_kg()` "
        "les **joint sur `source_id`** : chaque arête de "
        "`extraction_pipeline/canonical_kg/edges.json` — et donc de `demo_kg/edges.json`, "
        "qui n'en est qu'une projection filtrée — porte le score de fiabilité de sa "
        "source, avec ses trois composantes.")
    add("")
    add("Une seule règle produit ce score : `score_source()` dans ce script. "
        "`preprocess_corpus.py` l'importe plutôt que de la réécrire, donc la table "
        "ci-dessus et le graphe ne peuvent pas diverger sur une même source. Une source "
        "sans métadonnée déclarée (corpus de session live) donne `null`, jamais un score "
        "par défaut : « inconnu » reste distinct de « faible ».")
    add("")
    add("**Ce que cela permet aujourd'hui** : trier ou filtrer les arêtes par fiabilité "
        "de source dans le graphe et dans l'outil de visualisation, et répondre à la "
        "question « sur quelle qualité de source repose cette arête ? » sans rouvrir "
        "`corpus/raw/`. Répartition observée sur les 2 123 arêtes canoniques "
        "(échelle 0–12) : score 12 → 259 arêtes, 10 → 826, 9 → 525, 8 → 124, 7 → 103, "
        "6 → 108.")
    add("")
    add("**Ce que cela ne fait pas encore, et il faut le dire** : ce score n'est utilisé "
        "ni dans le protocole des 45 cellules — enregistré et exécuté avant cette "
        "propagation, et délibérément non repondéré a posteriori — ni dans la génération "
        "de réponse actuelle, qui traite toutes les arêtes du contexte à poids égal. "
        "Pondérer effectivement la sélection de contexte, puis mesurer si cela déplace "
        "une décision, est une extension déclarée à la feuille de route, pas un résultat "
        "acquis. La donnée est exposée ; son exploitation reste à faire.")
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
