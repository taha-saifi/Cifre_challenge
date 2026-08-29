# Déduplication par triple exact + reclassification finale des 11 clusters rejetés

Dernière itération sur le clustering de relations. Décisions appliquées directement à
`clusters_validation.json` (pas seulement proposées) conformément à la mission. Le canonical
KG a été reconstruit une dernière fois avec toutes les décisions cumulées.

Archive avant cette passe : `archive/pre_final_dedup_20260829T011315/`.

**Bug rencontré et corrigé en cours de route** : `export_clusters_for_review()` (introduit
lors de la stabilisation des IDs) reconstruisait un nouveau dict de validation à chaque export
sans jamais recopier le champ `split_assignments` — un split appliqué directement au fichier
disparaissait donc au premier ré-export. Corrigé dans `pipeline_lib.py` (le champ est
maintenant propagé dans les 4 branches du protocole d'ancrage). Les décisions `patch` et
`executed` avaient été perdues une première fois par ce bug et ont dû être réappliquées ;
vérifié après coup que le split survit maintenant à un ré-export. Un second point manqué :
`build_canonical_kg()` lit `open_kg/`, pas directement les assertions — `build_open_kg()`
doit être ré-exécuté après tout ajout à `structured_assertions.json`, ce qui n'avait pas été
fait pour les 6 nouveaux faits promus avant le premier calcul (0 edges au lieu des 6 attendus).
Corrigé en relançant `extract_entities → resolve_entities → build_open_kg` avant le
recalcul final.

Méthode de dédup : regroupement par `(subject_raw, predicate_raw, object_raw)` après
normalisation légère (espaces, casse) — **aucune fusion approximative** : un triple qui diffère
ne serait-ce que d'un mot reste distinct. Chaque triple unique conserve la liste complète de
ses `source_id`.

---

## 1. `exploit` — 63 → 53 triples uniques

**Classification** : 6 "fait CVE-spécifique", ~15 "glossaire/générique", ~32
"fragment/mésanalyse" (dont 3 mésanalyses actives : le mot "Exploited"/"Exploit" capturé à
l'intérieur des noms propres "Known Exploited Vulnerabilities" ×2 et "Exploit Code Maturity").

Les 6 faits CVE-spécifiques identifiés :
| Source | Triple |
|---|---|
| S18 | Attackers → exploit → critical SharePoint flaw *(CVE-2026-55040)* |
| S40 | attacker → exploits → CVE-2026-55040 |
| S17 | China-Nexus Actor → Exploits → VMware vCenter CVE-2026-59310 |
| S44 | attacker with network access to vCenter → can exploit → the flaw to write files outside the intended directory and execute arbitrary code *(CVE-2026-59310, vérifié via evidence complète)* |
| S12 | suspected APT actor → is exploiting → CVE-2026-59310 *(vérifié via evidence complète — objet tronqué dans le triple brut)* |
| S46 | Microsoft has not released proof-of-concept exploit code and there is no confirmed evidence of active exploitation *(CVE-2026-33824, fait négatif utile)* |

**Décision : `reject` — 6 > 5, seuil de la mission dépassé.** Les 6 faits restent mélangés à
53 triples partageant les mêmes phrases exactes ("exploit", "exploits", "Exploited"...), sans
séparation possible par le mécanisme de split (qui agit par phrase, pas par triple). Non
extraits individuellement pour rester dans le cadre fixé par la mission (extraction
individuelle réservée aux cas ≤5). **6 vrais faits perdus pour le canonical KG** — toujours
présents dans `openie_assertions.json`/`open_kg` à la couche brute.

---

## 2. `requires` — 39 → 32 triples uniques

**Classification** : 1 "fait CVE-spécifique", ~24 "glossaire/générique" (dont 8 occurrences de
2 phrases identiques dupliquées 4× chacune — glossaire CVSS Attack Complexity, 6 occurrences
de "Successful exploitation of vulnerability requires..." toutes issues de S51 seul,
3 occurrences de "FIRST requires as a condition of use..."), ~7 "fragment".

**Décision : `reject` le cluster générique**, **`accept` le fait extrait individuellement** :
- **1 fait promu** → nouveau prédicat `requires attacker capability` (cluster propre,
  `rc2_15fc4ed7a6ab78d9`) : `CVE-2026-33824 → requires attacker capability → ability to send
  specially crafted IKE traffic to a vulnerable system` (S46, evidence vérifiée contre le
  texte source).
- 31 triples restants rejetés (glossaire dupliqué + fragments).

---

## 3. `allows` — 21 → 20 triples uniques

**Classification** : 4 "fait CVE-spécifique", ~10 "glossaire/générique", ~6 "fragment".

**Décision : `reject` le cluster générique**, **`accept` les 4 faits extraits
individuellement** → nouveau prédicat `has technical impact` (cluster propre,
`rc2_88a5f4a2c3f52f51`), un edge par triple (evidence complète vérifiée pour chacun, l'objet
brut OpenIE était tronqué dans 3 cas sur 4) :

| CVE | Objet (texte complet, pas le triple OpenIE tronqué) | Source |
|---|---|---|
| CVE-2026-55040 | impersonation | S18 |
| CVE-2026-55040 | a lack of proper validation in SharePoint's JWT handling allows an unauthenticated attacker to forge JWT tokens and access the web application as a privileged account | S10 |
| CVE-2026-59310 | the exploit allows an unauthenticated attacker with network access to the vCenter management interface to traverse directories beyond their intended boundaries and achieve remote code execution without credentials or user interaction | S17 |
| CVE-2026-59310 | could allow a threat actor with network access to vCenter to execute arbitrary code | S31 |

Les deux faits CVE-2026-59310 (S17, S31) sont gardés distincts (règle "pas de fusion
approximative") bien que corroborant le même impact — deux sources indépendantes, valeur
ajoutée réelle (confirmation croisée), pas une contamination.

16 triples restants rejetés (glossaire CVSS/SSVC + fragments).

---

## 4. `is required` — 19 → 12 triples uniques

**Classification** : 0 "fait CVE-spécifique", 7 "glossaire/générique", 5 "fragment".

**Décision : `reject` entier.** Aucune extraction — le seuil "≤5 clairement identifiables" ne
s'applique pas puisqu'il n'y a rien à extraire.

---

## 5. `used` — 18 → 14 triples uniques

**Classification** : 0 "fait CVE-spécifique" au sens strict (aucun triple ne nomme une des 5
CVE, un acteur nommé, une organisation nommée ou un produit nommé de façon informative — même
"attackers are using valid credentials" ×2 reste un acteur générique sans ancrage), 6
"glossaire/générique", 8 "fragment".

**Décision : `reject` entier.**

---

## 6. `affect` — 17 → 15 triples uniques

**Classification** : 0 "fait CVE-spécifique", 10 "glossaire/générique" (dont le sous-ensemble
`vulnerability affects multiple product versions/platforms/operating systems`, redondant avec
`has affected product`/`has affected version bound` déjà `accept` côté structuré), 5
"fragment".

**Décision : `reject` entier.**

---

## 7. `publish` — 15 → 11 triples uniques

**Classification** : 1 "fait CVE-spécifique", 6 "glossaire/générique", 4 "fragment".

**Décision : `reject` le cluster générique**, **`accept` le fait extrait individuellement** →
nouveau prédicat `has vendor advisory` (cluster propre, `rc2_4766b8fa7cd0954d`) :
`CVE-2026-59310 → has vendor advisory → VMSA-2026-0006` (S12 ; evidence complète : *"Broadcom
initially published VMSA-2026-0006 on 29 July 2026"* — l'objet brut OpenIE était tronqué à
"VMSA-2026", corrigé ici avec le numéro complet tiré de l'evidence).

10 triples restants rejetés.

---

## 8. `cause` — 12 → 7 triples uniques

**Classification** : 0 "fait CVE-spécifique parmi les 5 cibles" (2 faits réels identifiés sur
CVE-2026-20349, un DoS Cisco ASA/FTD hors des 5 CVE du challenge — S17 : *"causes the device
to restart unexpectedly"* et *"insufficient error checking in the process..."*), 4
"glossaire/générique", 3 "fragment".

**Décision : `reject` entier.** Les 2 faits réels sur CVE-2026-20349 restent dans
`openie_assertions.json` mais ne sont pas extraits — hors périmètre des 5 CVE cibles du
challenge, et de toute façon fragmentaires (sujets tronqués).

---

## 9. `provided` — 10 → 7 triples uniques

**Classification** : 2 "fait CVE-spécifique" (nomment CVE-2026-55040/63520), 4
"glossaire/générique", 1 "fragment" (S16, "Hermes Agent → provided → orchestration" — contexte
non vérifiable, écarté par prudence plutôt que classé avec confiance).

**Décision : `reject` entier — 2 faits identifiés mais non extraits, entièrement redondants**
avec `has patch` déjà `accept` (mêmes CVE, mais objet vague "following updates" sans numéro
KB, contre les faits structurés propres `CVE → has patch → KB50028xx` déjà en place). Extraire
ces doublons de moindre qualité n'ajouterait aucune information nouvelle.

---

## 10. `added` — 10 → 8 triples uniques

**Classification** : 5 "fait CVE-spécifique" (nomment CVE-2026-55040 ×3 formes,
CVE-2026-59310, CVE-2026-65400), 1 "glossaire/générique" (KEV catalogue générique), 2
"fragment/hors-sujet" (Microsoft/IKE — polysémie légitime déjà vérifiée non-bug ; révision de
page).

**Décision : `reject` entier — 5 faits identifiés mais non extraits, entièrement redondants**
avec `has CISA exploit addition date` déjà `accept` (structuré depuis le JSON NVD, couvre
CVE-2026-33824/55040/59310/65400 avec la date exacte 2026-08-18 pour chacune — strictement
supérieur en qualité aux triples OpenIE ici, qui n'ont même pas la date). Aucune perte nette.

---

## 11. `included` — 6 → 6 triples uniques (aucune réduction par dédup)

**Classification** : 0 "fait CVE-spécifique", 3 "glossaire/générique" (CVSS, "is not considered
here" ×3), 3 "fragment".

**Décision : `reject` entier.**

---

## Récapitulatif chiffré

| Cluster | Avant | Après dédup | CVE-spécifique | Glossaire/générique | Fragment/mésanalyse | Décision finale | Edges créés |
|---|---:|---:|---:|---:|---:|---|---:|
| exploit | 63 | 53 | 6 | ~15 | ~32 | reject (6 perdus, >seuil) | 0 |
| requires | 39 | 32 | 1 | ~24 | ~7 | reject + 1 extrait | 1 |
| allows | 21 | 20 | 4 | ~10 | ~6 | reject + 4 extraits | 4 |
| is required | 19 | 12 | 0 | 7 | 5 | reject | 0 |
| used | 18 | 14 | 0 | 6 | 8 | reject | 0 |
| affect | 17 | 15 | 0 | 10 | 5 | reject | 0 |
| publish | 15 | 11 | 1 | 6 | 4 | reject + 1 extrait | 1 |
| cause | 12 | 7 | 0* | 4 | 3 | reject (2 perdus, hors 5 CVE) | 0 |
| provided | 10 | 7 | 2 | 4 | 1 | reject (2 redondants, non extraits) | 0 |
| added | 10 | 8 | 5 | 1 | 2 | reject (5 redondants, non extraits) | 0 |
| included | 6 | 6 | 0 | 3 | 3 | reject | 0 |
| **Total** | **230** | **185** | **19** | **~90** | **~76** | **9 reject + 2 extraits partiels** | **6 nouveaux edges** |

\* `cause` : 0 fait parmi les 5 CVE cibles ; 2 faits réels hors périmètre (CVE-2026-20349) non
comptés dans la colonne mais documentés au §8.

**6 nouveaux edges canoniques créés** au total (1 `requires attacker capability`, 4
`has technical impact`, 1 `has vendor advisory`), chacun sous une relation propre et non sous
l'étiquette générique bruitée d'origine, conformément à la consigne.

**Faits réels identifiés mais non promus au canonical KG** (limites de cette passe, pour le
§16 de la note) :
- **6 faits** dans `exploit`, non extraits car le cluster dépasse le seuil de 5 fixé par la
  mission et n'est pas séparable par phrase.
- **2 faits** dans `cause` (CVE-2026-20349, hors des 5 CVE cibles).
- **2+5 = 7 faits** dans `provided`/`added`, non extraits car strictement redondants avec des
  faits structurés déjà `accept` et de meilleure qualité (`has patch`, `has CISA exploit
  addition date`).

Total : 15 faits réels visibles dans `openie_assertions.json`/`open_kg` mais absents du
canonical KG à l'issue de cette passe, pour des raisons documentées cas par cas (pas un oubli).

---

## Reconstruction finale du canonical KG

Séquence complète ré-exécutée : `extract_structured → extract_entities → resolve_entities →
build_open_kg → build_relation_inventory → normalize_relations → cluster_relations →
export_clusters_for_review → apply_cluster_validation → build_canonical_kg →
evaluate_pipeline`.

| Étape | Edges canoniques |
|---|---:|
| Avant cette mission (état hérité des 2 passes précédentes) | 2081 |
| + `references` accepté tel quel | +24 |
| + `patch` splitté (`has patch` = 8 structurés + 2 minie propres + 1 fragment toléré) | +11 |
| + `executed` splitté (`is executed`) | +1 |
| + `requires attacker capability` (1 fait promu) | +1 |
| + `has technical impact` (4 faits promus) | +4 |
| + `has vendor advisory` (1 fait promu) | +1 |
| **Total final** | **2123** |

Vérifié : les 11 clusters rejetés + `contains` (non traité, hors périmètre de cette mission,
laissé `pending` comme précédemment) contribuent bien **0** edge chacun au résultat final.

## Ce qui n'a pas été touché

`contains` (`rc2_dd9245cc1ddc69c8`) n'était pas dans la liste des 11 clusters de cette mission
— laissé intact, toujours `pending`, exactement dans l'état où l'avait laissé
`cluster_review_16.md` (compromis non tranché entre 7 faits utiles "Produit contains
Faiblesse" et du bruit non séparable par phrase). Les 1154 autres clusters `pending` (dont les
775 singletons) n'ont pas été touchés non plus.

## Fichiers modifiés

- `extraction_pipeline/scripts/pipeline_lib.py` : correction du bug de perte de
  `split_assignments` dans `export_clusters_for_review()`.
- `relation_clustering/clusters_validation.json` : 17 décisions appliquées (11 reject, 3
  accept directs pour les nouveaux prédicats promus, 2 split, 1 accept pour `references`).
- `data/structured_assertions.json` : +6 (273 → 279).
- `canonical_kg/`, `open_kg/`, `relation_clustering/clusters_raw.json` : régénérés.

---

**Fin de cette itération sur le clustering de relations, comme demandé.** Le canonical KG
reste dans cet état (2123 edges) pour la suite du plan Jour 2 (qualification des lacunes,
roadmap J3-J4, rédaction).
