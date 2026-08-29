# T1b_c7 — Priorisation de correctif : CVE-2026-55040 vs CVE-2026-63520

## Décision

**Patcher CVE-2026-55040 en premier.** Si un seul correctif peut être appliqué cette
semaine, il doit porter sur CVE-2026-55040 (contournement d'authentification SharePoint,
CWE-1390) ; CVE-2026-63520 passe en second.

## Justification

### 1. Exploitation active et avérée, pas seulement théorique
- `has_SSVC_exploitation: active` pour CVE-2026-55040, contre `none` pour CVE-2026-63520
  (S03 / S06). C'est le discriminant le plus fort du sous-graphe.
- CISA a ajouté CVE-2026-55040 au catalogue KEV le **2026-08-18**, avec une date d'action
  exigée au **2026-08-21** (S03) — donc **déjà dépassée** au 2026-08-28 (date des
  observations EPSS). CVE-2026-63520 n'a aucune entrée KEV dans le contexte.
- Un PoC public existe : Rapid7 (Stephen Fewer) a publié le PoC et les détails techniques
  complets de CVE-2026-55040 (S10, S40).
- La société de threat intelligence Defused signale des attaquants **utilisant le PoC
  Rapid7 pour CVE-2026-55040 contre des honeypots SharePoint** (S18) : l'exploitation est
  observée dans la nature, pas seulement possible.

### 2. Probabilité d'exploitation nettement supérieure
- EPSS au 2026-08-28 : **0,3965 (percentile 0,9856)** pour CVE-2026-55040 contre
  **0,0289 (percentile 0,8586)** pour CVE-2026-63520 (S22 / S25) — soit un ordre de
  grandeur d'écart en probabilité.
- `has_SSVC_automatable: yes` pour CVE-2026-55040 vs `no` pour CVE-2026-63520 : la
  première se prête à une exploitation de masse automatisée.

### 3. Facilité d'exploitation, malgré des scores CVSS proches
- CVE-2026-55040 : baseScore **9,1 CRITICAL**, `AC:L`, `PR:N`, `UI:N`, sous-score
  d'exploitabilité **3,9**.
- CVE-2026-63520 : baseScore **8,1 HIGH**, `AC:H`, sous-score d'exploitabilité **2,2**.
- Les deux sont réseau et sans authentification ni interaction utilisateur, mais la
  complexité d'attaque élevée de CVE-2026-63520 constitue une barrière réelle que
  CVE-2026-55040 n'a pas.

### 4. Casser la chaîne d'exploitation au bon maillon
- Les deux CVE font partie d'une même chaîne : le contournement d'authentification
  CVE-2026-55040 combiné à CVE-2026-63520 donne une **désérialisation pleinement
  authentifiée** (S10), et le sous-graphe indique explicitement que CVE-2026-63520 est
  « chaîné à » la vulnérabilité de contournement d'authentification (S41), l'ensemble
  menant à une **RCE non authentifiée** contre un serveur SharePoint vulnérable (S18).
- Le contexte l'énonce directement : **« Patching CVE-2026-55040 break exploit chain »**
  (S40). Corriger le maillon d'authentification neutralise le scénario non authentifié le
  plus dangereux ; corriger d'abord CVE-2026-63520 laisserait le contournement d'auth
  exploitable seul (opérations en tant qu'utilisateur du site **et en tant
  qu'administrateur**, S18).

### 5. Ce que l'impact CVSS ne suffit pas à trancher
CVE-2026-63520 a un impact technique légèrement supérieur (`A:H`, impactScore 5,9, RCE
directe) contre CVE-2026-55040 (`A:N`, impactScore 5,2). C'est le seul axe où
CVE-2026-63520 devance. Mais les deux ont `SSVC_technicalImpact: total`, et sur une
décision de priorisation, la probabilité d'exploitation (active, KEV, PoC utilisé en
nature, EPSS ×14, automatisable) l'emporte sur un écart d'impact marginal.

### 6. Périmètre identique — pas d'arbitrage d'exposition à faire
Les deux CVE touchent exactement le même parc : SharePoint Enterprise Server 2016,
SharePoint Server 2019, SharePoint Server Subscription Edition (S03 / S06). Aucune des
deux ne concerne un périmètre plus restreint que l'autre : le choix se joue uniquement
sur le risque.

## Réserves et suite

- **Ne pas considérer CVE-2026-63520 comme réglée.** Rapid7 a publié ses détails
  techniques **en avance sur le calendrier prévu** (S41), et son statut SSVC `none` peut
  basculer rapidement. À planifier dès la fenêtre de correctif suivante.
- Les deux CVE sont évaluées par le MSRC en **« Exploitation More Likely »**, avec des
  statuts `publicly_disclosed: No` et `exploited: No` (S39 / S42) — ces derniers sont
  **contredits par la réalité observée** pour CVE-2026-55040 (PoC public Rapid7, KEV
  CISA, exploitation sur honeypots). Traiter les champs MSRC comme potentiellement
  périmés plutôt que comme une contre-indication.
- L'échéance CISA du 2026-08-21 étant dépassée, si le parc SharePoint est exposé sur
  Internet, appliquer en complément les mitigations vendeur immédiates (et l'exigence de
  triage forensique de BOD 26-04, S03) en attendant la fenêtre de patch — le retard sur
  KEV suppose de vérifier l'absence de compromission préalable, pas seulement de corriger.

> Analyse fondée exclusivement sur le sous-graphe canonical KG fourni (état
> pré-validation), sources S03, S06, S10, S18, S22, S25, S39, S40, S41, S42.
