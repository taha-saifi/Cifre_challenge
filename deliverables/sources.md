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

## Limite structurelle : la crédibilité n'atteint pas le graphe

Les champs de rang et de catégorie utilisés ci-dessus vivent dans `corpus/raw/`. `preprocess_corpus.py` ne les propage pas vers `corpus/clean/`, qui est pourtant le seul répertoire lu par le pipeline d'extraction. **Conséquence : une affirmation issue d'un billet commercial et une affirmation issue du NVD entrent dans le KG avec exactement le même poids.** Aucune pondération par fiabilité n'existe aujourd'hui. C'est une extension naturelle de la méthode, et l'une des premières à mener.

