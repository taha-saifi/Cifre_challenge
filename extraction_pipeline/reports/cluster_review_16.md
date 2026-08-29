# Revue ciblée de 15 clusters prioritaires (added, patch, + 13 à méthode mixte)

Note de comptage : la mission énumère "added, patch + 14 clusters à méthode mixte" pour un
total annoncé de 16 ; la liste nommée dans le message ne contient que 13 noms distincts en
plus de `patch` (déjà l'un des "14 à méthode mixte" dans le rapport précédent) et `added`,
soit **15 clusters distincts au total** — c'est ce qui est couvert ci-dessous, sans qu'aucun
16e candidat n'ait été identifiable dans la liste fournie.

**Aucune décision n'a été appliquée à `clusters_validation.json`.** Tout ce qui suit est une
proposition, y compris les `split_assignments` — à valider avant application.

**Constat transversal, à lire avant le détail par cluster** : le mécanisme de split
(`split_assignments`) agit au niveau de la *phrase membre* (ex. distinguer "has patch" de
"patch"). Pour la majorité de ces 15 clusters, ce n'est **pas le bon niveau de granularité** :
la contamination se trouve *à l'intérieur même* d'une seule phrase (ex. le mot "exploit" sert
aussi bien à un fait réel sur une CVE qu'à une phrase de glossaire CVSS dupliquée sur 4 pages
qu'à un fragment heuristique tronqué) — pas entre phrases différentes du même cluster. Dans ces
cas, un split par phrase ne peut rien isoler proprement ; je le signale explicitement plutôt
que de proposer un split qui donnerait une fausse impression de nettoyage. Seuls **`patch`** et
**`executed`** se sont révélés effectivement séparables par phrase.

---

## 1. `exploit` — 63 assertions, 13 phrases

**Membres** : exploit, exploits, exploited, Exploited, exploiting, Exploit, Exploits, are
exploited, can exploit, could exploit, has exploited, have exploited, is exploiting.

**Exemples représentatifs** :
| Méthode | Source | Subject → Object |
|---|---|---|
| minie | S18 | Attackers → exploit → critical SharePoint flaw |
| minie | S17 | China-Nexus Actor → Exploits → VMware vCenter CVE-2026-59310 |
| minie | S40 | attacker → exploits → CVE-2026-55040 |
| minie | S12 | suspected advanced persistent threat actor → is exploiting → CVE-2026-... |
| minie | S07/S39/S42/S52 | attacker → exploit → vulnerability *(identique, dupliqué sur 4 pages — glossaire CVSS "User Interaction")* |
| heuristic | S41 | "chained together with CVE-2026-5504[0]" → exploit → "chain against SharePoint" *(CVE tronquée)* |
| heuristic | S19 | "Reducing the Significant Risk of Kn[own]" → Exploited → "Vulnerabilities (Nov..." *(mot extrait à l'intérieur du TITRE de BOD 22-01, pas une relation)* |
| heuristic | S47 | "VulnCheck KEV (VulnCheck Known" → Exploited → "Vulnerabilities), Shadow Server..." *(même bug : "Exploited" fait partie du nom propre "Known Exploited Vulnerabilities")* |

**Diagnostic : polysémique + bruit, non séparable par phrase.** Quatre types mélangés sous
les mêmes phrases : (a) faits réels utiles (~12-14, ex. les 4 premiers ci-dessus, plus S57,
S44, S43, S09×2, S20×2), (b) texte de glossaire CVSS/SSVC dupliqué mot pour mot sur 4-6 pages
("attacker exploit vulnerability" répété identique sur S07/S39/S42/S52 ; "Exploit Code
Maturity" sur S50/S52/S54), (c) fragments heuristiques tronqués en milieu de mot, (d)
extractions activement fausses où "Exploited"/"Exploit" est un mot capturé à l'intérieur d'un
nom propre ("Known Exploited Vulnerabilities", "Exploit Code Maturity") sans rapport avec une
relation d'exploitation. Le même mot "Exploited" capitalisé donne un edge faux (S19, S47) alors
que "Exploits" capitalisé donne un edge juste (S17) — la qualité varie *au sein* de chaque
variante de casse/forme, donc `split_assignments` ne peut rien isoler proprement ici.

**Proposition : rejeter le cluster entier.** Pas de split proposé — le mécanisme actuel ne
peut pas séparer (a) de (b)/(c)/(d) puisqu'ils partagent les mêmes phrases exactes. Les faits
listés en (a) restent réels et présents dans `openie_assertions.json`/`open_kg` (rien n'est
perdu à cette couche) ; les récupérer proprement demanderait un filtrage au niveau de
l'assertion individuelle (par ex. sur la longueur/qualité du sujet, ou une liste noire de
textes de glossaire dupliqués), pas une décision de cluster — hors périmètre de cette passe.

---

## 2. `requires` — 39 assertions, 4 phrases

**Membres** : requires, require, does require, Requires.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| minie | S46 | attacker → requires → ability to send specially crafted IKE traffic |
| minie | S18 | equivalent application-layer securi[ty] → requires → authentication |
| minie | S08 | method → requires → non-empty signature |
| heuristic | S50/S51/S52 | "FIRST" → requires → "as a condition of use that any individual or..." *(identique ×3, boilerplate CVSS/FIRST)* |
| minie | S07/S39/S42/S52 | "Such conditions" → require → "collection of more information about target/computat[ional]..." *(identique ×6, glossaire Attack Complexity)* |
| minie | S51 | "Successful exploitation of vulnerab[ility]" → requires → 6 objets différents *(énumération générique CVSS User Interaction, pas de CVE nommée)* |

**Diagnostic : quasi entièrement générique/dupliqué, non séparable par phrase.** Sur 39
assertions, l'écrasante majorité est du texte de spécification CVSS/SSVC/FIRST répété
verbatim sur plusieurs pages. Les 3 faits réels identifiés (S46, S18, S08) sont noyés sous la
même phrase "requires"/"require" que le boilerplate.

**Proposition : rejeter le cluster entier.** Même limite que `exploit` : pas de split
possible. Les 3 faits réels ne sont de toute façon pas au cœur du cas d'usage priorisation
(détails techniques secondaires), leur perte est mineure.

---

## 3. `references` — 24 assertions, 2 phrases

**Membres** : references, reference.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| structured | S02-S06 | CVE-2026-33824/55040/59310/65400/63520 → references → URL *(19 occurrences, une par référence NVD)* |
| minie | S15/S55/S56 | Apple security documents → reference → vulnerabilities *(×3, disclaimer dupliqué mais correct)* |
| minie | S50/S52 | "then resultant CVSS Base [Score/metric val]" → reference → "end game Impact metric value" *(générique CVSS, mais cohérent avec le sens du cluster)* |

**Diagnostic : homogène, un seul sens réel.** 19/24 sont des références NVD structurées de
haute qualité pour les 5 CVE cibles ; les 5 restantes sont de moindre valeur mais ne
contredisent ni ne polluent le sens (toutes décrivent une relation de type "document
référence/couvre X"). Aucune trace de contamination polysémique ou de mésanalyse.

**Proposition : accepter tel quel, sans split.** `canonical_relation`: "references" (déjà la
valeur par défaut).

---

## 4. `contains` — 23 assertions, 3 phrases

**Membres** : contains, contain, contained /.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| minie | S29-S32, S43 | Microsoft IKE Extensions / SharePoint / VMware vCenter / macOS / ESX → contains/contain → *type de faiblesse* vulnerability *(7 occurrences, motif "teaser KEV" propre et homogène)* |
| minie | S51 | Devices → contain → monetary transactional data / PII / business/risk/health decisions *(×5, générique confidentialité Apple, hors sujet priorisation)* |
| minie | S19/S53/S54 | software/vulnerability → contains → vulnerability/specific characteristics *(générique SSVC)* |
| heuristic | S16 | "Session history" → contained / → "only" *(fragment, seule occurrence de cette phrase)* |

**Diagnostic : bruit isolable en partie, mais pas totalement.** Le noyau des 7 faits
"Produit contains Faiblesse" (S29-S32, S43) est propre, homogène et directement utile — mais
il partage la phrase exacte "contains"/"contain" avec le bruit générique et hors-sujet.
Seule la phrase `contained /` (1 occurrence, 100% fragment) est proprement isolable par split.

**Proposition de split (nettoyage partiel seulement, ne résout pas le mélange principal)** :
```json
"split_assignments": {
  "contained /": null
}
```
Avec ce split minimal, "contains"/"contain" resteraient à trancher en bloc (accept = garde le
noyau utile + le bruit générique/hors-sujet ; reject = perd les 7 faits KEV-teaser). Je ne
propose pas de trancher ce choix à ta place — c'est un vrai compromis, pas une évidence comme
pour `patch`.

---

## 5. `patch` — 22 assertions, 4 phrases *(déjà identifié, confirmé séparable)*

**Membres** : patch, has patch, patched, patching.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| structured | S40/S41 | CVE-2026-55040/63520 → has patch → KB50028xx - *nom produit (version)* *(8/8 propres)* |
| minie | S17 | Apple → patched → CVE-2026-65400 |
| minie | S44 | Broadcom → patched → vCenter's Syslog server |
| heuristic | S10 | "When we examined the decompiled" → patched → "code, we found that the new validation function was bei[ng]..." *(fragment)* |
| heuristic | S07/S39/S42/S52 | "Workarounds or hotfixes may offer i[nterim]" → patch → "or upgrade is issued" *(×4, identique, glossaire CVSS Remediation Level)* |
| heuristic | S01/S28 | "ations for when agencies must check whet[her]" → patch → "was applied" *(×2, fragment BOD 26-04)* |
| heuristic | S17/S45 | fragments divers, tous tronqués ou hors-sujet |

**Diagnostic : polysémique, mais séparable par phrase.** Contrairement aux clusters
précédents : "has patch" = 8/8 propres (structuré) ; "patched" = 2/3 propres (S17, S44) + 1
fragment (S10) ; "patch" = 0/9 exploitable (100% générique dupliqué ou fragments) ;
"patching" = 0/2 (fragments).

**Proposition de split** :
```json
"split_assignments": {
  "has patch": "has patch",
  "patched": "has patch",
  "patch": null,
  "patching": null
}
```
Résultat : 10 edges propres (`CVE has patch Advisory/Vendor`) sous une étiquette unique,
11 rejetés. Le seul flottement est le fragment S10 sous "patched" (1/3 de cette phrase) —
accepté ici parce que 2/3 de la phrase est solide et que ce fragment n'est pas *faux*, juste
peu informatif, pas un risque de contresens comme dans `exploit`.

---

## 6. `allows` — 21 assertions, 3 phrases

**Membres** : allows, allow, has allowed.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| minie | S17 | exploit → allows → unauthenticated attacker with network access... |
| minie | S18/S39 | vulnerability → allows → impersonation *(même fait, deux sources — normal, pas une contamination)* |
| minie | S51 | vulnerability → allows → unauthenticated remote code execution / command injection |
| minie | S31 | path traversal vulnerability → allow → threat actor *(tronqué mais réel)* |
| minie | S53 | CISA SSVC Calculator → allows → users ; Implementing SSVC → has allowed → CISA |
| heuristic | S51 | 2 fragments (données d'authentification, tronqués) |
| minie | S51 | "Providing small change based on met[rics]" → allows → "slightly-more-severe metric strings" *(méthodologie CVSS, pas un fait CVE)* |

**Diagnostic : cas le plus proche d'un compromis parmi les "non séparables".** Proportion de
faits réels plus élevée qu'`exploit`/`requires` (~8-9/21, contre CVSS/SSVC générique et
fragments pour le reste) — mais toujours mélangée à l'intérieur des mêmes phrases
"allows"/"allow" (S17/S18/S39/S51-RCE d'un côté, fragments et méthodologie CVSS de l'autre,
tous sous "allows").

**Proposition : rejeter le cluster entier, mais signalé comme le compromis le plus serré du
lot.** Pas de split possible pour la même raison structurelle que `exploit`. Si tu préfères
accepter malgré le bruit résiduel (~40% de contenu générique/fragmentaire), c'est une
alternative défendable ici plus que pour `exploit`/`requires` — à ton appréciation.

---

## 7. `is required` — 19 assertions, 3 phrases

**Membres** : is required, Required, required.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| heuristic | S07/S39/S42/S50/S52 | "If a specific configuration" → is required → "for an attack to succeed..." *(×5, quasi identique, glossaire Attack Complexity)* |
| minie | S50/S51/S52 | "Membership in FIRST" → is required → "implement" *(×3, identique, boilerplate FIRST)* |
| heuristic | S50/S52 | "Privileges" → Required → "is usually None for hard-coded credential vuln..." *(×2, glossaire Privileges Required)* |
| minie | S46 | IKE → is required → 4500 *(fragment de port réseau, peu exploitable tel quel)* |

**Diagnostic : quasi 100% générique/dupliqué.** Aucun fait CVE-spécifique propre identifié.
Cas le plus simple du lot.

**Proposition : rejeter le cluster entier.** Pas de split nécessaire — rien à en sauver.

---

## 8. `used` — 18 assertions, 3 phrases

**Membres** : used, is used, are using.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| heuristic | S50/S51/S52 | "that CVSS is owned by FIRST and" → used → "by permission" *(×3, identique, mention légale FIRST)* |
| minie | S11/S45 | attackers → are using → valid credentials *(×2, plausible mais sans CVE nommée)* |
| minie | S45 | IKE → is used → known peer addresses |
| heuristic | divers | fragments tronqués (S10, S47, S50×3, S51×3, S52×2) |

**Diagnostic : quasi entièrement générique/fragmentaire, aucun fait CVE-spécifique solide.**

**Proposition : rejeter le cluster entier.**

---

## 9. `affect` — 17 assertions, 7 phrases

**Membres** : affect, affected, affects, can affect, do affect, does affect, is affected.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| minie | S50/S52 | Characteristics → affect → Exploitability/Impact/Scope *(×6, glossaire CVSS)* |
| minie | S51 | vulnerability → affects → multiple product versions/platforms/operating systems *(×3, plausible mais sans CVE nommée — et redondant avec `has affected product`/`has affected version bound`, déjà acceptés côté structuré)* |
| heuristic | divers | fragments tronqués |

**Diagnostic : générique, et la portion la plus solide est redondante avec des faits
structurés déjà propres et acceptés** (`has affected product`, `has affected version bound` —
confirmés `accept` dans `clusters_validation.json`). Rien d'unique à préserver ici.

**Proposition : rejeter le cluster entier.**

---

## 10. `publish` — 15 assertions, 6 phrases

**Membres** : publish, publishing, published, are published, are publishing, has published.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| minie | S12 | Broadcom → published → VMSA-2026 *(seul fait vraiment utile du cluster — identifiant d'advisory non capturé ailleurs à ma connaissance)* |
| minie | S47/S48 | Scores → published → freely *(×2, fragment EPSS)* |
| minie | S08 | we → are publishing → technical analysis of vulnerability along wit[h]... *(plausible mais vague)* |
| heuristic | S50/S52/S53 | fragments génériques (CVSS/FIRST, notifications SSVC) |
| minie | S19/S38 | CISA/CNA → publish/has published → data requirements/data *(générique, procédural)* |

**Diagnostic : faible valeur globale, un seul fait notable (S12) noyé sous la même phrase
"published" que 2 fragments faibles.** Pas séparable proprement (S12 partage "published" avec
S47/S48).

**Proposition : rejeter le cluster entier**, en signalant que le fait S12 (Broadcom →
VMSA-2026) est une perte mineure mais réelle — à recapturer manuellement hors clustering si tu
juges l'identifiant d'advisory VMSA-2026-0006 utile pour le cas d'usage (non vérifié ici s'il
est déjà présent ailleurs sous une autre forme).

---

## 11. `cause` — 12 assertions, 2 phrases

**Membres** : cause, causes.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| heuristic | S07/S39/S42/S52 | "but the root" → cause → "may not be known" *(×4, identique, glossaire Report Confidence)* |
| heuristic | S17 | "The" → cause → "is insufficient error checking in the process..." *(réel mais concerne CVE-2026-20349 Cisco, hors des 5 CVE cibles du challenge)* |
| minie | S07/S42 | repeated exploitation → causes → service *(×2, tronqué — probablement "...service unavailable")* |
| minie | S51 | fragments méthodologie CVSS (Repudiation Impact) |

**Diagnostic : majoritairement dupliqué/générique**, avec un fait réel mais hors périmètre
(S17, CVE-2026-20349) et des fragments tronqués sans valeur autonome.

**Proposition : rejeter le cluster entier.**

---

## 12. `provided` — 10 assertions, 3 phrases

**Membres** : provided, has provided, is provided.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| minie | S40/S41 | vendor → has provided → following updates to remediate CVE-2026-55040/63520 *(même fait déjà capturé proprement via l'extraction structurée dédiée — Correctif 2 de la mission précédente ; version ici de moindre qualité, doublon)* |
| heuristic | S07/S39/S42 | "The information" → provided → 'in the Microsoft Knowledge Base is provided "...' *(×3, identique, disclaimer légal Microsoft)* |
| minie | S01/S28 | product → is provided → subject to Notification *(×2, mention légale CISA)* |
| minie | S16 | Hermes Agent → provided → orchestration *(hors contexte, sens peu clair)* |
| heuristic | S10 | 2 fragments tronqués |

**Diagnostic : soit doublon de moindre qualité d'un fait déjà mieux capturé ailleurs, soit
boilerplate légal, soit hors contexte.** Rien d'unique à préserver.

**Proposition : rejeter le cluster entier.**

---

## 13. `added` — 10 assertions, 4 phrases

**Membres** : added, Added, add, adds.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| minie | S17 | CISA → added → CVE-2026-59310 / CVE-2026-55040 / CVE-2026-65400 *(3 faits datés, réels)* |
| minie | S40/S41 | CISA → added/adds → CVE-2026-55040 *(2 faits datés, réels — doublons de la même info que S17)* |
| minie | S17 | CISA → added → "vulnerability to Known Exploited Vulnerabilities catalo[gue]" *(générique, pas de CVE nommée — sous la MÊME phrase "added" que les faits datés ci-dessus)* |
| minie | S45 | Microsoft → added → additional capabilities *(hors sujet, vérifié non-bug dans le rapport précédent — polysémie légitime du verbe)* |
| minie | S45 | Update → Added → Microsoft statement *(historique de révision de page, hors sujet)* |
| minie | S38 | CISA ADP → add → metrics *(ambigu, probablement plausible mais vague)* |

**Diagnostic révisé par rapport au rapport précédent — non séparable par phrase en réalité.**
En relisant ligne par ligne (pas seulement par regroupement de phrase) : le générique
("vulnerability to KEV catalogue") ET l'hors-sujet (S45) partagent tous deux la phrase "added"
avec les faits datés valides — donc, contrairement à ce que le rapport précédent laissait
supposer, `split_assignments` ne peut pas isoler proprement les 5 bons faits des 2 mauvais à
l'intérieur de "added" lui-même.

**Mais un fait plus important change la recommandation** : les 5 faits datés utiles ("CISA a
ajouté CVE-X au KEV") sont **entièrement redondants** avec un prédicat structuré déjà propre
et déjà accepté — `has CISA exploit addition date`, dérivé du champ NVD `cisaExploitAdd`,
vérifié couvrant exactement CVE-2026-33824/55040/59310/65400 (toutes datées 2026-08-18) :
```
S02 CVE-2026-33824 -> 2026-08-18
S03 CVE-2026-55040 -> 2026-08-18
S04 CVE-2026-59310 -> 2026-08-18
S05 CVE-2026-65400 -> 2026-08-18
```
(cluster `has CISA exploit addition date` : `decision: accept`, `review_status: confirmed`,
déjà dans le canonical KG.)

**Proposition : rejeter le cluster entier.** Contrairement à `patch`, ce n'est pas un
compromis — l'information utile existe déjà ailleurs, plus proprement, donc rien n'est perdu
en rejetant `added` en bloc.

---

## 14. `included` — 6 assertions, 2 phrases

**Membres** : included, is included.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| minie | S50 | "evasion of authentication mechanism" / "satisfaction" / "evasion of requisites" → is included → "is not considered here" *(×3, glossaire CVSS, formulation même bizarre en sortie — sujet et objet quasi identiques, mésanalyse probable)* |
| minie | S10 | payload → included → simply launches calc *(mineur mais correct, détail technique S10)* |
| heuristic | S10 | 2 fragments tronqués |

**Diagnostic : faible volume, faible valeur, rien de CVE-spécifique solide.**

**Proposition : rejeter le cluster entier.** Perte négligeable (1 détail technique mineur).

---

## 15. `executed` — 6 assertions, 3 phrases

**Membres** : executed, executing, is executed.

**Exemples** :
| Méthode | Source | Subject → Object |
|---|---|---|
| minie | S41 | attacker's arbitrary code → is executed → account running SharePoint Site instance *(seul membre de la phrase "is executed" — réel, technique, sur CVE-2026-63520)* |
| minie | S16 | system → executed → hundreds of hours of manual targeting analysis *(×2, doublon, sens douteux — probablement une inversion sujet/objet de MinIE)* |
| heuristic | S10 | 2 fragments identiques tronqués |
| heuristic | S16 | 1 fragment |

**Diagnostic : séparable par phrase, comme `patch`.** "is executed" = 1/1 propre (S41) ;
"executed"/"executing" = 0/5 exploitable.

**Proposition de split** :
```json
"split_assignments": {
  "is executed": "is executed",
  "executed": null,
  "executing": null
}
```
Résultat : 1 edge propre conservé (contexte de privilège d'exécution pour CVE-2026-63520), 5
rejetés.

---

## Récapitulatif

| Cluster | Volume | Diagnostic | Proposition |
|---|---:|---|---|
| exploit | 63 | polysémique, non séparable | reject entier |
| requires | 39 | générique/dupliqué, non séparable | reject entier |
| references | 24 | homogène | **accept tel quel** |
| contains | 23 | bruit partiellement isolable | split partiel (`contained /` → null) ; "contains"/"contain" à trancher en bloc |
| patch | 22 | polysémique, séparable | **split proposé** (has patch + patched → "has patch" ; patch, patching → null) |
| allows | 21 | non séparable, compromis le plus serré | reject entier (alternative : accept avec bruit résiduel) |
| is required | 19 | générique/dupliqué | reject entier |
| used | 18 | générique/dupliqué | reject entier |
| affect | 17 | générique, redondant avec structuré déjà accepté | reject entier |
| publish | 15 | faible valeur, 1 fait notable non isolable | reject entier |
| cause | 12 | générique/dupliqué | reject entier |
| provided | 10 | doublon de moindre qualité ou boilerplate | reject entier |
| added | 10 | polysémique, redondant avec structuré déjà accepté | reject entier |
| included | 6 | faible volume/valeur | reject entier |
| executed | 6 | séparable | **split proposé** (is executed → accept ; executed, executing → null) |

**Sur 15 clusters** : 1 accept direct (`references`), 2 splits proposés (`patch`, `executed`),
1 split partiel + décision en attente (`contains`), 11 rejets proposés (dont 2 — `affect` et
`added` — parce que leur contenu utile est déjà couvert ailleurs par des faits structurés
propres, pas seulement parce qu'ils sont bruités).

Rien n'a été appliqué. En chemin, aucun autre cluster parmi les 1168 `new` n'a été touché ni
inspecté au-delà de ces 15 — comme demandé.
