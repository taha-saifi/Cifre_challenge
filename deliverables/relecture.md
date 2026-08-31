# Relecture — grille §20 et critères éliminatoires §21

*Régénérée après la mise à jour des livrables (corpus de démonstration, serveur
d'exploration, contradiction inter-sources, roadmap réécrite). Chaque ligne renvoie à une
preuve dans le dépôt, jamais à une intention. Les écarts trouvés en régénérant sont
signalés **⚠️ NOUVEL ÉCART** plutôt que corrigés en silence.*

## Critères éliminatoires (§21) — aucun ne s'applique

| Critère éliminatoire | Statut | Preuve |
|---|---|---|
| Se limite à un chatbot RAG classique | **Non** | Pipeline d'extraction + protocole d'ablation. Un RAG existe désormais, mais comme **configuration comparée**, pas comme produit. |
| Se limite à une synthèse documentaire | **Non** | 45 cellules, décisions comparées, métriques calculées. |
| Traite un domaine sans méthode généralisable | **Non** | Note §3 (tableau d'objectivation, 7 étapes) et §14 ; gabarits de tâches indépendants du domaine. |
| Ne traite pas la qualité ou la complétude | **Non** | Objet des 5 configurations et du décompte de porteurs. |
| Ne propose pas de représentation structurée | **Non** | 2 123 arêtes canoniques + vue de présentation 27 nœuds / 21 arêtes. |
| N'identifie pas de relations critiques | **Non** | `carriers.json` : profil de 1 à 12 porteurs par tâche. |
| N'analyse pas la qualité des sources | **Non** | `sources.md` : 57 sources scorées par règle, 9 familles, + section corroboration/contradiction. |
| Ne distingue pas source / extraction / relation gap | **Non** | `decisions.json` contient désormais les **trois** types : 2 source (S27, S58), 2 extraction (T3, T8), 3 relation (T1, T1b, T4). |
| Ne propose aucune métrique | **Non** | Grounding, citations, 4 indicateurs binaires, exactitude vs clé pré-enregistrée. |
| **Ne propose aucune baseline** | **Non** | Config 1 (LLM seul) exécutée sur les 9 tâches : 3/9. Un RAG documentaire s'y ajoute dans l'outil interactif. |
| Ne propose aucune logique de persistance | **Non** | Cycle `new → pending → confirmed → needs_reconfirmation` ; 944/11/2/1154. |
| **Repose sur un LLM-as-a-Judge sans contrôle** | **Non** | Aucun modèle ne note aucune réponse. `score.py` est du pattern-matching pur. La roadmap 12–24 mois propose d'**étudier** le LLM-as-a-Judge, confronté aux mesures calculées — ce n'est pas la méthode d'évaluation actuelle. |
| Ne peut pas être défendue à l'oral | **Non** | Deck 8 slides, script minuté 2 min 40, **14 réponses** préparées (9 → 14 depuis la dernière relecture). |

## Grille d'évaluation (§20, 100 points)

| Critère | Poids | Où | Solidité |
|---|---:|---|---|
| Compréhension du sujet CIFRE | 10 | Note §1–3, §13–15 | Solide — la roadmap remonte désormais explicitement vers la question de thèse au lieu de prolonger le pipeline. |
| Pertinence du domaine | 5 | Note §2 | Solide — cinq mécanismes relationnels distincts. |
| Qualité de la recherche web et sélection | 10 | Note §4, `sources.md` | Solide — 57 sources, 9 familles, lacunes déclarées. |
| Évaluation critique de la crédibilité | 10 | Note §5, `sources.md` | **Renforcé** — la section corroboration/contradiction manquait ; elle documente désormais une contradiction réelle et une concordance à ne pas confondre avec un écart. Reste moyen sur fraîcheur/stabilité, non instrumentées. |
| Structuration / mini-KG | 10 | Note §6 | Solide sur la traçabilité, **fragile sur la résolution d'entités** (§16 point 1). |
| Identification des trois types de gaps | 10 | Note §7, `decisions.json` | **Renforcé** — les lacunes de source étaient documentées dans `sources.md` mais absentes du fichier de données ; elles y sont maintenant. |
| **Qualité du protocole expérimental** | **15** | Note §9, `task_selection.md` | Solide — 32 candidates, règle écrite, ablation calculée, clé pré-enregistrée, aucun retry. |
| Métriques, baselines, analyse | 10 | Note §10–11 | Solide — pas de juge LLM, réserves énoncées, dont l'effet de cadrage découvert. |
| Persistance et amélioration continue | 10 | Note §12 | Solide en conception, **jamais exercé** — dit explicitement. |
| Généralisation | 5 | Note §14 | **Moyen, mais mieux articulé** — toujours argumentée et non démontrée ; §14 dit désormais *pourquoi* elle devrait transférer et §15 *quand on le vérifiera*. |
| Clarté, esprit critique, défense orale | 5 | Deck, démonstrateur, script, questions | Solide — la démonstration s'ouvre sur un échec corrigé. |

## Distinctions du §20 explicitement traitées

| Distinction attendue | Où |
|---|---|
| Domaine d'application vs méthode généralisable | Note §3, §14 |
| Source fiable vs source fragile | `sources.md` ; `questions_23.md` Q12 |
| Information brute vs connaissance structurée | Note §6 (4 401 → 2 123) |
| Connaissance validée vs incertaine | Note §12 (944 acceptés / 1 154 en attente) |
| Connaissance extraite vs persistée | Note §12, phrase d'ancrage |
| **Absence de preuve vs preuve d'absence** | Note §5 (cas S58 triangulé par le NVD) |
| Erreur de source vs de retrieval | Note §7, arbre de décision |
| Erreur de graphe vs de raisonnement | Note §11 (config 1 vs configs KG-aware) |
| Réponse correcte vs recommandation fiable | Note §11 (16 vs 556 jetons vérifiables) |
| Contribution scientifique vs implémentation | Note §13 vs §6 |

## Contrôles de format — désormais **mesurés**, plus estimés

- [x] **Note : 4 pages pour le corps**, 5 au total AI Log inclus. **Mesuré par Word**
      (`experiments/build_docx.py`, COM `ComputeStatistics`), pas extrapolé d'un nombre de
      mots. Le §18.1 excluant l'AI Log du décompte, la contrainte est respectée.
- [x] **AI Usage Log ≤ ½ page** — 317 mots sur une page qui en porte ~680, soit ≈ 0,47 page.
- [x] **Deck : 8 slides**, `deliverables/deck.pptx`. Les blocs « À dire » passent en notes
      d'orateur, pas sur la planche.
- [x] Données synthétiques signalées **dans le contexte transmis au modèle**
      (`[Scenario experimental, non issu du corpus]`, 2 contextes sur 45), et non seulement
      dans la note.
- [x] Chiffres régénérables : `resultats.md` et `sources.md` sont produits par script.
- [x] Non-régression du protocole : `build_contexts.py --verify` passe 10/10.

## ⚠️ Nouveaux écarts trouvés en régénérant

1. **Une affirmation fausse a été écrite puis corrigée pendant cette passe.** Une première
   version de `sources.md` affirmait qu'« aucune arête canonique ne porte la date du PoC ».
   Vérification faite, c'est faux : l'arête
   `Rapid7 's Stephen Fewer published_PoC_for_CVE-2026-55040_on August 11` existe bel et
   bien. Le texte a été corrigé, et le constat réel est plus fort : les deux dates ont été
   extraites, une seule a été promue, **la contradiction a été arbitrée par le silence**.
2. **La couverture des lacunes de source était incohérente entre fichiers.** Elles étaient
   décrites dans `sources.md` mais absentes de `gap_classification`. Corrigé — un lecteur
   qui ouvrait le fichier de données aurait conclu que le type n'était pas traité.
3. **Le vocabulaire de relations du brief ne correspond pas au graphe.** `affects`,
   `chains_with`, `confirmed_exploited_by` n'existent pas ; les étiquettes réelles sont par
   exemple `has patch` (11) et `be chained to` (2), sur 946 étiquettes distinctes. Ces noms
   n'apparaissaient dans aucun livrable — ils venaient de la checklist de vérification, pas
   de la note. **Aucune correction n'était nécessaire dans `deliverables/`**, et il faut
   éviter de les employer à l'oral.
4. **La « couche synthétique » n'est pas une couche du graphe.** Le KG n'a ni type `Asset`
   ni prédicat d'exposition. Formulation corrigée en note §16 et deck slide 8 : c'est une
   phrase de contexte marquée, pas une seconde couche.
5. **Point qui reste ouvert et n'est pas de notre ressort** : le pitch de 20 minutes n'a
   pas été répété. Aucune preuve possible dans le dépôt.

## Points faibles à assumer à l'oral plutôt qu'à défendre

1. **La résolution d'entités ne fusionne presque rien** (2 fusions sur 3 699). Si le jury
   attaque la qualité du graphe, c'est par là — c'est mesuré, dit en §16, et c'est le
   premier chantier des 0–6 mois.
2. **1 154 clusters non revus.** Réponse : le KG canonique ne contient que ce qu'un humain
   a validé — la portion non revue est *exclue*, pas incluse à tort.
3. **Généralisation non démontrée.** §14 le dit et §15 dit quand ce sera levé.
4. **Précision de 0,026** — l'énoncer avant que le jury ne la trouve : artefact d'annotation
   éparse, seul le rappel est interprétable.
5. **L'effet de cadrage entre configurations 5 et 8** (décisions opposées à une phrase
   près) : preuve que le modèle lit le contexte, mais aussi variable jamais mesurée comme
   telle. Observation de l'outil de démonstration, pas résultat du protocole.
