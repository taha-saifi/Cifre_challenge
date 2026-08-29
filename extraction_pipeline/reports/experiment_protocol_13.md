# Protocole expérimental §13 — 5 configurations × 2 tâches

**Consignation brute uniquement — aucune interprétation.** L'analyse vient au bloc suivant.

10 appels exécutés, un seul par cellule, aucun retry. Le prompt de décision est mot pour mot
identique dans les 5 configurations pour une même tâche (voir §"Prompts exacts"). Chaque
appel a été exécuté par un agent isolé (aucune mémoire de cette conversation, aucune
connaissance du protocole expérimental, aucune instruction autre que : lire le fichier de
contexte indiqué le cas échéant, puis répondre à la question). Aucune règle écrite à la main
n'intervient dans la décision — chaque cellule est une réponse LLM libre.

Contextes exacts envoyés : `extraction_pipeline/reports/experiment_contexts/ctx_*.txt` (10
fichiers, copie conforme de ce qui a été lu par chaque agent).

---

## Prompts exacts (identiques dans les 5 configs, par tâche)

**Tâche A** : *"Étant donné les informations disponibles sur CVE-2026-55040 et
CVE-2026-63520, si l'équipe ne peut appliquer qu'un seul correctif cette semaine, lequel
prioriser, et pourquoi ? Formule ta réponse en une décision claire (lequel patcher en
premier) suivie de ta justification."*

**Tâche B** : *"Étant donné les informations disponibles sur CVE-2026-33824 et l'actif qui
l'exécute, ce correctif doit-il être traité en urgence cette semaine ou peut-il attendre le
prochain cycle de maintenance standard ? Formule ta réponse en une décision claire suivie de
ta justification."*

## Construction du contexte par configuration

- **Config 1 (LLM seul)** : aucun contexte, uniquement le prompt ci-dessus.
- **Config 4 (KG-aware complet)** : sous-graphe extrait de `canonical_kg/edges.json` actuel
  (2123 edges), filtré aux edges dont le sujet ou l'objet contient une des CVE concernées —
  104 triples pour la tâche A, 54 pour la tâche B. Tâche B augmentée d'une phrase de scénario
  marquée `[Scénario expérimental, non issu du corpus]` (voir note ci-dessous).
- **Config 5 (KG incomplet)** : identique à la config 4, moins l'information ciblée par la
  mission — tâche A : les 2 edges portant explicitement la relation de chaînage entre les deux
  CVE (`be chained to` source S41, et l'edge direct S18 reliant les deux CVE) ; tâche B : la
  phrase de scénario sur l'exposition de l'actif, retirée.
- **Config 7 (KG pré-validation)** : même construction que la config 4, mais depuis
  `archive/pre_final_dedup_20260829T011315/` (état du canonical KG avant les 3 dernières
  passes de validation/dédup/split — donc avec le bruit et la contamination
  `added`/`patch`/etc. encore présents, et sans les faits propres ajoutés depuis
  `references`/`has patch`/`has technical impact`/etc.) — 89 triples pour la tâche A, 50 pour
  la tâche B (moins de triples qu'en config 4 car les faits `has patch`, `references`, `has
  technical impact` n'existaient pas encore à cette date).
- **Config 8 (KG incomplet + signalement)** : identique à la config 5, plus une phrase de
  note explicite signalant l'incertitude sur l'information manquante.

**Note sur le gap Asset/exposition (tâche B)** : le canonical KG n'a jamais eu de couche
Asset/has_exposure (prévue dans l'autre pipeline `kg/regex`+`kg/llm`, resté en pause) — aucune
source du corpus ne documente un actif client concret exposé à internet. Sur ta décision, la
phrase de scénario suivante a été ajoutée aux configs 4 et 7 (retirée en 5 et 8), marquée comme
non issue du corpus : *"[Scénario expérimental, non issu du corpus] L'actif exécutant
CVE-2026-33824 est un serveur Windows exposé publiquement sur internet sur les ports IKE (UDP
500 et 4500)."*

**Phrase de signalement ajoutée en config 8** :
- Tâche A : *"Note : une relation potentielle entre CVE-2026-55040 et CVE-2026-63520 n'a pas
  pu être confirmée avec certitude dans les sources disponibles."*
- Tâche B : *"Note : une information potentielle concernant l'exposition de l'actif exécutant
  CVE-2026-33824 n'a pas pu être confirmée avec certitude dans les sources disponibles."*

---

## Tableau brut des décisions

| Config | Tâche A — CVE priorisée | Tâche B — urgence |
|---|---|---|
| 1 — LLM seul | **CVE-2026-63520** | **Indécis, par défaut "urgent jusqu'à vérification"** |
| 4 — KG complet | **CVE-2026-55040** | **Urgent** |
| 5 — KG incomplet | **CVE-2026-55040** | **Urgent** |
| 7 — KG pré-validation | **CVE-2026-55040** | **Urgent** |
| 8 — KG incomplet + signalement | **CVE-2026-55040** | **Urgent** |

---

## Observation méthodologique à consigner (pas une interprétation, un fait de construction)

Pour la tâche A, la config 5 retire les 2 edges portant littéralement une relation de
chaînage (`be chained to`, et l'edge direct S18 reliant les deux CVE). Mais le sous-graphe
contient d'autres edges, non ciblés par le retrait demandé, qui véhiculent la même information
de chaînage sous une autre étiquette de relation — notamment `break` (*"Patching CVE-2026-55040
break exploit chain"*, source S40) et `we achieved` (*"pairing with CVE-2026-55040
authentication bypass... fully authenticated deserialization"*, source S10). Les 4 réponses
KG-aware (config 4, 5, 7, 8) citent explicitement ce fait `break` comme élément de
justification, y compris en config 5/8 où le retrait était censé priver le modèle de
l'information de chaînage. Ceci est documenté ici tel quel, sans jugement sur son impact —
l'analyse de ce que cela signifie pour la comparaison config 4 vs config 5 revient au bloc
suivant.

---

## Annexe — réponses complètes

### Tâche A — Config 1 (LLM seul)

> Décision : patcher en priorité **CVE-2026-63520** cette semaine.
>
> Justification : en l'absence de détails techniques précis fournis pour ces deux CVE dans le
> message, la priorisation doit s'appuyer sur les principes standards de gestion des
> vulnérabilités (CVSS, exploitabilité, exposition) :
>
> - Le numéro d'identifiant plus élevé (63520 vs 55040) suggère généralement une divulgation
>   plus récente, ce qui est souvent corrélé à une fenêtre d'exploitation active plus courte et
>   à une attention accrue de la part des attaquants opportunistes qui scannent les CVE
>   fraîchement publiées avant que les correctifs ne soient largement déployés.
> - Une vulnérabilité récemment divulguée présente typiquement un risque plus élevé à court
>   terme car les preuves de concept (PoC) circulent rapidement après publication, alors qu'une
>   CVE plus ancienne a déjà eu le temps d'être corrigée, contournée par des mesures
>   compensatoires, ou son exploitation active s'est déjà stabilisée voire réduite.
> - En situation de ressource limitée (un seul correctif possible), le principe de base est de
>   traiter en priorité la vulnérabilité dont la fenêtre de risque est la plus critique et la
>   moins encore mitigée, ce qui favorise généralement la CVE la plus récente sauf si l'ancienne
>   présente un score de sévérité (CVSS) nettement supérieur ou une exploitation active
>   confirmée en conditions réelles (KEV).
>
> Recommandation pratique : avant d'exécuter cette décision, vérifier les scores CVSS
> respectifs, la présence dans le catalogue CISA KEV (Known Exploited Vulnerabilities), et
> l'exposition réelle de vos systèmes (surface d'attaque accessible depuis Internet, criticité
> des actifs concernés) — ces trois facteurs doivent primer sur la simple numérotation si les
> données sont disponibles.

### Tâche A — Config 4 (KG complet actuel)

> **Décision : patcher CVE-2026-55040 en premier.**
>
> **Justification :**
>
> - **Exploitation active et confirmée** : CVE-2026-55040 est marquée `has_SSVC_exploitation
>   active` et figure au catalogue CISA KEV (ajoutée le 2026-08-18, échéance d'action le
>   2026-08-21, déjà dépassée). À l'inverse, CVE-2026-63520 est `has_SSVC_exploitation none`.
> - **Exploit public disponible et utilisé en conditions réelles** : un PoC a été publié par
>   Stephen Fewer (Rapid7), et la société Defused a signalé que ce PoC est déjà utilisé contre
>   des honeypots SharePoint.
> - **Score EPSS bien plus élevé** : 0.3965 (39,7 % de probabilité d'exploitation, percentile
>   0.986) pour CVE-2026-55040, contre seulement 0.0289 (2,9 %, percentile 0.859) pour
>   CVE-2026-63520 — un facteur ~14x.
> - **Barrière d'exploitation quasi nulle** : contournement d'authentification, sans privilège
>   ni interaction utilisateur, complexité d'attaque faible (AC:L), automatisable
>   (`has_SSVC_automatable yes`), alors que CVE-2026-63520 requiert une complexité d'attaque
>   élevée (AC:H) et n'est pas automatisable.
> - **Effet de rupture de chaîne d'attaque** : les données indiquent explicitement que
>   CVE-2026-55040 (bypass d'authentification) est utilisée pour chaîner vers CVE-2026-63520
>   (désérialisation / exécution de code), aboutissant à une RCE non authentifiée complète.
>   Patcher CVE-2026-55040 « break exploit chain » (source S40) — cela neutralise donc aussi le
>   vecteur d'accès nécessaire pour exploiter CVE-2026-63520, réduisant le risque global même
>   sans corriger cette dernière immédiatement.
>
> En résumé : bien que CVE-2026-63520 ait un impact technique tout aussi total et un score CVSS
> élevé (8.1 vs 9.1), c'est CVE-2026-55040 qui est activement exploitée dans la nature,
> référencée au KEV avec échéance dépassée, et constitue le maillon d'entrée de la chaîne
> d'attaque combinée. La corriger en premier est à la fois la priorité réglementaire (BOD 26-04
> / CISA) et la mesure la plus efficace pour couper court à l'ensemble du scénario d'attaque.

### Tâche A — Config 5 (KG incomplet)

> **Décision : patcher CVE-2026-55040 en premier.**
>
> **Justification :**
>
> - **Exploitation active et confirmée** : le KG indique `has_SSVC_exploitation active` pour
>   CVE-2026-55040, avec un PoC public déjà en circulation (Rapid7/Stephen Fewer) et des
>   observations d'attaques réelles contre des honeypots SharePoint (« Defused » [source: S18]).
>   CVE-2026-63520, à l'inverse, a `has_SSVC_exploitation none` : aucune exploitation observée.
> - **Inscrite au catalogue CISA KEV avec échéance dépassée** : CVE-2026-55040 a une
>   `has_CISA_action_due_date` au 2026-08-21, déjà passée à la date actuelle (2026-08-29) —
>   l'obligation de remédiation est en retard. CVE-2026-63520 n'apparaît dans aucune entrée CISA
>   KEV dans les données disponibles.
> - **Score EPSS nettement supérieur** : la probabilité d'exploitation dans les 30 jours est de
>   0,397 (39,7 %, percentile 0,986) pour CVE-2026-55040, contre seulement 0,029 (2,9 %) pour
>   CVE-2026-63520, malgré un percentile proche (0,859). L'écart de probabilité brute est
>   déterminant.
> - **Gravité de l'impact et accessibilité de l'attaque** : CVE-2026-55040 a une complexité
>   d'attaque FAIBLE (`AC:L`) contre ÉLEVÉE (`AC:H`) pour CVE-2026-63520, ce qui la rend beaucoup
>   plus facile à exploiter en pratique, malgré un score de base légèrement inférieur (9,1 contre
>   8,1).
> - **Effet de chaîne** : selon les sources S10, CVE-2026-55040 (contournement d'authentification
>   par forgeage de JWT) combinée à une faille de type CVE-2026-63520 permettrait une
>   désérialisation authentifiée complète, menant à une exécution de code à distance. Patcher
>   CVE-2026-55040 « brise la chaîne d'exploitation » (`Patching CVE-2026-55040 break exploit
>   chain` [source: S40]), neutralisant ainsi une grande partie du risque combiné même sans
>   corriger immédiatement l'autre CVE.
>
> En résumé : CVE-2026-55040 combine exploitation active confirmée sur le terrain, échéance
> CISA déjà dépassée, score EPSS bien plus élevé, complexité d'attaque plus faible, et rôle de
> maillon initial dans une chaîne d'exploitation plus large — elle doit donc être corrigée en
> priorité cette semaine.

### Tâche A — Config 7 (KG pré-validation)

> **Décision : patcher CVE-2026-55040 en premier.**
>
> **Justification :**
>
> - **Exploitation active confirmée, pas seulement théorique** : CVE-2026-55040 a un
>   `SSVC_exploitation = active` et figure au catalogue KEV de la CISA (ajout le 2026-08-18,
>   échéance d'action au 2026-08-21, déjà dépassée) — contrairement à CVE-2026-63520 dont
>   `SSVC_exploitation = none`.
> - **EPSS radicalement plus élevé** : probabilité d'exploitation de 39,65 % pour CVE-2026-55040
>   contre seulement 2,89 % pour CVE-2026-63520 (observations du 2026-08-28), un écart de plus
>   d'un facteur 13.
> - **PoC public et automatisable** : Rapid7 (Stephen Fewer) a publié un PoC exploitable pour
>   CVE-2026-55040, `SSVC_automatable = yes`, et la firme Defused signale des attaques réelles
>   utilisant ce PoC contre des honeypots SharePoint — la menace est donc déjà en cours
>   d'exploitation dans la nature.
> - **Vecteur sans authentification, faible complexité** : score CVSS de 9,1 (CRITIQUE), AC:L,
>   PR:N, UI:N — un attaquant non authentifié peut agir immédiatement en tant qu'utilisateur du
>   site SharePoint, voire administrateur.
> - **C'est le maillon qui permet la chaîne complète** : les sources indiquent explicitement que
>   CVE-2026-55040 (bypass d'authentification) se combine avec CVE-2026-63520
>   (désérialisation/exécution de code) pour obtenir une exécution de code à distance non
>   authentifiée complète. Or corriger CVE-2026-55040 « brise la chaîne d'exploitation » (source
>   S40) : sans le bypass d'authentification initial, CVE-2026-63520 — qui exige de toute façon
>   une complexité d'attaque élevée (AC:H) et n'est pas activement exploitée seule — devient
>   beaucoup plus difficile à atteindre.
>
> En résumé, CVE-2026-55040 est le point d'entrée activement exploité, sous exigence CISA
> dépassée, avec PoC public en circulation ; le patcher en priorité neutralise à la fois le
> risque immédiat le plus élevé et casse la chaîne d'attaque combinée avec CVE-2026-63520.

### Tâche A — Config 8 (KG incomplet + signalement)

> Priorité : patcher CVE-2026-55040 en premier, avant CVE-2026-63520.
>
> Justification : CVE-2026-55040 est déjà exploité activement dans la nature (statut SSVC «
> exploitation: active », ajout au catalogue KEV de la CISA le 2026-08-18 avec échéance d'action
> au 2026-08-21, désormais dépassée), avec un PoC public (Rapid7/Stephen Fewer) réutilisé par des
> attaquants contre des honeypots SharePoint. Son score EPSS est très élevé (39,65 %, percentile
> 98,6 %), contre seulement 2,9 % (percentile 85,9 %) pour CVE-2026-63520, dont l'exploitation
> est classée « none » en SSVC. CVE-2026-55040 est aussi trivialement exploitable (AC:L, PR:N,
> UI:N, score CVSS 9.1/CRITICAL) et permet un contournement d'authentification complet (forge de
> jetons JWT) donnant des accès jusqu'au niveau administrateur — une faille qui, de plus, sert de
> brique d'entrée à une chaîne d'exploitation : les sources indiquent explicitement que la
> combiner avec une faille de type CVE-2026-63520 permettrait d'obtenir une désérialisation
> authentifiée complète, et que corriger CVE-2026-55040 « casse la chaîne d'exploitation »
> (source S40). CVE-2026-63520, bien que de sévérité HIGH (8.1) avec un impact potentiellement
> plus large (disponibilité aussi touchée), a une complexité d'attaque élevée (AC:H), n'est pas
> connue comme activement exploitée, et son urgence est donc nettement moindre cette semaine.

### Tâche B — Config 1 (LLM seul)

> **Décision : impossible de trancher sur cette base — traiter par défaut comme urgent jusqu'à
> vérification, sans engager de correctif immédiat aveugle.**
>
> **Justification :**
>
> Aucune information concrète sur CVE-2026-33824 ni sur l'actif concerné n'a été fournie dans le
> message (pas de score CVSS, pas de vecteur d'attaque, pas d'exploitabilité connue, pas de
> description de l'actif — exposition internet ou réseau interne, criticité métier, données
> traitées, présence de mesures compensatoires comme WAF/segmentation). Je ne dispose pas non
> plus, dans mes connaissances générales, d'un enregistrement fiable pour cet identifiant CVE
> précis (numérotation 2026, donc très récente ou hors de mes données d'entraînement fiables).
> Répondre « urgence cette semaine » ou « cycle standard » sans ces éléments reviendrait à
> deviner.
>
> Ma recommandation opérationnelle, en l'absence de ces données :
>
> 1. **Traiter par défaut en urgence (patch cette semaine)** si l'un des critères suivants est
>    vrai — ce qui est la posture de prudence standard tant que l'évaluation n'est pas faite :
>    CVSS ≥ 7 (High/Critical), exploit public ou exploitation active (EPSS élevé / présence KEV),
>    actif exposé à internet ou accessible depuis une zone à faible confiance, ou actif critique
>    pour le métier (production, données sensibles, PII/PCI).
> 2. **Peut attendre le cycle standard** uniquement si l'analyse confirme : sévérité
>    faible/moyenne, absence d'exploit connu, actif isolé/non exposé, mesures compensatoires
>    déjà en place (segmentation réseau, IPS/WAF bloquant le vecteur, accès restreint), et pas de
>    preuve d'exploitation active.
>
> Avant de fixer un délai, il faut obtenir : le score CVSS et le vecteur d'attaque de
> CVE-2026-33824, son statut d'exploitation (KEV CISA, EPSS, PoC public), le rôle et l'exposition
> réseau de l'actif, ainsi que sa criticité métier. Sans ces données, la décision par défaut la
> plus sûre est de **considérer le correctif comme urgent** jusqu'à preuve du contraire, plutôt
> que de le reporter au cycle standard.

### Tâche B — Config 4 (KG complet actuel + scénario exposition)

> **Décision : correctif à traiter en urgence cette semaine, pas d'attente du cycle standard.**
>
> Justification :
>
> - **Sévérité critique et exploitation triviale** : CVSS 9.8 (CRITICAL), vecteur réseau (AV:N),
>   complexité faible (AC:L), aucun privilège requis (PR:N), aucune interaction utilisateur
>   (UI:N) — un attaquant distant non authentifié peut compromettre totalement confidentialité,
>   intégrité et disponibilité (C:H/I:H/A:H).
> - **Exploitation active confirmée** : le statut SSVC indique `exploitation active`,
>   automatisable (`SSVC_automatable yes`), avec un impact technique total. L'EPSS du
>   2026-08-28 est à 0,727 avec un percentile de 0,994 — c'est-à-dire un risque d'exploitation
>   quasi maximal comparé à l'ensemble des CVE connues.
> - **Inscription au catalogue CISA KEV avec échéance dépassée** : ajoutée le 2026-08-18, avec
>   une date d'action requise fixée au 2026-08-21 — cette échéance est déjà passée à la date
>   d'aujourd'hui (2026-08-29), ce qui signale un retard sur une obligation de correction
>   prioritaire.
> - **Exposition de l'actif concerné** : le serveur Windows exécutant ce CVE est exposé
>   publiquement sur Internet via les ports IKE (UDP 500/4500), exactement le vecteur requis
>   pour l'exploitation (envoi de trafic IKE spécialement conçu) — il n'y a donc aucune barrière
>   réseau atténuant le risque.
> - **Correctif disponible** : Microsoft a publié une mise à jour de sécurité pour ce CVE, donc
>   rien ne justifie de différer l'application.
>
> L'ensemble de ces facteurs (exploitation active en conditions réelles, exposition directe sur
> Internet, criticité maximale, échéance CISA déjà dépassée) impose un traitement immédiat, hors
> cycle de maintenance standard.

### Tâche B — Config 5 (KG incomplet, sans le scénario d'exposition)

> **Décision : correctif à traiter en urgence cette semaine, sans attendre le cycle de
> maintenance standard.**
>
> Justification :
>
> - **Sévérité maximale** : score CVSS 3.1 de 9,8/10 (CRITICAL), vecteur AV:N/AC:L/PR:N/UI:N —
>   exploitable à distance, sans authentification, sans interaction utilisateur, avec impact
>   total sur confidentialité, intégrité et disponibilité (double free menant à exécution de
>   code, CWE-415).
> - **Exploitation active confirmée** : le statut SSVC indique une exploitation « active » et un
>   potentiel « automatable » (yes), avec un impact technique qualifié de « total ».
> - **Inscrite au catalogue CISA KEV** : ajoutée le 2026-08-18, avec une date d'échéance
>   d'action (CISA_action_due_date) fixée au 2026-08-21 — délai déjà dépassé à la date actuelle,
>   ce qui signifie que l'actif est en violation de la directive BOD 26-04 tant que le correctif
>   n'est pas appliqué.
> - **Score EPSS très élevé** : probabilité d'exploitation de 72,7 % avec un percentile de
>   99,4 % (observation du 2026-08-28), plaçant cette CVE parmi les plus susceptibles d'être
>   exploitées à court terme, toutes vulnérabilités confondues.
> - **Contexte de menace aggravant** : une des références pointe vers une analyse d'une campagne
>   de cyberattaque autonome pilotée par IA (unit42.paloaltonetworks.com), suggérant une
>   exploitation automatisée à grande échelle.
> - **Correctif disponible** : Microsoft a déjà publié les mises à jour de sécurité
>   correspondantes, donc aucun blocage technique n'empêche une application immédiate.
> - **Composant vulnérable exposé au réseau** : l'extension IKE de Windows (utilisée pour
>   IPsec/VPN) est par nature exposée au trafic réseau, ce qui correspond directement au vecteur
>   d'attaque décrit (envoi de trafic IKE spécialement conçu).
>
> La combinaison sévérité critique + exploitation active confirmée + présence au KEV CISA avec
> échéance dépassée + EPSS extrême ne laisse aucune marge pour attendre le prochain cycle
> standard : le correctif doit être déployé en urgence, en priorité absolue.

### Tâche B — Config 7 (KG pré-validation + scénario exposition)

> **Décision : traitement en urgence cette semaine, hors cycle standard.**
>
> **Justification :**
>
> - **Sévérité et exploitabilité maximales** : CVSS 9.8 (CRITICAL), vecteur réseau, complexité
>   faible, aucun privilège ni interaction utilisateur requis (AV:N/AC:L/PR:N/UI:N), avec impact
>   total sur confidentialité, intégrité et disponibilité — un scénario de compromission
>   complète à distance.
> - **Exploitation active confirmée** : le statut SSVC indique `exploitation: active` et
>   `automatable: yes`, ce qui signifie que l'attaque est déjà exploitée dans la nature et peut
>   être automatisée à grande échelle.
> - **Score EPSS extrême** : probabilité d'exploitation de 72,7 % avec un percentile de 99,4 %,
>   plaçant cette CVE parmi les plus dangereuses actuellement suivies.
> - **Inscription au catalogue CISA KEV avec échéance dépassée** : la date limite d'action CISA
>   était le 2026-08-21 — nous sommes déjà après cette échéance (date d'observation la plus
>   récente : 2026-08-28/29). Le correctif est donc déjà en retard par rapport aux obligations
>   BOD 26-04.
> - **Exposition directe de l'actif** : l'actif concerné est un serveur Windows exposé
>   publiquement sur internet sur les ports IKE (UDP 500 et 4500) — exactement le vecteur
>   d'attaque exploité par cette CVE (extension IKE Windows), sans aucune barrière réseau
>   intermédiaire.
>
> La combinaison d'un exploit actif, d'une exposition réseau directe sur le port vulnérable,
> d'un score de criticité maximal et d'une échéance réglementaire déjà dépassée exclut toute
> possibilité d'attendre le prochain cycle de maintenance standard. Le correctif doit être
> appliqué en procédure d'urgence, ou à défaut l'actif doit être isolé/mis hors ligne
> immédiatement en attendant le patch.

### Tâche B — Config 8 (KG incomplet + signalement)

> **Décision : traitement en urgence cette semaine, hors cycle standard.**
>
> **Justification :**
>
> - **Sévérité maximale** : score CVSS 9.8 (CRITICAL), avec vecteur réseau, complexité faible,
>   aucun privilège requis et aucune interaction utilisateur (AV:N/AC:L/PR:N/UI:N) — une
>   exploitation à distance sans conditions préalables est possible.
> - **Impact total** : confidentialité, intégrité et disponibilité toutes cotées HIGH, avec
>   exécution de code à distance (RCE) confirmée par plusieurs sources (S02, S45, S46).
> - **Exploitation active et automatisable** : le statut SSVC indique une exploitation
>   « active » et un caractère « automatable » (yes), avec un impact technique qualifié de
>   « total ».
> - **Inscrite au catalogue CISA KEV** : ajoutée le 2026-08-18, avec une date d'action requise
>   fixée au 2026-08-21 — cette échéance est déjà dépassée à la date d'aujourd'hui (2026-08-29),
>   ce qui aggrave le retard et impose une remédiation immédiate.
> - **Score EPSS très élevé** : probabilité d'exploitation de 72,7 % et percentile de 99,4 %
>   (observé le 2026-08-28), ce qui place cette CVE parmi les plus susceptibles d'être exploitées
>   dans un avenir proche.
> - **Correctif disponible** : Microsoft a publié les mises à jour de sécurité correspondantes,
>   donc rien ne justifie d'attendre — l'application peut se faire sans délai technique.
> - **Surface d'exposition très large** : quasiment toutes les versions actuelles de Windows
>   10/11 et Windows Server (2016 à 2025) sont concernées, augmentant la probabilité que l'actif
>   visé soit affecté.
>
> Le seul point d'incertitude relevé dans les données est l'exposition réseau exacte de l'actif
> exécutant cette CVE, qui n'a pas pu être confirmée avec certitude. Cependant, étant donné la
> combinaison d'une exploitation active confirmée, d'une inscription KEV avec échéance dépassée,
> et d'un score de criticité maximal, le principe de précaution impose de traiter ce correctif
> en urgence cette semaine plutôt que d'attendre le prochain cycle de maintenance standard —
> indépendamment de la confirmation de l'exposition, puisque l'attaque est déjà documentée comme
> active dans la nature.

---

## Fichiers produits

- `extraction_pipeline/reports/experiment_contexts/ctx_{A,B}{1,4,5,7,8}.txt` — contexte exact
  envoyé à chaque cellule (10 fichiers, dont 2 vides pour la config 1).
- Ce rapport (`experiment_protocol_13.md`) — tableau + annexe complète, aucune analyse.
