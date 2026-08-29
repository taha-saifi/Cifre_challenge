# Vérification par lecture directe des sources — 4 familles ambiguës

Méthode : lecture intégrale de `corpus/clean/S*.json` (`clean_text`) pour chaque source
listée dans la mission, sans passer par un nouveau clustering. Pour chaque famille :
verdict, passage(s) exact(s) cité(s) avec `source_id`, et statut de capture par le
pipeline (canonique / présent mais mal capturé / absent).

Aucune complétion par supposition. Un passage ambigu est cité tel quel.

---

## Famille 1 — Statut de correctif disponible / absent (CVE-2026-55040, CVE-2026-63520, CVE-2026-59310)

**Verdict : l'information existe clairement dans le texte pour les trois CVE.**

- **CVE-2026-55040** — S40 : *"The vendor has provided the following updates to remediate
  CVE-2026-55040.\n- KB5002882 - Microsoft SharePoint Server Subscription Edition (version
  16.0.19725.20434).\n- KB5002883 - Microsoft SharePoint Server 2019 ...\n- KB5002891 -
  Microsoft SharePoint Enterprise Server 2016 ..."*
- **CVE-2026-63520** — S41 : *"The vendor has provided the following updates to remediate
  CVE-2026-63520.\n- KB5002893 - Microsoft SharePoint Server Subscription Edition ...\n-
  KB5002894 / KB5002896 - Microsoft SharePoint Server 2019 ...\n- KB5002905 / KB5002906 -
  Microsoft SharePoint Enterprise Server 2016 ..."*
- **CVE-2026-59310** — S17 : *"Broadcom released patches for CVE-2026-59310 — a CVSS 9.8
  path traversal vulnerability in the Syslog Server component of VMware vCenter — on July
  29, 2026."*

Aucun des trois textes ne mentionne un workaround vendeur distinct du patch pour ces trois
CVE précis (contrairement à CVE-2026-33824, hors périmètre de cette question, où S07 donne
un workaround explicite — voir note en fin de section).

**Capture par le pipeline — mal capturée ou absente, pas par manque d'information source :**

- Les clusters candidats cités dans la mission (`has issued` vol 6, `offer` vol 5,
  `remediates` vol 1) ne contiennent **aucun** des trois faits ci-dessus. Les trois
  proviennent d'une seule et même phrase générique, dupliquée mot pour mot sur plusieurs
  pages MSRC/SSVC : *"Workarounds or hotfixes may offer interim remediation until an
  official patch or upgrade is issued... Official Fix / A complete vendor solution is
  available. Either the vendor has issued an official patch, or an upgrade is available."*
  Cette phrase décrit la métrique CVSS "Remediation Level" en général — ce n'est **pas**
  une affirmation vendeur par CVE. Le sujet OpenIE ("vendor") n'est jamais résolu à
  Microsoft/Broadcom/Apple. `remediates` (S54) vient de la même famille de texte, cette
  fois dans le guide SSVC générique de CISA (`cve_ids: []`), qui définit "Fix" vs
  "Workaround" sans jamais citer de CVE.
- Le fait réel pour CVE-2026-55040 **a été extrait par OpenIE** depuis S40, mais fragmenté
  en deux triples inexploitables tels quels, chacun dans un cluster à occurrence unique
  (donc noyé dans la longue traîne à 866 clusters à 1 membre) :
  - `has provided following updates to remediate CVE-2026-55040 KB5002882` (sujet
    "vendor" → objet "CVE-2026-55040 here")
  - `be remediate` (sujet "updates" → objet "CVE-2026-55040 KB5002882")

  Cause probable : la phrase source est suivie d'une liste à puces (`- KB5002882 - ...`),
  et MinIE segmente mal la frontière entre la phrase et la liste — même classe de problème
  que celui déjà documenté pour le chaînage sur S10 (verbe et objet séparés par une liste).
  Le même mécanisme s'applique très probablement à CVE-2026-63520 sur S41 (non re-vérifié
  triple par triple, mais structure de phrase identique).
- Le fait pour CVE-2026-59310 (Broadcom, patch du 29 juillet) **n'a produit aucun triple du
  tout**. Vérifié dans `data/openie_audit.json` :
  ```
  source_id: S17, chunk_id: S17_C01, sentence_index: 8
  evidence: "Broadcom released patches for CVE-2026-59310 — a CVSS 9.8 path traversal
             vulnerability in the Syslog Server component of VMware vCenter — on July
             29, 2026"
  status: no_triples, backend: minie, batch_rejected_triples: {}
  ```
  MinIE lui-même n'a rien renvoyé pour cette phrase (`batch_rejected_triples` vide — donc
  ce n'est pas un filtre de notre pipeline qui a rejeté un triple, MinIE n'en a produit
  aucun). Cause probable : la double incise entre tirets cadratins ("— a CVSS 9.8 ... —")
  perturbe le parseur de dépendances de MinIE.

**Note hors périmètre (CVE-2026-33824)** : S07 (MSRC, IKE) contient un workaround vendeur
explicite non demandé dans cette question mais utile à signaler : *"Customers who cannot
immediately install the security update can take one of the following actions... Block
inbound traffic on UDP ports 500 and 4500 for systems that do not use IKE... These actions
reduce the attack surface but do not replace installing the security update."* — non
vérifié pour sa capture dans le canonical KG, signalé pour information seulement.

---

## Famille 2 — Statut d'ajout au catalogue KEV

**Verdict : l'information existe clairement et est datée par CVE dans le corpus — mais pas
dans les deux sources demandées (S17, S19) de façon homogène.**

- **S17** contient trois affirmations datées et nommées par CVE, à l'intérieur du cluster
  candidat `added` :
  - *"CISA added CVE-2026-59310 to its Known Exploited Vulnerabilities catalogue on August
    18."*
  - *"CISA added CVE-2026-55040 to the Known Exploited Vulnerabilities catalogue on August
    18, with a remediation deadline of August 21."*
  - *"CISA added CVE-2026-65400 to the Known Exploited Vulnerabilities catalogue on August
    18, rescoring the vulnerability from its initial rating of 7.1 to 9.8 critical
    following confirmation of active exploitation."*
- **S19**, en revanche, ne contient **aucune date d'ajout par CVE**. C'est le texte de la
  directive BOD 26-04 : toutes ses phrases sur le KEV sont génériques et procédurales,
  jamais liées à un CVE précis, par ex. : *"CISA identifies a cybersecurity vulnerability
  by its CVE ID."* et *"if CISA adds a vulnerability to the KEV that was not in the KEV,
  the timeline for action will shorten according to Table 1."* — c'est un fait générique
  sur le fonctionnement du KEV, pas un fait daté.

**Capture par le pipeline — le cluster `added` mélange les deux registres sans les
distinguer :**

```
S17  CISA -> CVE-2026-55040   (daté, spécifique — "on August 18, with a remediation deadline of August 21")
S40  CISA -> CVE-2026-55040   (daté, spécifique — même fait que S17, source différente)
S41  CISA -> CVE-2026-55040   (daté, spécifique — "August 18, 2026: CISA adds ... to its KEV catalog")
S19  CISA -> vulnerability to KEV            (générique, non daté par CVE)
S19  CISA -> vulnerability to KEV Catalog    (générique, non daté par CVE)
S45  Microsoft -> additional capabilities    (hors sujet — ne parle pas du KEV du tout,
                                               décrit des extensions du protocole IKE ;
                                               contamination du cluster, pas un cas KEV)
```

Le cluster `added` (volume 6) contient donc à la fois 3 faits spécifiques et fiables (tous
sur CVE-2026-55040, jamais 59310/65400/33824/63520 malgré leur présence ailleurs dans le
corpus — cf. Famille 4), 2 généralités de S19, et 1 edge hors-sujet (S45). Rien n'a été
fusionné à tort à l'intérieur d'un même cluster de sens contraire ; le problème ici est un
mélange registre générique / registre daté sous un même prédicat de surface identique
("added"), pas une erreur de fusion active/passif.

---

## Famille 3 — Chaînage entre CVE (CVE-2026-55040 / CVE-2026-63520)

**Verdict : l'information existe clairement, dans un seul sens, corroborée par quatre
sources indépendantes. Aucune contradiction de sens trouvée dans le corpus.**

Quatre formulations explicites de chaînage, toutes dans le même sens (55040 = bypass
d'authentification = prérequis ; 63520 = RCE = étape chaînée après/avec 55040) :

- **S41** (Rapid7, page dédiée à 63520) : *"As CVE-2026-63520 can be chained to the
  authentication bypass vulnerability, CVE-2026-55040, the resulting exploit chain allows
  for unauthenticated RCE against a vulnerable server."* — c'est la formulation la plus
  directe et la plus autorisée (Rapid7 est le découvreur des deux CVE). Sujet grammatical :
  CVE-2026-63520 ; verbe : "can be chained to" ; objet : CVE-2026-55040.
- **S09** (Rapid7, analyse technique de 63520) : *"When combined with the authentication
  bypass, CVE-2026-55040, the resulting exploit chain is unauthenticated RCE against a
  vulnerable SharePoint server."*
- **S10** (VulnCheck, analyse indépendante) : *"shipped an exploit last week chaining two
  recently disclosed Microsoft SharePoint CVEs"* (liste CVE-2026-55040 et CVE-2026-63520
  immédiatement après) et plus loin : *"pairing with the CVE-2026-55040 authentication
  bypass, we achieved a fully authenticated deserialization that executes a calc process on
  our vulnerable SharePoint server"* — direction identique : le composant RCE (objet de
  l'article, 63520) est utilisé "avec" 55040.
- **S18** (Help Net Security, cite un tiers) : *"When paired with another vulnerability,
  CVE-2026-63520, CVE-2026-55040 'could lead to unauthenticated remote code execution
  against a vulnerable SharePoint server', according to NHS England Digital."* — formulation
  plus faible (discours rapporté, attribué à NHS England Digital, pas une affirmation
  directe de Rapid7/Microsoft/Help Net Security elle-même) et grammaticalement moins nette
  sur la direction (les deux CVE sont citées côte à côte dans une construction "when paired
  with"). À noter tel quel, sans trancher si cette formulation doit compter au même niveau
  de confiance que S41/S09.

**S40** (Rapid7, page 55040) évoque le chaînage ("this authentication bypass can be
chained to additional vulnerabilities within the authenticated attack surface of the target
site") mais **ne nomme jamais CVE-2026-63520 explicitement** dans le texte — seulement "the
RCE component" / "additional vulnerabilities". Donc S40 seul ne suffit pas à établir la
paire par ID de CVE ; c'est S41/S09/S10/S18 qui le font.

**S08** (Rapid7, analyse technique de 55040) ne mentionne pas CVE-2026-63520 du tout — son
seul usage de "chain" concerne une chaîne interne de quatre faiblesses à l'intérieur de
55040 lui-même ("The root cause is a chain of four distinct weaknesses that, when combined,
allow..."), sans rapport avec le chaînage inter-CVE. Absence normale, pas un signal.

**Capture par le pipeline** : cohérente avec ce qui a déjà été documenté au point 3 de
l'audit précédent — `be chained to` (S41, S40) et `be chained with` (S51, hors sujet ici)
restent deux clusters canoniques séparés, sous le seuil Jaccard de fusion. S09, S10, S18 ne
sont pas représentés du tout dans les clusters `be chained to`/`be chained with` malgré des
formulations explicites — signal supplémentaire que le chaînage 55040/63520 est mieux
attesté dans le texte brut que dans le graphe canonique actuel.

---

## Famille 4 — Statut d'exploitation confirmée

**Verdict : l'information existe clairement, mais le corpus contient deux registres
distincts qui ne se contredisent pas frontalement mais qui se situent à des moments et des
niveaux de confiance différents — à ne pas fusionner en un seul fait "exploité : oui/non".**

**Registre 1 — confirmation officielle CISA (KEV), datée, par lot de CVE :**
- S01 (alerte CISA du 18 août) : *"CISA has added four new vulnerabilities to its Known
  Exploited Vulnerabilities (KEV) Catalog, based on evidence of active exploitation."*
  suivi de la liste des 4 CVE (33824, 55040, 59310, 65400). Affirmation d'exploitation
  active, mais générique au lot des 4, pas détaillée par CVE dans cette phrase précise.
- S17 reprend et détaille par CVE avec des dates d'exploitation observée (voir Famille 1/2) :
  exploitation de 59310 débutée le 3 août ("Exploitation began five days later, on August
  3"), de 55040 "within hours" du PoC public du 13 août, et pour 65400 une confirmation
  néerlandaise (NCSC) datée du 12 août.

**Registre 2 — déclaration MSRC "Exploited" par CVE, au moment de la publication initiale,
qui dit le contraire ou "pas encore" :**
- **S39** (MSRC, CVE-2026-55040) : tableau *"Exploitability assessment... Publicly
  disclosed / No ... Exploited / No"*.
- **S42** (MSRC, CVE-2026-63520) : même tableau, mêmes valeurs, *"Publicly disclosed / No
  ... Exploited / No"*.
- Ces deux valeurs sont explicitement qualifiées dans le texte lui-même : *"The following
  table provides an exploitability assessment for this vulnerability at the time of
  original publication."* — donc "No" documente l'état **au moment de la publication
  initiale** (14 juillet pour 55040, 11 août pour 63520), pas l'état actuel. Ce n'est pas
  une contradiction avec le KEV d'août : ce sont deux instantanés à des dates différentes,
  le texte le dit lui-même. À citer tel quel plutôt qu'à réconcilier.
- **S18** (13 août, avant l'ajout KEV du 18 août) confirme cette lecture temporelle :
  *"Microsoft has yet to confirm the bug has been exploited in the wild, even as it flags
  the flaw as a likely target."* — un troisième point dans le temps, entre le "No" de S39
  (14 juillet) et le KEV du 18 août.

**S07** (CVE-2026-33824) ne contient **pas** le tableau "Exploited / Publicly disclosed"
présent sur S39/S42 — son texte s'arrête après "Report Confidence" et enchaîne directement
sur la section de mitigation. Absence à signaler telle quelle : soit le champ n'existe pas
sur cette page MSRC pour ce CVE, soit il a été perdu en amont (scraping/prétraitement) —
non tranché ici, pas vérifié contre la page source live.

**Capture par le pipeline — absente, pas seulement mal groupée :**

Vérifié dans `data/openie_audit.json` pour S39 et S42 :
```
S39  status: skipped    evidence: "Exploited" (fragment isolé, cellule de tableau)
S39  status: no_triples evidence: "Publicly disclosed"
S42  status: skipped    evidence: "Exploited"
S42  status: no_triples evidence: "Publicly disclosed"
```
Ces deux lignes ne sont **jamais devenues des assertions**, ni structurées ni OpenIE — elles
sont éliminées avant même d'atteindre MinIE (`skipped`), très probablement parce que la
cellule de tableau isolée ("Exploited" seul, sans sujet ni verbe) ne passe pas le filtre de
pré-extraction `is_extractable_sentence()`. Ce n'est donc pas un problème de clustering :
l'information n'existe nulle part dans `openie_assertions.json` ni `canonical_kg/`, alors
que le texte source la porte sans ambiguïté. C'est potentiellement la donnée la plus
directement utile à la décision de priorisation dans toute cette famille (l'éditeur
lui-même affirme "non exploité" au moment de la publication) et elle est absente du graphe
à tous les niveaux.

Les clusters candidats `exploit` (volume 19) et `be exploited` (volume 12) cités dans la
mission sont, comme signalé dans l'inventaire neutre, à 100% `Mention→Mention` : exemples
réels `attacker → vulnerability` (S07), `vulnerability → solely` (S07, S39) — ce dernier est
une mésanalyse MinIE de la phrase "the vulnerability can be exploited solely at the will of
the attacker" (définition CVSS générique de "User Interaction", pas un fait sur le statut
réel d'exploitation). Confirmé : ces deux clusters sont inexploitables tels quels pour cette
question, comme l'inventaire le laissait supposer.

---

## Synthèse — ce qui ressort de cette vérification

| Famille | Info dans le texte | Capturée proprement par le pipeline actuel |
|---|---|---|
| 1. Patch/workaround | Oui, claire, par CVE (S40, S41, S17) | Non — générique dupliquée (clusters candidats) ou fragmentée (S40, singleton) ou totalement absente (S17, `no_triples`) |
| 2. Ajout KEV daté | Oui, claire et datée (S17) ; générique seulement dans S19 | Partiellement — le cluster `added` mélange les deux registres et une contamination hors-sujet (S45) sans les distinguer |
| 3. Chaînage 55040↔63520 | Oui, claire, cohérente sur 4 sources indépendantes (S41, S09, S10, S18) | Partiellement — seuls S41/S40 apparaissent dans les clusters `be chained to`/`with` ; S09/S10/S18 en sont absents malgré des formulations explicites |
| 4. Statut d'exploitation | Oui, mais à deux registres temporels distincts (CISA/KEV vs MSRC "at time of publication") qu'il ne faut pas fusionner naïvement | Non — "Exploited: No/Yes" par CVE (S39, S42) n'existe nulle part dans le graphe, `skipped` avant MinIE ; seul le fait générique et daté par lot (S01) est en théorie capturable via structured_assertions (`cisaExploitAdd`, non re-vérifié ici) |

Aucune correspondance vers un schéma métier n'a été proposée. Ces observations sont des
constats de lecture, pas des décisions de fusion ou de correction de pipeline.
