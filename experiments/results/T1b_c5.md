# T1b — c5 : arbitrage de priorisation CVE-2026-55040 vs CVE-2026-63520

## Décision

**Patcher CVE-2026-55040 en premier** (KB5002882 / KB5002883 / KB5002891 selon la version de SharePoint), et reporter CVE-2026-63520 à la fenêtre suivante.

## Justification

### 1. Exploitation active constatée, pas seulement théorique

- `CVE-2026-55040 has_SSVC_exploitation active` (S03) vs `CVE-2026-63520 has_SSVC_exploitation none` (S06).
- CVE-2026-55040 a été ajoutée au catalogue CISA KEV le **2026-08-18**, avec une **date d'action exigée au 2026-08-21** — déjà dépassée à la date d'observation (2026-08-28). CVE-2026-63520 n'a aucune entrée KEV dans le sous-graphe.
- Un PoC public existe (Rapid7 / Stephen Fewer, dépôt GitHub `sfewer-r7/CVE-2026-55040`) et la société de threat intelligence Defused a signalé que **des attaquants utilisent ce PoC Rapid7 contre des honeypots SharePoint** (S18). Pour CVE-2026-63520, seuls des détails techniques publiés existent, sans exploitation observée.

C'est le facteur décisif : le risque n'est pas hypothétique d'un côté et l'est de l'autre.

### 2. Probabilité d'exploitation (EPSS) d'un ordre de grandeur supérieur

| | CVE-2026-55040 | CVE-2026-63520 |
|---|---|---|
| EPSS probabilité (2026-08-28) | **0.3965** | 0.0289 |
| EPSS percentile | **98.6 %** | 85.9 % |

Environ **13,7× plus de probabilité** d'exploitation à 30 jours pour CVE-2026-55040.

### 3. Facilité d'exploitation nettement plus élevée

- CVE-2026-55040 : `AV:N/AC:L/PR:N/UI:N`, score d'exploitabilité **3.9** (maximum), `SSVC_automatable: yes`.
- CVE-2026-63520 : `AV:N/AC:H/PR:N/UI:N`, score d'exploitabilité **2.2**, `SSVC_automatable: no`.

Une complexité d'attaque **LOW** + automatisable signifie exploitation de masse / scan-and-exploit possible ; **HIGH** + non automatisable signifie attaque ciblée et coûteuse.

### 4. Le score CVSS brut est trompeur ici — et l'écart est faible

CVE-2026-55040 a un baseScore de **9.1 (CRITICAL)** contre **8.1 (HIGH)** pour CVE-2026-63520. L'unique avantage « impact » de CVE-2026-63520 est la disponibilité (`A:H` vs `A:N`) et un impactScore légèrement supérieur (5.9 vs 5.2), pour une exécution de code à distance (CWE-20) contre un contournement d'authentification (CWE-1390). Mais :
- les deux ont un `SSVC_technicalImpact: total` — la compromission est totale dans les deux cas ;
- CVE-2026-55040 permet, via forge de jetons JWT, d'agir **en tant qu'administrateur** du serveur SharePoint sans authentification (S10, S18), ce qui est en pratique équivalent à une prise de contrôle.

L'impact marginalement supérieur de CVE-2026-63520 ne compense pas un écart d'exploitabilité et d'exploitation active de cette ampleur.

### 5. Argument décisif : casser la chaîne d'exploitation

Le sous-graphe indique explicitement `Patching CVE-2026-55040 break exploit chain` (S40). Rapid7 décrit un enchaînement où le contournement d'authentification CVE-2026-55040 est **couplé** à la désérialisation pour obtenir une « fully authenticated deserialization » (S10, structure similaire à CVE-2026-63520). Autrement dit, **CVE-2026-55040 est le maillon d'entrée** : la corriger neutralise le vecteur d'accès non authentifié et réduit du même coup l'exploitabilité pratique de la chaîne, alors que corriger uniquement CVE-2026-63520 laisserait le contournement d'authentification — déjà exploité dans la nature — ouvert.

### 6. Périmètre identique, donc pas d'arbitrage d'exposition

Les deux CVE affectent exactement les mêmes produits (SharePoint Enterprise Server 2016, SharePoint Server 2019, SharePoint Server Subscription Edition), même éditeur, même assessment MSRC (« Exploitation More Likely », non divulguée publiquement selon MSRC). Le périmètre à patcher est le même : le choix se joue donc uniquement sur le risque, et le risque penche sans ambiguïté vers CVE-2026-55040.

## Recommandation opérationnelle

1. **Cette semaine** : appliquer KB5002882 (Subscription Edition, 16.0.19725.20434), KB5002883 (2019, 16.0.10417.20175), KB5002891 (Enterprise 2016, 16.0.5561.1001) selon les versions déployées. Traiter en priorité les instances exposées sur Internet (l'action requise CISA/BOD 26-04 impose d'évaluer l'exposition Internet de chaque actif).
2. **En complément immédiat, sans attendre la fenêtre suivante** : recherche de compromission (« Forensics Triage Requirements » CISA) — l'échéance CISA du 2026-08-21 étant dépassée, on ne peut pas exclure une exploitation antérieure au correctif.
3. **Fenêtre suivante** : appliquer les correctifs CVE-2026-63520 (KB5002893 / KB5002894 / KB5002896 / KB5002905 / KB5002906). Noter que ces KB portent des versions plus récentes que celles de CVE-2026-55040 (ex. 16.0.19725.20522 > 16.0.19725.20434), donc **cumulatives** : si la fenêtre le permet techniquement, appliquer directement le correctif le plus récent couvre probablement les deux — à valider auprès de MSRC avant de s'en remettre à cette hypothèse.
4. **Surveiller** l'EPSS de CVE-2026-63520 et une éventuelle bascule de son `SSVC_exploitation` : Rapid7 ayant publié les détails techniques par anticipation, la probabilité d'exploitation peut monter rapidement.

## Limites de l'analyse

Ce raisonnement repose sur un sous-graphe explicitement décrit comme **incomplet**. Points non couverts : criticité métier réelle des serveurs SharePoint concernés, exposition Internet effective du parc, existence de mesures d'atténuation temporaires, et fenêtre de maintenance disponible. Une exposition Internet nulle sur les instances concernées modifierait le calcul — mais pas la conclusion, l'écart d'exploitation active restant déterminant.
