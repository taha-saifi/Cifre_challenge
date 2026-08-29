# T1b_c8 — Priorisation CVE-2026-55040 vs CVE-2026-63520

## Décision

**Patcher CVE-2026-55040 en premier** (KB5002882 / KB5002883 / KB5002891 selon la version de SharePoint), et reporter CVE-2026-63520 à la semaine suivante.

## Justification

### 1. CVE-2026-55040 est exploitée dans la nature, CVE-2026-63520 ne l'est pas

C'est le facteur décisif, et il l'emporte sur toute comparaison de scores CVSS.

- `has_SSVC_exploitation active` pour CVE-2026-55040, contre `none` pour CVE-2026-63520.
- CVE-2026-55040 est au catalogue **CISA KEV** (`has_CISA_exploit_addition_date 2026-08-18`), avec une **échéance d'action au 2026-08-21** — donc **déjà dépassée** à la date d'observation (2026-08-28). CVE-2026-63520 n'a aucune entrée KEV.
- Un **PoC public** existe pour CVE-2026-55040 (Rapid7 / Stephen Fewer, dépôt GitHub `sfewer-r7/CVE-2026-55040` référencé dans la CVE), et la threat intel rapporte que **des attaquants utilisent ce PoC contre des honeypots SharePoint** (source S18, Defused). Pour CVE-2026-63520, seules des « technical details » Rapid7 sont mentionnées, sans PoC d'exploitation observé.

### 2. Le risque probabiliste diverge d'un ordre de grandeur

- EPSS au 2026-08-28 : **0,3965 (percentile 0,9856)** pour CVE-2026-55040 contre **0,0289 (percentile 0,8586)** pour CVE-2026-63520 — soit ~14× plus de probabilité d'exploitation à 30 jours.

### 3. La facilité d'exploitation penche nettement du même côté

- CVE-2026-55040 : CVSS 9.1 CRITICAL, `AV:N/AC:L/PR:N/UI:N`, **exploitability score 3,9** (maximum), `SSVC_automatable yes` — attaque réseau, sans privilège, sans interaction utilisateur, **automatisable en masse**.
- CVE-2026-63520 : CVSS 8.1 HIGH, mais `AC:H` (complexité d'attaque élevée) et `SSVC_automatable no`, d'où un **exploitability score de seulement 2,2**.

Le seul avantage « papier » de CVE-2026-63520 est son impact technique légèrement supérieur (impact score 5,9 contre 5,2, grâce à `A:H` alors que CVE-2026-55040 est `A:N`), et sa nature d'exécution de code à distance (CWE-20, improper input validation) face à un contournement d'authentification (CWE-1390). **Cet écart d'impact ne compense pas l'écart d'exploitabilité et d'exploitation active** : les deux atteignent `SSVC_technicalImpact total`, et une compromission totale reste une compromission totale.

### 4. Patcher CVE-2026-55040 casse aussi la chaîne d'exploitation

Les sources indiquent que CVE-2026-55040 sert de maillon d'entrée : « pairing with CVE-2026-55040 authentication bypass we achieved fully authenticated deserialization » (S10), et « Patching CVE-2026-55040 break exploit chain » (S40). Corriger d'abord le contournement d'authentification **retire l'accès non authentifié** qui rend exploitable la partie désérialisation/exécution de code. L'ordre inverse laisserait ouverte la porte d'entrée déjà activement utilisée.

### 5. Périmètre identique — pas d'argument d'exposition différentiel

Les deux CVE touchent exactement les mêmes produits (SharePoint Enterprise Server 2016, Server 2019, Subscription Edition). Le choix ne peut donc pas se faire sur le périmètre d'actifs concernés ; il se fait bien sur le risque.

## Limites et réserves (à assumer explicitement)

- Le lien de chaînage entre les deux CVE **n'est pas confirmé avec certitude** dans les sources disponibles (note explicite du sous-graphe, et assertions S10 issues d'extraction ouverte, donc formulées de manière bruitée : « we know similar structure to CVE-2026-63520 »). Ce point est traité ici comme un **argument de renfort**, pas comme le fondement de la décision. Même sans chaînage, les points 1 à 3 suffisent.
- Les deux CVE ont le même verdict MSRC (`publicly_disclosed No`, `exploited No`, « Exploitation More Likely »). Cette évaluation MSRC est en **contradiction apparente** avec les données CISA KEV / SSVC / threat intel pour CVE-2026-55040 (statut `exploited No` alors que la CVE est au KEV et exploitée). En cas de divergence, on retient la donnée la plus défavorable et la plus fraîche : KEV + observation d'exploitation active.
- Le sous-graphe est déclaré **incomplet**. Une donnée d'exposition réelle du parc (serveurs SharePoint accessibles depuis Internet, versions déployées) modifierait l'urgence opérationnelle mais pas l'ordre de priorité entre les deux correctifs.

## Recommandation opérationnelle

1. **Cette semaine** : déployer le correctif CVE-2026-55040 sur les instances SharePoint exposées en priorité (Subscription Edition → KB5002882 ; 2019 → KB5002883 ; Enterprise 2016 → KB5002891). L'échéance CISA BOD 26-04 étant dépassée, traiter cela comme un retard à rattraper, pas comme un patch planifié.
2. **En complément immédiat, sans attendre le patch** : recherche de compromission (forensics triage exigé par l'action requise CISA) sur les instances concernées, puisque l'exploitation est active depuis au moins le 2026-08-18.
3. **Semaine suivante** : CVE-2026-63520 (KB5002893 / KB5002894 / KB5002896 / KB5002905 / KB5002906), en surveillant tout signal d'exploitation qui justifierait de la remonter.
