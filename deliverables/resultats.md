# Résultats du protocole expérimental (§13)

*Document généré par `experiments/build_report.py` depuis `carriers.json`, `scores.json` et `decisions.json`. Ne pas éditer à la main : toute correction se fait dans les données puis par régénération.*

**9 tâches × 5 configurations = 45 cellules.** Un seul appel par cellule, aucun retry, chaque cellule exécutée par un agent isolé ne connaissant ni le protocole ni les autres cellules. Le prompt de décision est identique dans les cinq configurations d'une même tâche ; seul le contexte varie.

## 1. Tableau des décisions

| Tâche | 1 — LLM seul | 4 — KG complet | 5 — KG incomplet | 7 — KG pré-validation | 8 — KG incomplet + signalement |
|---|---|---|---|---|---|
| **T1** | CVE-2026-63520 | CVE-2026-55040 | CVE-2026-55040 | CVE-2026-55040 | CVE-2026-55040 |
| **T1b** | refus de trancher | CVE-2026-55040 | CVE-2026-55040 | CVE-2026-55040 | CVE-2026-55040 |
| **T2** | indécis, urgent par défaut | urgent | urgent | urgent | urgent |
| **T3** | ne peut pas affirmer | aucun workaround documenté | aucun workaround documenté | aucun workaround documenté | aucun workaround documenté |
| **T4** | ne peut pas conclure | oui, exploitation active | oui, exploitation active | oui, exploitation active | oui, exploitation active |
| **T5** | ne peut pas conclure | 4 hors délai, 63520 exclue | 4 hors délai, 63520 exclue | 4 hors délai, 63520 exclue | 4 hors délai, 63520 exclue |
| **T6** | refus de classer | 33824 > 59310 > 55040 > 65400 > 63520 | 55040 > 59310 > 33824 > 65400 > 63520 | 55040 > 33824 > 59310 > 65400 > 63520 | 55040 > 59310 > 33824 > 65400 > 63520 |
| **T7** | reporter au cycle standard | corriger en urgence | corriger en urgence | corriger en urgence | corriger en urgence |
| **T8** | ne peut pas conclure | oui, KB5002893/94/96/905/906 | remédiation existe, référence indisponible | existe probablement, référence indisponible | non déterminable |

## 2. Effet de l'ablation : la décision change-t-elle par rapport à la config 4 ?

| Tâche | Porteurs du fait ablaté | Ablation complète ? | c5 ≠ c4 | c8 ≠ c4 |
|---|---:|---|---|---|
| T1 | 12 | **non** | non | non |
| T1b | 12 | oui | non | non |
| T2 | n/a | s.o. | non | non |
| T3 | 1 | oui | non | non |
| T4 | 1 | oui | non | non |
| T5 | 4 | oui | non | non |
| T6 | 10 | oui | **OUI** | **OUI** |
| T7 | 2 | oui | non | non |
| T8 | 5 | oui | **OUI** | **OUI** |

Sur 9 tâches, **2** voient leur décision changer entre la config 4 et la config 5.

## 3. Grounding et citations (calculés, sans juge LLM)

`grounding` = part des jetons littéralement vérifiables de la réponse (identifiants CVE, références KB, identifiants de source, dates ISO, scores CVSS) que l'on retrouve dans le contexte exact fourni à cette cellule. La comparaison est faite par correspondance de chaînes, jamais par appréciation.

| Tâche | c1 | c4 | c5 | c7 | c8 |
|---|---|---|---|---|---|
| **T1** | 1/1 | 7/7 | 6/7 | 6/6 | 7/7 |
| **T1b** | 2/4 | 23/23 | 24/24 | 15/15 | 18/18 |
| **T2** | 1/1 | 4/5 | 4/4 | 3/3 | 7/8 |
| **T3** | 1/1 | 5/5 | 4/4 | 11/11 | 6/6 |
| **T4** | 1/1 | 14/14 | 11/11 | 12/12 | 13/13 |
| **T5** | 1/1 | 35/35 | 36/36 | 26/26 | 37/37 |
| **T6** | 0/4 | 37/38 | 25/26 | 16/16 | 35/35 |
| **T7** | 1/2 | 17/17 | 18/18 | 9/9 | 18/18 |
| **T8** | 1/1 | 13/13 | 9/9 | 13/13 | 7/7 |

Agrégé : config 1 (LLM seul) **9/16** jetons ancrés ; configs KG-aware **551/556**.

Le ratio de la config 1 est trompeur pris seul : les rares jetons qu'elle ancre sont surtout l'identifiant CVE recopié depuis la question. Le signal réel est le **volume** de faits vérifiables produits — 16 jetons sur 9 tâches en config 1 contre 556 pour les configurations KG-aware, soit un facteur 35×. Sans graphe, le modèle ne se trompe pas beaucoup : il n'avance presque rien de vérifiable.

Deux réserves sur cette métrique, à énoncer plutôt qu'à masquer. D'abord elle compte des nombres employés rhétoriquement : le « 7.0 » de T7-c1 est un seuil dans une phrase conditionnelle, pas une affirmation sur la CVE. Ensuite la config 1 n'est pas un isolement parfait — en T6-c1 le modèle cite les identifiants de source S02–S06 et S21–S25 sans avoir lu le corpus, ce que seul son environnement d'exécution peut lui avoir fourni. La baseline « LLM seul » est donc légèrement optimiste.

## 4. Indicateurs observables (§14.3)

Comptés, pas notés : *décision explicite formulée*, *incertitude nommée*, *information complémentaire demandée*, *niveau de confiance énoncé*.

| Config | Décision explicite | Incertitude nommée | Info demandée | Confiance énoncée |
|---|---:|---:|---:|---:|
| 1 — LLM seul | 9/9 | 6/9 | 5/9 | 7/9 |
| 4 — KG complet | 9/9 | 3/9 | 1/9 | 6/9 |
| 5 — KG incomplet | 9/9 | 5/9 | 2/9 | 7/9 |
| 7 — KG pré-validation | 9/9 | 4/9 | 1/9 | 8/9 |
| 8 — KG incomplet + signalement | 8/9 | 8/9 | 1/9 | 8/9 |

## 4b. Exactitude par configuration (contre la clé pré-enregistrée)

La clé a été écrite et gelée avant l'exécution de toute cellule. Pour les tâches dont le fait testé est ablaté (T4, T8), la réponse attendue en configuration 5 et 8 est un constat explicite d'impossibilité de conclure, pas la réponse positive.

| Configuration | Exactitude | Incertitude nommée |
|---|---:|---:|
| 1 — LLM seul | 3/9 | 6/9 |
| 4 — KG complet | 9/9 | 3/9 |
| 5 — KG incomplet | 7/9 | 5/9 |
| 7 — KG pré-validation | 8/9 | 4/9 |
| 8 — KG incomplet + signalement | 7/9 | 8/9 |

## 5. Classification des écarts (§7)

Brief §7: source gap / extraction gap / relation gap. Assigned by the mechanical decision tree: is the fact in corpus/clean? if not -> source gap. Is it in openie_assertions / open_kg? if not -> extraction gap. Is it in canonical_kg under a usable label? if not -> relation gap.

- **T1 — relation gap.** The chaining fact IS in canonical_kg, under 3 Tier-1 labels plus 9 Tier-2 carriers (carriers.json). The Day-2 ablation removed 2 of 3 Tier-1 carriers, so the gap it created was never the gap it intended: label duplication, not absence.
- **T1b — relation gap.** All 3 Tier-1 carriers removed and the decision still did not move, because 9 Tier-2 carriers remain -- notably 'Patching CVE-2026-55040 break exploit chain' (S40), cited verbatim by the c5 answer.
- **T3 — extraction gap.** S17 states 'Broadcom released patches for CVE-2026-59310 ... on July 29, 2026' (source_verification_report.md), yet the vCenter subgraph has no has_patch edge at all. The fact is in the corpus and absent from the graph.
- **T4 — relation gap.** Ablating has_SSVC_exploitation did not change the answer: has_CISA_exploit_addition_date independently implies active exploitation. Two structured fields encode one decision-relevant fact under unrelated labels.
- **T6 — no gap -- control.** The EPSS signal has 10 carriers but all of one functional kind; removing them all does change the ranking. This is the positive control showing the protocol can detect an effect when one exists.
- **T8 — extraction gap (partially repaired).** The KB list is present in S41's text and was fragmented at extraction (cluster_dedup_final.md), then recovered via the 'has patch' split decision. Ablating the 5 recovered edges degrades the answer to 'reference unavailable' -- a clean single-purpose carrier set.

