# Relecture — grille §20 et critères éliminatoires §21

*Vérification point par point avant soumission. Chaque ligne renvoie à une preuve dans le
dépôt, jamais à une intention.*

## Critères éliminatoires (§21) — aucun ne s'applique

| Critère éliminatoire | Statut | Preuve |
|---|---|---|
| Se limite à un chatbot RAG classique | **Non** | Aucun RAG : pipeline d'extraction + protocole d'ablation. Aucun composant de retrieval sémantique. |
| Se limite à une synthèse documentaire | **Non** | 45 cellules expérimentales, décisions comparées, métriques calculées. |
| Traite un domaine sans méthode généralisable | **Non** | Note §3 (tableau d'objectivation) et §14 ; gabarits de tâches indépendants du domaine. |
| Ne traite pas la qualité ou la complétude | **Non** | C'est l'objet même : ablation, décompte de porteurs, 5 configurations. |
| Ne propose pas de représentation structurée | **Non** | 2 123 arêtes canoniques + vue de présentation 27 nœuds / 21 arêtes. |
| N'identifie pas de relations critiques | **Non** | Note §8 ; `carriers.json` donne le profil de porteurs par tâche. |
| N'analyse pas la qualité des sources | **Non** | `sources.md` : 57 sources scorées par règle, 9 familles principales. |
| Ne distingue pas source / extraction / relation gap | **Non** | Note §7 : arbre de décision mécanique, un exemple tracé par type. |
| Ne propose aucune métrique | **Non** | Note §10 : grounding, citations, 4 indicateurs binaires, exactitude vs clé. |
| **Ne propose aucune baseline** | **Non** | Configuration 1 (LLM seul) exécutée sur les 9 tâches : 3/9. |
| Ne propose aucune logique de persistance | **Non** | Note §12 : cycle `new → pending → confirmed → needs_reconfirmation`. |
| **Repose sur un LLM-as-a-Judge sans contrôle** | **Non** | Aucun modèle ne note aucune réponse. Grounding et citations calculés par correspondance de chaînes ; exactitude contre clé pré-enregistrée. |
| Ne peut pas être défendue à l'oral | **Non** | Deck 8 slides + script de démo minuté + réponses §23 préparées. |

## Grille d'évaluation (§20, 100 points)

| Critère | Poids | Où c'est traité | Solidité |
|---|---:|---|---|
| Compréhension du sujet CIFRE | 10 | Note §1–3, §13–15 | Solide — la question « un KG complet garantit-il une réponse correcte ? » est traitée expérimentalement, pas rhétoriquement. |
| Pertinence du domaine | 5 | Note §2 | Solide — cinq mécanismes relationnels distincts, aucun réductible à de la synthèse. |
| Qualité de la recherche web et sélection | 10 | Note §4, `sources.md` | Solide — 57 sources, 9 familles, aucune inventée, lacunes déclarées. |
| Évaluation critique de la crédibilité | 10 | Note §5, `sources.md` | **Moyen** — scoring par règle, mais deux dimensions non instrumentées (fraîcheur, stabilité), et la crédibilité n'est pas propagée au graphe. Assumé en §16. |
| Structuration / mini-KG | 10 | Note §6 | Solide sur la traçabilité, **fragile sur la résolution d'entités** (§16 point 1). |
| Identification des trois types de gaps | 10 | Note §7 | Solide — typologie rendue mécaniquement décidable, un exemple réel par type. |
| **Qualité du protocole expérimental** | **15** | Note §9, `task_selection.md` | Solide — 32 candidates, règle de sélection écrite, ablation calculée, clé pré-enregistrée, aucun retry. |
| Métriques, baselines, analyse | 10 | Note §10–11 | Solide — pas de juge LLM, réserves énoncées. |
| Persistance et amélioration continue | 10 | Note §12 | Solide en conception, **jamais exercé** — dit explicitement. |
| Généralisation | 5 | Note §14 | **Moyen** — argumentée, non démontrée. Assumé. |
| Clarté, esprit critique, défense orale | 5 | Deck, démonstrateur, script | Solide — la démonstration s'ouvre sur un échec corrigé. |

## Distinctions du §20 explicitement traitées

| Distinction attendue | Où |
|---|---|
| Domaine d'application vs méthode généralisable | Note §3, §14 |
| Source fiable vs source fragile | `sources.md`, scoring par autorité |
| Information brute vs connaissance structurée | Note §6 (assertions → arêtes canoniques) |
| Connaissance validée vs incertaine | Note §12 (944 acceptés / 1 154 en attente) |
| Connaissance extraite vs persistée | Note §12, phrase d'ancrage |
| **Absence de preuve vs preuve d'absence** | Note §5 (cas S58 triangulé par le NVD) |
| Erreur de source vs de retrieval | Note §7, arbre de décision |
| Erreur de graphe vs de raisonnement | Note §11 (config 1 vs configs KG-aware) |
| Réponse correcte vs recommandation fiable | Note §11 (16 vs 556 jetons vérifiables) |
| Contribution scientifique vs implémentation | Note §13 (décompte de porteurs) vs §6 (pipeline) |

## Contrôles de contenu

- [x] **Données synthétiques signalées** — la couche actif/exposition est marquée
      `[Scénario expérimental, non issu du corpus]` **dans le contexte transmis au
      modèle**, pas seulement dans la note. Rappelée en §16 point 8.
- [x] **Chiffres régénérables** — `resultats.md` et `sources.md` sont produits par script
      depuis les données ; aucun chiffre saisi à la main.
- [x] **Provenance** — chaque arête conserve `source_id` + texte-preuve ; le
      démonstrateur affiche les identifiants de source.
- [x] **Aucune affirmation non vérifiée** sur les CVE : tout provient du corpus ou des
      champs structurés.
- [x] **Non-régression du protocole** — `build_contexts.py --verify` reproduit les 10
      contextes d'origine à l'octet près après tous les travaux de rédaction.

## Points faibles à assumer à l'oral plutôt qu'à défendre

1. **La résolution d'entités ne fusionne presque rien** (2 fusions sur 3 699). Si le jury
   attaque la qualité du graphe, c'est par là. Réponse : c'est mesuré, dit en §16 point 1,
   et c'est le premier chantier de la roadmap 0–6 mois.
2. **1 154 groupes de relations non revus.** Réponse : le KG canonique ne contient que ce
   qu'un humain a validé — la portion non revue est *exclue*, pas incluse à tort.
3. **Généralisation non démontrée.** Réponse : dit en §14 et §16 ; c'est le premier
   livrable des 6–12 mois.
4. **Précision de 0,026 sur le jeu d'évaluation.** À énoncer **avant** que le jury ne la
   trouve : c'est un artefact d'annotation éparse, et c'est précisément l'exemple de
   métrique qui donnerait un faux sentiment de fiabilité.
