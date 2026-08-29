# Correction des 3 problèmes de capture identifiés par lecture directe

Archive de l'état AVANT correction : `archive/pre_fix_v2_20260828T223726/`
(`openie_audit.json`, `openie_assertions.json`, `canonical_kg/edges.json`, `canonical_kg/nodes.json`).

Tous les chiffres "avant" ci-dessous viennent de cette archive, jamais de la mémoire du run
précédent.

---

## Correctif 1 — Filtre de pré-extraction trop agressif (MSRC "Exploited"/"Publicly disclosed")

**Diagnostic confirmé** : les deux champs sont spécifiques à MSRC, pas des sous-champs CVSS.
Vérifié en comparant les 8 champs CVSS de la table MSRC (Attack Vector, Attack Complexity,
Privileges Required, User Interaction, Scope, Confidentiality/Integrity/Availability) aux
champs déjà capturés par `nvd_assertions()` depuis le JSON NVD structuré
(`pipeline_lib.py:179-183` : `attackVector`, `attackComplexity`, `privilegesRequired`,
`userInteraction`, `scope`, `confidentialityImpact`, `integrityImpact`, `availabilityImpact`)
— ce sont exactement les mêmes champs, déjà présents avec une meilleure provenance (JSON
structuré NVD plutôt que texte HTML). Aucune extraction supplémentaire nécessaire pour ces 8
champs. Seuls "Publicly disclosed", "Exploited" et "Exploitability assessment" n'ont aucun
équivalent CVSS structuré — ce sont bien des métadonnées MSRC propres.

**Implémenté** : `msrc_exploitability_assertions()` dans `pipeline_lib.py`, scopée aux pages
`msrc.microsoft.com` par regex exacte sur la séquence de labels ("Publicly disclosed\n(Yes|No)
\nExploited\n(Yes|No)\n..."), routée comme extraction structurée (même mécanisme que
`nvd_assertions()`), et exclue du flux OpenIE via `msrc_exploitability_captured_lines()` (statut
d'audit dédié `captured_by_structured_extraction` plutôt que `skipped`/`no_triples`).

**Preuve avant/après** :

| | Avant | Après |
|---|---|---|
| S39 "Exploited" | `status: skipped, reason: length` | `structured_assertions.json` : `CVE-2026-55040 has MSRC exploited status No` |
| S39 "Publicly disclosed" | `status: no_triples` | `structured_assertions.json` : `CVE-2026-55040 has MSRC publicly disclosed status No` |
| S42 (mêmes champs, CVE-2026-63520) | idem | `CVE-2026-63520 has MSRC exploited status No` / `has MSRC publicly disclosed status No` |
| Canonical KG | absent à tous les niveaux | 6 edges, `domain: CVE`, `range: Value`, decision `accept` (cluster à source unique, sans risque de contamination — voir Correctif 3) |

Le filtre général `is_extractable_sentence()` n'a **pas** été touché — la mission demandait
explicitement de ne pas le relâcher globalement, et le point 1 de l'audit précédent avait déjà
confirmé qu'il élimine correctement le bruit générique (710+544 skips légitimes).

---

## Correctif 2 — Échecs MinIE sur listes à puces et incises

**Cause racine identifiée (commune aux deux sous-cas)** : `sentence_split()` retire la
ponctuation finale de chaque unité via `clean_surface()` avant que `extract_openie()` ne
rejoigne les phrases par `\n` pour former le texte envoyé à MinIE par lot de 8. Test direct
contre le service MinIE en cours d'exécution : un lot de phrases jointes par `\n` **sans**
point final est traité par MinIE comme **une seule phrase continue** (le champ `sentence` de
retour de MinIE fusionne littéralement 4 lignes d'origine en une chaîne unique séparée par
" - "), pas comme des phrases indépendantes délimitées par les retours à la ligne. Restaurer le
point final avant l'envoi (sans toucher au texte stocké dans `evidence`, qui reste
period-less pour préserver l'alignement exact avec le retour MinIE, lui-même
`clean_surface()`-é) corrige ce comportement à la racine.

**Implémenté** : `ensure_terminal_punctuation()`, appliquée uniquement à la construction de
`batch_text` et au fallback single-retry — jamais à `unit["evidence"]` stocké. Vérifié que le
champ `sentence` retourné par MinIE reste bien égal à l'`evidence` stockée (les deux passent
par `clean_surface()`, qui retire le point ajouté), donc l'alignement exact
`fact_sentence == unit["evidence"]` n'est pas cassé.

### a) Incises entre tirets cadratins (S17, correctif testé et validé)

Reproduction exacte du lot réel (8 phrases, phrase Broadcom en position 8/8) :

- **Avant** (period-stripped) : la phrase Broadcom hérite du `sentence` de retour MinIE fusionné
  avec les 7 phrases précédentes du lot ("Top 5 Cybersecurity News Stories... This week's
  Cybersecurity News...") — `align_triple_to_sentence` ne peut pas la rattacher à sa vraie
  phrase, elle apparaît en `no_triples` dans l'audit malgré un triple techniquement généré
  quelque part dans le fatras.
- **Après** (point restauré) : `sentence` retourné par MinIE = *"Broadcom released patches for
  CVE-2026-59310 — a CVSS 9.8 path traversal vulnera..."* — correspond exactement à
  `unit["evidence"]`. Triple obtenu : **`Broadcom | released patches for | CVE-2026-59310`**.
  Statut d'audit passé de `no_triples` à `extracted`.

Recherche d'autres occurrences du même pattern (incise entre tirets cadratins autour d'un fait
CVE) dans le reste du corpus : non systématisée au-delà de ce cas précis — la correction est
générale (elle s'applique à tout le pipeline de batching, pas seulement à cette phrase), donc
tout autre cas similaire bénéficie automatiquement du même correctif sans qu'il ait fallu le
lister nommément.

**Verdict : correctif pleinement fonctionnel pour ce sous-cas.**

### b) Phrase suivie de liste à puces (S40, S41)

Recherche dans tout le corpus du motif "...remediate...\n- KB....." : **seulement 2
occurrences, S40 et S41** (mêmes deux sources déjà identifiées, même gabarit de billet Rapid7 —
pas un pattern récurrent ailleurs).

Test du correctif proposé par la mission ("teste si joindre la phrase d'intro avec chaque item
de liste comme phrase complète") contre le service MinIE réel, deux variantes :
```
"The vendor has provided the following update to remediate CVE-2026-55040: KB5002882 -
Microsoft SharePoint Server Subscription Edition (version 16.0.19725.20434)."
→ vendor | has provided | following update to remediate CVE-2026-55040
  KB5002882 Microsoft SharePoint Server Subscription Edition | is | version QUANT_O_1
  (le KB reste détaché de la relation avec la CVE)

"The vendor has provided the update KB5002882 - Microsoft SharePoint Server Subscription
Edition (version 16.0.19725.20434) to remediate CVE-2026-55040."
→ KB5002882 Microsoft SharePoint Server Subscription Edition | be remediate | CVE-2026-55040
  (lie bien KB et CVE, mais sujet pollué par le nom de produit complet, pas un triple propre)
```
**Verdict : le correctif proposé par la mission ne fonctionne pas de façon fiable — dit
explicitement plutôt que forcé.** Cause : un item de liste seul ("- KB5002882 - Nom produit
(version X)") n'a aucun verbe ; aucune reformulation testée par jointure ne produit un triple
`has_patch(CVE, KB)` propre avec MinIE, avec ou sans point final restauré.

**Action retenue** : extraction structurée dédiée plutôt que réparation de MinIE, même stratégie
que le Correctif 1. Nouvelle fonction `vendor_remediation_kb_assertions()`, scopée par regex
au motif exact "vendor has provided the following update(s) to remediate CVE-X" suivi d'items
`- KB....`, routée comme extraction structurée et exclue du flux OpenIE
(`vendor_remediation_captured_lines()`).

**Preuve avant/après** :

| | Avant | Après |
|---|---|---|
| S40, "The vendor has provided..." | `extracted`, 2 triples garbled : `vendor \| has provided following updates to remediate CVE-2026-55040 KB5002882 \| CVE-2026-55040 here` et `updates \| be remediate \| CVE-2026-55040 KB5002882` (objet contaminé par la liste suivante) | `structured_assertions.json` : 3 triples propres `CVE-2026-55040 has patch KB5002882 - Microsoft SharePoint Server Subscription Edition (version 16.0.19725.20434)` (+ KB5002883, KB5002891) |
| S41, idem pour CVE-2026-63520 | idem (contamination croisée) | 5 triples propres `CVE-2026-63520 has patch KB50028{93,94,96,905,906}...` |
| Canonical KG | 0 edge exploitable pour ces faits | 8 edges `has patch` (structurés) — **actuellement en attente de revue de cluster, voir Correctif 3** |

Note secondaire : même après le fix de ponctuation seul (sans l'extraction structurée dédiée),
la phrase d'intro isolée ("The vendor has provided the following updates to remediate
CVE-2026-55040") n'est plus contaminée par la liste qui suit — elle produit désormais 2 triples
propres mais incomplets (`vendor has provided following updates to remediate CVE-2026-55040` /
`updates be remediate CVE-2026-55040`, sans numéro KB). C'est un progrès réel (fin de la
contamination croisée) mais insuffisant seul pour capturer le fait complet — d'où le besoin de
l'extraction structurée dédiée en complément.

---

## Correctif 3 — Contamination du cluster `added`

**Vérification S45 (Microsoft → added → additional capabilities)** : **ce n'est pas un bug
d'extraction.** Phrase source : *"this is a set of additional capabilities Microsoft added to
the IKE Protocol, including authentication via cryptographically generated addresses..."* — le
triple `(Microsoft, added, additional capabilities)` est une lecture fidèle et correcte de
cette phrase réelle. Il ne s'agit pas d'une segmentation défaillante : c'est un cas de
polysémie légitime — le même lemme "add" dénote deux actions réelles sans rapport (Microsoft
qui ajoute des fonctionnalités à un protocole vs CISA qui ajoute un CVE à un catalogue). Rien à
corriger à la source ; ce triple restera présent, correctement, tant que le clustering se fait
sur la forme de surface du prédicat sans distinguer le sens.

**Élargissement à 2-3 autres clusters de volume similaire** : le même mélange registre
daté/spécifique vs générique/procédural a été recherché dans `publishes` (volume 6),
`be manufactured by` (volume 6), `recommends` (volume 3), `is provided without` (volume 12).

- **`publishes`** : mélange confirmé, même structure que `added` — S19 générique
  ("CISA publishes answers to KEV Status" / "Exploit Automation", texte de directive
  procédurale) coexiste avec S40/S41 datés et spécifiques ("Rapid7 publishes technical
  details for CVE-2026-63520 ahead of schedule") et deux fragments mal résolus (S50/S51,
  sujet "which" non résolu). **Récurrent, pas isolé.**
- **`be manufactured by`**, **`is provided without`** : homogènes (même texte de disclaimer
  Apple dupliqué sur 3 pages quasi identiques S15/S55/S56) — pas de mélange daté/générique ici,
  un problème différent (pages en quasi-doublon) hors du périmètre de ce correctif.
- **`recommends`** : homogène, uniquement générique (S53/S54, même passage SSVC/CISA sur les
  vulnérabilités "Track").

**Conclusion** : le mélange registre daté/générique est confirmé récurrent (au moins 2 clusters
sur 5 examinés), mais **aucune règle systémique n'a été codée dans cette passe**, conformément
à la consigne explicite de ne pas inventer une correction générale à partir d'un ou deux cas.
Le mécanisme de clustering (Jaccard sur les tokens du prédicat de surface) n'a structurellement
aucun signal pour distinguer les deux registres — la distinction repose sur la présence d'une
date + d'un CVE nommé dans la phrase source, un signal absent du clustering actuel. C'est une
décision de conception (faut-il ajouter la spécificité temporelle/nominale comme critère de
séparation ?) qui dépasse le périmètre "corriger 3 problèmes de capture" et reste ouverte.

**État du cluster `added` après re-clustering** (conséquence normale du Correctif 2, qui a fait
apparaître de nouvelles phrases "added" — le cluster a grossi de 6 à 10 membres, son
`cluster_id` a donc changé et sa décision précédente ne s'est pas reportée automatiquement) :

```
added | members: [added, Added, add, adds] | 10 assertions | decision: pending
  S17 minie  CISA -> CVE-2026-59310                (daté, spécifique — nouveau grâce au Correctif 2)
  S17 minie  CISA -> CVE-2026-55040                (daté, spécifique)
  S17 minie  CISA -> CVE-2026-65400                (daté, spécifique — nouveau)
  S17 minie  CISA -> vulnerability to KEV catalogue (générique)
  S38 minie  CISA ADP -> metrics                    (hors sujet)
  S40 minie  CISA -> CVE-2026-55040                (daté, spécifique)
  S41 minie  CISA -> CVE-2026-55040                (daté, spécifique, x2 : "added"/"adds")
  S45 minie  Microsoft -> additional capabilities   (hors sujet, vérifié non-bug ci-dessus)
  S45 minie  Update -> Microsoft statement          (hors sujet, historique de révision de page)
```

**Décision prise : laissé `pending`, non accepté.** Accepter en l'état ferait entrer 3 faits
hors-sujet/génériques dans le canonical KG aux côtés de 5 faits datés fiables. Aucun mécanisme
de "split" automatisé n'existe dans `apply_cluster_validation()` (vérifié dans le code :
seule la décision `"accept"` produit une entrée dans `accepted_relation_mapping.json` ;
`"split"` est un label documenté dans le README mais n'a aucun traitement propre — une vraie
scission demanderait une édition manuelle de `clusters_raw.json`, hors périmètre de cette
passe). Reste en attente de revue humaine, comme les 95 autres clusters pending existants.

**Découverte additionnelle du même type** : le cluster `patch`/`has patch` (mission Correctif 2)
a lui aussi grossi par fusion Jaccard (`has patch` a rejoint un cluster préexistant `patch` /
`patched` / `patching`, 22 membres). Sur ces 22, seuls 10 sont fiables (8 `has patch`
structurés + `Apple patched CVE-2026-65400` (S17) + `Broadcom patched vCenter's Syslog server`
(S44)) ; les 12 autres sont des mésanalyses `heuristic` (fallback regex, sujets tronqués comme
"ations for when agencies must check whet" ou "until an official"). **Également laissé
`pending`**, pour la même raison — accepter en bloc polluerait le canonical KG. Documenté ici
plutôt que forcé.

---

## Synthèse — comparaison globale avant/après (pipeline complet)

| Métrique | Avant (archive) | Après |
|---|---|---|
| `structured_assertions.json` | 259 | 273 (+6 MSRC, +8 vendor-KB) |
| `openie_assertions.json` | 2337 | 4122 |
| Statuts audit — `no_triples` | 2663 | 1709 |
| Statuts audit — `extracted` | 1000 | 1669 |
| Statuts audit — `skipped` | 1407 | 1419 |
| Statuts audit — `failed` (nouveau statut, voir note) | 0 | 273 |
| `open_kg` edges | — | 4395 |
| `canonical_kg` edges | 2407 | 2081 |

**Note sur le nouveau statut `failed` (273 occurrences)** : ce n'est pas une régression.
Avant le correctif, des phrases mal délimitées étaient absorbées dans le parse (faux) d'une
phrase voisine et ressortaient en `no_triples` sans jamais être identifiées individuellement
comme problématiques. Après le correctif, chaque phrase est soumise séparément à MinIE, qui
peut désormais signaler honnêtement (`failedSentences` dans sa réponse) les phrases qu'il ne
sait vraiment pas parser — vérifié sur un échantillon aléatoire de 8 : toutes sont des phrases
syntaxiquement complexes (clauses imbriquées, parenthétiques denses, tournures inhabituelles
comme *"The key question, of course, is did it work?"*), pas des phrases simples qui
fonctionnaient avant. Le fallback heuristique (`heuristic_triples()`) est tenté sur chacune et
échoue aussi à y trouver un motif — d'où le statut `failed` plutôt que `extracted` en secours.

## Réponse directe aux 3 questions du livrable

1. **Nouveaux edges has_patch/workaround pour 55040, 63520, 59310** :
   - CVE-2026-55040 : 8 faits liés au patch (3 `has patch` structurés + 5 nouveaux fragments
     OpenIE `was patched by Microsoft...`/`be remediate` grâce au Correctif 2)
   - CVE-2026-63520 : 6 faits (5 `has patch` structurés + 1 `be remediate`)
   - CVE-2026-59310 : 1 fait (`Broadcom released patches for CVE-2026-59310`, Correctif 2a)
   - **Tous présents dans `openie_assertions.json`/`structured_assertions.json` et dans
     `open_kg`. Dans `canonical_kg` : seuls les 6 faits MSRC sont actuellement promus (cluster
     accepté) ; les 14 faits `has patch`/`patched`/`be remediate` restent en attente de revue
     de cluster (voir Correctif 3).**
2. **Statut d'exploitation par CVE (S39/S42)** : 6 nouveaux edges structurés, tous promus en
   canonical KG (`has MSRC exploited status`, `has MSRC publicly disclosed status`,
   `has MSRC exploitability assessment`, pour CVE-2026-55040 et CVE-2026-63520).
3. **État du cluster `added`** : toujours contaminé après nettoyage (10 membres, 5 datés
   fiables + 2 génériques + 3 hors-sujet dont S45 vérifié non-bug), laissé `pending` par choix
   délibéré plutôt que forcé en `accept`. Confirmé récurrent sur au moins un autre cluster
   (`publishes`).

## Fichiers modifiés

- `extraction_pipeline/scripts/pipeline_lib.py` : `ensure_terminal_punctuation()`,
  `msrc_exploitability_assertions()`, `msrc_exploitability_captured_lines()`,
  `vendor_remediation_kb_assertions()`, `vendor_remediation_captured_lines()` ; branchées dans
  `extract_structured()` et `extract_openie()`.
- `extraction_pipeline/relation_clustering/clusters_validation.json` : 3 clusters MSRC
  passés à `accept` manuellement (justifié ci-dessus, source unique et déterministe).
- Toutes les autres sorties (`data/`, `open_kg/`, `canonical_kg/`, `evaluation/`) régénérées
  par un run complet du pipeline.

## Ce qui reste explicitement en attente de validation humaine

- Décision de split/accept sur les clusters `added` (10 membres) et `patch` (22 membres) —
  aucun mécanisme de split automatisé n'existe actuellement dans le pipeline.
- Décision de conception plus large : faut-il un signal de spécificité temporelle/nominale
  (date + CVE nommé) dans le clustering pour séparer le registre daté du registre générique,
  au-delà de la similarité Jaccard sur le prédicat de surface ? Confirmé récurrent
  (`added`, `publishes`), pas isolé — mais correction systémique explicitement hors périmètre
  de cette passe.
- Le re-clustering déclenché par le Correctif 2 a un effet de bord large : `clusters_validation.json`
  compte maintenant **1168 clusters `pending` sur 2108** (940 `accept`) — contre un total
  d'environ 1401 clusters avant cette passe. Le Correctif 2 a fait apparaître ~1800 nouvelles
  assertions OpenIE (669 phrases nouvellement `extracted` + toutes celles qui ont changé de
  phrase de rattachement), ce qui a fait grossir ou recomposer un grand nombre de clusters
  existants ; comme `cluster_id` est un hash du contenu exact du cluster (`stable_id("rc", *
  relation_raw des membres)`), tout cluster dont la composition a changé — même par l'ajout
  d'un seul membre — obtient un nouvel identifiant et perd la décision `accept`/`reject` qui
  lui avait été attribuée précédemment. Seuls les clusters dont la composition est restée
  strictement identique ont conservé leur décision. Cet effet de bord n'a pas été résorbé dans
  cette passe (seuls les 3 clusters MSRC ont été explicitement re-décidés, cf. ci-dessus) — la
  grande majorité de ces 1168 clusters pending n'a pas été relue et reste hors périmètre des 3
  correctifs demandés.
