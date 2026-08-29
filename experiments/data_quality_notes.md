# Défauts de données constatés pendant la clôture des livrables

Constats faits en construisant la vue de présentation et la table de qualité des
sources. Le KG est **gelé** pour la durée du protocole expérimental : rien n'est corrigé
ici, tout est consigné pour la section « limites » de la note. Corriger le graphe
maintenant invaliderait les 45 cellules déjà exécutées.

## 1. 87 identifiants de nœuds dupliqués dans `canonical_kg/nodes.json`

`nodes.json` contient **1956 entrées pour 1867 identifiants distincts**. 87 identifiants
apparaissent deux fois, avec des libellés qui ne diffèrent que par la casse :

```json
{"id": "e_2e5f87b467beeae0", "label": "Active", "aliases": ["Active"], "source_ids": ["S51"]}
{"id": "e_2e5f87b467beeae0", "label": "active", "aliases": ["active"], "source_ids": ["S16"]}
```

**Cause** : l'identifiant est calculé sur une forme normalisée insensible à la casse,
mais le libellé, lui, n'est pas normalisé. Deux graphies produisent donc un même
identifiant et deux enregistrements distincts sont émis.

**Conséquence** : tout consommateur qui construit un dictionnaire `{id: label}` — ce que
font `build_contexts.py`, `carrier_check.py` et `build_presentation_view.py` — ne
conserve silencieusement que le dernier libellé rencontré. Les arêtes ne sont pas
corrompues (elles référencent des identifiants, pas des libellés), mais **le libellé
affiché d'un nœud dépend de l'ordre du fichier**, et le nombre de nœuds annoncé est
surévalué de 89.

**À retenir pour la note** : le décompte correct est **1867 nœuds distincts**, pas 1956.
Le chiffre 1956 figure dans des rapports antérieurs ; il compte des entrées, pas des
entités.

## 2. La résolution d'entités est quasi inopérante

`evaluation/metrics.json` : `entity_mentions_raw` 3699 → `entities_canonical` 3697, soit
**2 fusions**, un `entity_compression_ratio` de 1,0005.

C'est la limite la plus sérieuse du graphe, et elle explique plusieurs symptômes
observés ailleurs :

- la longue traîne de **946 relations canoniques** dont 535 à occurrence unique ;
- des nœuds comme `Patching CVE-2026-55040` traités comme des entités distinctes de
  `CVE-2026-55040`, ce qui empêche l'arête `break` (S40) de se rattacher à la CVE
  elle-même ;
- le fait que le décompte de porteurs doive s'appuyer sur le texte de l'`evidence`
  plutôt que sur la structure du graphe : sans résolution d'entités fiable, deux arêtes
  parlant du même objet ne partagent pas nécessairement de nœud.

La docstring de `structural_metrics()` anticipait exactement ce cas de figure. La
métrique a donc fait son travail — elle a signalé le problème ; c'est le traitement qui
n'a pas suivi, faute de temps.

## 3. Crédibilité des sources non propagée au pipeline

`build_corpus.py` déclare pour chaque source un rang (`primary` / `secondary`) et une
catégorie (`official`, `publisher`, `researcher`, `journalistic`, `commercial`,
`official_framework`). Ces champs sont écrits dans `corpus/raw/` mais **ne sont pas
propagés dans `corpus/clean/`** par `preprocess_corpus.py` — or c'est `clean/` que lit
`discover_sources()`.

**Conséquence** : le pipeline d'extraction n'a jamais eu connaissance de la crédibilité
d'une source. Une affirmation issue d'un billet commercial et une affirmation issue du
NVD entrent dans le graphe avec exactement le même poids. Aucune pondération par
fiabilité n'existe aujourd'hui — c'est une extension naturelle, pas un correctif urgent,
et c'est à énoncer plutôt qu'à laisser supposer le contraire.

## 4. Le mécanisme de dérive n'a jamais été exercé

`clusters_validation.json` : 0 cluster en `needs_reconfirmation`, 0 `previous_decision`,
`composition_changed_since_review` faux sur les 2111. Le mécanisme de re-validation est
implémenté et testé unitairement, mais aucune dérive réelle ne l'a encore déclenché.
Le présenter comme éprouvé en conditions réelles serait faux.
