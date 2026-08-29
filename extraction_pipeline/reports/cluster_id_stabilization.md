# Stabilisation des identifiants de cluster + rapport de catégorisation

Archive de l'état avant migration : `archive/pre_cluster_id_migration_20260828T230446/`
(`clusters_raw.json`, `clusters_validation.json`, `accepted_relation_mapping.json`,
`canonical_kg/edges.json`, `canonical_kg/nodes.json` — l'ancien schéma d'ID, 940 `accept` /
1168 `pending`, aucun `reject`/`split`).

Aucune nouvelle décision de revue n'a été prise dans cette passe. Le canonical KG est
inchangé : toujours **2081 edges**, exactement les mêmes qu'avant (vérifié).

---

## 1. Nouveau mécanisme d'ID

**Ancien schéma** : `cluster_id = stable_id("rc", *member_phrases)` — hash de la composition
exacte. Tout changement de composition (même l'ajout d'un seul membre) change l'ID, donc perd
la décision précédente.

**Nouveau schéma** : `cluster_id = stable_id("rc2", normalize_relation(representative))` —
hash de la forme normalisée du prédicat dominant (le membre le plus fréquent du cluster,
après lemmatisation déterministe existante : minuscule, retrait des auxiliaires, retrait des
suffixes -s/-es/-ies/-ing/-ed). Deux clusters gardent le même ID tant que leur membre
dominant se normalise de façon identique, même si des membres satellites apparaissent ou
disparaissent.

L'ancien hash exact est conservé sous un nouveau champ `content_id` (même formule qu'avant),
qui sert uniquement à détecter *quand* la composition a réellement changé — il n'est plus
utilisé comme identifiant.

**Collisions de concept-ID** : détectées explicitement (deux clusters distincts partageant
par coïncidence le même prédicat dominant normalisé, sans que Jaccard les ait jugés
similaires). Vérifié sur les données actuelles : **0 collision** parmi les 2108 clusters.
Le mécanisme de détection reste en place (suffixe `_dupN` + flag `concept_id_collision`) au
cas où cela se produirait sur un futur run.

## 2. Détection de dérive de composition

Chaque enregistrement de `clusters_validation.json` porte maintenant :
- `content_id_at_last_decision` / `member_phrases_at_decision` : l'ancrage — composition au
  moment de la dernière décision réelle (`accept`/`reject`/`split`).
- `composition_changed_since_review` (bool) et `diff: {added: [...], removed: [...]}` par
  rapport à cet ancrage.
- `previous_decision` : la décision précédente, conservée visible quand elle a été
  rétrogradée.
- `review_status` : `new` (jamais revu sous cet ID) / `confirmed` (décision valide, ancrage à
  jour) / `needs_reconfirmation` (décision existante mais composition dérivée depuis
  l'ancrage — `decision` forcé à `pending` tant que non reconfirmé) / `pending` (jamais décidé,
  rien à protéger).

**Choix d'implémentation non spécifié par la mission, tranché ici** : pour sortir un cluster
de `needs_reconfirmation`, un simple ré-enregistrement de `"decision": "accept"` ne suffit pas
— le format de fichier n'a pas d'horodatage, donc rien ne permet de distinguer "l'humain vient
de relire le diff et confirme" de "le fichier n'a simplement pas été touché depuis le dernier
export". Un champ `"reconfirm": true` doit accompagner explicitement la décision pour que
l'ancrage soit rafraîchi ; sinon le prochain export re-rétrograde le cluster en `pending` avec
le même diff. Documenté dans l'en-tête de `clusters_review.md`.

## 3. Migration de l'historique

`scripts/migrate_cluster_ids.py` (nouveau, à usage ponctuel) : pour chacun des 940
enregistrements `accept` de l'ancien fichier, retrouve le cluster d'origine (par son ancien
`cluster_id`), calcule sa clé de concept (`normalize_relation(representative)`), et amorce un
enregistrement sous le nouvel ID avec l'ancienne composition comme ancrage.

**Résultat de la migration** : 940/940 décisions migrées, **0 collision de clé de concept**
parmi les clusters historiquement décidés (donc pas de conflit "deux anciens clusters accept
pointent vers le même nouveau concept-ID").

**Résultat après recalcul des clusters actuels par-dessus cet amorçage** :

| review_status | Nombre | Signification |
|---|---:|---|
| `confirmed` | 940 | Anciennement `accept`, ancrage toujours exact — **aucune dérive détectée** |
| `needs_reconfirmation` | **0** | — |
| `new` | 1168 | Jamais associé à une décision connue sous aucun concept-ID |

**Pourquoi `needs_reconfirmation` est à 0, et ce que ça signifie réellement** : ce n'est pas
que le mécanisme ne détecte rien — c'est que les 940 décisions `accept` actuellement dans
`clusters_validation.json` ne pouvaient, par construction de l'ANCIEN mécanisme (hash exact),
survivre que si leur composition n'avait *déjà* pas changé d'un seul membre depuis leur
dernière régénération. Autrement dit : l'ancien système a lui-même déjà silencieusement
éliminé toute trace d'un cluster `accept` qui aurait dérivé — c'est exactement le problème
signalé dans la mission. Il n'existe **aucune trace sur disque** d'une décision `accept`
antérieure au Correctif 2 qui aurait ensuite dérivé sans être remise à zéro : je n'ai pas
archivé `clusters_validation.json` avant le Correctif 2 (seulement `openie_audit.json`,
`openie_assertions.json`, `canonical_kg/edges.json` — voir `archive/pre_fix_v2_.../`), donc
cette portion de l'historique est irrécupérable. Le nouveau mécanisme protège désormais
**à partir de maintenant** : toute dérive future d'un cluster actuellement `accept` sera
détectée et signalée au prochain export, plus jamais silencieusement perdue.

---

## 4. Rapport de catégorisation (parmi les 1168 clusters non-`accept`)

Comme `needs_reconfirmation` est vide, la première catégorie demandée par la mission
("accept/reject avant Correctif 2, reconfirmation rapide") est **vide** — il n'y a rien à
reconfirmer rapidement, pour la raison expliquée ci-dessus. Les 1168 se répartissent donc
entièrement entre "vraiment nouveaux" et le sous-ensemble contaminé déjà identifié :

### 4a. Volume des 1168 clusters `new`

| Taille | Nombre de clusters |
|---|---:|
| ≥ 10 assertions | 25 |
| 5–9 assertions | 51 |
| 2–4 assertions | 317 |
| 1 assertion (singleton) | 775 |

**1168, c'est trop pour une revue humaine raisonnable en un seul passage** — dit
explicitement, comme demandé, plutôt que de proposer un raccourci. Les 775 singletons en
particulier ne peuvent, par construction (un seul membre, jamais comparé à rien d'autre),
receler aucune contamination de mélange — leur risque principal est individuel (mésanalyse
isolée), pas un mélange de sens. Ce n'est pas une suggestion de les accepter en bloc, juste
une observation sur la nature du risque qui les concerne.

### 4b. Clusters connus contaminés nécessitant un vrai split

- **`added`** (`cluster_id: rc2_7e9e5ac30f2216fd`, `review_status: new`, 10 assertions) :
  membres `[added, Added, add, adds]`. Contient à la fois des faits datés fiables (CISA ajoute
  telle CVE au KEV, à des dates précises) et au moins 2 faits hors-sujet vérifiés non-bugs
  (Microsoft ajoutant des capacités à IKE ; une note de révision de page) — détaillé dans
  `fix_report_v2.md`.
- **`patch`** (`cluster_id: rc2_a4895eb44afc336f`, `review_status: new`, 22 assertions) :
  membres `[patch, has patch, patched, patching]`. 8 faits structurés propres (KB → CVE) +
  2 faits `minie` propres + 12 mésanalyses `heuristic` (sujets tronqués) — détaillé dans
  `fix_report_v2.md`.

**Signal faible pour repérer d'autres cas similaires** (fourni pour donner une idée d'échelle,
pas pour trier automatiquement) : parmi les 76 clusters de volume ≥ 5, **14** mélangent
plusieurs `extraction_method` (`minie`/`heuristic`/`structured`) parmi leurs membres —
`patch` en fait partie (3 méthodes mélangées). **`added` n'en fait PAS partie** (tous ses
membres viennent de `minie`) — preuve que ce signal est incomplet, il ne détecte que la
contamination par qualité d'extraction, pas la polysémie comme celle d'`added`. Liste
complète des 14 :

```
exploit (63, minie+heuristic)      requires (39)      references (24, minie+structured)
contains (23)      patch (22, 3 méthodes)      allows (21)      is required (19)
used (18)      affect (17)      publish (15)      cause (12)      provided (10)
included (6)      executed (6)
```

Aucune de ces 14 n'a été inspectée en détail dans cette passe — les lister n'est pas un
jugement sur leur contamination réelle, seulement un signal pour prioriser une future revue.

### 4c. Faut-il implémenter le mécanisme de split maintenant ?

**Évalué, puis implémenté** — code seul, aucune décision de cluster changée. Justification :

- Le besoin n'est pas hypothétique : 2 clusters concrets (`added`, `patch`) en ont déjà besoin
  aujourd'hui, plus potentiellement une partie des 14 clusters à méthode mixte.
- Le changement est petit et isolé : ~25 lignes dans `accepted_relation_map()` et
  `derived_from_map()`, aucune modification du mécanisme d'ID ni du clustering lui-même.
- Sans lui, un humain qui atteint `added`/`patch` dans sa revue serait bloqué : le schéma
  actuel ne peut représenter qu'une décision uniforme par cluster.

**Implémentation** : nouveau champ optionnel `split_assignments` sur un enregistrement de
décision — `{"phrase": "label canonique", ...}`. Une phrase absente ou associée à `null` est
rejetée (exclue du canonical KG) — reject-par-défaut, pour qu'un split partiellement rempli ne
laisse jamais passer une phrase non explicitement tranchée sous une mauvaise étiquette.
`derived_from_map()` groupe la provenance par étiquette assignée, pas par cluster entier : deux
phrases d'un même cluster splitté vers des étiquettes différentes ne se citent plus l'une
l'autre comme `derived_from`.

Testé isolément (cluster synthétique `added`/`Added`/`add`/`adds`, `add` mappé à `null`) :
seule la phrase explicitement assignée ressort. **Non appliqué à `added` ni `patch`** — aucune
décision de split n'a été prise pour ces deux clusters, conformément à la consigne de ne pas
faire de nouvelle revue en masse. C'est un outil disponible pour la prochaine étape, pas une
correction déjà appliquée.

---

## Fichiers modifiés

- `extraction_pipeline/scripts/pipeline_lib.py` : `cluster_concept_key()`, `cluster_relations()`
  (nouveau schéma d'ID + détection de collision), `export_clusters_for_review()` (réécrit,
  protocole d'ancrage/dérive/reconfirmation), `split_assignment_labels()`,
  `accepted_relation_map()` et `derived_from_map()` (support `split`).
- `extraction_pipeline/scripts/migrate_cluster_ids.py` (nouveau, usage ponctuel déjà exécuté).
- `extraction_pipeline/reports/cluster_id_migration_conflicts.json` (nouveau, vide ici — 0
  collision).
- `relation_clustering/clusters_raw.json`, `clusters_validation.json`,
  `accepted_relation_mapping.json`, `canonical_kg/` : régénérés avec le nouveau schéma ;
  edges canonique inchangés (2081, vérifié identique à l'ancien schéma).

## Ce qui reste explicitement en attente — pas de nouvelle revue en masse effectuée

- **1168 clusters `new`** à trier — dit explicitement : trop pour un seul passage de revue
  humaine raisonnable. Priorisation suggérée mais non appliquée : les 76 clusters de volume
  ≥ 5 d'abord (`added`, `patch`, et les 14 à méthode mixte en tête), les 775 singletons
  ensuite ou en parallèle par lot.
- **`added` et `patch`** : le mécanisme de split est prêt, mais aucune décision de split n'a
  été prise pour eux — j'attends ta lecture avant de proposer une répartition phrase par
  phrase.
- Aucun cluster n'a été accepté en bloc dans cette passe.
