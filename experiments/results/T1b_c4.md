# T1b — c4 : priorisation de correctif entre CVE-2026-55040 et CVE-2026-63520

## Décision

**Patcher CVE-2026-55040 en premier** (KB5002882 / KB5002883 / KB5002891 selon la version de SharePoint), et traiter CVE-2026-63520 dans un second temps.

## Justification

### 1. Exploitation active constatée, pas seulement théorique
- `has_SSVC_exploitation = active` pour CVE-2026-55040, contre `none` pour CVE-2026-63520 [S03, S06].
- Un PoC public existe : « Rapid7's Stephen Fewer published_PoC_for CVE-2026-55040 », avec un dépôt de référence `github.com/sfewer-r7/CVE-2026-55040` [S10, S03].
- Ce PoC est déjà utilisé dans la nature : la firme de threat intelligence Defused signale des attaquants utilisant le PoC Rapid7 contre des honeypots SharePoint [S18].
- Pour CVE-2026-63520, seule une divulgation technique Rapid7 existe, sans exploitation observée [S06, S41].

### 2. Obligation réglementaire déjà échue (KEV / BOD 26-04)
- CVE-2026-55040 est au catalogue CISA KEV : `has_CISA_exploit_addition_date = 2026-08-18`, `has_CISA_action_due_date = 2026-08-21` [S03].
- À la date des observations (28/08/2026), l'échéance CISA est **dépassée**. CVE-2026-63520 ne porte aucune entrée KEV ni échéance.

### 3. Probabilité d'exploitation (EPSS) d'un ordre de grandeur supérieur
Observations du 2026-08-28 :

| | CVE-2026-55040 | CVE-2026-63520 |
|---|---|---|
| EPSS probabilité | 0,3965 | 0,0289 |
| EPSS percentile | 0,9856 | 0,8586 |

Soit environ **13,7×** plus de probabilité d'exploitation à 30 jours pour CVE-2026-55040 [S22, S25].

### 4. Facilité d'exploitation nettement plus grande
- CVE-2026-55040 : `AV:N/AC:L/PR:N/UI:N`, score d'exploitabilité **3,9** (maximum), `SSVC_automatable = yes` — donc exploitable à grande échelle, automatisable, sans authentification ni interaction utilisateur [S03].
- CVE-2026-63520 : `AC:H`, score d'exploitabilité **2,2**, `SSVC_automatable = no` — complexité d'attaque élevée [S06].

C'est le facteur qui l'emporte sur la comparaison brute des scores CVSS de base (9,1 CRITICAL vs 8,1 HIGH) et sur l'impact technique (`technicalImpact = total` pour les deux ; l'impact disponibilité `A:H` de CVE-2026-63520 est son seul avantage relatif, ce qui explique son `impactScore` légèrement supérieur : 5,9 vs 5,2).

### 5. Le point décisif : CVE-2026-55040 est le maillon d'entrée de la chaîne d'exploitation
- CVE-2026-55040 est un contournement d'authentification (CWE-1390, forge de jetons JWT) permettant à un attaquant **non authentifié** d'agir comme utilisateur du site *ou comme administrateur* [S18, S10].
- Le chaînage documenté : « pairing with CVE-2026-55040 authentication bypass we_achieved fully authenticated deserialization » et « CVE-2026-63520 be_chained_to authentication bypass vulnerability » [S10, S41]. Les deux mènent ensemble à une RCE non authentifiée [S18].
- Conclusion explicite de la source : **« Patching CVE-2026-55040 break exploit chain »** [S40].

Corriger CVE-2026-55040 casse donc la chaîne complète et neutralise aussi la voie d'exploitation non authentifiée de CVE-2026-63520, dont l'exploitation isolée resterait de complexité élevée. L'inverse n'est pas vrai : patcher seulement CVE-2026-63520 laisserait intact un contournement d'authentification activement exploité, automatisable et déjà en KEV.

## Plan d'action recommandé

1. **Cette semaine** — déployer le correctif CVE-2026-55040 sur tous les SharePoint concernés (Enterprise Server 2016, Server 2019, Subscription Edition) :
   - KB5002891 — SharePoint Enterprise Server 2016 (16.0.5561.1001)
   - KB5002883 — SharePoint Server 2019 (16.0.10417.20175)
   - KB5002882 — SharePoint Server Subscription Edition (16.0.19725.20434)
2. **En parallèle, sans coût de patch** — restreindre l'exposition Internet des serveurs SharePoint et surveiller les indicateurs de forge JWT / accès privilégié anormal ; l'échéance CISA du 21/08 étant dépassée, une recherche de compromission préalable (triage forensique attendu par BOD 26-04) est justifiée avant de considérer l'incident clos [S03].
3. **Semaine suivante** — appliquer les correctifs CVE-2026-63520 (KB5002905/KB5002906 pour 2016, KB5002894/KB5002896 pour 2019, KB5002893 pour Subscription Edition), les correctifs étant plus récents et cumulatifs en version (ex. 16.0.5565.1001 > 16.0.5561.1001), ce qui suggère qu'un déploiement ultérieur du lot CVE-2026-63520 couvre également le précédent — à valider auprès de la documentation MSRC avant planification.

## Réserves

- Les deux CVE portent `MSRC_exploited_status = No` [S39, S42], ce qui contredit apparemment le SSVC `active` et le signalement Defused ; ces attributs MSRC datent probablement d'avant l'inscription au KEV du 18/08. La priorisation retenue s'appuie sur les sources les plus récentes (KEV du 18/08, EPSS du 28/08, rapport Defused).
- Le contexte ne dit rien de l'exposition réelle du parc (serveurs accessibles depuis Internet ou non) ni des contraintes de fenêtre de maintenance ; ces éléments peuvent modifier le séquencement opérationnel mais pas l'ordre de priorité, la chaîne d'exploitation étant rompue par le patch de CVE-2026-55040.
