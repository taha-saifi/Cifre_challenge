# Qualité des sources (§14.1)

*Document généré par `experiments/build_source_quality.py`. Les scores sont dérivés de métadonnées déclarées à la collecte, par une règle unique appliquée à toutes les sources — pas par une appréciation source par source. On peut contester la règle ; on n'a pas à contester 57 jugements individuels.*

## Règle de scoring

| Dimension | Règle | Échelle |
|---|---|---|
| Autorité | catégorie déclarée de l'émetteur | official 5 · framework 4 · éditeur 4 · chercheur 3 · presse 2 · commercial 1 |
| Niveau de preuve | source de première main ou rapport de seconde main | primary 2 · secondary 1 |
| Accessibilité | méthode ayant permis la collecte | API 5 · HTML direct 4 · navigateur requis 3 · PDF 3 · non tentée 0 |

**Deux dimensions du §14.1 ne sont pas instrumentées, et il faut le dire plutôt que de les simuler : la *fraîcheur* et la *stabilité dans le temps*.** Le seul champ temporel disponible est `date_accessed`, un horodatage de collecte (toutes les sources le 2026-08-28), pas une date de publication. Les scorer reviendrait à inventer une mesure.

## Sources principales et corpus de corroboration

Le brief (§9) recommande 5 à 10 sources principales ; le corpus compte 57 fichiers déclarés. L'écart tient à une différence d'unité : ces fichiers se ramènent à **9 familles de sources principales**, interrogées plusieurs fois. Le NVD n'est pas cinq sources parce qu'on l'a consulté pour cinq CVE : c'est un système de référence, requêté cinq fois.

**9 familles principales couvrent 32 fichiers** et portent les faits décisionnels ; les 25 fichiers restants corroborent, datent, ou fournissent le cadre normatif (spécifications CVSS, SSVC, ATT&CK). La base probante est étroite, le corpus est large — et c'est cette distinction, pas le volume, qui répond au §9.

### Familles principales

| Famille | Fichiers | Rang | Catégorie | Score | Sources |
|---|---:|---|---|---:|---|
| **NVD (NIST)** | 5 | primary | official | 12 | S02, S03, S04, S05, S06 |
| **FIRST EPSS** | 7 | primary | official | 12 | S21, S22, S23, S24, S25, S47, S48 |
| **CISA KEV** | 6 | primary | official | 11 | S01, S29, S30, S31, S32, S58 |
| **CISA BOD 26-04** | 1 | primary | official | 11 | S19 |
| **Apple** | 3 | primary | publisher | 10 | S15, S55, S56 |
| **Broadcom** | 2 | primary | publisher | 10 | S27, S43 *(dont S27 inaccessible)* |
| **Microsoft MSRC** | 3 | primary | publisher | 9 | S07, S39, S42 |
| **Rapid7** | 4 | primary | researcher | 9 | S08, S09, S40, S41 |
| **VulnCheck** | 1 | primary | researcher | 9 | S10 |

## Distribution du corpus complet

- **Catégorie** : official 24 · official_framework 11 · publisher 8 · researcher 8 · journalistic 4 · commercial 2
- **Rang** : primary 48 · secondary 9
- **Méthode de collecte** : html_trafilatura 35 · api_json 10 · playwright+html_trafilatura 10 · not_attempted 1 · pdf_pdfplumber 1

## Lacunes de source documentées (§7.1)

Deux sources n'ont pas produit de contenu exploitable. Elles sont **enregistrées comme telles, jamais remplacées par du contenu plausible** — c'est la règle qui a gouverné toute la collecte.

- **S27 — Broadcom VMSA-2026-0006** · statut `failed` · Accès non disponible : source volontairement non tentée (login Broadcom requis).
- **S58 — CISA KEV catalog entry: CVE-2026-63520** · statut `partial_suspect` · Échec requests (page KEV filtrée sans données par-CVE (Due Date/Required Action/Date Added absents)) ; échec Playwright (page KEV filtrée sans données par-CVE (Due Date/Required Action/Date Added absents)).

Le cas S58 mérite d'être défendu explicitement : la page KEV de CVE-2026-63520 a répondu 200 mais sans données par-CVE, si bien que le graphe ne contient aucune échéance CISA pour cette vulnérabilité. On pourrait y voir une lacune de collecte qui fausserait la tâche T5. Ce n'est pas le cas : l'enregistrement NVD de cette même CVE (S06) ne contient **aucun** champ `cisa*`, alors que S02–S05 en contiennent quatre chacun. Deux sources indépendantes concordent — CVE-2026-63520 n'est pas au catalogue KEV. C'est une **preuve d'absence**, pas une **absence de preuve**.

## Corroboration et contradiction entre sources

Le §14.1 attend une dimension « cohérence avec d'autres sources ». Elle n'est pas calculable par règle — deux sources peuvent diverger sans qu'aucune ne soit fautive — mais les divergences réellement constatées dans le corpus sont consignées ici plutôt que résolues d'autorité.

**Contradiction conservée telle quelle — date de publication du PoC de CVE-2026-55040.** Deux sources donnent deux dates différentes pour le même événement :

| Source | Rang | Affirmation |
|---|---|---|
| **S10** — VulnCheck | primary, researcher | « published a PoC for CVE-2026-55040 (the first part of the chain) **on August 11** » |
| **S17** — DIESEC | secondary, commercial | « **On August 13**, a proof-of-concept exploit for CVE-2026-55040 […] was made publicly available » |

Écart de deux jours sur un fait daté et vérifiable. Elle **n'est pas arbitrée** : la source la mieux placée (S10, chercheur ayant publié le PoC, primaire) est aussi la plus crédible selon la règle de scoring ci-dessus, mais rien dans les données ne permet d'exclure que S17 date la reprise publique plutôt que la publication initiale. La divergence est donc gardée comme **donnée expérimentale** — c'est exactement le cas de figure que le §7.1 du brief désigne sous « une source contredit une autre source mais la contradiction n'est pas identifiée ».

**Ce que le graphe en a fait — le point le plus instructif, et il n'est pas à notre avantage.** Les deux dates ont été extraites par OpenIE, mais une seule a survécu :

- S10 → arête canonique `Rapid7 's Stephen Fewer published_PoC_for_CVE-2026-55040_on August 11` ;
- S17 → 3 assertions extraites (`proof-of-concept | exploit was made available O | August 13`) **restées dans `open_kg`**, jamais promues, leur cluster de relation n'ayant pas été accepté.

La contradiction a donc été **arbitrée par le silence** : la formulation qui s'est trouvée regroupée dans un cluster accepté est passée, l'autre est restée en attente. Personne n'a constaté le conflit ni tranché — le graphe affirme aujourd'hui « August 11 » sans aucune trace qu'une seconde date existait dans le corpus. C'est une limite de conception réelle : **la porte de validation humaine protège contre les fausses relations, pas contre l'arbitrage involontaire d'un désaccord factuel**, parce qu'elle statue sur des étiquettes de relation et jamais sur la cohérence des valeurs. Aucun mécanisme de détection de contradiction n'existe dans le pipeline.

**Concordance vérifiée, à ne pas confondre avec une contradiction.** S11 (« 361 victim IPs by August 7 ») et S17 (« By August 14 […] 361 compromised vCenter servers ») annoncent le **même nombre, 361**, à deux dates d'observation différentes. Ce sont deux instantanés concordants, pas un écart — le noter évite de présenter à tort une corroboration comme un désaccord.

## Le score d'autorité atteint désormais chaque arête

Les champs de rang et de catégorie utilisés ci-dessus sont déclarés dans `corpus/raw/`. Ils sont maintenant **copiés** vers `corpus/clean/` par `preprocess_corpus.py` (champ `source_authority`), et `build_canonical_kg()` les **joint sur `source_id`** : chaque arête de `extraction_pipeline/canonical_kg/edges.json` — et donc de `demo_kg/edges.json`, qui n'en est qu'une projection filtrée — porte le score de fiabilité de sa source, avec ses trois composantes.

Une seule règle produit ce score : `score_source()` dans ce script. `preprocess_corpus.py` l'importe plutôt que de la réécrire, donc la table ci-dessus et le graphe ne peuvent pas diverger sur une même source. Une source sans métadonnée déclarée (corpus de session live) donne `null`, jamais un score par défaut : « inconnu » reste distinct de « faible ».

**Ce que cela permet aujourd'hui** : trier ou filtrer les arêtes par fiabilité de source dans le graphe et dans l'outil de visualisation, et répondre à la question « sur quelle qualité de source repose cette arête ? » sans rouvrir `corpus/raw/`. Répartition observée sur les 2 123 arêtes canoniques (échelle 0–12) : score 12 → 259 arêtes, 10 → 826, 9 → 525, 8 → 124, 7 → 103, 6 → 108.

**Ce que cela ne fait pas encore, et il faut le dire** : ce score n'est utilisé ni dans le protocole des 45 cellules — enregistré et exécuté avant cette propagation, et délibérément non repondéré a posteriori — ni dans la génération de réponse actuelle, qui traite toutes les arêtes du contexte à poids égal. Pondérer effectivement la sélection de contexte, puis mesurer si cela déplace une décision, est une extension déclarée à la feuille de route, pas un résultat acquis. La donnée est exposée ; son exploitation reste à faire.

