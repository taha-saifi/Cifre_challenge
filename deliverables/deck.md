# Pitch deck — 8 slides

*Structure imposée par le §18.2. Durée : 20 minutes. Chaque slide porte un titre-message,
pas un titre-catégorie — le titre dit la conclusion, le corps l'étaye.*

---

## Slide 1 — Mission choisie et problème traité

### Titre
**« Nous ne pouvons patcher qu'une chose cette semaine. Laquelle ? »**

### Corps
- Priorisation de correctifs de sécurité — 5 CVE au catalogue CISA KEV, août 2026.
- Deux failles SharePoint chaînables, une faille IKE Windows, une vCenter, une macOS.
- Décider suppose une **relation** (le chaînage), une **condition** (l'exposition), une
  **échéance** (l'obligation CISA), une **contradiction** (CVSS 8,1 mais EPSS 0,029), et
  une **absence** (aucun contournement documenté pour vCenter).
- Aucune de ces cinq choses ne se lit dans un document isolé.

### À dire
Le domaine est un terrain, pas le sujet. Le sujet, c'est ce qui arrive à une
recommandation quand le graphe qui la nourrit est incomplet.

---

## Slide 2 — Corpus web et qualité des sources

### Titre
**9 familles de sources portent la décision ; 48 autres fichiers corroborent**

### Corps
- 57 sources déclarées, 56 exploitables → **9 familles principales** : NVD, FIRST EPSS,
  CISA KEV, CISA BOD 26-04, MSRC, Rapid7, VulnCheck, Apple, Broadcom.
- Scoring par règle unique : autorité, niveau de preuve, accessibilité.
- **Deux dimensions non instrumentées et déclarées comme telles** : fraîcheur et
  stabilité — le seul champ temporel est un horodatage de collecte.
- **Deux lacunes de source documentées** : S27 (login éditeur requis, délibérément non
  tentée), S58 (page KEV sans données par-CVE).
- **Une contradiction inter-sources conservée** : date du PoC de CVE-2026-55040, 11 août
  (S10, VulnCheck) contre 13 août (S17, DIESEC) — non arbitrée.

### À dire
La règle tenue de bout en bout : rien n'est inventé, rien n'est remplacé. Une source
inaccessible est enregistrée comme inaccessible. Et sur la contradiction : les deux dates
ont été extraites, une seule a survécu à la validation — le graphe affirme « 11 août » sans
trace qu'une autre date existait. La porte humaine statue sur des étiquettes de relation,
jamais sur la cohérence des valeurs. C'est une limite découverte, pas un choix.

---

## Slide 3 — Représentation de connaissance / mini-KG

### Titre
**Un graphe sans schéma présupposé : les relations sont découvertes, pas décrétées**

### Corps
- Pipeline **non-LLM**, auditable : OpenIE (MinIE) sur le texte libre + mappage
  déterministe des champs structurés (NVD, EPSS).
- 56 sources → 4 401 arêtes ouvertes → **2 123 arêtes canoniques** sur 1 867 nœuds.
- Chaque assertion conserve `source_id` + le texte exact qui la justifie.
- **Aucune arête ne devient canonique sans validation humaine.**
- Vue de présentation projetée par règle : **27 nœuds / 21 arêtes**, provenance conservée.

### Visuel
La vue de présentation (les 5 CVE, leurs correctifs, faiblesses, éditeurs, et l'arête de
chaînage), avec en encart le rapport d'échelle au graphe complet.

---

## Slide 4 — Relations critiques et knowledge gaps

### Titre
**Une relation est critique quand elle est le seul porteur du fait — c'est un nombre, pas une intuition**

### Corps
- Typologie §7 rendue **mécaniquement décidable** : le fait est-il dans le corpus ? dans
  les extractions ? dans le graphe sous une étiquette exploitable ? → lacune de source /
  d'extraction / de relation.
- Notion de **porteur** : arête dont le texte-preuve porte le fait visé.
- Profil mesuré : de **1 porteur** (statut d'exploitation macOS) à **12** (chaînage
  SharePoint).
- Exemple de lacune d'extraction réelle : S17 énonce que Broadcom a publié des correctifs
  pour vCenter ; le sous-graphe n'en contient **aucune** trace.

### À dire
C'est la contribution centrale, et elle est née d'un échec — slide 6.

---

## Slide 5 — Protocole expérimental

### Titre
**9 tâches × 5 configurations = 45 cellules, et aucune étape laissée au jugement**

### Corps
- Configurations §13 : LLM seul · KG complet · KG incomplet · KG avant validation ·
  KG incomplet + signalement.
- Un appel par cellule, **aucun retry**, agent isolé ignorant le protocole. Prompt
  identique dans les 5 configurations ; **seul le contexte varie**.
- 32 tâches candidates énumérées, 9 retenues par règle écrite, 23 écartées avec motif.
- **Les cibles d'ablation sont calculées**, pas choisies : l'ablation est l'ensemble
  complet des porteurs.
- Clé de décision **pré-enregistrée** avant toute exécution.

### À dire
Le tableau d'objectivation — une ligne par étape où un jugement aurait pu s'introduire,
et le mécanisme qui l'a remplacé.

---

## Slide 6 — Métriques, baselines et premiers résultats

### Titre
**Le graphe ne rend pas le modèle moins faux : il le rend vérifiable**

### Corps
| Configuration | Exactitude | Incertitude nommée |
|---|---:|---:|
| LLM seul | 3/9 | 6/9 |
| KG complet | **9/9** | 3/9 |
| KG incomplet | 7/9 | 5/9 |
| KG avant validation | 8/9 | 4/9 |
| KG incomplet + signalement | 7/9 | **8/9** |

- **16 jetons vérifiables sans graphe, 556 avec** — facteur 35.
- Grounding et citations **calculés par correspondance de chaînes**. Aucun modèle ne note
  aucune réponse (§21 : le LLM-as-a-Judge sans contrôle est éliminatoire).
- Signalement : à information égale, l'incertitude passe de 5 à 8 réponses sur 9 **sans
  perte d'exactitude**.

### À dire
Le LLM seul ne se trompe pas beaucoup : il n'avance presque rien de contrôlable. Sur
l'arbitrage SharePoint il choisit la mauvaise CVE, au motif que le numéro le plus élevé
serait le plus récent.

---

## Slide 7 — Composant produit et généralisation

### Titre
**Un détecteur de redondance relationnelle — construit, appliqué, et qui a corrigé notre propre conclusion**

### Corps
- Pour un fait : combien d'arêtes le portent, sous quelles étiquettes, que resterait-il
  si on retirait la principale ?
- **Avant génération** : un fait à porteur unique est un point de fragilité.
- **Avant expérimentation** : toute évaluation par ablation sur un graphe d'extraction
  ouverte est ininterprétable sans ce décompte.
- Généralisation par construction — aucun schéma présupposé, le décompte ne dépend que
  d'un couple d'entités et d'un texte-preuve :
  santé (contre-indication) · droit (règle/exception) · finance (méthode de calcul datée)
  · éducation (prérequis).

### À dire honnêtement
La généralisation est **argumentée, pas démontrée** : aucun second domaine n'a été traité
dans le temps imparti. C'est la première validation de la roadmap.

---

## Slide 8 — Roadmap CIFRE, risques et limites

### Titre
**De la mesure d'un cas à une méthode d'évaluation de la complétude**

### Corps
- **0–6 mois** — généraliser le décompte de porteurs en **métrique de complétude
  indépendante du domaine** ; formaliser l'ablation comme méthode reproductible.
- **6–12 mois** — **second domaine, idéalement un cas SpotworkAI** ; benchmark
  RAG / GraphRAG / KG-aware ; première publication méthodologique.
- **12–24 mois** — du **rétrospectif au prédictif** : repérer les faits fragiles avant
  génération ; confrontation à GraphRAG, à la complétion de graphe, et au LLM-as-a-Judge.
- **24–36 mois** — validation sur cas et bases réels SpotworkAI ; composant intégré à la
  plateforme ; thèse.
- **Limites** — résolution d'entités quasi inopérante (3 699 → 3 697) · 1 154 clusters
  non revus sur 2 111 · précision 0,026 du gold set, artefact d'annotation éparse ·
  crédibilité des sources non propagée au graphe · aucune couche actif/exposition dans le
  graphe · une contradiction inter-sources arbitrée par le silence.
- **Outil de démonstration** — même template de prompt que les 45 cellules, **transport et
  modèle différents** (API OpenRouter, modèles gratuits) : illustre le mécanisme, non
  comparable en exactitude à `resultats.md`.
- **Risque principal** — que la redondance relationnelle soit propre aux extractions
  ouvertes et non aux graphes sur schéma.

### À dire
La trajectoire remonte les cinq niveaux : cas d'usage, décision métier, problème
expérimental, question scientifique, question de thèse. Le décompte de porteurs est
l'amorce empirique, pas le point d'arrivée — la thèse commence là où il devient une
métrique de complétude indépendante du domaine. Sur les limites, deux méritent d'être
dites avant qu'on les trouve : la précision de 0,026 est un artefact d'annotation éparse
et non un échec, et la contradiction sur la date du PoC montre que la validation humaine
statue sur des étiquettes de relation, jamais sur la cohérence des valeurs. Enfin, si la
démo interactive est montrée : configurations 5 et 8, contexte identique à une phrase
près, décisions opposées — le modèle lit bien le contexte, mais la formulation du
signalement est une variable que nous n'avons jamais mesurée.

---

## Démonstrateur — 2 à 3 minutes, après la slide 6

Voir `deliverables/demo_script.md`.
