# Audit du pipeline d'extraction — rapport final

Auditeur : session `knowledge-graphs-f4`, qui n'a pas construit ce pipeline
(voir note de contexte ci-dessous). Contexte reconstruit intégralement par
lecture de `pipeline_lib.py` (810 lignes), `config.py`, `README.md`, et des
données/rapports générés, avant toute correction.

**Note de contexte** : cette session (`knowledge-graphs-f4`) travaillait sur
un pipeline d'extraction distinct (`kg/`, méthode regex + LLM) au moment où la
mission d'audit est arrivée. `extraction_pipeline/` a été construit par une
session sœur (`knowledge-graphs-c6`) sur le même projet — son `README.md` le
dit explicitement ("never reads or modifies the legacy extractor or `kg/`
directory"). Tu as confirmé vouloir que cette session reprenne la mission
malgré cela ; le travail ci-dessous part donc d'une lecture complète du code,
pas d'un historique de conception dont je disposerais déjà.

## Résumé des runs

| | Avant (run original) | Après (chunking fix seul) | Après (tous les fixes) |
|---|---:|---:|---:|
| OpenIE — extracted (phrases) | 1283 | 1287 | 1000 |
| OpenIE — no_triples | 2391 | 2376 | 2663 |
| OpenIE — skipped | 1415 | 1407 | 1407 |
| OpenIE assertions (triples) | 3358 | 3402 | **2337** |
| Clusters de relations | 1423 | 1423 | **1401** |
| Canonical edges | 2616 | 2450 | **2407** |

La baisse de 3358→2337 assertions OpenIE et la disparition des méga-clusters
"is"/"has"/"are"/"be" (point 3) expliquent l'essentiel de l'écart — c'est une
baisse de **bruit**, pas de couverture : voir point 3.

---

## 1. Audit des "skipped" (1415) et "no_triples" (2391)

**Skipped (1415)** — inspection de `is_extractable_sentence()` + 12 exemples
réels par motif :
- `table_or_placeholder` (710) : lignes de tableau Markdown (`|`) — légitime.
  Un seul faux positif trouvé (S08 : `"...0#.w|nt authority\\local service..."`,
  un pipe littéral dans un nom de compte Windows) — fréquence négligeable
  (1/710), non corrigé.
- `length` (544) : fragments de cellules de tableau CVSS isolés (S07 :
  `"Metric"`, `"Value"`, `"Low"`...) et blobs de code/JWT/certificats
  (S08/S09, jusqu'à 1831 caractères) — légitime dans les deux cas.
- `url_or_figure` (123), `navigation` (6), `heading` (2) : légitimes.

**Aucun pattern de raté systématique trouvé dans les skips.**

**No_triples (2391)** — 10 exemples aléatoires (seed fixe pour reproductibilité) :
6-7 légitimement sans relation (citations, boutons UI, code, questions
marketing), 2 pertes probables de MinIE sur des phrases syntaxiquement
complexes (S12, S50), et **1 bug réel trouvé** : S54 (`"is enough to prevent
the vulnerability from being wormable"`, un fragment sans sujet).

**Correction appliquée** : ce fragment ne venait pas du découpage en phrases
mais du **chunking en amont** (`preprocess_corpus.py`, écrit plus tôt dans
cette session, pas dans `extraction_pipeline/`) — `chunk_text()` construit le
chevauchement entre chunks avec `current[-overlap:]`, une coupe par nombre de
caractères qui peut tomber au milieu d'un mot. Confirmé sur S50 : le chunk 7
commençait littéralement par `"edge of the vulnerable system..."`, coupé au
milieu de *"knowledge"*. 38 % des phrases de S54 (161/424) commençaient par
une minuscule — signature de ce bug. **Fix** : `chunk_text()` ignore
maintenant le mot partiel en tête de chevauchement
(`preprocess_corpus.py:120-133`). `corpus/clean/*.json` régénéré — seul le
champ `chunks` a changé (vérifié par hash : `clean_text` identique sur les 56
sources). Preuve avant/après : chunk 7 de S50 commence maintenant par `"of
the vulnerable system..."` (mot entier).

## 2. Comptage des assertions structurées

**Aucune action nécessaire** — déjà correct. `structured_assertions.json`
(259, exclusivement `extraction_method: "structured"`) est compté et rapporté
**séparément** de `openie_assertions.json` dans les trois rapports
(`extraction_report.md`, `final_summary.md`, `evaluation/report.md`). Pas de
mélange.

**Clarification de terminologie** (pas un bug) : le "1283" du brief de
mission est le compte de *phrases* avec statut `extracted` dans l'audit — pas
le nombre d'assertions. Une phrase "extracted" produit souvent plusieurs
triples (MinIE peut extraire 2-3 faits d'une même phrase), d'où
`openie_assertions.json` (3358 avant fix) > `extracted` (1283). Deux
dénominateurs différents, pas une perte de données.

## 3. Qualité des clusters de relations

**Alerte trouvée avant même de lire les clusters en détail** :
`clusters_validation.json` marquait **1419 clusters sur 1423 en "accept"**
(4 "reject" seulement) — un taux de 99,7 % qui n'a pas l'air d'une revue
qualité réelle cluster par cluster.

**Faux synonymes fusionnés à tort (le pire cas)** : les deux plus gros
clusters par volume étaient `"is"` (595 assertions) et `"has"` (271
assertions) — des copules/auxiliaires nus que MinIE extrait quand il ne
trouve pas de vrai verbe de relation. `"are"` (82) et `"be"` (53) même
problème. À eux quatre : 1001 assertions (30 % du total OpenIE) rassemblées
sous une étiquette sans aucune valeur sémantique — et, vu le taux d'accept,
très probablement déjà validées comme "relations canoniques" légitimes.

**Correction appliquée** (`pipeline_lib.py`, `is_usable_triple()`) :
- Nouveau filtre `is_bare_auxiliary_predicate()` : rejette un prédicat
  entièrement composé de mots auxiliaires/copules/négation (is/has/are/be/
  can/could/does/not...). Un prédicat avec ne serait-ce qu'un mot de contenu
  passe toujours (ex. "is called" n'est pas affecté).
- Plafond de longueur du prédicat resserré de 160 → 100 caractères. Preuve :
  81 prédicats distincts dépassaient 60 caractères, jusqu'à 158 — des
  clauses entières mal analysées par MinIE (ex. *"has been documented as
  deliberate tactic during ransomware negotiations targeted capability to
  crash firewall is merely inconvenience It is coordination tool"*, 157
  caractères — plusieurs phrases concaténées). p99 des prédicats réels est à
  85 caractères ; 100 les garde tous sans effort.

**Preuve avant/après** : `is`/`has`/`are`/`be` ont **disparu** de la liste
des clusters après re-run (0 occurrence). Nouveau top 3 par volume :
`"has affected version bound"` (39), `"has affected product"` (29), `"has
vendor"` (29) — des relations réellement informatives.

**Vrai synonyme resté séparé (trouvé, PAS corrigé)** : `"affects"/"affect"`
sont bien fusionnés, mais `"is affected by"/"are affected by"` (voix
passive) restent dans un **cluster séparé** — même relation en sens inverse.
Cause : le seuil de Jaccard (0,80) sur les tokens ne les rapproche pas assez
(`{"affect"}` vs `{"affect","by"}` → Jaccard 0,5), et surtout **le pipeline
ne fait aucune normalisation actif/passif** (ce qui exigerait d'échanger
sujet et objet, pas seulement de renommer le prédicat).

**⚠️ Point à trancher par toi** (conforme à ton propre critère : "changerait
le schéma de sortie de façon incompatible") : faut-il ajouter une détection
actif/passif qui échange source/target à la canonicalisation pour ces cas ?
Je n'ai pas implémenté cela — ça change la structure même de
`build_canonical_kg()` (aujourd'hui : relabel seulement, jamais de swap
source/target), et c'est exactement le genre de décision que tu as dit
vouloir trancher toi-même.

Le reste de l'échantillon inspecté (`exploit`/`exploited`/`exploits`,
`allows`/`allow`, `requires`/`require`, `contains`/`contain`,
`use`/`uses`/`Uses`) est **correctement fusionné** — la logique Jaccard
fonctionne bien sur les variantes flexionnelles/casse, le problème était
concentré sur les auxiliaires nus et les prédicats trop longs, pas sur le
seuil général.

Les 1305 clusters restés "accept" après le fix n'ont **pas** été repassés en
revue un par un par moi (échelle non réaliste) — j'ai vérifié un échantillon
ciblé (mots-clés affect/patch/fix/mitigat/remediat/chain/exploit/vulnerab/
workaround, ~90 clusters inspectés) sans trouver d'autre faux-synonyme
manifeste. 96 nouveaux clusters (composition changée par les fixes) sont
repassés à `"pending"` — comportement voulu, pas re-acceptés en bloc par moi
(je ne voulais pas répéter l'erreur du rubber-stamp initial).

## 4. Traçabilité canonique → brut

**Trouvé** : les edges canoniques n'avaient ni `domain`, ni `range`, ni
`derived_from` — seulement `predicate_canonical` ajouté au-dessus de l'edge
open-KG existant. Les trois couches (assertions évidence-complètes → open KG
→ canonical KG) étaient bien toutes préservées et consultables séparément
(`build_canonical_kg()` ne fait que filtrer/enrichir, jamais supprimer côté
open KG) — ce sous-point était déjà correct.

**Correction appliquée** (`pipeline_lib.py`, `build_canonical_kg()`) :
- `domain`/`range` : type d'entité (`entity_type`) du nœud source/cible,
  regardé dans `open_kg/nodes.json`.
- `derived_from` : liste complète des `member_phrases` du cluster accepté
  dont est issu ce edge — donc chaque edge canonique montre maintenant
  *toutes* les formulations brutes regroupées sous son label, pas seulement
  la sienne propre (déjà disponible via `predicate_raw`).

Preuve : un edge `predicate_canonical: "exploit"` porte maintenant
`"derived_from": ["exploit", "Exploits", "exploited", "exploits", "has
exploited", "have exploited"]` et `"domain"/"range": "Mention"` (type
générique — limite résiduelle de `infer_type()`, pas quelque chose que j'ai
introduit ni corrigé, à améliorer si tu veux un typage plus fin plus tard).

## 5. Métriques d'étape

**Trouvé** : `evaluate_pipeline()` ne calculait que des comptages bruts +
une precision/recall/F1 globale au niveau canonique (et seulement si un gold
set existait — qui était vide). Aucune métrique par étage (entités, OpenIE,
résolution d'entités, clusters), et — bug distinct trouvé en marge — la
comparaison gold existante utilisait les **ID internes SHA256** des entités
comme identifiants attendus, ce qu'aucun humain ne peut écrire à la main
dans un fichier gold.

**Corrections appliquées** :
1. `structural_metrics()` (nouveau) : métriques calculables sans gold —
   ratio de compression des entités (mentions brutes / entités canoniques),
   distribution de taille des clusters (médiane, max, % multi-phrases),
   nombre de clusters encore "pending", ratio relations canoniques / phrases
   brutes distinctes.
2. `gold_evaluation()` (réécrit) : precision/recall/F1 à **trois niveaux**
   (résolution d'entités, triples OpenIE, triples canoniques), comparés sur
   des **labels lisibles** (`canonical_label`, pas les hash), et **restreints
   aux sources annotées dans le gold** (sinon comparer 8 faits gold contre
   les 2325 assertions de tout le corpus fait chuter la precision à ~0,3 %
   sans rapport avec la qualité réelle — bug que j'ai fait puis corrigé
   moi-même en cours de route, voir le fichier pour la trace).

**⚠️ Limite à connaître avant de lire les chiffres** : le gold set (point 6)
est volontairement non-exhaustif (quelques faits sûrs par source, pas tout).
Le **recall** est donc interprétable (100 % sur openie/canonical, 89 % sur
les entités — le pipeline retrouve bien ce qu'un humain a repéré comme
correct). La **precision** ne l'est pas encore (elle chute mécaniquement dès
que le gold ne couvre pas tout un vrai positif) — elle ne redevient
significative qu'une fois le gold complété/validé par toi.

## 6. Gold set minimal (ébauche — À VALIDER PAR TOI)

**12 sources** annotées dans `evaluation/gold/*.json`, chacune avec un champ
`_note` explicite marquant le fichier comme brouillon :
- Données (déjà identifiées par toi) : S03 (NVD structuré), S22 (EPSS
  structuré), S18 (texte libre, cve-specific, court), S41 (texte libre,
  cve-specific, cas `chains_with`).
- Ajoutées pour la diversité : S06 (NVD structuré, cas négatif — pas
  d'entrée KEV), S15 (texte libre, très court, quasi aucun triple attendu —
  comportement correct documenté), S09 (texte libre, long/chunké, cas où
  MinIE produit du bruit — documenté sans faux triples de complaisance),
  S20 (MITRE ATT&CK, framework, long), S54 (SSVC PDF, framework, long — la
  source du bug de chunking corrigé au point 1, utile comme test de
  non-régression), S47 (FIRST EPSS, framework, court), S43 (Broadcom,
  multi-CVE), S29 (format teaser catalogue KEV).

**Méthodologie, à évaluer par toi** : entités et triples canoniques
rédigés indépendamment (à partir du contenu source, pas de la sortie du
pipeline) ; triples OpenIE en revanche **échantillonnés et vérifiés** dans
la sortie réelle du pipeline plutôt qu'écrits à l'aveugle — la comparaison
se fait par égalité de chaîne exacte, écrire une formulation à l'aveugle
face à un style d'extraction MinIE que je ne maîtrise pas parfaitement
aurait pénalisé le pipeline sur du simple désaccord de formulation, pas sur
une vraie erreur. C'est donc un contrôle de non-régression sur ces phrases
précises, pas une mesure de rappel OpenIE indépendante — à garder à l'esprit
si tu étends ce gold set.

## 7. Alignement vers des standards (STIX / UCO)

Aucun mapping existant trouvé (recherche `stix`/`uco` dans tout
`extraction_pipeline/`, hors vendor). Première passe proposée sur les
relations canoniques les plus fréquentes du corpus réel :

| Relation locale | Volume | Équivalent standard proposé | Confiance |
|---|---:|---|---|
| `mitigated_by` | (schéma KG existant, pas encore dans ce pipeline OpenIE) | STIX 2.1 `course-of-action` --`mitigates`--> `vulnerability` | Moyenne-haute — SRO natif STIX pour ce cas précis |
| `has affected product`/`has vendor` | 29/29 | Pas d'équivalent SRO STIX propre — CPE va normalement en `external_references`/propriété sur la Vulnerability SDO, pas en Relationship Object | Basse (garder extension locale) |
| `has weakness` (CVE→CWE) | (structuré) | Pas d'équivalent SRO — CWE est conventionnellement une `external_reference` (source_name: "cwe") sur la Vulnerability SDO | Basse (garder extension locale) |
| `chains_with` (CVE→CVE) | — | Aucun équivalent standard connu ; `relationship_type` custom nécessaire dans les deux ontologies | Basse (garder extension locale) |
| `exploit`/variantes | 19 | Rapprochable de STIX `indicator`--`indicates`-->`vulnerability` ou `malware`--`exploits`-->`vulnerability` selon le sujet réel | Moyenne — dépend du typage du sujet, pas automatique |

**Avertissement de confiance** : je n'ai pas de moyen de vérifier ces
correspondances contre la spec STIX 2.1/UCO à jour depuis cet environnement
— elles viennent de ma connaissance générale du standard, pas d'une
consultation directe. Seul `mitigated_by → course-of-action mitigates`
me semble suffisamment solide pour être implémenté sans revalidation
externe ; les autres méritent une vérification humaine avant tout code
d'export STIX/UCO. Aucun code d'alignement n'a été écrit — uniquement cette
table de correspondance, comme demandé ("sans forcer un alignement").

---

## Fichiers modifiés

- `preprocess_corpus.py` (hors `extraction_pipeline/`, projet racine) :
  fix du chunking mot-coupé.
- `corpus/clean/S*.json` : régénéré (seul `chunks` a changé, `clean_text`
  identique — vérifié par hash sur les 56 sources).
- `extraction_pipeline/scripts/pipeline_lib.py` : filtre auxiliaires nus +
  plafond de longueur de prédicat resserré ; `domain`/`range`/`derived_from`
  sur les edges canoniques ; métriques structurelles + gold à 3 niveaux
  correctement scopées.
- `extraction_pipeline/evaluation/gold/*.json` : 12 fichiers créés (ébauche).
- Toutes les données/rapports générés (`data/`, `open_kg/`,
  `relation_clustering/`, `canonical_kg/`, `evaluation/`, `reports/`) :
  régénérés par un run complet final, cohérents entre eux.

## Ce qui reste explicitement en attente de ta validation

1. **Point 3** : faut-il implémenter la normalisation actif/passif
   (échange source/target) pour fusionner `affects`/`is affected by` et
   cas similaires ? Change la structure de `build_canonical_kg()`.
2. **Point 6** : le gold set de 12 sources est un brouillon — à relire,
   corriger, étendre avant de t'y fier comme référence de mesure.
3. **Point 7** : la table de correspondance STIX/UCO n'est pas vérifiée
   contre la spec à jour — à valider avant tout export réel vers ces formats.
4. **96 clusters "pending"** (issus des fixes) : besoin d'une vraie revue
   humaine, je ne les ai pas acceptés en bloc à ta place.
