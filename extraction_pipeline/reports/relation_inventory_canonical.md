# Inventaire neutre des clusters canoniques — extraction_pipeline

Généré par lecture directe de `canonical_kg/edges.json` (2407 edges, 1305 predicate_canonical distincts).
Aucun regroupement thématique, aucune correspondance vers un schéma métier. Trié par volume décroissant.

Données complètes (tous les champs, sans troncature d'`evidence`) : `reports/relation_inventory_canonical.json`.

## Note de méthode — écart avec la prémisse de la mission

La mission indique que les `structured_assertions.json` (NVD/EPSS) "ne passent pas par le clustering". Lecture du code (`pipeline_lib.py`, `build_relation_inventory()` et `cluster_relations()`, lignes 698-728) : en réalité les assertions structurées et les assertions OpenIE sont concaténées et clusterisées ensemble, sans distinction de source. Empiriquement, sur les 259 assertions structurées, **aucune ne fusionne avec un cluster d'origine OpenIE** — les 33 prédicats structurés (noms de champs déjà normalisés, ex. `has affected product`) restent chacun dans leur propre cluster à 259/259. Donc le résultat final ressemble à ce que la mission décrit, mais le mécanisme réel diffère de la description (séparation de fait, pas de droit). Signalé ici comme observation, aucune correction appliquée.

## Section 1 — Clusters canoniques dérivés d'OpenIE (MinIE + fallback heuristique)

1272 prédicats canoniques distincts, 2148 edges au total.

| # | predicate_canonical | volume | domain→range (count) | derived_from (relation_raw regroupées) | exemples (source_id, subject → object) |
|---|---|---|---|---|---|
| 1 | `exploit` | 19 | Mention→Mention (16); Mention→CVE (2); Organization→Mention (1) | Exploits; exploit; exploited; exploits; has exploited; have exploited | [S07] attacker → vulnerability<br>[S09] we → issue<br>[S09] VulnCheck analysis → issue |
| 2 | `allows` | 18 | Mention→Mention (11); Mention→Organization (7) | allow; allows; has allowed | [S09] this → constructing gadget chain method<br>[S10] service → external data sources<br>[S17] exploit → unauthenticated attacker with network access to vCenter management interface to traverse directories beyond intended boundaries |
| 3 | `be scored` | 18 | Mention→Mention (18) | be scored; be scoring | [S07] Base Score increases → relative to impacted component<br>[S07] confidentiality → relative to impacted component<br>[S07] Confidentiality Integrity and Authentication metrics → relative to impacted component |
| 4 | `be listed in` | 15 | Mention→Mention (11); Mention→Product (4) | be listed in | [S01] common vulnerabilities → CISA 's KEV Catalog<br>[S01] exposures → CISA 's KEV Catalog<br>[S01] exploited vulnerability → KEV catalog |
| 5 | `contains` | 15 | Mention→Mention (13); Product→Mention (1); Organization→Mention (1) | contain; contains | [S08] that → actor token SigningToken value<br>[S08] actor token 's x5t header → SharePoint 's own STS certificate thumbprint<br>[S10] BDCM model file → gadget |
| 6 | `use` | 13 | Mention→Mention (10); Organization→Mention (2); Product→Mention (1) | Uses; do use; use; uses | [S07] systems → IKE<br>[S08] we → string AAAA<br>[S08] we → SID of S-1-5-21-4203888158-2793536450-3921675298-500 |
| 7 | `be exploited` | 12 | Mention→Mention (12) | be exploit; be exploited | [S07] vulnerability → solely<br>[S39] vulnerability → solely<br>[S40] this → chain |
| 8 | `be scored relative to impacted component If` | 12 | Mention→Mention (12) | be scored relative to impacted component If | [S07] Base Score increases → so<br>[S07] confidentiality → so<br>[S07] Confidentiality Integrity and Authentication metrics → so |
| 9 | `is provided without` | 12 | Mention→Mention (12) | is provided without | [S15] Alfredo Pesoli via Bynario Atlas Information about products not manufactured by Apple → recommendation Apple<br>[S15] Alfredo Pesoli via Bynario Atlas Information about products not manufactured by Apple → endorsement Apple<br>[S15] Alfredo Pesoli via Bynario Atlas Information about products not manufactured by independent websites → recommendation Apple |
| 10 | `represents intrinsic qualities of` | 11 | Mention→Mention (11) | represents intrinsic qualities of | [S50] Base → vulnerability<br>[S50] Threat → vulnerability<br>[S50] Environmental → vulnerability |
| 11 | `be provided by` | 10 | Mention→Mention (6); Mention→Organization (3); Mention→Vendor (1) | be provided by | [S37] required additional information → CVE Program<br>[S38] CWE → originating CNA<br>[S38] CWE → CISA ADP |
| 12 | `refers` | 10 | Mention→Mention (10) | refer; refers | [S07] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures<br>[S07] integrity → There is complete loss of protection For example<br>[S39] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures |
| 13 | `apply to` | 9 | Mention→Mention (9) | Do apply to; applies to; apply to; do apply to | [S14] choice of means → court<br>[S19] directives → statutorily defined national security systems<br>[S39] updates for SharePoint Enterprise Server 2016 → version |
| 14 | `be prevent` | 9 | Mention→Mention (9) | be prevent | [S16] approach → known from causing harm to endpoints Cortex Xpanse layers of protection including Advanced WildFire to prevent known from causing harm to endpoints Cortex Xpanse<br>[S16] approach → known from causing harm to endpoints Cortex Xpanse layers of protection including Advanced WildFire to prevent unknown malware<br>[S16] approach → known from causing harm to endpoints Cortex Xpanse layers of protection including Behavioral Threat Protection to prevent known from causing harm to endpoints Cortex Xpanse |
| 15 | `is in` | 9 | Mention→Mention (9) | do in; is in; was in | [S08] first weakness → SPJsonWebSecurityTokenHandlerV2.ValidateToken<br>[S08] most fundamental weakness → SPJsonWebSecurityTokenHandlerV2.ValidateToken<br>[S16] Zhuhai → China |
| 16 | `like to thank` | 9 | Mention→Mention (4); Mention→Product (2); Mention→Organization (2); Mention→URL (1) | like to thank | [S40] we → Rapid7 for responsibly reporting issue through coordinated vulnerability disclosure<br>[S40] we → Rapid7<br>[S41] we → Rapid7 for responsibly reporting issue through coordinated vulnerability disclosure |
| 17 | `refers to accessibility of` | 9 | Mention→Mention (9) | refers to accessibility of | [S42] availability → information resources<br>[S42] availability → processor cycles<br>[S42] availability → disk space |
| 18 | `be bypass authentication on` | 8 | CVE→Mention (4); Mention→Mention (4) | be bypass authentication on | [S08] leverage CVE-2026-55040 → vulnerable SharePoint server<br>[S08] perform operations as SharePoint site user → vulnerable SharePoint server<br>[S08] perform operations as administrator vulnerability → vulnerable SharePoint server |
| 19 | `be used` | 8 | Mention→Mention (8) | be used; be using | [S08] actor token 's signing key → x5t<br>[S09] other gadget chains → also<br>[S50] nomenclature → communicated |
| 20 | `help` | 8 | Mention→Mention (8) | help | [S11] reverse SSH connection → bypass firewalls persistence remote access also<br>[S11] reverse SSH connection → bypass firewalls gain remote access also<br>[S11] reverse SSH connection → bypass other network security measures persistence remote access also |
| 21 | `include` | 8 | Mention→Mention (8) | include; includes | [S17] Affected configurations → SSL VPN<br>[S17] Affected configurations → Zero Trust Network Access deployments<br>[S20] Adversaries may attempt to exploit weakness in system → network device administration |
| 22 | `apply` | 7 | CVE→Mention (5); Mention→Mention (2) | applies; apply | [S10] SharePoint → additional validation<br>[S19] it → systems<br>[S43] CVE-2026-59309 → patches listed in Fixed Version ' column of Response Matrix ' found below Workarounds |
| 23 | `change over` | 7 | Mention→Mention (7) | change over; changes over; do change over | [S50] vulnerability → time<br>[S51] vulnerability → time<br>[S51] attributes For organization → time |
| 24 | `define` | 7 | Mention→Mention (7) | define; defines | [S09] we → new parameter called<br>[S10] we → something like get specific value from database<br>[S10] MethodInstance A Parameter → argument for return type for Method The Parameter |
| 25 | `is required for` | 7 | Mention→Mention (7) | is required for | [S07] specific configuration → attack to succeed<br>[S39] specific configuration → attack to succeed<br>[S42] specific configuration → attack to succeed |
| 26 | `make` | 7 | Mention→Mention (7) | make; makes | [S10] we → entire blog post about intricacies of BDC<br>[S10] concept → Deserialize method run<br>[S17] what → them attractive targets |
| 27 | `added` | 6 | Organization→CVE (3); Organization→Mention (2); Vendor→Mention (1) | added; adds | [S17] CISA → CVE-2026-55040<br>[S19] CISA → vulnerability to KEV<br>[S19] CISA → vulnerability to KEV Catalog |
| 28 | `be managed by` | 6 | Mention→Mention (6) | be managed by | [S07] resources → same security authority<br>[S07] information resources → software component due to successfully exploited vulnerability Confidentiality<br>[S39] resources → same security authority |
| 29 | `be manufactured by` | 6 | Mention→Vendor (3); Mention→Mention (3) | be manufactured by | [S15] products → Apple<br>[S15] products → independent websites<br>[S55] products → Apple |
| 30 | `be used by` | 6 | Mention→Mention (6) | be used by | [S10] NET types → BCS models<br>[S46] standard ports → IKE<br>[S46] standard ports → IKE NAT traversal |
| 31 | `created Stakeholder-Specific Vulnerability Categorization system to provide` | 6 | Product→Mention (6) | created Stakeholder-Specific Vulnerability Categorization system to provide | [S53] Carnegie Mellon University 's Software Engineering Institute in collaboration with CISA → cyber community vulnerability analysis methodology prevalence of affected product in singular system<br>[S53] Carnegie Mellon University 's Software Engineering Institute in collaboration with CISA → cyber community vulnerability analysis methodology state governments<br>[S53] Carnegie Mellon University 's Software Engineering Institute in collaboration with CISA → cyber community vulnerability analysis methodology local governments |
| 32 | `has issued` | 6 | Mention→Mention (6) | has issued | [S07] vendor → official patch<br>[S07] vendor → upgrade<br>[S39] vendor → official patch |
| 33 | `measure` | 6 | Mention→Mention (6) | measure; measures | [S50] Threat metrics → current state of exploit techniques for vulnerability<br>[S52] Temporal metrics → current state of exploit code availability and is typically based on current state of exploit techniques<br>[S52] Temporal metrics → current state of exploit existence of workarounds and is typically based on current state of exploit techniques |
| 34 | `publishes` | 6 | Organization→Mention (3); Mention→Mention (2); Organization→CVE (1) | publishes | [S19] CISA → answers to KEV Status<br>[S19] CISA → answers to Exploit Automation<br>[S40] Rapid7 → technical details |
| 35 | `take additional information on` | 6 | Mention→Mention (6) | take additional information on | [S50] consumer → effort required into consideration when applying mitigations remediation When calculating Vulnerability Response Effort effort required to deploy quickest available response<br>[S50] consumer → effort required into consideration when applying scheduling remediation When calculating Vulnerability Response Effort effort required to deploy quickest available response<br>[S51] consumer → effort required into consideration when applying mitigations initial response to impact of vulnerabilities for deployed products in infrastructure |
| 36 | `are constant over` | 5 | Mention→Mention (5) | are constant over | [S50] vulnerability → time<br>[S50] vulnerability → time<br>[S51] vulnerability → time |
| 37 | `be implement` | 5 | Mention→Mention (5) | be implement | [S19] binding operational directives → cybersecurity policies<br>[S19] binding operational directives → principles<br>[S19] binding operational directives → standards |
| 38 | `be used to derive` | 5 | Mention→Mention (5) | be used to derive | [S50] values → score<br>[S50] individual characteristics → score CVSS<br>[S50] methodology → score CVSS |
| 39 | `offer` | 5 | Mention→Mention (5) | offer | [S39] Workarounds → interim remediation<br>[S39] hotfixes → interim remediation<br>[S42] Remediation Level → interim remediation |
| 40 | `produce` | 5 | Mention→Mention (5) | produce | [S17] single unauthenticated HTTP request → network outage equivalent to site power failure In context of 2026 's threat landscape<br>[S51] CVSS analysts → resulting severity scores<br>[S52] None → following vector |
| 41 | `read` | 5 | Mention→Mention (5) | read | [S16] memory data exfiltrated through Citrix NetScaler out-of-bounds memory → vulnerability<br>[S16] maximum → attempts<br>[S43] Out-of-bounds → vulnerability VMware ESX |
| 42 | `send` | 5 | Mention→Mention (5) | send; sends | [S07] unauthenticated attacker → specially crafted packets<br>[S08] attacker → JWT<br>[S45] unauthenticated attacker → specially crafted packets |
| 43 | `Based on` | 4 | Mention→Mention (4) | Based on | [S01] Prioritizing Security Updates → risk<br>[S19] Prioritizing Security Updates → risk<br>[S19] Prioritizing Security Updates → Risk A Binding Operational Directive |
| 44 | `accepts` | 4 | Mention→Mention (4) | accept; accepted; accepts | [S08] issuer validation → unregistered certificates<br>[S08] ValidateTokenIssuer → Issuer '<br>[S08] method → issuer returns to caller instead of throwing SecurityTokenException exception |
| 45 | `address` | 4 | Mention→Mention (3); Product→Mention (1) | address | [S43] VMware ESX → multiple vulnerabilities<br>[S43] vCenter → multiple vulnerabilities<br>[S43] Workstation → multiple vulnerabilities |
| 46 | `analyst assign greater value` | 4 | Mention→Mention (4) | analyst assign greater value; analyst assign greater value to | [S50] asset to analyst 's organization → measured in terms of Confidentiality is<br>[S50] asset to analyst 's organization → measured in terms of Integrity is<br>[S50] asset to analyst 's organization → measured in terms of Availability That is |
| 47 | `applies whether` | 4 | Mention→Mention (4) | applies whether | [S50] mapping between quantitative scores → Threat are assessed<br>[S50] mapping between quantitative scores → Environmental metric groups are assessed<br>[S50] mapping between qualitative scores → Threat are assessed |
| 48 | `apply to loss of` | 4 | Mention→Mention (4) | apply to loss of | [S50] confidentiality → integrity<br>[S50] Integrity impact metrics → integrity<br>[S52] confidentiality → integrity |
| 49 | `are across` | 4 | Mention→Mention (4) | are across | [S50] vulnerability → user environments<br>[S50] vulnerability → user environments<br>[S51] vulnerability → user environments |
| 50 | `are across user environments over` | 4 | Mention→Mention (4) | are across user environments over | [S50] vulnerability → time<br>[S50] vulnerability → time<br>[S51] vulnerability → time |
| 51 | `are assigned` | 4 | Mention→Mention (4) | are assigned; is assigned | [S50] Base metrics → values<br>[S50] vector within MacroVector → score of highest severity vector in MacroVector<br>[S50] vector within MacroVector → score of mean from MacroVectors below it |
| 52 | `are exposed such as` | 4 | Mention→Product (2); Mention→Mention (2) | are exposed such as | [S19] asset → CISA 's CDM Program<br>[S19] asset → Cyber Hygiene services<br>[S19] set of assets → CISA 's CDM Program |
| 53 | `are part of` | 4 | Mention→Mention (4) | are part of; is part of | [S44] host 's own outbound network behavior → same review<br>[S51] they → same security scope A vulnerability<br>[S51] device Devices → redundant clusters |
| 54 | `are published` | 4 | Mention→Mention (4) | are published; has published; publish; published | [S19] it → updates<br>[S38] CNA → data<br>[S47] Scores → freely |
| 55 | `are same In` | 4 | Mention→Mention (4) | are same In | [S07] vulnerable component → case<br>[S07] impacted component → case<br>[S39] vulnerable component → case |
| 56 | `are unique to` | 4 | Mention→Mention (4) | are unique to | [S50] vulnerability → user 's environment Base metric values<br>[S51] vulnerability → user 's environment Base metric values<br>[S52] vulnerability → user 's environment |
| 57 | `asset to analyst 's organization assign greater value` | 4 | Mention→Mention (4) | asset to analyst 's organization assign greater value; asset to analyst 's organization assign greater value to | [S50] analyst → measured in terms of Confidentiality is<br>[S50] analyst → measured in terms of Integrity is<br>[S50] analyst → measured in terms of Availability That is |
| 58 | `be Required to` | 4 | Mention→Mention (4) | be Required to | [S50] high privileges → None<br>[S50] Modified Privileges → None<br>[S52] high privileges → None |
| 59 | `be assessed` | 4 | Mention→Mention (4) | be assessed; be assessing | [S50] vulnerable system → relative to vulnerable system<br>[S50] vulnerable system → Therefore<br>[S50] it → Base metrics |
| 60 | `be compatible backwards` | 4 | Mention→Mention (4) | be compatible backwards | [S50] which equivalence set of vectors p in ordering of vectors → compatible with qualitative severity score boundaries from CVSS v3.x<br>[S50] which equivalence set of vectors p in ordering of vectors → compatible<br>[S51] qualitative severity scores → compatible with qualitative severity score boundaries from CVSS v3.x |
| 61 | `be considered` | 4 | Mention→Mention (4) | be considered | [S50] exploiting vulnerability → Low value for Attack Complexity independent of attacker 's knowledge Furthermore<br>[S50] exploiting vulnerability → Low value for Attack Complexity independent of capabilities Furthermore<br>[S51] resulting CVSS-BTE score → closer to Risk Environmental |
| 62 | `be exploited at will of` | 4 | Mention→Mention (4) | be exploited at will of | [S07] vulnerability → attacker<br>[S39] vulnerability → attacker<br>[S42] vulnerability → attacker |
| 63 | `be identified by` | 4 | Mention→Product (2); Mention→Mention (2) | be identified by | [S01] those → Common Vulnerabilities listed in CISA 's KEV Catalog on publicly exposed assets<br>[S01] those → exposures<br>[S28] specifically those → Common Vulnerabilities listed in CISA 's KEV Catalog on publicly exposed assets |
| 64 | `be launched from` | 4 | Mention→Mention (4) | be launched from | [S50] attack → same shared proximity<br>[S52] attack → same shared physical network<br>[S52] attack → same shared physical or logical network |
| 65 | `be listed in CISA 's KEV Catalog on` | 4 | Mention→Mention (4) | be listed in CISA 's KEV Catalog on | [S01] common vulnerabilities → publicly exposed assets<br>[S01] exposures → publicly exposed assets<br>[S28] common vulnerabilities → publicly exposed assets |
| 66 | `be perform` | 4 | Mention→Mention (4) | be perform | [S51] targeted user → specific<br>[S51] targeted user → attacker 's payload<br>[S51] targeted user → attacker 's payload user 's interactions |
| 67 | `be posed by` | 4 | Mention→Mention (4) | be posed by | [S16] emerging threat → AI-enabled attackers<br>[S50] relative severity → vulnerability to user 's environment at specific point in time Assessment of Threat<br>[S50] relative severity → vulnerability to user 's environment at specific point in time Assessment of Environmental metrics |
| 68 | `be required into consideration when` | 4 | Mention→Mention (4) | be required into consideration when | [S50] effort → applying mitigations remediation When calculating Vulnerability Response Effort<br>[S50] effort → applying scheduling remediation When calculating Vulnerability Response Effort<br>[S51] effort → applying mitigations |
| 69 | `be used to calculate` | 4 | Mention→Mention (4) | be used to calculate | [S50] metrics → them<br>[S50] metrics → them Regarding prioritization<br>[S51] metrics → them |
| 70 | `consider` | 4 | Mention→Mention (4) | consider; considers; is considered | [S50] Only increase in access → vulnerability<br>[S51] therefore they are part of same security scope A vulnerability → impact to Subsequent System<br>[S52] organizational vulnerability management process → factors |
| 71 | `created Stakeholder-Specific Vulnerability Categorization system` | 4 | Product→Mention (4) | created Stakeholder-Specific Vulnerability Categorization system; created Stakeholder-Specific Vulnerability Categorization system in | [S53] Carnegie Mellon University 's Software Engineering Institute in collaboration with CISA → 2019 Stakeholder-Specific Vulnerability Categorization<br>[S53] Carnegie Mellon University 's Software Engineering Institute in collaboration with CISA → 2019 prevalence of affected product in singular system<br>[S53] Carnegie Mellon University 's Software Engineering Institute in collaboration with CISA → Stakeholder-Specific Vulnerability Categorization |
| 72 | `depends on sub-formulas for` | 4 | Mention→Mention (4) | associated depends on sub-formulas for; depends on sub-formulas for | [S52] Base Score formula → Impact Sub-Score<br>[S52] Environmental Score formula → Modified Impact Sub-Score<br>[S52] Environmental Score formula → ModifiedImpact |
| 73 | `do reflect` | 4 | Mention→Mention (4) | do reflect; reflect | [S50] Exploitability metrics → ease means<br>[S50] Exploitability metrics → technical means<br>[S51] low → significant differences between conditions currently compressed in definition of high complexity |
| 74 | `exploitation in-the-wild publication of details occur` | 4 | Mention→Mention (4) | exploitation in-the-wild publication of details occur; exploitation in-the-wild publication of details occur proviso | [S40] to publish → earlier<br>[S40] to publish → proviso<br>[S41] to publish → earlier |
| 75 | `exploitation third-party publication of details occur` | 4 | Mention→Mention (4) | exploitation third-party publication of details occur; exploitation third-party publication of details occur proviso | [S40] to publish → earlier<br>[S40] to publish → proviso<br>[S41] to publish → earlier |
| 76 | `gives attacker` | 4 | Mention→Mention (4) | gives attacker | [S17] platform estates compromised vCenter instance → reach<br>[S54] unpatched vulnerability → guest account remotely<br>[S54] unpatched vulnerability → guest account easily |
| 77 | `has exploited issue by` | 4 | Mention→Mention (4) | has exploited issue by; have exploited issue by | [S09] we → leveraging Database Line-of-Business system<br>[S09] we → leveraging ObjectDataProvider<br>[S09] VulnCheck analysis → leveraging DotNetAssembly LOB system |
| 78 | `includes further discussion of CVSS guidelines on scoring` | 4 | Mention→Mention (4) | includes further discussion of CVSS guidelines on scoring; includes further discussion of CVSS guidelines on scoring rubrics | [S50] User Guide → v4<br>[S50] User Guide → v4<br>[S52] User Guide → companion to Specification |
| 79 | `is unpatched when` | 4 | Mention→Mention (4) | is unpatched when | [S07] typical vulnerability → initially published Workarounds<br>[S07] typical vulnerability → initially published hotfixes<br>[S42] typical vulnerability → initially published Workarounds prioritization |
| 80 | `meet` | 4 | Mention→Mention (4) | meet | [S01] catalog → specified criteria<br>[S28] catalog → specified criteria<br>[S38] CVE Records → specific threat characteristics |
| 81 | `protect` | 4 | Mention→Mention (4) | protect; protects | [S07] us → customers<br>[S17] something → access to other systems<br>[S39] us → customers |
| 82 | `recommends remediating Track vulnerabilities within` | 4 | Organization→Mention (4) | recommends remediating Track vulnerabilities within | [S53] available CISA → standard<br>[S53] CISA → standard changes<br>[S54] CISA → standard |
| 83 | `reflects characteristics of` | 4 | Mention→Mention (4) | reflect characteristics of; reflects characteristics of | [S50] Threat group → vulnerability<br>[S50] Exploitability metrics → thing<br>[S51] Threat group → vulnerability |
| 84 | `represent characteristics of` | 4 | Mention→Mention (4) | represent characteristics of; represents characteristics of | [S50] they → thing<br>[S52] Environmental group → vulnerability<br>[S52] they → thing |
| 85 | `required per` | 4 | Mention→Mention (4) | required per | [S29] Forensic triage → BOD-26-04<br>[S30] Forensic triage → BOD-26-04<br>[S31] Forensic triage → BOD-26-04 |
| 86 | `see` | 4 | Mention→Mention (4) | see | [S09] we → BDC LobSystem definition<br>[S10] you → above<br>[S44] we → pattern |
| 87 | `stay` | 4 | Mention→Mention (4) | stay | [S51] definition of automatable → materially same as definition of decision point by same name in stakeholder specific vulnerability categorization heuristics<br>[S51] definition of automatable → currently same as definition of decision point by same name in stakeholder specific vulnerability categorization heuristics<br>[S51] definition of automatable → same as definition of decision point by same name in stakeholder specific vulnerability categorization heuristics |
| 88 | `subvert` | 4 | Mention→Mention (4) | subvert | [S51] Successful exploitation of vulnerability requires targeted user to perform specific → protection mechanisms<br>[S51] Successful exploitation of vulnerability requires targeted user to perform conscious interactions with vulnerable component → protection mechanisms<br>[S51] Successful exploitation of vulnerability requires targeted user to perform attacker 's payload → protection mechanisms |
| 89 | `to provide` | 4 | Mention→Mention (4) | to provide | [S50] consumers → initial response to impact of vulnerabilities for deployed products in infrastructure<br>[S50] consumers → initial response to impact of vulnerabilities for services in infrastructure<br>[S51] consumers → initial response to impact of vulnerabilities for deployed products in infrastructure |
| 90 | `to publish occur` | 4 | Mention→Mention (4) | to publish occur | [S40] exploitation in-the-wild publication of details → proviso<br>[S40] exploitation third-party publication of details → proviso<br>[S41] exploitation in-the-wild publication of details → proviso |
| 91 | `to publish occur proviso` | 4 | Mention→Mention (4) | to publish occur proviso | [S40] exploitation in-the-wild publication of details → earlier<br>[S40] exploitation third-party publication of details → earlier<br>[S41] exploitation in-the-wild publication of details → earlier |
| 92 | `used Hermes Agent with DeepSeek` | 4 | Mention→Mention (4) | used Hermes Agent with; used Hermes Agent with DeepSeek; used Hermes Agent with DeepSeek as | [S16] actor → Based on analysis of session logs<br>[S16] actor → Based on analysis of configuration files<br>[S16] actor → DeepSeek |
| 93 | `'s` | 3 | Mention→Mention (3) | 's | [S10] it → familiar<br>[S17] it → this<br>[S49] what → new |
| 94 | `Defused warned` | 3 | Mention→Product (2); Mention→CVE (1) | Defused warned | [S18] Threat intelligence firm → are using now Rapid7 POC<br>[S18] Threat intelligence firm → are using Rapid7 POC for CVE-2026-55040 against SharePoint honeypots Microsoft<br>[S18] Threat intelligence firm → are using Rapid7 POC |
| 95 | `Defused warned on X that attackers` | 3 | Mention→Product (2); Mention→CVE (1) | Defused warned on X that attackers | [S18] Threat intelligence firm → are using now Rapid7 POC<br>[S18] Threat intelligence firm → are using Rapid7 POC for CVE-2026-55040 against SharePoint honeypots Microsoft<br>[S18] Threat intelligence firm → are using Rapid7 POC |
| 96 | `Is exposed` | 3 | Mention→Mention (3) | Is exposed; are exposed; is exposed | [S19] vulnerable asset → publicly<br>[S19] system → publicly<br>[S46] IKE → unnecessarily |
| 97 | `Runs` | 3 | Mention→Mention (3) | Runs; run; runs | [S10] LosFormatted TypeConfuseDelegate → calc<br>[S10] File Manager → files<br>[S51] they → what instructions |
| 98 | `added CVE-2026-55040 to` | 3 | Organization→Mention (3) | added CVE-2026-55040 to; adds CVE-2026-55040 to | [S17] CISA → Known Exploited Vulnerabilities catalogue<br>[S40] CISA → Known Exploited Vulnerabilities<br>[S41] CISA → KEV catalog |
| 99 | `aim to compromise` | 3 | Mention→Mention (3) | aim to compromise | [S19] nation-states → U.S. critical infrastructure to steal sensitive information<br>[S19] nation-states → U.S. critical infrastructure disrupt operations<br>[S19] nation-states → U.S. critical infrastructure undermine national security |
| 100 | `are defined` | 3 | Mention→Mention (3) | are defined; defined; has defined | [S10] we → MethodInstance<br>[S17] same targeting logic → 2026 's threat landscape<br>[S50] associated metric value in abbreviated form → colon |
| 101 | `are managed by` | 3 | Mention→Mention (3) | are managed by | [S07] both → same security authority Confidentiality metric measures<br>[S39] both → same security authority Confidentiality metric measures<br>[S42] both → same security authority Confidentiality metric measures |
| 102 | `are most` | 3 | Mention→Mention (3) | are most; is most | [S17] defenders → dependent<br>[S47] attacks → likely limited remediation effort<br>[S50] availability → important business function |
| 103 | `are publishing technical analysis of` | 3 | Mention→Mention (2); Mention→CVE (1) | are publishing technical analysis of; are publishing technical analysis of vulnerability | [S08] we → Today<br>[S08] we → vulnerability<br>[S09] we → CVE-2026-63520 analysis |
| 104 | `assess` | 3 | Mention→Mention (3) | assess | [S41] customers → exposure to authentication bypass vulnerability with authenticated vulnerability checks available in July 15 content release Upcoming webinar Interested in AI tooling leveraged throughout research process<br>[S51] analysts → network<br>[S51] analysts → Adjacent |
| 105 | `be Local in` | 3 | Mention→Mention (3) | be Local in | [S51] library mentioned in previous example → case<br>[S51] only operates on local files → case<br>[S51] attack vector → case |
| 106 | `be Sharing without` | 3 | Mention→Mention (3) | be Sharing without | [S15] Screen → valid credentials Description<br>[S55] Screen → valid credentials Description<br>[S56] Screen → valid credentials Description |
| 107 | `be access` | 3 | Mention→Mention (3) | be access | [S20] Internet-facing host → network<br>[S20] system → network<br>[S52] high privileges → particular function |
| 108 | `be achieve` | 3 | Mention→Mention (3) | be achieve | [S09] NET type available in Global Assembly Cache set arbitrary properties on instances → OS command execution<br>[S09] leverage property-setter side-effects → OS command execution<br>[S54] use of multiple vulnerabilities → overall outcome |
| 109 | `be based on` | 3 | Mention→Mention (3) | be based on | [S50] very different meanings → metrics used to calculate them Regarding prioritization<br>[S51] very different meanings → metrics used to calculate them Regarding prioritization<br>[S51] to have rapid response times for transactional purposes → regulatory requirements |
| 110 | `be containing` | 3 | Mention→Mention (3) | be contained; be containing | [S08] outer token 's nameid claim → either attacker controlled Windows Security Identifier<br>[S08] outer token 's nameid claim → either attacker controlled attacker<br>[S16] actor → connectivity tests |
| 111 | `be corroborated by` | 3 | Mention→Mention (3) | be corroborated by | [S07] vulnerability → research<br>[S42] vulnerability → research<br>[S52] vulnerability → research |
| 112 | `be determine` | 3 | Organization→Mention (3) | be determine | [S38] CISA ADP → missing CVSS<br>[S38] CISA ADP → CWE<br>[S38] CISA ADP → CPE metric |
| 113 | `be found` | 3 | Mention→Mention (3) | be found | [S10] trial of Canary Intelligence → request<br>[S10] Target Intelligence → request<br>[S10] Exploit & Vulnerability Intelligence products Weekly Initial Access Intelligence exploits → request |
| 114 | `be identifying` | 3 | Mention→Mention (2); Product→Mention (1) | be identifying | [S40] AD In example with identifying information redacted to bypass authentication on target SharePoint site to assume identity of user → SharePoint site administrator user<br>[S40] AD In example with identifying information Rapid7 Labs proof-of-concept script discovers potential SharePoint users via SID enumeration → SharePoint site administrator user<br>[S40] AD In example with identifying information then → SharePoint site administrator user |
| 115 | `be increasing` | 3 | Mention→Mention (3) | be increasing | [S51] having lower impact on embedding implementation → impacts<br>[S51] having → impacts<br>[S51] having with high privileges → impacts |
| 116 | `be mentioned in` | 3 | Mention→Mention (3) | be mentioned in | [S51] library → previous example<br>[S51] only operates on local files → previous example<br>[S51] attack vector → previous example |
| 117 | `be outlining` | 3 | Mention→Mention (3) | be outlining | [S51] additional language → specific product versions<br>[S51] additional language → platforms<br>[S51] additional language → operating system |
| 118 | `be overcome` | 3 | Mention→Mention (3) | be overcome | [S19] enough attempts → obstacles<br>[S50] attacker → conditions<br>[S54] enough attempts → obstacles |
| 119 | `be participate in successful compromise` | 3 | Mention→Mention (3) | be participate in successful compromise | [S07] requirement for user other than attacker → vulnerable component<br>[S39] requirement for user other than attacker → vulnerable component<br>[S42] requirement for user other than attacker → vulnerable component |
| 120 | `be present present on` | 3 | Mention→Mention (3) | be present present on | [S51] vulnerability → multiple product versions<br>[S51] vulnerability → platforms<br>[S51] vulnerability → operating systems |
| 121 | `be protected by` | 3 | Mention→Mention (3) | be protected by | [S50] any/all files → vulnerable system<br>[S50] any/all files → Subsequent System<br>[S52] any/all files → impacted component |
| 122 | `be provided in` | 3 | Mention→Organization (3) | be provided in | [S07] information → Microsoft Knowledge Base<br>[S39] information → Microsoft Knowledge Base<br>[S42] information → Microsoft Knowledge Base |
| 123 | `be providing` | 3 | Mention→Mention (3) | be provided; be providing | [S16] agent → orchestration<br>[S17] network security perimeter → remote access to corporate network<br>[S17] VPN concentrator → remote access to corporate network |
| 124 | `be recognized as` | 3 | Mention→Mention (3) | be recognized as | [S07] impact → undesirable<br>[S42] impact → undesirable<br>[S52] impact → undesirable |
| 125 | `be recognized as undesirable without specific details For` | 3 | Mention→Mention (3) | be recognized as undesirable without specific details For | [S07] impact → example<br>[S42] impact → example<br>[S52] impact → example |
| 126 | `be resulting from` | 3 | Mention→Mention (3) | be resulting from | [S14] damage → inaccuracy of incompleteness of information<br>[S50] impacted system → successfully exploited vulnerability<br>[S52] impact to availability of impacted component → successfully exploited vulnerability |
| 127 | `be serving as` | 3 | Mention→Mention (3) | be serving as | [S54] Wireshark → PoC for packet replay attacks on ethernet Shared<br>[S54] Wireshark → PoC for packet replay attacks on Wi-Fi<br>[S54] Wireshark → PoC for packet replay attacks on observable |
| 128 | `be support` | 3 | Mention→Mention (2); Mention→Organization (1) | be support; be supporting | [S19] Update agency vulnerability management processes → ongoing vulnerability remediation based on vulnerabilities identified in CVE database<br>[S19] procedures → ongoing vulnerability remediation based on vulnerabilities identified in CVE database<br>[S41] requests → information Microsoft requests |
| 129 | `becomes` | 3 | Mention→Mention (3) | becomes; has become | [S17] on-premises SharePoint Server → sustained target<br>[S39] remediation → final<br>[S42] remediation → final |
| 130 | `consume` | 3 | Mention→Mention (3) | consume | [S42] attacks → network bandwidth<br>[S50] attacks → network bandwidth<br>[S52] attacks → network bandwidth |
| 131 | `describes conditions beyond` | 3 | Mention→Mention (3) | describes conditions beyond | [S07] this metric → attacker 's control<br>[S39] this metric → attacker 's control<br>[S42] this metric → attacker 's control |
| 132 | `differ on` | 3 | Mention→Mention (3) | differ on | [S51] Base metrics → different product versions<br>[S51] Base metrics → platforms<br>[S52] reports → impacts |
| 133 | `enable` | 3 | Mention→Mention (3) | enable | [S07] which → remote code execution Acknowledgements<br>[S45] which → remote code execution<br>[S50] vulnerable system → attack |
| 134 | `enable consumer to customize` | 3 | Mention→Mention (3) | enable consumer to customize | [S50] confidentiality → assessment<br>[S50] integrity → assessment<br>[S50] availability → assessment |
| 135 | `exploit along with Snort rules` | 3 | Mention→Mention (3) | exploit along with Snort rules | [S10] complete RCE → encrypted PCAPs<br>[S10] complete RCE → unencrypted PCAPs and ASM queries<br>[S10] complete RCE → ASM queries |
| 136 | `exploit along with Suricata` | 3 | Mention→Mention (3) | exploit along with Suricata | [S10] complete RCE → encrypted PCAPs<br>[S10] complete RCE → unencrypted PCAPs and ASM queries<br>[S10] complete RCE → ASM queries |
| 137 | `exploit along with version scanner` | 3 | Mention→Mention (3) | exploit along with version scanner | [S10] complete RCE → encrypted PCAPs<br>[S10] complete RCE → unencrypted PCAPs and ASM queries<br>[S10] complete RCE → ASM queries |
| 138 | `exposes administrative control point at` | 3 | Mention→Mention (3) | exposes administrative control point at | [S44] it → once including ability to clone<br>[S44] it → once including ability to export<br>[S44] it → once including ability to delete virtual machine disks |
| 139 | `give` | 3 | Mention→Mention (3) | give; gives | [S17] data warehouses → attacker standing access to substantial share of organisation 's cloud data estate<br>[S54] credentials → adversary<br>[S54] exploit → threat actor limited control |
| 140 | `has advanced knowledge of target system` | 3 | Mention→Mention (3) | has advanced knowledge of target system; has advanced knowledge of target system For | [S50] attacker → including general configuration<br>[S50] attacker → including default defense mechanisms<br>[S50] attacker → example |
| 141 | `has analysis of` | 3 | Mention→Mention (3) | has analysis of | [S10] team → SharePoint RCE chain<br>[S16] our → session logs<br>[S16] our → configuration files |
| 142 | `has released` | 3 | Mention→Mention (2); Vendor→Mention (1) | has released; is released; released | [S11] Broadcom → emergency patch<br>[S46] same region of memory → double free condition<br>[S46] Microsoft → there is |
| 143 | `identified` | 3 | Mention→Mention (3) | identified; was identified | [S16] we → limited usage<br>[S16] Langflow Exploitation DeepSeek → Langflow vulnerability<br>[S50] vulnerability → means |
| 144 | `identify in` | 3 | Mention→Mention (3) | identify in | [S51] analyst → form of machine readable list of vulnerabilities as CVE IDs complete list of specific related vulnerabilities<br>[S51] analyst → form of machine parsable list of vulnerabilities as CVE IDs or CWEs complete list of specific related vulnerabilities<br>[S51] analyst → form of machine readable list of vulnerabilities as CWEs complete list of specific related vulnerabilities |
| 145 | `implement` | 3 | Mention→Mention (3) | implement; implements | [S08] SPJsonWebSecurityTokenHandlerV2 class → validation logic<br>[S08] base class SPJsonWebSecurityBaseTokenHandlerV2 → validation logic<br>[S08] SharePoint → own validation logic |
| 146 | `install` | 3 | Mention→Mention (2); Mention→CVE (1) | install; installs | [S07] vulnerability Customers → security<br>[S44] malicious cron job → reverse_ssh<br>[S45] security teams → CVE-2026-33824 security |
| 147 | `is applicable to` | 3 | Mention→Mention (3) | is applicable to | [S51] hypothetical vulnerability → multiple operating systems produced by same vendor on legacy operating system different product versions<br>[S51] hypothetical vulnerability → multiple operating systems produced by same vendor on legacy operating system platforms<br>[S51] hypothetical vulnerability → multiple operating systems produced by same vendor on legacy operating system operating systems For example |
| 148 | `is common for` | 3 | Mention→Mention (3) | is common for | [S51] it → vulnerability to be present on multiple product versions<br>[S51] it → vulnerability to be present on platforms<br>[S51] it → vulnerability to be present on operating systems |
| 149 | `is due to` | 3 | Mention→Mention (3) | is due to | [S09] this → unrestricted subsystem<br>[S41] vulnerability → unsafe<br>[S52] this → small inaccuracies |
| 150 | `is form of` | 3 | Mention→Mention (3) | is form of | [S19] security-based → limited control<br>[S19] physical to achieve total control denial-of-service attack → limited control<br>[S54] physical to achieve total control denial-of-service attack → limited control |
| 151 | `is more` | 3 | Mention→Mention (2); CVE→Mention (1) | is more | [S17] operational consequence of CVE-2026-20349 → significant Zero Trust Network Access deployments<br>[S48] pulling file once per day → efficient<br>[S48] loading scores into database joining against asset inventory feeding dashboard → efficient |
| 152 | `is represented` | 3 | Mention→Mention (3) | is represented; represent | [S08] Name ID → SharePoint user<br>[S52] CVSS score → Temporal metrics<br>[S52] CVSS score → Environmental metrics |
| 153 | `is unauthorized prior to` | 3 | Mention→Mention (3) | is unauthorized prior to | [S07] attacker → attack<br>[S39] attacker → attack<br>[S42] attacker → attack vulnerability |
| 154 | `is used to record` | 3 | Mention→Mention (3) | is used to record | [S50] it → CVSS metric information<br>[S52] it → CVSS metric information in concise form set of CVSS metrics commonly<br>[S52] it → CVSS metric information in concise form set of CVSS metrics |
| 155 | `local low privileged attacker represents direct serious loss of` | 3 | Mention→Mention (3) | local low privileged attacker represents direct serious loss of | [S51] Gaining access to password → confidentiality<br>[S51] Gaining access to password → integrity<br>[S51] Gaining access to password → availability |
| 156 | `makes accessible via` | 3 | Mention→Mention (3) | makes accessible via | [S47] EPSS → CSV<br>[S47] EPSS → API<br>[S47] EPSS → github repo |
| 157 | `manages` | 3 | Mention→Mention (3) | manages | [S17] platform → virtualisation<br>[S17] something → other systems<br>[S51] security team → environment |
| 158 | `marked exploit development directories as` | 3 | Mention→Mention (3) | marked exploit development directories as | [S16] actor → trusted granting full access to read<br>[S16] actor → trusted granting full access modify<br>[S16] actor → trusted granting full access execute code |
| 159 | `meet to determine` | 3 | Mention→Mention (3) | meet to determine | [S53] internal groups → overall response notification internally Typically<br>[S53] internal groups → overall response notification externally<br>[S54] internal groups → overall response notification externally |
| 160 | `obtain` | 3 | Mention→Mention (3) | obtain; obtained | [S10] you → SID<br>[S10] you → user principal name<br>[S16] Exploit Acquisition DeepSeek → public n8n |
| 161 | `overlaps consistent with` | 3 | Mention→Mention (3) | overlaps consistent with | [S12] broader campaign including global exploitation activity → suspected Chinese-nexus APT<br>[S12] broader campaign including infrastructure → suspected Chinese-nexus APT<br>[S12] broader campaign including behavioral → suspected Chinese-nexus APT |
| 162 | `participate` | 3 | Mention→Mention (3) | participate | [S07] separate user → vulnerable system<br>[S39] separate user → vulnerable system<br>[S42] separate user → vulnerable system |
| 163 | `protect customers through` | 3 | Mention→Mention (3) | protect customers through | [S07] us → coordinated vulnerability disclosure<br>[S39] us → coordinated vulnerability disclosure<br>[S42] us → coordinated vulnerability disclosure |
| 164 | `publish Qualitative Severity Ratings` | 3 | Mention→Mention (3) | publish Qualitative Severity Ratings; publish Qualitative Severity Ratings from; publish Qualitative Severity Ratings in | [S50] Other vendors → advisories product security advisories<br>[S50] Other vendors → product security advisories<br>[S50] Other vendors → CVSS Specification Document product security advisories |
| 165 | `recommends` | 3 | Organization→Mention (3) | recommends | [S53] available CISA → remediating Track vulnerabilities<br>[S53] CISA → remediating<br>[S54] CISA → remediating Track vulnerabilities |
| 166 | `refers to limiting disclosure as well as preventing access by or disclosure to` | 3 | Mention→Mention (3) | refers to limiting disclosure as well as preventing access by or disclosure to | [S07] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures<br>[S39] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures<br>[S42] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures |
| 167 | `refers to limiting information access to only authorized users` | 3 | Mention→Mention (3) | refers to limiting information access to only authorized users | [S07] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures<br>[S39] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures<br>[S42] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures |
| 168 | `refers to preventing access by` | 3 | Mention→Mention (3) | refers to preventing access by | [S07] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures<br>[S39] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures<br>[S42] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures |
| 169 | `refers to preventing access disclosure to` | 3 | Mention→Mention (3) | refers to preventing access disclosure to | [S07] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures<br>[S39] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures<br>[S42] impact to confidentiality of information resources managed by software component due to successfully exploited vulnerability Confidentiality → same security authority Confidentiality metric measures |
| 170 | `refers to trustworthiness of information` | 3 | Mention→Mention (3) | refers to trustworthiness of information | [S07] integrity → There is complete loss of protection For example<br>[S39] integrity → There is complete loss of protection For example<br>[S52] impact to integrity of successfully exploited vulnerability Integrity → metric measures |
| 171 | `refers to veracity` | 3 | Mention→Mention (3) | refers to veracity | [S07] integrity → There is complete loss of protection For example<br>[S39] integrity → There is complete loss of protection For example<br>[S52] impact to integrity of successfully exploited vulnerability Integrity → metric measures |
| 172 | `requiring` | 3 | Mention→Mention (3) | is required; requiring | [S42] successful exploitation → significant effort<br>[S42] successful exploitation → precise conditions<br>[S46] IKE → 4500 |
| 173 | `resides in` | 3 | Mention→Mention (3) | resides in | [S08] vulnerability → SPJsonWebSecurityTokenHandlerV2 class<br>[S08] vulnerability → base class SPJsonWebSecurityBaseTokenHandlerV2<br>[S17] vulnerability → SharePoint 's JSON Web Token validation path |
| 174 | `returns` | 3 | Mention→Mention (3) | returned; returns | [S08] it → AAAA<br>[S16] actor → attempts<br>[S52] Roundup → smallest number |
| 175 | `supports` | 3 | Mention→Mention (3) | does support; supports | [S46] Sentrium → organisations<br>[S50] IT asset → business function<br>[S51] implementation → mode |
| 176 | `take a second pass of analysis to determine` | 3 | Organization→Mention (3) | take a second pass of analysis to determine | [S38] CISA ADP → missing CVSS<br>[S38] CISA ADP → CWE<br>[S38] CISA ADP → CPE metric |
| 177 | `take malicious actions in` | 3 | Mention→Mention (3) | take malicious actions in | [S51] attacker → system still<br>[S51] attacker → system by impersonating user of same privileges leading to Repudiation impact<br>[S51] attacker → system |
| 178 | `upload` | 3 | Mention→Mention (3) | upload | [S09] attacker → malicious<br>[S09] we → malicious BDC model<br>[S09] we → malicious BDC model |
| 179 | `was addressed with` | 3 | Mention→CVE (3) | was addressed with | [S15] authentication issue → improved state management CVE-2026-65400<br>[S55] authentication issue → improved state management CVE-2026-65400<br>[S56] authentication issue → improved state management CVE-2026-65400 |
| 180 | `we achieved` | 3 | Mention→Mention (2); CVE→Mention (1) | we achieved | [S10] NET type → fully authenticated deserialization<br>[S10] method → fully authenticated deserialization<br>[S10] pairing with CVE-2026-55040 authentication bypass → fully authenticated deserialization |
| 181 | `August 21 2026 arrives Cybersecurity News Stories August 21 2026` | 2 | Mention→Mention (2) | August 21 2026 arrives Cybersecurity News Stories August 21 2026; Cybersecurity arrives Cybersecurity News Stories August 21 2026 | [S17] August 21 2026 → This week 's<br>[S17] Cybersecurity → This week 's |
| 182 | `CISA has added flaw to catalog of` | 2 | Mention→Mention (2) | CISA has added flaw to catalog of | [S45] it → actively exploited vulnerabilities flag<br>[S45] it → ordered flag |
| 183 | `Is vulnerability as identified by` | 2 | Mention→Mention (2) | Is vulnerability as identified by | [S19] KEV Status → common vulnerabilities<br>[S19] KEV Status → exposures |
| 184 | `SSVC decision points be updated` | 2 | Mention→Mention (1); Product→Mention (1) | SSVC decision points be updated | [S38] CVSS provided by originating CNA if CVE Record is updated by originating CNA to provide information → shortly thereafter<br>[S38] CVSS provided by CISA ADP if CVE Record is updated by originating CNA to provide information → shortly thereafter |
| 185 | `SSVC decision points be updated shortly thereafter by CISA ADP Additional information about` | 2 | Mention→Product (1); Product→Product (1) | SSVC decision points be updated shortly thereafter by CISA ADP Additional information about | [S38] CVSS provided by originating CNA if CVE Record is updated by originating CNA to provide information → CISA ADP including contact information<br>[S38] CVSS provided by CISA ADP if CVE Record is updated by originating CNA to provide information → CISA ADP including contact information |
| 186 | `Sign up` | 2 | Mention→Mention (2) | Sign up | [S10] practitioner community → enjoy comprehensive vulnerability data<br>[S10] practitioner community → request |
| 187 | `Sign up for VulnCheck community` | 2 | Mention→Mention (2) | Sign up for VulnCheck community | [S10] practitioner community → enjoy comprehensive vulnerability data<br>[S10] practitioner community → request |
| 188 | `Sign up to get` | 2 | Mention→Mention (2) | Sign up to get; Sign up today to get | [S10] practitioner community → here free access to VulnCheck KEV<br>[S10] practitioner community → here free access to VulnCheck KEV |
| 189 | `Sign up today` | 2 | Mention→Mention (2) | Sign up today | [S10] practitioner community → enjoy comprehensive vulnerability data<br>[S10] practitioner community → request |
| 190 | `accessed` | 2 | Mention→Mention (2) | accessed | [S16] actor → DeepSeek traceability<br>[S16] actor → Qwen traceability |
| 191 | `account for` | 2 | Mention→Mention (2) | account for; accounts for | [S51] analyst → reasonable worst-case scenario<br>[S53] vulnerability analysis methodology → vulnerability 's exploitation status |
| 192 | `achieve remote code execution without` | 2 | Mention→Mention (1); Mention→Organization (1) | achieve remote code execution without | [S17] exploit → credentials<br>[S17] exploit → user interaction CISA |
| 193 | `acknowledges` | 2 | Organization→Mention (1); Organization→Product (1) | acknowledges | [S41] Rapid7 → disclosure schedule<br>[S41] Rapid7 → requests supporting information Microsoft requests |
| 194 | `acts as critical bridge between` | 2 | Mention→Mention (2) | acts as critical bridge between | [S40] SharePoint → internal users<br>[S41] SharePoint → internal users |
| 195 | `adjusts scores of` | 2 | Mention→Mention (2) | adjusts scores of | [S50] small score modification factor → vectors<br>[S51] small score modification factor → vectors |
| 196 | `align to mission space For` | 2 | Organization→Organization (1); Mention→Organization (1) | align to mission space For | [S53] email vulnerability@cisa.dhs.gov → CISA SSVC questions<br>[S53] include → CISA SSVC questions |
| 197 | `allow attacker` | 2 | Mention→Mention (2) | allow attacker | [S18] exploiting vulnerability → modify data<br>[S39] exploiting vulnerability → modify data |
| 198 | `allow attacker to disclose` | 2 | Mention→Mention (2) | allow attacker to disclose | [S18] exploiting vulnerability → files<br>[S39] exploiting vulnerability → files |
| 199 | `allows call to` | 2 | Mention→Mention (2) | allows call to | [S08] this → SPJsonWebSecurityBaseTokenHandlerV2.ValidateActorIsSelfIssuer to succeed nameid<br>[S08] this → SPJsonWebSecurityBaseTokenHandlerV2.ValidateActorIsSelfIssuer to succeed signature |
| 200 | `allows unauthorized attacker to execute` | 2 | Mention→Mention (1); Product→Mention (1) | allows unauthorized attacker to execute | [S33] Information Double free in Windows IKE Extension → code<br>[S35] Required CVE Record Information Improper input validation in Microsoft Office SharePoint → code |
| 201 | `are affected by` | 2 | Mention→Mention (2) | are affected by; is affected by | [S43] to execute code on host Non VMXNET3 virtual adapters → issue<br>[S51] system → vulnerability |
| 202 | `are assigned values by` | 2 | Mention→Mention (2) | are assigned values by | [S50] Base metrics → analyst<br>[S52] Base metrics → analyst |
| 203 | `are combined which to form` | 2 | Mention→Mention (2) | are combined which to form | [S51] vulnerabilities → chained resulting score along with chained score<br>[S51] vulnerabilities → chained resulting score |
| 204 | `are designed` | 2 | Mention→Mention (2) | are designed | [S51] CVSS Base scores → should not be used alone to assess risk<br>[S51] CVSS Base scores → should not be used to assess risk |
| 205 | `are direct responsibility of` | 2 | Mention→Mention (2) | are direct responsibility of | [S50] such systems → system operators<br>[S51] Heuristically → system operators |
| 206 | `are how particular kind of` | 2 | Mention→Mention (2) | are how particular kind of; describe how particular kind of | [S51] one → buffer overflow resulting score<br>[S51] certain kinds of SQL Injection vulnerabilities → buffer overflow |
| 207 | `are leveraged in` | 2 | Mention→Mention (2) | are leveraged in | [S50] Safety metric values → Supplemental metric group<br>[S50] Safety metric values → Environmental metric group |
| 208 | `are subscribed to Reducing` | 2 | Mention→Mention (2) | are subscribed to Reducing | [S28] you → Significant Risk of Known Exploited Vulnerabilities for Cybersecurity<br>[S28] you → Significant Risk of Known Exploited Vulnerabilities for Infrastructure Security Agency |
| 209 | `are used as` | 2 | Mention→Mention (2) | are used as | [S50] characteristics of vulnerability → additional insight into characteristics of vulnerability<br>[S51] characteristics of vulnerability → additional insight into characteristics of vulnerability |
| 210 | `are with` | 2 | Mention→Mention (2) | are with | [S39] you → MSRC Security Update Guide<br>[S42] you → MSRC Security Update Guide |
| 211 | `associated depends on` | 2 | Mention→Mention (2) | associated depends on | [S52] Base Score formula → impact<br>[S52] Base Score formula → Exploitability |
| 212 | `assume` | 2 | Mention→Mention (2) | assume | [S14] therein NCSC-NL → responsibility<br>[S14] Kingdom of the Netherlands → responsibility |
| 213 | `attempt to exploit weakness in` | 2 | Mention→Mention (2) | attempt to exploit weakness in | [S20] Adversaries → Internet-facing host to initially access network<br>[S20] Adversaries → system |
| 214 | `be able` | 2 | Mention→Mention (2) | be able | [S50] prior → able to exploit vulnerability After successful exploitation<br>[S50] prior → able to exploit vulnerability |
| 215 | `be aligned to` | 2 | Mention→Mention (2) | be aligned to | [S50] purpose → safety<br>[S51] purpose → safety |
| 216 | `be attempted to use` | 2 | Mention→Mention (2) | be attempted to use | [S16] actor → Western models<br>[S16] provider-side controls → Western models |
| 217 | `be based on characteristics of` | 2 | Mention→Mention (2) | be based on characteristics of; be based on specific characteristics of | [S51] these → specific environment<br>[S52] individual Base metrics → user 's environment Characteristics |
| 218 | `be based on evidence of` | 2 | Mention→Mention (2) | be based on evidence of | [S01] catalog → active exploitation<br>[S40] catalog → active exploitation |
| 219 | `be built into` | 2 | Mention→Mention (2) | be built into | [S50] protections → vulnerable system<br>[S51] protections → vulnerable component |
| 220 | `be bypass operations as` | 2 | CVE→Mention (2) | be bypass operations as | [S40] leverage CVE-2026-55040 perform → SharePoint site user<br>[S40] leverage CVE-2026-55040 perform → administrator vulnerability |
| 221 | `be calling` | 2 | Mention→Mention (2) | be calling | [S09] client.svc / ProcessQuery endpoint → FindSpecificDefault method to locate malicious gadget chain POST / /<br>[S09] client.svc / ProcessQuery endpoint → FindSpecificDefault method trigger |
| 222 | `be categorized as` | 2 | Mention→Mention (2) | be categorized as | [S50] injuries → Marginal<br>[S50] injuries → worse |
| 223 | `be certified` | 2 | Mention→Mention (2) | be certified | [S19] Federal Risk → environments<br>[S19] Authorization Management Program → environments |
| 224 | `be chained to` | 2 | Mention→Product (1); CVE→CVE (1) | be chained to | [S40] authentication bypass → additional vulnerabilities within authenticated attack surface of target site Rapid7 Labs<br>[S41] CVE-2026-63520 → CVE-2026-55040 |
| 225 | `be checking version via` | 2 | Mention→Mention (2) | be checking version via | [S16] it → curl commands non-responsive<br>[S16] it → curl commands |
| 226 | `be considered highest severity vector of MacroVector Since` | 2 | Mention→Mention (2) | be considered highest severity vector of MacroVector Since; be considered highest severity vector together of MacroVector Since | [S50] they → EQ6 are not independent<br>[S50] they → EQ6 are not independent |
| 227 | `be controlled` | 2 | Mention→Mention (2) | be controlled | [S08] attacker → Windows Security Identifier<br>[S08] attacker → attacker |
| 228 | `be crash` | 2 | Mention→Mention (2) | be crash | [S17] targeted capability → firewall<br>[S17] VPN on demand → firewall |
| 229 | `be deny` | 2 | Mention→Mention (2) | be deny | [S50] ability → service to legitimate users<br>[S50] ability → service |
| 230 | `be deploy reverse SSH tool for` | 2 | Mention→Mention (2) | be deploy reverse SSH tool for | [S11] active campaign → persistence<br>[S11] active campaign → remote access Compromises |
| 231 | `be described in` | 2 | Mention→Mention (2) | be described in | [S50] guidelines → document<br>[S51] guidelines → document |
| 232 | `be emptied exploit directories after` | 2 | Mention→Mention (2) | be emptied exploit directories after | [S16] actor → use logging Vulnerabilities CVEs<br>[S16] actor → disabled Codex conversation logging Vulnerabilities CVEs |
| 233 | `be enforcing` | 2 | Mention→Mention (2) | be enforcing | [S17] simultaneously firewall → network security perimeter providing remote access to corporate network<br>[S17] simultaneously firewall → VPN concentrator |
| 234 | `be enhance` | 2 | Mention→Mention (2) | be enhance | [S14] maintains page → access to information<br>[S14] maintains page → access to security advisories |
| 235 | `be ensure` | 2 | Mention→Mention (2) | be ensure | [S19] Establish internal validation → adherence with Directive to evaluate adherence with Directive<br>[S19] Establish enforcement procedures → adherence with Directive to evaluate adherence with Directive |
| 236 | `be establish` | 2 | Mention→Mention (2) | be establish | [S11] attacker → persistence remote access<br>[S11] attacker → gain remote access |
| 237 | `be execute` | 2 | Mention→Mention (2) | be execute | [S12] vulnerability → arbitrary code<br>[S51] to use credentials → code |
| 238 | `be exploited That` | 2 | Mention→Mention (2) | be exploited That | [S50] vulnerability → ease means<br>[S50] vulnerability → technical means |
| 239 | `be filtering by` | 2 | Mention→Mention (2) | be filtering by | [S48] Basic → score range<br>[S48] Basic → percentile range |
| 240 | `be found below` | 2 | Mention→Mention (2) | be found below | [S43] Response Matrix ' → arbitrary code Response Matrix 3a<br>[S43] Response Matrix ' → 3b |
| 241 | `be identified in` | 2 | Mention→Mention (2) | be identified in | [S19] vulnerabilities → CVE database<br>[S19] KEV catalog → CVE database |
| 242 | `be incorporate` | 2 | Mention→Mention (2) | be incorporate | [S50] standardized method → additional provider-supplied assessment<br>[S51] standardized method → additional provider-supplied assessment |
| 243 | `be install` | 2 | Mention→Mention (2) | be install | [S16] only / model checks → request<br>[S16] connectivity tests → request |
| 244 | `be integrated` | 2 | Mention→Mention (2) | be integrated | [S40] document management platform → deeply<br>[S41] document management platform → deeply |
| 245 | `be issued by Director of` | 2 | Mention→Mention (2) | be issued by Director of | [S19] guidelines → Office of Management Federal agencies<br>[S19] guidelines → Office of Budget Federal agencies |
| 246 | `be launched from outside` | 2 | Mention→Mention (2) | be launched from outside | [S50] attack → logically adjacent administrative network domain<br>[S50] attack → logically adjacent administrative network domain |
| 247 | `be launched over` | 2 | Mention→Mention (2) | be launched over | [S50] attack → wide area network<br>[S50] attack → wide area network |
| 248 | `be listed` | 2 | Mention→Mention (2) | be listed | [S01] exploited vulnerability → currently<br>[S28] exploited vulnerability → currently |
| 249 | `be maintain` | 2 | Mention→Mention (2) | be maintain; be maintaining | [S12] using reverse SSH → access to compromised systems<br>[S52] organization → vulnerable product |
| 250 | `be produced by` | 2 | Mention→Mention (2) | be produced by | [S51] multiple operating systems → same vendor<br>[S51] Base Score → scoring more chained vulnerabilities Chained vulnerabilities |
| 251 | `be providing transparency to` | 2 | Mention→Mention (2) | be providing transparency to | [S50] open framework → individual characteristics used to derive score CVSS<br>[S50] open framework → methodology |
| 252 | `be rated` | 2 | Mention→Mention (2) | be rated | [S51] higher-scored vector → chance<br>[S51] Devices → High Devices |
| 253 | `be read` | 2 | Mention→Mention (2) | be read | [S12] attribution assessment findings → follow-up publication<br>[S12] latest findings → follow-up publication |
| 254 | `be recover` | 2 | Mention→Mention (2) | be recover | [S50] system → services<br>[S51] resilience of Component/System → services |
| 255 | `be reflect more` | 2 | Mention→Mention (2) | be reflect more | [S52] scoring Temporal metrics in order → relative severity posed by vulnerability to user 's environment at specific point<br>[S52] scoring Environmental metrics in order → relative severity posed by vulnerability to user 's environment at specific point |
| 256 | `be remediate` | 2 | Mention→CVE (2) | be remediate | [S40] updates → CVE-2026-55040 KB5002882<br>[S41] updates → CVE-2026-63520 KB5002893 |
| 257 | `be reporting through` | 2 | Mention→Mention (2) | be reporting through | [S19] vulnerability → CDM Program<br>[S19] vulnerability → CDM Program |
| 258 | `be represented in` | 2 | Mention→Mention (2) | be represented in | [S50] Safety impact → Supplemental Metrics group<br>[S51] Safety impact → Supplemental Metrics group |
| 259 | `be required for` | 2 | Mention→Mention (2) | be required for | [S10] tools → high-precision operations<br>[S10] tools → infinite efficiency |
| 260 | `be required into` | 2 | Mention→Mention (2) | be required into | [S50] effort → consideration<br>[S51] effort → consideration |
| 261 | `be required to achieve` | 2 | Mention→Mention (2) | be required to achieve | [S08] HTTP requests → authentication bypass<br>[S09] HTTP requests → unsafe |
| 262 | `be required to deploy` | 2 | Mention→Mention (2) | be required to deploy | [S50] effort → quickest available response<br>[S51] effort → quickest available response |
| 263 | `be running SharePoint in` | 2 | Mention→Mention (2) | be running SharePoint in | [S17] organisations → hybrid configurations<br>[S17] organisations → ADFS-integrated configurations |
| 264 | `be set arbitrary properties on` | 2 | Mention→Mention (2) | be set arbitrary properties on | [S09] NET type available in Global Assembly Cache to achieve OS command execution → instances<br>[S09] leverage property-setter side-effects → instances |
| 265 | `be signed by` | 2 | Mention→Mention (2) | be signed by | [S08] actor token → trusted certificate actortoken claim<br>[S08] tokens → unregistered certificates |
| 266 | `be support ongoing vulnerability remediation based on` | 2 | Mention→Mention (2) | be support ongoing vulnerability remediation based on | [S19] Update agency vulnerability management processes → KEV catalog<br>[S19] procedures → KEV catalog |
| 267 | `be supporting information for` | 2 | Organization→Mention (2) | be supporting information for | [S40] Rapid7 requests → upcoming disclosure<br>[S41] Rapid7 requests → upcoming disclosure |
| 268 | `be taken by attacker to evade` | 2 | Mention→Mention (2) | be taken by attacker to evade; be taken by attacker to evade existing | [S50] use Network metric captures measurable actions → actively existing built-in security-enhancing conditions<br>[S50] use Network metric captures measurable actions → built-in security-enhancing conditions |
| 269 | `be targeting` | 2 | Mention→Mention (1); Mention→CVE (1) | be targeting | [S12] active exploitation campaign → internet-accessible VMware vCenter systems<br>[S45] more information on attacks → CVE-2026-33824 vulnerability |
| 270 | `be to run` | 2 | Mention→Mention (2) | be to run | [S52] default configuration for vulnerable component → listening service with administrator privileges in analyst 's environment<br>[S52] default configuration for vulnerable component → Availability impacts |
| 271 | `be used to make` | 2 | Mention→Mention (2) | be used to make | [S51] data → business management decisions<br>[S51] data → risk management decisions |
| 272 | `break` | 2 | Mention→Mention (2) | break | [S40] which → complex<br>[S40] which → high-impact |
| 273 | `bypass` | 2 | Mention→Mention (2) | bypass | [S12] it → security controls designed primarily to prevent unsolicited inbound access<br>[S39] unauthenticated attacker → authentication |
| 274 | `cause exploitation events` | 2 | Mention→Mention (2) | cause exploitation events | [S54] cyber threat actor → ease<br>[S54] cyber threat actor → speed |
| 275 | `causes` | 2 | Mention→Mention (2) | causes | [S51] successful attack → only negligible impact to other components<br>[S51] vulnerability → potential repudiation |
| 276 | `change` | 2 | Mention→Mention (2) | change; changes | [S19] action → value of Publicly Exposed from Yes<br>[S51] that → Attack Complexity |
| 277 | `collaborated to adjust` | 2 | Mention→Mention (2) | collaborated to adjust | [S52] SIG → formula parameters in to align metric combinations to SIG 's proposed severity ratings<br>[S52] SIG → formula parameters |
| 278 | `collaborated with Deloitte & Touche LLP to adjust` | 2 | Mention→Mention (2) | collaborated with Deloitte & Touche LLP to adjust | [S52] SIG → formula parameters in to align metric combinations to SIG 's proposed severity ratings<br>[S52] SIG → formula parameters |
| 279 | `compromised` | 2 | Mention→Mention (2) | compromised | [S01] threat actors → system<br>[S28] threat actors → system |
| 280 | `consists of` | 2 | Mention→Mention (2) | consists of | [S50] CVSS vector string → compressed textual representation of values used to derive score<br>[S51] CVSS vector string → compressed textual representation of values used to derive score |
| 281 | `continue to track` | 2 | Mention→Mention (2) | continue to track | [S53] organization → vulnerability<br>[S53] organization → reassess |
| 282 | `contribute to production of` | 2 | Mention→Mention (2) | contribute to production of | [S51] subset of industry members → goods<br>[S51] subset of industry members → services |
| 283 | `create` | 2 | Mention→Mention (2) | create; creates | [S09] we → BusinessDataMetadataCatalog folder<br>[S17] coordination tool → pressure |
| 284 | `demonstrated operational security awareness having emptied exploit directories after` | 2 | Mention→Mention (2) | demonstrated operational security awareness having emptied exploit directories after | [S16] actor → use logging Vulnerabilities CVEs<br>[S16] actor → disabled Codex conversation logging Vulnerabilities CVEs |
| 285 | `depends on` | 2 | Mention→Mention (2) | depends on | [S44] cross-reference outbound SSH connections from vCenter host against known-good baselines since reverse_ssh persistence → outbound tunnel<br>[S52] Environmental Score formula → sub-formulas |
| 286 | `deployed open-source reverse_ssh framework to establish` | 2 | Mention→Mention (2) | deployed open-source reverse_ssh framework to establish | [S11] attacker → persistence remote access<br>[S11] attacker → gain remote access |
| 287 | `determine` | 2 | Mention→Mention (2) | determine; determines | [S54] organization → vulnerability 's scope<br>[S54] measure → present state of exploitation of vulnerability |
| 288 | `die` | 2 | Mention→Mention (2) | die | [S14] authenticatieproces Hierdoor kunnen onbevoegden authenticatiepogingen uitvoeren → normaal niet geaccepteerd zouden worden Update<br>[S14] zijn uitgebracht → ervoor zorgen dat alleen geldige inloggegevens |
| 289 | `disables` | 2 | Mention→Mention (2) | disables; disables / / | [S08] code → signature requirements<br>[S08] false single line → JWT library 's cryptographic signature verification |
| 290 | `disclosed` | 2 | Mention→CVE (1); Mention→Mention (1) | disclosed | [S11] France Broadcom → CVE-2026-59310<br>[S11] Broadcom → flaw |
| 291 | `do need to pass` | 2 | Mention→Mention (2) | do need to pass | [S10] we → them as arguments to method<br>[S10] we → them |
| 292 | `document` | 2 | Mention→Mention (2) | document | [S10] official SharePoint GitHub docs → BDCM schema<br>[S16] findings → threat actor developing AI-augmented offensive capabilities |
| 293 | `does correspond to` | 2 | Mention→Mention (2) | does correspond to | [S12] IP address → unique company<br>[S12] IP address → physical system |
| 294 | `embeds` | 2 | Mention→Mention (2) | embeds | [S51] implementation → vulnerable system<br>[S51] implementation → library |
| 295 | `emphasizes` | 2 | Mention→Mention (2) | emphasizes | [S19] it → robust vulnerability management practices<br>[S19] it → continuous monitoring requirements |
| 296 | `enabled them to increase` | 2 | Mention→Mention (2) | enabled them to increase | [S16] threat actor developing AI-augmented offensive capabilities → dramatically scale<br>[S16] threat actor developing AI-augmented offensive capabilities → scale |
| 297 | `enabled them to increase dramatically speed of` | 2 | Mention→Mention (2) | enabled them to increase dramatically speed of; enabled them to increase speed of | [S16] threat actor developing AI-augmented offensive capabilities → campaigns<br>[S16] threat actor developing AI-augmented offensive capabilities → campaigns |
| 298 | `establishes` | 2 | Mention→Mention (2) | establishes | [S17] initial execution → persistent reverse SSH tunnel to attacker-controlled infrastructure<br>[S19] which → policy for management of federal information resources |
| 299 | `executed` | 2 | Mention→Mention (2) | executed; is executed | [S16] system → hundreds of hours of manual targeting analysis<br>[S41] attacker 's arbitrary code → attacker-controlled OS command |
| 300 | `exploit issue to bypass` | 2 | Mention→Mention (2) | exploit issue to bypass | [S43] malicious actor with network access to vCenter → authentication unauthorized access to system<br>[S43] malicious actor with network access to vCenter → gain unauthorized access to system |
| 301 | `expose` | 2 | Mention→Mention (2) | expose; exposes | [S44] it → administrative control point<br>[S46] patching systems → IKE services |
| 302 | `gain` | 2 | Mention→Mention (2) | gain | [S50] attacker → control<br>[S51] one → code execution as local user from it |
| 303 | `grant attacker Confidentiality` | 2 | Mention→Mention (2) | grant attacker Confidentiality | [S50] compromise → Availability impacts<br>[S52] compromise → Availability impacts |
| 304 | `grant attacker Confidentiality listening service with` | 2 | Mention→Mention (2) | grant attacker Confidentiality listening service with | [S50] compromise → administrator privileges<br>[S52] compromise → administrator privileges |
| 305 | `grant total control of` | 2 | Mention→Mention (2) | grant total control of | [S01] publicly exposed assets → asset post-exploitation<br>[S28] publicly exposed assets → asset post-exploitation |
| 306 | `has allowed CISA to` | 2 | Mention→Mention (2) | has allowed CISA to | [S53] Stakeholder-Specific Vulnerability Categorization → better prioritize vulnerability response to public Stakeholder-Specific Vulnerability Categorization On Demand Training On Demand Training<br>[S53] Stakeholder-Specific Vulnerability Categorization → better prioritize vulnerability messaging to public Stakeholder-Specific Vulnerability Categorization On Demand Training On Demand Training |
| 307 | `has been exploited in` | 2 | Mention→Mention (2) | has been exploited in; have been exploited in | [S18] bug → wild<br>[S58] vulnerabilities → wild Organizations |
| 308 | `has been updated` | 2 | Mention→Mention (2) | has been updated | [S28] information → recently<br>[S51] CVSS Specification Document → clarify |
| 309 | `has catalog of` | 2 | Mention→Mention (2) | has catalog of | [S45] its → actively exploited vulnerabilities<br>[S45] its → ordered |
| 310 | `has corresponding Base value of` | 2 | Mention→Mention (2) | has corresponding Base value of; has corresponding Base values of | [S50] its → safety<br>[S52] its → Not Defined Not Defined |
| 311 | `has that` | 2 | Mention→Mention (2) | has that; is that | [S08] token → actor 's signature<br>[S08] effect → attacker |
| 312 | `has vulnerability reporting through` | 2 | Mention→Mention (2) | has vulnerability reporting through | [S19] their → CDM Program<br>[S19] their → CDM Program |
| 313 | `have impact on resulting score` | 2 | Mention→Mention (2) | have impact on resulting score | [S51] New metric groups → existing metric groups optionally<br>[S51] New metric groups → existing metric groups |
| 314 | `have to be recalled for` | 2 | Mention→Mention (2) | have to be recalled for | [S50] deployed → depot level repair units<br>[S50] deployed → replacement units |
| 315 | `hone autonomous attack processes` | 2 | Mention→Mention (2) | hone autonomous attack processes | [S16] they → pivot<br>[S16] they → assess |
| 316 | `impact availability of` | 2 | Mention→Mention (2) | impact availability of | [S18] attacker → system<br>[S39] attacker → system |
| 317 | `implement token parsing for` | 2 | Mention→Mention (2) | implement token parsing for | [S08] SPJsonWebSecurityTokenHandlerV2 class → Bearer service-to-service<br>[S08] base class SPJsonWebSecurityBaseTokenHandlerV2 → Bearer service-to-service |
| 318 | `include SQL like` | 2 | Mention→Mention (2) | include SQL like | [S20] Adversaries may attempt to exploit weakness in system → SNMP<br>[S20] Adversaries may attempt to exploit weakness in system → Smart Install |
| 319 | `include standard services like` | 2 | Mention→Mention (2) | include standard services like | [S20] Adversaries may attempt to exploit weakness in system → SMB<br>[S20] Adversaries may attempt to exploit weakness in system → SSH |
| 320 | `includes Claude Code for` | 2 | Mention→Mention (2) | includes Claude Code for | [S16] this → connectivity testing<br>[S16] this → proxy validation |
| 321 | `increase` | 2 | Mention→Mention (2) | increase | [S52] kit → CVSS score<br>[S52] situations → Base Score |
| 322 | `information exposure gives threat actor` | 2 | Mention→Mention (2) | information exposure gives threat actor | [S19] behavior of software → low stochastic opportunity for total control In context defined in Circular A-130 as information system operated about<br>[S19] exploit → low stochastic opportunity for total control In context defined in Circular A-130 as information system operated about |
| 323 | `integrated` | 2 | Mention→Mention (2) | integrated; is integrated | [S16] actor → open-source FofaMap-Platinum-Full-Expert Model Context Protocol server<br>[S51] information → using automation |
| 324 | `involve` | 2 | Mention→Mention (2) | involve; involves | [S10] RCE → submitting BDC<br>[S50] remotely only resolution to vulnerability → physical replacement e.g. units |
| 325 | `is accessible to` | 2 | Mention→Mention (2) | is accessible to | [S19] asset in scope of directive → unauthenticated entities<br>[S19] asset in scope of directive → untrusted entities |
| 326 | `is associated with attack Only increase in` | 2 | Mention→Mention (2) | is associated with attack Only increase in; is associated with attack Only increase in access | [S52] outcome → most directly<br>[S52] outcome → access |
| 327 | `is available as` | 2 | Mention→Mention (2) | is available as | [S48] Basic filtering by score range → is partial CVE ID search Full parameter reference<br>[S48] Basic filtering by percentile range → is partial CVE ID search Full parameter reference |
| 328 | `is based upon` | 2 | Mention→Product (1); Mention→Mention (1) | is based upon | [S08] below analysis → decompilation of Microsoft.SharePoint.IdentityModel module from fully patched SharePoint Server Subscription Edition instance<br>[S08] below analysis → code review instance |
| 329 | `is being exploited in` | 2 | Mention→Mention (2) | is being exploited in | [S11] recently patched critical vulnerability in VMware vCenter Syslog Server → active campaign to deploy reverse SSH tool for persistence<br>[S11] recently patched critical vulnerability in VMware vCenter Syslog Server → active campaign to deploy reverse SSH tool for remote access Compromises |
| 330 | `is consistent across` | 2 | Mention→Mention (2) | is consistent across | [S17] observed attack chain → confirmed victims<br>[S44] observed attack chain → victims |
| 331 | `is critical directory-traversal vulnerability in` | 2 | Mention→Mention (1); CVE→Mention (1) | is critical directory-traversal vulnerability in; is directory-traversal vulnerability in | [S12] critical vCenter vulnerability CVE-2026 → VMware vCenter Syslog server systems<br>[S44] CVE-2026-59310 → VMware vCenter Syslog server |
| 332 | `is defined as Yes regardless of` | 2 | Mention→Mention (2) | is defined as Yes regardless of | [S19] Publicly Exposed → physical location<br>[S19] Publicly Exposed → logical location |
| 333 | `is derived from` | 2 | Mention→Mention (2) | is derived from | [S52] Exploitability sub-score equation → Base Exploitability metrics<br>[S52] Impact sub-score equation → Base Impact metrics |
| 334 | `is efficient than querying API per` | 2 | Mention→Mention (2) | is efficient than querying API per | [S48] pulling file once per day → CVE<br>[S48] loading scores into database joining against asset inventory feeding dashboard → CVE |
| 335 | `is important When` | 2 | Mention→Mention (2) | is important When | [S19] definition of scope → evaluating technical impact<br>[S54] definition of scope → evaluating technical impact |
| 336 | `is internet-exposed without` | 2 | Mention→Mention (2) | is internet-exposed without | [S17] SSL VPN listener → intermediate rate-limiting access controls<br>[S17] SSL VPN listener → IP-based access controls |
| 337 | `is notable them automatically autonomous process of` | 2 | Mention→Mention (2) | is notable them automatically autonomous process of | [S16] sampling of scope → target identification<br>[S16] narrowing → target identification |
| 338 | `is presented` | 2 | Mention→Mention (2) | is presented; presents | [S42] disclosed information → direct serious impact<br>[S50] list of possible values → availability of system for Vulnerable System |
| 339 | `is primary logon name for user in` | 2 | Mention→Mention (1); Mention→Organization (1) | is primary logon name for user in | [S40] UPN → Windows AD<br>[S40] UPN → Microsoft Entra ID |
| 340 | `is recommended to enrich` | 2 | Mention→Mention (2) | is recommended to enrich | [S51] it → results from vulnerability scanning solutions with asset data<br>[S51] it → results |
| 341 | `is represented as vector string` | 2 | Mention→Mention (2) | is represented as vector string | [S52] CVSS score → Temporal metrics<br>[S52] CVSS score → Environmental metrics |
| 342 | `is to increase` | 2 | Mention→Mention (2) | is to increase | [S50] conditions primary purpose → security<br>[S50] conditions primary purpose → increase |
| 343 | `is to mitigate` | 2 | Mention→Mention (2) | is to mitigate | [S50] primary purpose of conditions → explicitly attacks<br>[S50] primary purpose of conditions → attacks |
| 344 | `is updated to reflect` | 2 | Mention→Mention (1); Mention→CVE (1) | is updated to reflect | [S40] blog → medium severity<br>[S40] blog → CISA 's addition of CVE-2026-55040 to KEV catalog |
| 345 | `is used to record CVSS metric information in` | 2 | Mention→Mention (2) | is used to record CVSS metric information in | [S50] it → concise form<br>[S50] it → machine-readable form |
| 346 | `is used to record CVSS metric information set of` | 2 | Mention→Mention (2) | is used to record CVSS metric information set of | [S52] it → CVSS metrics commonly<br>[S52] it → CVSS metrics |
| 347 | `is used transfer set of` | 2 | Mention→Mention (2) | is used transfer set of | [S52] it → CVSS metrics commonly<br>[S52] it → CVSS metrics |
| 348 | `is usefulness of` | 2 | Mention→Mention (2) | is usefulness of | [S50] prioritization → numerical CVSS score<br>[S51] prioritization → numerical CVSS score |
| 349 | `it has added flaw to catalog of` | 2 | Organization→Mention (2) | it has added flaw to catalog of | [S45] CISA → actively exploited vulnerabilities flag<br>[S45] CISA → ordered flag |
| 350 | `lack` | 2 | Mention→Mention (2) | lack | [S17] August 11 onwards → corresponding maintenance window<br>[S17] August 11 onwards → hardware failure record |
| 351 | `lead to` | 2 | Mention→Mention (2) | lead to | [S50] vulnerability → successful attack<br>[S54] component failure → overall mission failure Mission prevalence |
| 352 | `lead to heap corruption` | 2 | Mention→Mention (2) | lead to heap corruption | [S46] class of vulnerability → specially crafted IKE packets<br>[S46] class of vulnerability → potentially allowing attacker to influence memory allocation behaviour specially crafted IKE packets |
| 353 | `lead to unauthenticated remote code execution against vulnerable SharePoint server` | 2 | CVE→Mention (1); CVE→CVE (1) | lead to unauthenticated remote code execution against vulnerable SharePoint server | [S18] CVE-2026-55040 → vulnerability<br>[S18] CVE-2026-55040 → CVE-2026-63520 |
| 354 | `log out from` | 2 | Mention→Mention (2) | log out from | [S51] attacker → own account<br>[S51] attacker → own account |
| 355 | `maintained` | 2 | Mention→Observation (1); Mention→Mention (1) | maintained; maintains | [S16] threat actor → active<br>[S48] api.first.org/epss FIRST.org → EPSS API interface |
| 356 | `measure current state of` | 2 | Mention→Mention (2) | measure current state of | [S50] Threat metrics → exploit code availability<br>[S52] Temporal metrics → exploit techniques |
| 357 | `patched` | 2 | Vendor→CVE (1); Mention→Mention (1) | patched | [S17] Apple → CVE-2026-65400<br>[S44] Broadcom → vCenter 's Syslog server |
| 358 | `perform` | 2 | Mention→Mention (2) | perform; performs | [S18] remote unauthenticated attacker → operations<br>[S51] library → image conversion |
| 359 | `perform operations as` | 2 | Mention→Mention (2) | perform operations as | [S18] remote unauthenticated attacker → SharePoint site user<br>[S18] remote unauthenticated attacker → administrator |
| 360 | `possess` | 2 | Mention→Mention (2) | possess | [S42] attacker → privileges<br>[S50] attacker → privileges |
| 361 | `present high-risk attack surface` | 2 | Mention→Mention (2) | present high-risk attack surface | [S40] vulnerabilities within architecture → active directories<br>[S40] vulnerabilities within architecture → cloud infrastructure |
| 362 | `present high-risk attack surface CVE-2026-63520` | 2 | Mention→Mention (2) | present high-risk attack surface CVE-2026-63520 | [S41] vulnerabilities within architecture → active directories<br>[S41] vulnerabilities within architecture → cloud infrastructure |
| 363 | `prevent` | 2 | Mention→Mention (2) | prevent; prevents | [S54] that → vulnerability<br>[S54] that → vulnerability |
| 364 | `provide argument` | 2 | Mention→Mention (2) | provide argument | [S51] expected response is yes Analysts → unauthenticated remote code execution<br>[S51] expected response is yes Analysts → command injection |
| 365 | `provide copy of` | 2 | Mention→Mention (2) | provide copy of | [S19] agencies → policies<br>[S19] agencies → updated vulnerability management policies |
| 366 | `provide demonstration` | 2 | Mention→Mention (2) | provide demonstration | [S51] expected response is yes Analysts → unauthenticated remote code execution<br>[S51] expected response is yes Analysts → command injection |
| 367 | `provides outbound command-and-control channel` | 2 | Mention→Mention (2) | provides outbound command-and-control channel | [S11] reverse SSH connection → persistence remote access<br>[S11] reverse SSH connection → gain remote access |
| 368 | `recognizes` | 2 | Vendor→Mention (1); Mention→Mention (1) | recognizes | [S42] Microsoft → efforts of those in security community<br>[S50] first → contributions of following CVSS Special Interest Group members listed in alphabetical order by last name |
| 369 | `refer thing to formally as` | 2 | Mention→Mention (2) | refer thing to formally as | [S50] we → vulnerable system<br>[S52] we → vulnerable component Impact metrics |
| 370 | `released security updates for` | 2 | Vendor→CVE (2) | released security updates for | [S46] Microsoft → CVE-2026-33824 Applying updates Mitigation<br>[S46] Microsoft → CVE-2026-33824 Applying updates remediation |
| 371 | `released security updates on` | 2 | Vendor→Mention (2) | released security updates on | [S46] Microsoft → 14 April 2026 Applying updates Mitigation<br>[S46] Microsoft → 14 April 2026 Applying updates remediation |
| 372 | `report` | 2 | Mention→Mention (2) | report | [S19] Automate reporting on status of vulnerabilities listed in KEV Catalog via automated reporting through Continuous Diagnostics → status<br>[S19] Automate reporting on status of vulnerabilities listed in KEV Catalog via automated reporting through Mitigation Dashboard → status |
| 373 | `requires attention from` | 2 | Mention→Mention (2) | requires attention from | [S53] vulnerability → organization 's internal Necessary actions<br>[S53] vulnerability → organization 's |
| 374 | `resides` | 2 | Mention→Mention (2) | resides | [S52] vulnerable component → security scope<br>[S54] vulnerability → affected component |
| 375 | `resolves` | 2 | Mention→Mention (2) | resolves | [S08] JWT → actor token 's signing key using x5t<br>[S09] DbTypeReflector class → arbitrary assembly-qualified type names |
| 376 | `restart events from` | 2 | Mention→Mention (2) | restart events from | [S17] Review firewall for unexpected → August 11 onwards BleepingComputer<br>[S17] VPN service logs → August 11 onwards BleepingComputer |
| 377 | `result in injuries categorized as` | 2 | Mention→Mention (2) | result in injuries categorized as | [S50] exploited vulnerability → Marginal<br>[S50] exploited vulnerability → worse |
| 378 | `revokes BOD 19-02 risk of` | 2 | Mention→Mention (2) | revokes BOD 19-02 risk of | [S19] directive → cyber incidents hereby<br>[S19] directive → cyber incidents |
| 379 | `rule out entirely possibility of` | 2 | Mention→Mention (2) | rule out entirely possibility of; rule out possibility of | [S14] NCSC-NL → errors<br>[S14] NCSC-NL → errors |
| 380 | `send crafted packets to Windows machine with` | 2 | Mention→Mention (2) | send crafted packets to Windows machine with | [S07] unauthenticated attacker → Internet Key Exchange<br>[S45] unauthenticated attacker → Internet Key Exchange |
| 381 | `serves` | 2 | Mention→Mention (2) | serves | [S17] SharePoint → environments<br>[S50] solution → function |
| 382 | `started` | 2 | Mention→Mention (2) | started | [S16] the Operation Hermes Agent responding to Telegram command → HTTP file server<br>[S48] it → publishing time series date |
| 383 | `subvert protections built into` | 2 | Mention→Mention (2) | subvert protections built into | [S50] user → vulnerable system<br>[S51] user → vulnerable component |
| 384 | `supplement Base Score with` | 2 | Mention→Mention (2) | supplement Base Score with | [S52] Consumers of CVSS → Temporal Scores specific to use of vulnerable product to produce severity more accurate for organizational environment<br>[S52] Consumers of CVSS → Environmental Scores specific to use of vulnerable product to produce severity more accurate for organizational environment |
| 385 | `supports MEFs` | 2 | Mention→Mention (2) | supports MEFs | [S54] vulnerable component → Support only<br>[S54] vulnerable component → Support |
| 386 | `supports organisations in` | 2 | Mention→Mention (2) | supports organisations in | [S46] Sentrium → identifying<br>[S46] Sentrium → managing exposure to critical infrastructure vulnerabilities |
| 387 | `sustained over` | 2 | Mention→Mention (2) | sustained over | [S16] higher intent including refined exploitation parameters → multiple days<br>[S16] higher intent including proxy anonymization → multiple days |
| 388 | `take action` | 2 | Mention→Mention (2) | take action | [S51] user of system → mitigate<br>[S51] operator → mitigate |
| 389 | `take action to` | 2 | Mention→Mention (2) | take action to | [S51] user of system → remediate<br>[S51] operator → remediate |
| 390 | `take precedence` | 2 | Mention→Mention (2) | take precedence | [S38] originating CNA 's data → CWE<br>[S38] originating CNA 's data → CPE string |
| 391 | `takes environmental factors into` | 2 | Mention→Mention (2) | takes environmental factors into | [S51] Once information is integrated using automation CVSS-BE score → consideration Additionally<br>[S51] Once information is integrated using automation CVSS-BE score → consideration |
| 392 | `threaten` | 2 | Mention→Mention (2) | threaten | [S19] persistent increasingly sophisticated malicious cyber campaigns → public sector<br>[S19] persistent increasingly sophisticated malicious cyber campaigns → private sector |
| 393 | `to confirms` | 2 | Vendor→Mention (2) | to confirms | [S40] Microsoft → disclosure plan<br>[S41] Microsoft → disclosure plan |
| 394 | `to walk through` | 2 | Mention→Mention (2) | to walk through | [S08] August 13 → full here<br>[S41] August 13 → full |
| 395 | `treat` | 2 | Mention→Mention (2) | treat | [S17] organisations → infrastructure components<br>[S17] defenders → infrastructure component |
| 396 | `treat infrastructure component as` | 2 | Mention→Mention (2) | treat infrastructure component as; treat infrastructure components as | [S17] organisations → foundational<br>[S17] defenders → foundational rather than as attack surface |
| 397 | `use access for` | 2 | Mention→Mention (2) | use access for | [S11] attackers → data theft<br>[S11] attackers → operational disruptions |
| 398 | `used this for` | 2 | Mention→Mention (2) | used this for | [S16] actor → connectivity testing<br>[S16] actor → proxy validation Session history |
| 399 | `warrant further reductions in` | 2 | Mention→Mention (2) | warrant further reductions in | [S19] technological advances → timelines<br>[S19] adversarial advances → timelines |
| 400 | `was discovered by` | 2 | Mention→Mention (1); Mention→Product (1) | was discovered by | [S41] vulnerability → Stephen Fewer<br>[S41] vulnerability → is being disclosed in accordance with Rapid7 's vulnerability disclosure policy |
| 401 | `were built for For` | 2 | Mention→Mention (2) | were built for For | [S44] regulation 's 24-hour early-warning → German organizations under NIS2 class of incident<br>[S44] 72-hour incident-notification obligations → German organizations under NIS2 class of incident |
| 402 | `work` | 2 | Mention→Mention (2) | work | [S19] agencies → certified cloud service offerings through FedRAMP PMO to ensure compliance with Directive For cloud offerings<br>[S19] agencies → certified cloud service offerings to ensure compliance with Directive For cloud offerings |
| 403 | `worked in 2020 to develop` | 2 | Organization→Mention (2) | worked in 2020 to develop | [S53] CISA → own customized SSVC decision tree to examine vulnerabilities relevant to United States government singular system<br>[S53] CISA → own customized SSVC decision tree singular system |
| 404 | `worked to develop` | 2 | Organization→Mention (2) | worked to develop | [S53] CISA → own customized SSVC decision tree to examine vulnerabilities relevant to United States government singular system<br>[S53] CISA → own customized SSVC decision tree singular system |
| 405 | `worked with SEI to develop` | 2 | Organization→Mention (2) | worked with SEI to develop | [S53] CISA → own customized SSVC decision tree to examine vulnerabilities relevant to United States government singular system<br>[S53] CISA → own customized SSVC decision tree singular system |
| 406 | `write` | 2 | Mention→Mention (2) | write | [S42] unauthenticated attacker → arbitrary code<br>[S43] VMXNET3 out-of-bounds → vulnerability VMware ESX |
| 407 | `'s familiar to` | 1 | Mention→Mention (1) | 's familiar to | [S10] it → us |
| 408 | `'ve focused rest of blog on what worked` | 1 | Mention→Mention (1) | 've focused rest of blog on what worked | [S10] we → spec Instead |
| 409 | `AV is defined than` | 1 | Mention→Mention (1) | AV is defined than | [S50] metric → once |
| 410 | `Are aware of exploited vulnerability included in` | 1 | Mention→Mention (1) | Are aware of exploited vulnerability included in | [S58] you → KEV catalog |
| 411 | `August 21 2026 arrives` | 1 | Mention→Mention (1) | August 21 2026 arrives | [S17] Cybersecurity → Cybersecurity News Stories August 21 2026 |
| 412 | `August 21 2026 arrives at moment` | 1 | Mention→Mention (1) | August 21 2026 arrives at moment | [S17] Cybersecurity → Cybersecurity News Stories August 21 2026 |
| 413 | `Based on Risk to support` | 1 | Mention→Mention (1) | Based on Risk to support | [S19] Prioritizing Security Updates → agencies |
| 414 | `Based to support` | 1 | Mention→Mention (1) | Based to support | [S19] Prioritizing Security Updates → agencies |
| 415 | `CISA has added flaw` | 1 | Mention→Mention (1) | CISA has added flaw | [S45] it → flag |
| 416 | `CISA has added flaw flag as` | 1 | Mention→Mention (1) | CISA has added flaw flag as | [S45] it → exploited |
| 417 | `CPE string be updated` | 1 | Mention→Mention (1) | CPE string be updated | [S38] SSVC decision points → shortly thereafter |
| 418 | `CPE string be updated shortly thereafter by CISA ADP Additional information about` | 1 | Mention→Product (1) | CPE string be updated shortly thereafter by CISA ADP Additional information about | [S38] SSVC decision points → CISA ADP including contact information |
| 419 | `CWE be updated` | 1 | Mention→Mention (1) | CWE be updated | [S38] SSVC decision points → shortly thereafter |
| 420 | `CWE be updated shortly thereafter by CISA ADP Additional information about` | 1 | Mention→Product (1) | CWE be updated shortly thereafter by CISA ADP Additional information about | [S38] SSVC decision points → CISA ADP including contact information |
| 421 | `Cybersecurity arrives` | 1 | Mention→Mention (1) | Cybersecurity arrives | [S17] August 21 2026 → Cybersecurity News Stories August 21 2026 |
| 422 | `Cybersecurity arrives at moment` | 1 | Mention→Mention (1) | Cybersecurity arrives at moment | [S17] August 21 2026 → Cybersecurity News Stories August 21 2026 |
| 423 | `Dit wordt mogelijk gemaakt door onvoldoende state management tijdens` | 1 | Mention→Mention (1) | Dit wordt mogelijk gemaakt door onvoldoende state management tijdens | [S14] toegang kunnen verkrijgen zonder geldige inloggegevens → functionaliteit waarbij netwerkaanvallers |
| 424 | `Handles` | 1 | Mention→Mention (1) | Handles | [S16] How n8n → Vulnerability Disclosure |
| 425 | `Is vulnerability on` | 1 | Mention→Product (1) | Is vulnerability on | [S19] KEV Status → CISA 's Known Exploited Vulnerabilities Catalog |
| 426 | `Lets` | 1 | Mention→Mention (1) | Lets | [S17] JWT authentication bypass → Attackers Impersonate Admins |
| 427 | `Lets Attackers Impersonate Admins On` | 1 | Mention→Mention (1) | Lets Attackers Impersonate Admins On | [S17] JWT authentication bypass → August 13 |
| 428 | `NET type achieved` | 1 | Mention→Mention (1) | NET type achieved | [S10] we → fully authenticated deserialization |
| 429 | `Name` | 1 | Mention→Mention (1) | Name | [S08] controlled User Principal → attacker |
| 430 | `Process` | 1 | Organization→Organization (1) | Process | [S38] CISA ADP → CISA ADP |
| 431 | `Sign up for VulnCheck community to get` | 1 | Mention→Mention (1) | Sign up for VulnCheck community to get | [S10] practitioner community → here free access to VulnCheck KEV |
| 432 | `Text` | 1 | Mention→Mention (1) | Text | [S09] AS output </Property> <Property Name="RdbCommandType" Type="System.String"> → </Property> |
| 433 | `That is need consider means` | 1 | Mention→Mention (1) | That is need consider means | [S50] analyst → vulnerability |
| 434 | `There 's` | 1 | CVE→Mention (1) | There 's | [S10] detailed write-up on CVE-2026-55040 here from Rapid7 team → TL |
| 435 | `There is availability of` | 1 | Mention→Mention (1) | There is availability of | [S42] total loss of availability → impacted component |
| 436 | `Updates` | 1 | Mention→Mention (1) | Updates | [S38] CNA → CVE Record |
| 437 | `Updates CVE Record If CNA later updates CVE Record with` | 1 | Mention→Mention (1) | Updates CVE Record If CNA later updates CVE Record with | [S38] CNA → own CVSS |
| 438 | `accept images from` | 1 | Mention→Mention (1) | accept images from | [S51] programs → untrusted sources |
| 439 | `accepts issuer` | 1 | Mention→Mention (1) | accepts issuer | [S08] method → returns to caller instead of throwing SecurityTokenException exception |
| 440 | `accepts that as` | 1 | Mention→Mention (1) | accepts that as | [S17] SharePoint → valid |
| 441 | `accepts tokens with` | 1 | Mention→Mention (1) | accepts tokens with | [S08] library → alg |
| 442 | `accessed DeepSeek through` | 1 | Mention→Mention (1) | accessed DeepSeek through | [S16] actor → native API endpoints traceability |
| 443 | `accessed Qwen through` | 1 | Mention→Mention (1) | accessed Qwen through | [S16] actor → native API endpoints traceability |
| 444 | `achieve` | 1 | Mention→Mention (1) | achieve | [S16] placeholder values → code execution |
| 445 | `acknowledges receipt of` | 1 | Product→Mention (1) | acknowledges receipt of | [S40] chain to Microsoft Microsoft → disclosure the same day |
| 446 | `added CVE-2026-55040 Weak Authentication On` | 1 | Organization→Mention (1) | added CVE-2026-55040 Weak Authentication On | [S40] CISA → August 18 2026 |
| 447 | `added CVE-2026-55040 on` | 1 | Organization→Mention (1) | added CVE-2026-55040 on | [S17] CISA → August 18 |
| 448 | `added CVE-2026-55040 with remediation deadline of` | 1 | Organization→Mention (1) | added CVE-2026-55040 with remediation deadline of | [S17] CISA → August 21 |
| 449 | `added to IKE Protocol including authentication` | 1 | Vendor→Mention (1) | added to IKE Protocol including authentication | [S45] Microsoft → additional capabilities |
| 450 | `added via easier interoperability with non-Internet Protocol Security` | 1 | Vendor→Mention (1) | added via easier interoperability with non-Internet Protocol Security | [S45] Microsoft → additional capabilities |
| 451 | `added via generated addresses` | 1 | Vendor→Mention (1) | added via generated addresses | [S45] Microsoft → additional capabilities |
| 452 | `adjust Base` | 1 | Mention→Mention (1) | adjust Base | [S52] Environmental metrics → code |
| 453 | `adjust Base to` | 1 | Mention→Mention (1) | adjust Base to | [S52] Environmental metrics → specific computing environment code |
| 454 | `adjust Temporal severities` | 1 | Mention→Mention (1) | adjust Temporal severities | [S52] Environmental metrics → code |
| 455 | `adjust Temporal severities to` | 1 | Mention→Mention (1) | adjust Temporal severities to | [S52] Environmental metrics → specific computing environment code |
| 456 | `adjusts` | 1 | Mention→Mention (1) | adjusts | [S51] Group renamed to Threat Metric Group The Threat Metric Group → reasonable worst case |
| 457 | `adjusts scores of vectors within` | 1 | Mention→Mention (1) | adjusts scores of vectors within | [S51] small score modification factor → vector group |
| 458 | `adjusts scores of vectors within qualitatively equivalent set of` | 1 | Mention→Mention (1) | adjusts scores of vectors within qualitatively equivalent set of | [S50] small score modification factor → vectors |
| 459 | `advised` | 1 | Vendor→Mention (1) | advised | [S45] Microsoft → security teams |
| 460 | `affects wide range of` | 1 | Mention→Mention (1) | affects wide range of | [S46] vulnerability → supported Windows platforms including Windows Server 2016 |
| 461 | `affects wide range of supported Windows platforms including Windows Server 2016 through to` | 1 | Mention→Product (1) | affects wide range of supported Windows platforms including Windows Server 2016 through to | [S46] vulnerability → Windows Server 2025 |
| 462 | `agreed upon with` | 1 | Mention→Mention (1) | agreed upon with | [S38] specific informational elements → CVE Program |
| 463 | `align to` | 1 | Mention→Mention (1) | align to | [S53] Stakeholder-Specific Vulnerability Categorization details other decision tree models → mission space |
| 464 | `allow attacker on network to authenticate to` | 1 | Mention→Mention (1) | allow attacker on network to authenticate to | [S32] improper authentication vulnerability → Screen Sharing without valid credentials Known To Be Used in Ransomware Campaigns |
| 465 | `allow threat actor with` | 1 | Mention→Mention (1) | allow threat actor with | [S31] path traversal vulnerability → network access to vCenter to execute arbitrary code Known To Be Used in Ransomware Campaigns |
| 466 | `allowed attacker to maintain` | 1 | Mention→Mention (1) | allowed attacker to maintain | [S12] capabilities → outbound control channel |
| 467 | `allowed attacker to maintain outbound control channel from` | 1 | Mention→Mention (1) | allowed attacker to maintain outbound control channel from | [S12] capabilities → compromised systems |
| 468 | `allows attacker to compromise other files on` | 1 | Mention→Mention (1) | allows attacker to compromise other files on | [S51] reader → same operating system |
| 469 | `allows call to succeed` | 1 | Mention→Mention (1) | allows call to succeed | [S08] this → nameid |
| 470 | `allows constructing gadget chain through` | 1 | Mention→Mention (1) | allows constructing gadget chain through | [S09] this → System.Windows.Data.ObjectDataProvider class 's property-setter side-effect method |
| 471 | `allows unauthorized attacker to bypass` | 1 | Mention→Mention (1) | allows unauthorized attacker to bypass | [S30] weak authentication vulnerability → security feature over network Known To Be Used in Ransomware Campaigns |
| 472 | `allows unauthorized attacker to bypass security feature over` | 1 | Product→Mention (1) | allows unauthorized attacker to bypass security feature over | [S39] Weak authentication in Microsoft Office SharePoint → network Exploitability |
| 473 | `allows users to export` | 1 | Mention→Mention (1) | allows users to export | [S53] SSVC Calculator → data organization |
| 474 | `analyst assign` | 1 | Mention→Mention (1) | analyst assign | [S50] asset to analyst 's organization → greater value |
| 475 | `appeared to allow` | 1 | Mention→Mention (1) | appeared to allow | [S16] actor → DeepSeek to narrow targeting scope |
| 476 | `appears to be accepting tokens from` | 1 | Mention→Mention (1) | appears to be accepting tokens from | [S08] intent → certificates |
| 477 | `applies additional validation Starting with` | 1 | Mention→Mention (1) | applies additional validation Starting with | [S10] SharePoint → August 2026 CU |
| 478 | `applies as Federal Civilian Executive Branch systems` | 1 | Mention→Mention (1) | applies as Federal Civilian Executive Branch systems | [S19] it → systems |
| 479 | `applies to court in` | 1 | Mention→Mention (1) | applies to court in | [S14] choice of means → summary proceedings |
| 480 | `apply patches listed in` | 1 | CVE→Mention (1) | apply patches listed in | [S43] CVE-2026-41709 → Fixed Version ' column |
| 481 | `approved by` | 1 | Mention→Mention (1) | approved by | [S38] ADP → CVE Board |
| 482 | `are aid to scoring` | 1 | Mention→Mention (1) | are aid to scoring | [S51] scoring rubrics → vulnerabilities by supplementing metric definitions in Specification Document The Internet Engineering Task Force vulnerability |
| 483 | `are as` | 1 | Mention→Mention (1) | are as | [S51] details → follows |
| 484 | `are available to` | 1 | Mention→Mention (1) | are available to | [S10] artifacts → Initial Access Intelligence customers |
| 485 | `are blocked to provide additional protection against` | 1 | Mention→Mention (1) | are blocked to provide additional protection against | [S10] Types → potentially unsafe type usage |
| 486 | `are building` | 1 | Mention→Mention (1) | are building | [S48] you → time series |
| 487 | `are clustered` | 1 | Mention→Mention (1) | are clustered | [S50] vectors → severity |
| 488 | `are clustered in sets called` | 1 | Mention→Mention (1) | are clustered in sets called | [S50] vectors → severity |
| 489 | `are considered to have value of` | 1 | Mention→Mention (1) | are considered to have value of | [S52] omitted metrics → Not Defined |
| 490 | `are constructing` | 1 | Mention→Mention (1) | are constructing | [S16] threat actors → persistent AI offensive infrastructure |
| 491 | `are constructing persistent AI offensive infrastructure Rather than using AI tools in` | 1 | Mention→Mention (1) | are constructing persistent AI offensive infrastructure Rather than using AI tools in | [S16] threat actors → isolation |
| 492 | `are defined earlier` | 1 | Mention→Mention (1) | are defined earlier | [S50] associated metric value in abbreviated form → colon |
| 493 | `are defined in specification` | 1 | Mention→Mention (1) | are defined in specification | [S50] associated metric value in abbreviated form → colon |
| 494 | `are dependent on` | 1 | Mention→Mention (1) | are dependent on | [S17] defenders → remote access to respond |
| 495 | `are designed to measure severity of` | 1 | Mention→Mention (1) | are designed to measure severity of | [S51] CVSS Base scores → vulnerability |
| 496 | `are direct responsibility rather than` | 1 | Mention→Mention (1) | are direct responsibility rather than | [S51] Heuristically → users |
| 497 | `are facing` | 1 | Mention→Mention (1) | are facing | [S17] organisations → vulnerability |
| 498 | `are frequent attack vector for malicious cyber actors including those backed by` | 1 | Mention→Mention (1) | are frequent attack vector for malicious cyber actors including those backed by | [S19] equally Known exploited vulnerabilities → nation-states |
| 499 | `are generated by` | 1 | Mention→Mention (1) | are generated by | [S47] Scores → Empirical Security |
| 500 | `are how particular kind of buffer overflow to` | 1 | Mention→Mention (1) | are how particular kind of buffer overflow to | [S51] certain kinds of SQL Injection vulnerabilities → cross-site scripting attack |
| 501 | `are met such as` | 1 | Mention→Mention (1) | are met such as | [S51] other preconditions → first |
| 502 | `are number of recommendations for` | 1 | Mention→Mention (1) | are number of recommendations for | [S51] version of CVSS Below → consumers |
| 503 | `are ordered` | 1 | Mention→Mention (1) | are ordered | [S51] vector sets → totally |
| 504 | `are precursors to` | 1 | Mention→Mention (1) | are precursors to | [S51] certain kinds of SQL Injection vulnerabilities → cross-site scripting attack |
| 505 | `are present in` | 1 | Mention→Mention (1) | are present in | [S10] Types → list |
| 506 | `are produced by` | 1 | Mention→Mention (1) | are produced by | [S52] code Base Scores → organization maintaining vulnerable product |
| 507 | `are publicized` | 1 | Mention→Mention (1) | are publicized | [S39] only existence of vulnerabilities → Sometimes |
| 508 | `are published by` | 1 | Mention→Mention (1) | are published by | [S41] technical details → third-party |
| 509 | `are publishing technical analysis of CVE-2026-63520 analysis` | 1 | Mention→Mention (1) | are publishing technical analysis of CVE-2026-63520 analysis | [S09] we → Today |
| 510 | `are rated with` | 1 | Mention→Mention (1) | are rated with | [S51] full capacity redundancy → recovery requirements |
| 511 | `are relevant to` | 1 | Mention→Mention (1) | are relevant to | [S52] vulnerability → particular user 's environment Considerations |
| 512 | `are required to have` | 1 | Mention→Mention (1) | are required to have | [S51] Devices → rapid response times for transactional purposes based on regulatory requirements |
| 513 | `are required to have rapid response times for` | 1 | Mention→Mention (1) | are required to have rapid response times for | [S51] Devices → transactional purposes |
| 514 | `are salient to` | 1 | Mention→Mention (1) | are salient to | [S51] metric value → metric-group-based equivalence set change |
| 515 | `are set to default value of Defined reasonable worst case of` | 1 | Mention→Mention (1) | are set to default value of Defined reasonable worst case of | [S50] metrics → explicit values |
| 516 | `are shared between` | 1 | Mention→Mention (1) | are shared between | [S51] credentials → web application |
| 517 | `are simplified to illustrate` | 1 | Mention→Mention (1) | are simplified to illustrate | [S51] examples → concepts |
| 518 | `are standard ports` | 1 | Mention→Mention (1) | are standard ports | [S46] UDP ports → used by IKE NAT traversal At time of writing |
| 519 | `are uncertain of true nature of` | 1 | Mention→Mention (1) | are uncertain of true nature of | [S52] Reporters → vulnerability |
| 520 | `are users of` | 1 | Mention→Mention (1) | are users of | [S50] such systems → system operators |
| 521 | `arises from` | 1 | Mention→Mention (1) | arises from | [S46] vulnerability → double free condition |
| 522 | `ask` | 1 | Mention→Mention (1) | ask | [S47] practitioners → questions |
| 523 | `ask about score` | 1 | Mention→Mention (1) | ask about score | [S47] practitioners → questions |
| 524 | `ask most` | 1 | Mention→Mention (1) | ask most | [S47] practitioners → questions |
| 525 | `asset to analyst 's organization assign` | 1 | Mention→Mention (1) | asset to analyst 's organization assign | [S50] analyst → greater value |
| 526 | `assume high privileges while` | 1 | Mention→Mention (1) | assume high privileges while | [S51] analyst → assessing vulnerability in library having lower impact on embedding implementation increasing impacts |
| 527 | `attack has been updated to allow for` | 1 | Mention→Mention (1) | attack has been updated to allow for | [S51] possible User Interaction Base Metric → additional granularity |
| 528 | `augmented` | 1 | Mention→Mention (1) | augmented | [S41] we → agentic work |
| 529 | `augmented agentic work with` | 1 | Mention→Mention (1) | augmented agentic work with | [S41] we → manual source code review |
| 530 | `augments information in CVE Record` | 1 | Mention→Mention (1) | augments information in CVE Record | [S38] ADP → ADP 's contributions |
| 531 | `authenticate as` | 1 | Mention→Mention (1) | authenticate as | [S08] we → using urn |
| 532 | `automate` | 1 | Mention→Mention (1) | automate | [S50] attacker → exploitation events |
| 533 | `automate exploitation events for vulnerability across` | 1 | Mention→Mention (1) | automate exploitation events for vulnerability across | [S50] attacker → multiple targets |
| 534 | `base64` | 1 | Mention→Mention (1) | base64 | [S08] we → Constructing above JWT |
| 535 | `be Constructing` | 1 | Mention→Mention (1) | be Constructing | [S08] we → above JWT |
| 536 | `be Fix` | 1 | Mention→Mention (1) | be Fix | [S54] type → official patch |
| 537 | `be Listing generic types of` | 1 | Mention→Mention (1) | be Listing generic types of | [S51] local privileges → vulnerabilities |
| 538 | `be Local` | 1 | Mention→Mention (1) | be Local | [S51] attack vector → does not support mode |
| 539 | `be Sharing` | 1 | Mention→Mention (1) | be Sharing | [S14] de Screen → feature |
| 540 | `be Starting with` | 1 | Mention→Mention (1) | be Starting with | [S10] SharePoint → August 2026 CU |
| 541 | `be Taken` | 1 | Mention→Mention (1) | be Taken | [S17] available patch → together |
| 542 | `be Tracked as` | 1 | CVE→CVE (1) | be Tracked as | [S18] CVE-2026-55040 → CVE-2026-55040 |
| 543 | `be Training On` | 1 | Mention→Mention (1) | be Training On | [S53] Demand → Demand Training |
| 544 | `be Weak Authentication On` | 1 | Organization→Mention (1) | be Weak Authentication On | [S40] CISA → August 18 2026 |
| 545 | `be able to` | 1 | Mention→Mention (1) | be able to | [S51] they → access |
| 546 | `be accompanied by` | 1 | Mention→Mention (1) | be accompanied by | [S18] in-depth technical analysis of flaw → proof-of-concept |
| 547 | `be achieved in` | 1 | Mention→Mention (1) | be achieved in | [S40] this → number of ways including via user 's Active Directory |
| 548 | `be affected by` | 1 | Mention→Mention (1) | be affected by | [S51] vulnerable system → vulnerability being scored Vendor |
| 549 | `be affecting` | 1 | Mention→Mention (1) | be affecting | [S53] vulnerability → organization |
| 550 | `be allow inbound traffic on UDP ports only from` | 1 | Mention→Mention (1) | be allow inbound traffic on UDP ports only from | [S07] configure firewall rules → known |
| 551 | `be allow inbound traffic only from` | 1 | Mention→Mention (1) | be allow inbound traffic only from | [S45] to configure firewall rules → known peer addresses |
| 552 | `be allowing` | 1 | Mention→Mention (1) | be allowing | [S46] class of vulnerability → attacker to influence memory allocation behaviour |
| 553 | `be answer` | 1 | Mention→Mention (1) | be answer | [S19] agencies → Asset Exposure |
| 554 | `be applied` | 1 | Mention→Mention (1) | be applied | [S46] patching → immediately |
| 555 | `be apply significant severity to` | 1 | Mention→Mention (1) | be apply significant severity to | [S50] allowing usage of end-user risk analysis system → metrics |
| 556 | `be assessing vulnerability in` | 1 | Mention→Mention (1) | be assessing vulnerability in | [S51] analyst → library |
| 557 | `be assume` | 1 | Mention→Mention (1) | be assume | [S51] / administrator account → log back in as root |
| 558 | `be attached to` | 1 | Mention→Mention (1) | be attached to | [S17] cloud credentials → production MLflow server |
| 559 | `be authorized to access vulnerable system affected by` | 1 | Mention→Mention (1) | be authorized to access vulnerable system affected by | [S51] person → vulnerability being scored Vendor |
| 560 | `be automated list of` | 1 | Mention→Mention (1) | be automated list of | [S50] application to CVSS assessment → possible values |
| 561 | `be backed by` | 1 | Mention→Mention (1) | be backed by | [S19] those → nation-states |
| 562 | `be based on availability of` | 1 | Mention→Mention (1) | be based on availability of | [S52] vulnerability → exploit code |
| 563 | `be be in` | 1 | Mention→Mention (1) | be be in | [S43] severity of issue → Critical severity range |
| 564 | `be block ongoing attacks When` | 1 | CVE→CVE (1) | be block ongoing attacks When | [S45] patching CVE-2026-33824 security flaw → asked for more information on attacks actively targeting CVE-2026-33824 vulnerability |
| 565 | `be bypassed What by` | 1 | Mention→Mention (1) | be bypassed What by | [S39] kind of security feature → successfully exploiting vulnerability |
| 566 | `be bypassed as` | 1 | Mention→Mention (1) | be bypassed as | [S39] authentication feature → vulnerability |
| 567 | `be chained with` | 1 | Mention→Mention (1) | be chained with | [S51] other types of related vulnerabilities → vulnerabilities being assessed Specifically |
| 568 | `be cloned public repository for` | 1 | Mention→CVE (1) | be cloned public repository for | [S16] actor → CVE-2026-0300 |
| 569 | `be collected during` | 1 | Mention→Mention (1) | be collected during | [S12] evidence → recent incident response engagement |
| 570 | `be communicated within` | 1 | Mention→Mention (1) | be communicated within | [S51] this → vulnerability disclosure notice |
| 571 | `be compressed` | 1 | Mention→Mention (1) | be compressed | [S51] conditions → currently |
| 572 | `be compute` | 1 | Mention→Mention (1) | be compute | [S17] access → resources |
| 573 | `be connected to` | 1 | Mention→Mention (1) | be connected to | [S12] QUIRSO → attacker 's infrastructure |
| 574 | `be connected to attacker 's infrastructure on` | 1 | Mention→Mention (1) | be connected to attacker 's infrastructure on | [S12] QUIRSO → 3 August |
| 575 | `be considered as` | 1 | Mention→Mention (1) | be considered as | [S51] constituent elements of Subsequent System vulnerability → causing impact to Subsequent System |
| 576 | `be considered when` | 1 | Mention→Mention (1) | be considered when | [S50] other negative outcome as result of successful exploitation → assessing Impact metrics of vulnerability For example |
| 577 | `be covered in` | 1 | Mention→Mention (1) | be covered in | [S17] Metabase zero-day → August 14 post |
| 578 | `be create` | 1 | Mention→Mention (1) | be create | [S51] additional step → small change in score based on metric value changes within metric-group-based vector sets |
| 579 | `be defined` | 1 | Mention→Mention (1) | be defined | [S10] method → method |
| 580 | `be defined as` | 1 | Mention→Mention (1) | be defined as | [S52] helper functions → follows |
| 581 | `be defined for System of` | 1 | Mention→Mention (1) | be defined for System of | [S50] logical systems → Interest |
| 582 | `be deleted by` | 1 | Mention→Mention (1) | be deleted by | [S16] file → actor |
| 583 | `be described` | 1 | Mention→Mention (1) | be described | [S50] safety → Supplemental metric |
| 584 | `be described consistent with` | 1 | Mention→Mention (1) | be described consistent with | [S50] safety → above table |
| 585 | `be deserialization gadget in` | 1 | Mention→Mention (1) | be deserialization gadget in | [S10] only argument → case |
| 586 | `be deserializing it via` | 1 | Mention→Mention (1) | be deserializing it via | [S10] Using LosFormatted TypeConfuseDelegate → BDCM |
| 587 | `be designed` | 1 | Mention→Mention (1) | be designed | [S16] integrated environment → reuse |
| 588 | `be designed to prevent` | 1 | Mention→Mention (1) | be designed to prevent | [S12] security controls → unsolicited inbound access |
| 589 | `be designed to retain successful procedures across` | 1 | Mention→Mention (1) | be designed to retain successful procedures across | [S16] integrated environment → sessions |
| 590 | `be download` | 1 | Mention→Mention (1) | be download | [S51] user interaction receive → malicious content |
| 591 | `be enabled by` | 1 | Mention→Mention (1) | be enabled by | [S51] exploit-prevention techniques → default |
| 592 | `be evaluate` | 1 | Mention→Organization (1) | be evaluate | [S19] adherence with Directive provide → reporting to CISA |
| 593 | `be evaluate adherence with` | 1 | Product→Mention (1) | be evaluate adherence with | [S19] adherence with Directive provide reporting to CISA → directive |
| 594 | `be examine` | 1 | Mention→Mention (1) | be examine | [S53] to develop own customized SSVC decision tree → vulnerabilities relevant to United States government |
| 595 | `be execute code as` | 1 | Mention→Mention (1) | be execute code as | [S51] to use credentials → administrator |
| 596 | `be exfiltrated through` | 1 | Mention→Mention (1) | be exfiltrated through | [S16] memory data → Citrix NetScaler out-of-bounds memory |
| 597 | `be exploitable exploitable at` | 1 | Mention→Mention (1) | be exploitable exploitable at | [S50] attack → protocol level |
| 598 | `be exploited by` | 1 | Mention→Mention (1) | be exploited by | [S11] critical directory traversal vulnerability in vCenter Syslog server → unauthenticated attacker with network access to execute arbitrary code vendor |
| 599 | `be exploited from across` | 1 | Mention→Mention (1) | be exploited from across | [S50] vulnerability → network |
| 600 | `be exposed` | 1 | Mention→Mention (1) | be exposed | [S16] this → actor 's entire workspace |
| 601 | `be feeding` | 1 | Mention→Mention (1) | be feeding | [S48] loading scores into database joining against asset inventory → dashboard |
| 602 | `be followed by deployment of` | 1 | Mention→Mention (1) | be followed by deployment of | [S44] path-traversal exploitation of Syslog service → malicious cron job |
| 603 | `be forge JWT tokens as` | 1 | Mention→Mention (1) | be forge JWT tokens as | [S10] unauthenticated attacker → privileged account |
| 604 | `be forge access web application as` | 1 | Mention→Mention (1) | be forge access web application as | [S10] unauthenticated attacker → privileged account |
| 605 | `be found inside` | 1 | Mention→Organization (1) | be found inside | [S10] ValidateSafeBcsType → Microsoft.SharePoint / / |
| 606 | `be gathered during` | 1 | Mention→Mention (1) | be gathered during | [S44] QUIRSO 's telemetry → active incident-response engagement |
| 607 | `be granted by` | 1 | Mention→Mention (1) | be granted by | [S50] administrative privileges → default |
| 608 | `be granted by default in` | 1 | Mention→Mention (1) | be granted by default in | [S50] administrative privileges → consumer analyst 's environment |
| 609 | `be granted by default without` | 1 | Mention→Mention (1) | be granted by default without | [S50] administrative privileges → authenticating user |
| 610 | `be held by` | 1 | Mention→Mention (1) | be held by | [S43] Pwn2Own → Zero day initiative |
| 611 | `be hit` | 1 | Mention→Mention (1) | be hit | [S10] valid BDCM model instantiate System.Object visible in debugger As you can see above → Activator.CreateInstance |
| 612 | `be hosted by` | 1 | Mention→Mention (1) | be hosted by | [S51] applications → device Devices |
| 613 | `be hosted in` | 1 | Mention→Mention (1) | be hosted in | [S19] federal information systems → third-party environments |
| 614 | `be hosting` | 1 | Mention→Mention (1) | be hosting | [S51] web servers → login pages |
| 615 | `be identifying cross-agency status in` | 1 | Mention→Mention (1) | be identifying cross-agency status in | [S19] National Cyber Director → implementation of Directive report to Secretary of Homeland Security |
| 616 | `be identifying cross-agency status in implementation of` | 1 | Mention→Mention (1) | be identifying cross-agency status in implementation of | [S19] National Cyber Director → directive |
| 617 | `be identifying outstanding issues in` | 1 | Mention→Mention (1) | be identifying outstanding issues in | [S19] National Cyber Director → implementation of Directive report to Secretary of Homeland Security |
| 618 | `be identifying outstanding issues in implementation of` | 1 | Mention→Mention (1) | be identifying outstanding issues in implementation of | [S19] National Cyber Director → directive |
| 619 | `be imported within` | 1 | Mention→Mention (1) | be imported within | [S10] NET assemblies used → SharePoint |
| 620 | `be in to use` | 1 | Mention→Mention (1) | be in to use | [S52] result → integer arithmetic FIRST sincerely |
| 621 | `be included in` | 1 | Mention→Mention (1) | be included in | [S58] actively exploited vulnerability → KEV catalog |
| 622 | `be indicating` | 1 | Mention→Mention (1) | be indicating | [S16] NSC_AAAC =-RRB- → session hijacking intent |
| 623 | `be inferred from` | 1 | Mention→Mention (1) | be inferred from | [S12] exact number of victim organizations → IP addresses |
| 624 | `be informed by analysis of` | 1 | Mention→Mention (1) | be informed by analysis of | [S50] computer network defense → adversary campaigns |
| 625 | `be inject code remotely on` | 1 | Mention→Mention (1) | be inject code remotely on | [S42] unauthenticated attacker → Microsoft SharePoint |
| 626 | `be installed on` | 1 | Mention→Mention (1) | be installed on | [S42] software → systems |
| 627 | `be instructing DeepSeek to use` | 1 | Mention→Mention (1) | be instructing DeepSeek to use | [S16] custom procedure template → actor 's fofoapi.py script |
| 628 | `be integrated with` | 1 | Mention→Mention (1) | be integrated with | [S51] database → vulnerability |
| 629 | `be issued during` | 1 | Mention→Mention (1) | be issued during | [S45] advisory → April 2026 Patch |
| 630 | `be issued during April 2026 Patch` | 1 | Mention→Mention (1) | be issued during April 2026 Patch | [S45] advisory → Tuesday |
| 631 | `be joining against` | 1 | Mention→Mention (1) | be joining against | [S48] loading scores into database feeding dashboard → asset inventory |
| 632 | `be know in advance` | 1 | Mention→Mention (1) | be know in advance | [S40] attacker → user |
| 633 | `be labeled` | 1 | Mention→Mention (1) | be labeled | [S50] numerical CVSS scores → using nomenclature |
| 634 | `be leading to` | 1 | Mention→Mention (1) | be leading to | [S51] same privileges → Repudiation impact |
| 635 | `be leveraged to generate` | 1 | Mention→Mention (1) | be leveraged to generate | [S50] CVSS metrics → score |
| 636 | `be leveraged to pivot into` | 1 | Mention→Mention (1) | be leveraged to pivot into | [S17] admin-level access to SharePoint → adjacent systems |
| 637 | `be limit` | 1 | Mention→Mention (1) | be limit | [S16] actor → local response storage |
| 638 | `be listed in alphabetical order by` | 1 | Mention→Mention (1) | be listed in alphabetical order by | [S50] following CVSS Special Interest Group members → last name |
| 639 | `be locate` | 1 | Mention→Mention (1) | be locate | [S09] FindSpecificDefault method trigger → malicious gadget chain POST / / |
| 640 | `be looking` | 1 | Mention→Mention (1) | be looking | [S10] NET type → just |
| 641 | `be looking at` | 1 | Mention→Mention (1) | be looking at | [S10] NET type → function signature |
| 642 | `be made from` | 1 | Mention→Mention (1) | be made from | [S19] removals → the previous quarter |
| 643 | `be make` | 1 | Mention→Mention (1) | be make | [S54] chaining vulnerabilities → exploitation automatable |
| 644 | `be needed to` | 1 | Mention→Mention (1) | be needed to | [S10] layout more importantly → look |
| 645 | `be noting removals made from` | 1 | Mention→Mention (1) | be noting removals made from | [S19] list → the previous quarter |
| 646 | `be observed during` | 1 | Mention→Mention (1) | be observed during | [S12] post-exploitation activity → intrusion |
| 647 | `be observed to execute via tool like` | 1 | Mention→Mention (1) | be observed to execute via tool like | [S09] notepad.exe → Process Explorer |
| 648 | `be operated by` | 1 | Mention→Mention (1) | be operated by | [S19] certain systems → Intelligence Community |
| 649 | `be operated by Department of` | 1 | Mention→Mention (1) | be operated by Department of | [S19] certain systems → War |
| 650 | `be operating systems as` | 1 | Mention→Mention (1) | be operating systems as | [S19] agencies → Federal Civilian Executive Branch agencies |
| 651 | `be operating through` | 1 | Mention→Mention (1) | be operating through | [S16] Autonomous Attack Cycle DeepSeek → Hermes Agent framework |
| 652 | `be outlined in` | 1 | Mention→Mention (1) | be outlined in | [S19] actions → directive |
| 653 | `be où` | 1 | Mention→Mention (1) | be où | [S13] émis un avertissement après avoir été informé de plusieurs incidents → une vulnérabilité de la fonction de partage d'écran d'Apple |
| 654 | `be patched by` | 1 | CVE→CWE (1) | be patched by | [S40] authentication bypass vulnerability CVE-2026-55040 → Microsoft Common Weakness Enumeration of CWE-1390 are disclosing first vulnerability in chain |
| 655 | `be patched by Microsoft Common Weakness Enumeration of` | 1 | CVE→CWE (1) | be patched by Microsoft Common Weakness Enumeration of | [S40] authentication bypass vulnerability CVE-2026-55040 → CWE-1390 |
| 656 | `be patched by Microsoft for August 2026 Common Weakness Enumeration of` | 1 | CVE→CWE (1) | be patched by Microsoft for August 2026 Common Weakness Enumeration of | [S40] authentication bypass vulnerability CVE-2026-55040 → CWE-1390 |
| 657 | `be patched by Microsoft in next update cycle for August 2026 Common Weakness Enumeration of` | 1 | CVE→CWE (1) | be patched by Microsoft in next update cycle for August 2026 Common Weakness Enumeration of | [S40] authentication bypass vulnerability CVE-2026-55040 → CWE-1390 |
| 658 | `be perform conscious interactions with` | 1 | Mention→Mention (1) | be perform conscious interactions with | [S51] targeted user → vulnerable component |
| 659 | `be pertaining to` | 1 | Mention→Mention (1) | be pertaining to | [S19] status updates → directive |
| 660 | `be positioned to provide direct assessment of` | 1 | Mention→Mention (1) | be positioned to provide direct assessment of | [S50] best → Provider Urgency Recovery |
| 661 | `be pour` | 1 | Mention→Mention (1) | be pour | [S13] été exploitée → installer des mineurs de cryptomonnaie Monero La vulnérabilité |
| 662 | `be preferred over those with` | 1 | Mention→Mention (1) | be preferred over those with | [S50] Threat intelligence sources → only partial coverage |
| 663 | `be process` | 1 | Mention→Mention (1) | be process | [S10] request → model |
| 664 | `be produce severity more accurate for` | 1 | Mention→Mention (1) | be produce severity more accurate for | [S52] use of vulnerable product → organizational environment |
| 665 | `be producing` | 1 | Mention→Mention (1) | be producing | [S16] same autonomous capability → forensic artifacts |
| 666 | `be protect against` | 1 | Mention→Mention (1) | be protect against | [S19] efforts → campaigns |
| 667 | `be protect against campaigns by` | 1 | Mention→Mention (1) | be protect against campaigns by | [S19] efforts → ensuring security of information technology assets across federal enterprise Cyber threat actors |
| 668 | `be protected by Vulnerable System For` | 1 | Mention→Mention (1) | be protected by Vulnerable System For | [S50] any/all files → example |
| 669 | `be provide` | 1 | Mention→Product (1) | be provide | [S38] CVE Program → additional CVE information for record Access for more information about CVE Program Container The CISA ADP |
| 670 | `be provide cyber community` | 1 | Product→Mention (1) | be provide cyber community | [S53] Carnegie Mellon University 's Software Engineering Institute in collaboration with CISA → vulnerability analysis methodology |
| 671 | `be provided by CVE Program for` | 1 | Mention→Mention (1) | be provided by CVE Program for | [S37] required additional information → vulnerability |
| 672 | `be provided by Microsoft on` | 1 | Mention→Mention (1) | be provided by Microsoft on | [S41] details → July 31 |
| 673 | `be published by CVE Numbering Authority with` | 1 | Mention→Mention (1) | be published by CVE Numbering Authority with | [S38] CVE Records → additional related information |
| 674 | `be raise bar in` | 1 | Product→Mention (1) | be raise bar in | [S40] Rapid7 Labs ' continued effort → Vulnerability Intelligence |
| 675 | `be rated as There are details of how exactly to configure Elo scoring algorithm` | 1 | Mention→Mention (1) | be rated as There are details of how exactly to configure Elo scoring algorithm | [S51] higher-scored vector → chance |
| 676 | `be rated as There are details of run` | 1 | Mention→Mention (1) | be rated as There are details of run | [S51] higher-scored vector → chance |
| 677 | `be reduce` | 1 | Mention→Mention (1) | be reduce | [S51] using threat intelligence → CVSS-BTE score |
| 678 | `be reduced wherever` | 1 | Mention→Mention (1) | be reduced wherever | [S46] exposure → possible |
| 679 | `be refined` | 1 | Mention→Mention (1) | be refined | [S52] Base Score → Base Impact metrics |
| 680 | `be regarding` | 1 | Mention→Mention (1) | be regarding | [S50] information → availability of state of exploitation techniques |
| 681 | `be regarding availability of` | 1 | Mention→Mention (1) | be regarding availability of | [S50] information → exploitation code/processes |
| 682 | `be reporting` | 1 | Organization→Mention (1) | be reporting | [S19] CISA → instructions |
| 683 | `be represent` | 1 | Mention→Mention (1) | be represent | [S52] to use modified metrics → situations |
| 684 | `be required to enable` | 1 | Mention→Mention (1) | be required to enable | [S19] necessary actions → prompt response to requirements of Directive |
| 685 | `be requiring` | 1 | Mention→Mention (1) | be requiring | [S50] vulnerability → physical access to device |
| 686 | `be requiring unauthenticated form with` | 1 | Mention→Mention (1) | be requiring unauthenticated form with | [S16] attack sequence → file upload |
| 687 | `be responding to` | 1 | Mention→Mention (1) | be responding to | [S16] the Operation Hermes Agent → Telegram command |
| 688 | `be restrict` | 1 | Mention→Mention (1) | be restrict | [S17] firewall rules → access to known administrator IP |
| 689 | `be run it for` | 1 | Mention→Mention (1) | be run it for | [S10] what → us |
| 690 | `be run method with` | 1 | Mention→Mention (1) | be run method with | [S10] hey → arguments |
| 691 | `be running in` | 1 | Mention→Mention (1) | be running in | [S51] CVSS User space programs ' capabilities → lower privilege levels |
| 692 | `be running that with` | 1 | Mention→Mention (1) | be running that with | [S52] same Internet service → reduced privileges |
| 693 | `be running with` | 1 | Mention→Mention (1) | be running with | [S50] that same Internet service → reduced privileges |
| 694 | `be select most permissive model for` | 1 | Mention→Mention (1) | be select most permissive model for | [S16] this → campaign Note |
| 695 | `be selected of` | 1 | Mention→Mention (1) | be selected of | [S10] overload → static method |
| 696 | `be send crafted IKE traffic to` | 1 | Mention→Mention (1) | be send crafted IKE traffic to | [S46] ability → vulnerable system |
| 697 | `be send crafted request to` | 1 | Mention→Mention (1) | be send crafted request to | [S51] access → web server |
| 698 | `be set` | 1 | Mention→Mention (1) | be set | [S19] timelines → forth |
| 699 | `be set How` | 1 | Mention→Mention (1) | be set How | [S47] EPSS → thresholds |
| 700 | `be set When assessed in` | 1 | Mention→Mention (1) | be set When assessed in | [S50] subsequent system impact → environmental metric group only |
| 701 | `be set by` | 1 | Mention→Product (1) | be set by | [S19] time frame → CISA pursuant to Directive |
| 702 | `be shared with other components across` | 1 | Mention→Mention (1) | be shared with other components across | [S51] resources → multiple security scopes |
| 703 | `be sharing with` | 1 | Mention→Mention (1) | be sharing with | [S16] intelligence → team |
| 704 | `be spanning` | 1 | Mention→Mention (1) | be spanning | [S16] confirmed victims → multiple sectors |
| 705 | `be stack below` | 1 | Mention→Mention (1) | be stack below | [S08] SPJsonWebSecurityTokenHandlerV2.ValidateToken debugger call → shows |
| 706 | `be supplemented with analysis of` | 1 | Mention→Mention (1) | be supplemented with analysis of | [S51] CVSS Base Score → environment |
| 707 | `be taken by attacker` | 1 | Mention→Mention (1) | be taken by attacker | [S50] use Network metric captures measurable actions → circumvent |
| 708 | `be talk about` | 1 | Mention→Mention (1) | be talk about | [S10] a minute → concept |
| 709 | `be thought` | 1 | Mention→Mention (1) | be thought | [S50] Such vulnerability → greater severity |
| 710 | `be thought of as attack being exploitable at protocol level` | 1 | Mention→Mention (1) | be thought of as attack being exploitable at protocol level | [S50] Such vulnerability → greater severity |
| 711 | `be to run Availability impacts For` | 1 | Mention→Mention (1) | be to run Availability impacts For | [S52] default configuration for vulnerable component → example |
| 712 | `be to run Availability impacts in` | 1 | Mention→Mention (1) | be to run Availability impacts in | [S52] default configuration for vulnerable component → analyst 's environment |
| 713 | `be to run Availability impacts in analyst 's environment For` | 1 | Mention→Mention (1) | be to run Availability impacts in analyst 's environment For | [S52] default configuration for vulnerable component → example |
| 714 | `be to run listening service with` | 1 | Mention→Mention (1) | be to run listening service with | [S52] default configuration for vulnerable component → administrator privileges |
| 715 | `be to run listening service with administrator privileges For` | 1 | Mention→Mention (1) | be to run listening service with administrator privileges For | [S52] default configuration for vulnerable component → example |
| 716 | `be to run listening service with administrator privileges in analyst 's environment For` | 1 | Mention→Mention (1) | be to run listening service with administrator privileges in analyst 's environment For | [S52] default configuration for vulnerable component → example |
| 717 | `be traverse directories beyond` | 1 | Mention→Mention (1) | be traverse directories beyond | [S17] network access to vCenter management interface → intended boundaries |
| 718 | `be treated as` | 1 | Mention→Mention (1) | be treated as | [S12] match → investigative lead |
| 719 | `be treated unsolicited inbound access by` | 1 | Mention→Mention (1) | be treated unsolicited inbound access by | [S12] presence of reverse_ssh → itself |
| 720 | `be use as` | 1 | Mention→Mention (1) | be use as | [S10] logical code object → exploit |
| 721 | `be use in` | 1 | Mention→Mention (1) | be use in | [S08] x5t value → inner actortoken token |
| 722 | `be used While specific products using library generate CVSS scores specific to how they use library` | 1 | Mention→Mention (1) | be used While specific products using library generate CVSS scores specific to how they use library | [S51] library → ways |
| 723 | `be used for` | 1 | Mention→Mention (1) | be used for | [S50] CVSS standard → generating scores |
| 724 | `be used in` | 1 | Mention→Mention (1) | be used in | [S47] EPSS possible Exploitation activity data → EPSS |
| 725 | `be useful when` | 1 | Mention→Mention (1) | be useful when | [S50] Base metrics → scoring |
| 726 | `be using CVSS User space programs ' capabilities running in` | 1 | Mention→Mention (1) | be using CVSS User space programs ' capabilities running in | [S51] vulnerabilities → lower privilege levels |
| 727 | `be using conventional workflows with` | 1 | Mention→Mention (1) | be using conventional workflows with | [S16] conducted manual operations → confirmed impact |
| 728 | `be utilize Environmental Metric Group to improve quality of` | 1 | Mention→Mention (1) | be utilize Environmental Metric Group to improve quality of | [S51] Vulnerability Management team → resulting CVSS scores |
| 729 | `be utilized by` | 1 | Mention→Mention (1) | be utilized by | [S50] security mechanisms → vulnerable system |
| 730 | `be verified` | 1 | Mention→Mention (1) | be verified | [S08] signature → cryptographically |
| 731 | `be verified against` | 1 | Mention→Mention (1) | be verified against | [S08] signature → resolved signing key code |
| 732 | `be win` | 1 | Mention→Mention (1) | be win | [S51] attack → race condition |
| 733 | `becomes aware of` | 1 | Organization→Mention (1) | becomes aware of | [S54] CISA → vulnerability |
| 734 | `began` | 1 | Mention→Mention (1) | began | [S17] exploitation → five days later |
| 735 | `began five days later on` | 1 | Mention→Mention (1) | began five days later on | [S17] exploitation → August 3 |
| 736 | `begin to construct` | 1 | Mention→Mention (1) | begin to construct | [S08] we → malicious JWT |
| 737 | `begin to use` | 1 | Mention→Mention (1) | begin to use | [S08] we → new FormDigestValue |
| 738 | `behavior of software gives threat actor` | 1 | Mention→Mention (1) | behavior of software gives threat actor | [S19] information exposure → low stochastic opportunity for total control In context defined in Circular A-130 as information system operated about |
| 739 | `behavior of software gives threat actor low stochastic opportunity for` | 1 | Mention→Mention (1) | behavior of software gives threat actor low stochastic opportunity for | [S54] information exposure → about |
| 740 | `believe` | 1 | Mention→Mention (1) | believe | [S16] they → account |
| 741 | `bound to` | 1 | Mention→Mention (1) | bound to | [S10] new external list → model |
| 742 | `breaches` | 1 | Mention→Mention (1) | breaches | [S52] impact of vulnerability → impacts components |
| 743 | `breaches security/trust boundary outside` | 1 | Mention→Mention (1) | breaches security/trust boundary outside | [S52] impact of vulnerability → security scope |
| 744 | `bypass authentication In` | 1 | Mention→Mention (1) | bypass authentication In | [S39] unauthenticated attacker → network-based attack |
| 745 | `call Deserialize` | 1 | Mention→Mention (1) | call Deserialize | [S10] we → Deserialize |
| 746 | `call Deserialize with base64-encoded string as` | 1 | Mention→Mention (1) | call Deserialize with base64-encoded string as | [S10] we → only argument Deserialize |
| 747 | `calls to fetch` | 1 | Mention→Mention (1) | calls to fetch | [S10] SharePoint → entity 's rows method |
| 748 | `capture effects of` | 1 | Mention→Mention (1) | capture effects of | [S50] Impact metrics → successfully exploited vulnerability Analysts |
| 749 | `captures` | 1 | Mention→Mention (1) | captures | [S50] metric → answer to question |
| 750 | `captures adversary control of` | 1 | Mention→Mention (1) | captures adversary control of | [S54] technical impact → computer system |
| 751 | `captures answer` | 1 | Mention→Mention (1) | captures answer | [S54] Automatable → exploitation events |
| 752 | `captures answer to` | 1 | Mention→Mention (1) | captures answer to | [S54] Automatable → question exploitation events |
| 753 | `caused exposure of` | 1 | Mention→Mention (1) | caused exposure of | [S16] same autonomous capability → operation |
| 754 | `caused exposure of operation` | 1 | Mention→Mention (1) | caused exposure of operation | [S16] same autonomous capability → producing forensic artifacts |
| 755 | `causes it to disclose plaintext password of` | 1 | Mention→Mention (1) | causes it to disclose plaintext password of | [S51] operating system → root |
| 756 | `causes web server to disclose plaintext password of` | 1 | Mention→Mention (1) | causes web server to disclose plaintext password of | [S51] web server → root |
| 757 | `change Attack Complexity to` | 1 | Mention→Mention (1) | change Attack Complexity to | [S51] that → High |
| 758 | `check` | 1 | Mention→Mention (1) | check | [S10] type from LobSystem → type |
| 759 | `chose to bind` | 1 | Mention→Mention (1) | chose to bind | [S10] we → it |
| 760 | `code` | 1 | Mention→Mention (1) | code | [S10] cs → above |
| 761 | `compares to` | 1 | Mention→Mention (1) | compares to | [S47] EPSS → other tools |
| 762 | `compute` | 1 | Mention→Mention (1) | compute | [S08] we → x5t |
| 763 | `configured Claude Code anti-attribution settings on` | 1 | Mention→Mention (1) | configured Claude Code anti-attribution settings on | [S16] actor → tools |
| 764 | `configured Claude Code with CLAUDE_CODE_ATTRIBUTION_HEADER anti-attribution settings on` | 1 | Mention→Mention (1) | configured Claude Code with CLAUDE_CODE_ATTRIBUTION_HEADER anti-attribution settings on | [S16] actor → tools |
| 765 | `configured multiple large language models In` | 1 | Mention→Mention (1) | configured multiple large language models In | [S16] actor → parallel with use of DeepSeek as autonomous operator platform |
| 766 | `configured system to limit` | 1 | Mention→Mention (1) | configured system to limit | [S16] actor → local response storage |
| 767 | `confirms` | 1 | Vendor→Mention (1) | confirms | [S40] Microsoft → findings |
| 768 | `consolidated remote access onto Cisco ASA during` | 1 | Mention→Mention (1) | consolidated remote access onto Cisco ASA during | [S17] organisations → 2020 |
| 769 | `consolidated remote access onto FTD hardware during` | 1 | Mention→Mention (1) | consolidated remote access onto FTD hardware during | [S17] organisations → 2020 |
| 770 | `constrain` | 1 | Mention→Mention (1) | constrain | [S52] analysts → impacts |
| 771 | `constrain impacts to` | 1 | Mention→Mention (1) | constrain impacts to | [S52] analysts → reasonable final outcome |
| 772 | `contained in` | 1 | Mention→Mention (1) | contained in | [S14] damage resulting from inaccuracy of incompleteness of information → advisory security advisory |
| 773 | `contains authentication bypass vulnerability in` | 1 | Mention→Mention (1) | contains authentication bypass vulnerability in | [S43] VMware vCenter → VMware Directory Service Broadcom |
| 774 | `contains web-friendly version of Cybersecurity` | 1 | Mention→Mention (1) | contains web-friendly version of Cybersecurity | [S19] page → risk |
| 775 | `continue to add` | 1 | CVE→Mention (1) | continue to add | [S28] CVE-2026-65400 Apple macOS Improper Authentication Vulnerability types of vulnerabilities are frequent attack vector for malicious cyber actors → vulnerabilities |
| 776 | `continued` | 1 | Mention→Mention (1) | continued | [S12] we → investigating activity Follow-up Investigation Published As announced in initial analysis |
| 777 | `continues to deliver` | 1 | Mention→Mention (1) | continues to deliver | [S42] attacker → attack |
| 778 | `crashes` | 1 | Mention→Mention (1) | crashes | [S51] same security scope A vulnerability → web server |
| 779 | `dans coin supérieur gauche de` | 1 | Mention→Mention (1) | dans coin supérieur gauche de | [S13] Cliquez sur menu Apple → votre écran |
| 780 | `decide on vulnerability response actions consistent with` | 1 | Mention→Mention (1) | decide on vulnerability response actions consistent with | [S53] analyst → priorities |
| 781 | `decided to go` | 1 | Mention→Mention (1) | decided to go | [S10] we → different route Based on prior experience building overload being selected instead of static method |
| 782 | `defer` | 1 | Mention→Mention (1) | defer | [S17] organisation → applying critical vCenter patch |
| 783 | `defer applying critical vCenter patch how` | 1 | Mention→Mention (1) | defer applying critical vCenter patch how | [S17] organisation → long |
| 784 | `defer applying critical vCenter patch without` | 1 | Mention→Mention (1) | defer applying critical vCenter patch without | [S17] organisation → accepting active exploitation risk |
| 785 | `define DefaultValues for` | 1 | Mention→Mention (1) | define DefaultValues for | [S10] output value is TypeDescriptor element → parameter |
| 786 | `define in model to do something` | 1 | Mention→Mention (1) | define in model to do something | [S10] we → something like get specific value from database |
| 787 | `defined MethodInstance as` | 1 | Mention→Mention (1) | defined MethodInstance as | [S10] we → Finder |
| 788 | `defines argument for` | 1 | Mention→Mention (1) | defines argument for | [S10] MethodInstance A Parameter → method |
| 789 | `defines type of` | 1 | Mention→Mention (1) | defines type of | [S10] TypeDescriptor element → parent Parameter element A TypeDescriptor |
| 790 | `demonstrated` | 1 | Mention→Mention (1) | demonstrated | [S16] actor → operational security awareness |
| 791 | `demonstrates impact to` | 1 | Mention→Mention (1) | demonstrates impact to | [S51] Subsequent System concepts → Subsequent System to Vulnerable System |
| 792 | `deployed` | 1 | Mention→Mention (1) | deployed | [S11] attacker → open-source reverse_ssh framework |
| 793 | `describe additional extrinsic attributes of` | 1 | Mention→Mention (1) | describe additional extrinsic attributes of | [S50] new metrics → vulnerability |
| 794 | `describes issue as` | 1 | CVE→Mention (1) | describes issue as | [S10] CVE-2026-63520 Rapid7 's disclosure for CVE-2026-63520 → unsafe |
| 795 | `describes level of` | 1 | Mention→Mention (1) | describes level of | [S42] this metric → privileges |
| 796 | `deserialize` | 1 | Mention→Mention (1) | deserialize | [S10] method → object |
| 797 | `deserves` | 1 | Mention→Mention (1) | deserves | [S44] Hypervisor management infrastructure → same monitoring rigor |
| 798 | `detects` | 1 | Mention→Mention (1) | detects | [S11] generic YARA rule → reverse_ssh client binaries |
| 799 | `determined following preliminary metrics subgroups` | 1 | Mention→Mention (1) | determined following preliminary metrics subgroups | [S50] SIG → relevant MacroVectors |
| 800 | `developed` | 1 | Mention→Mention (1) | developed | [S16] actor → same autonomous capability |
| 801 | `developed for offensive use` | 1 | Mention→Mention (1) | developed for offensive use | [S16] actor → same autonomous capability |
| 802 | `dictated` | 1 | Mention→Mention (1) | dictated | [S10] we → XML-based specs |
| 803 | `did encompass more traditional vulnerability research such as` | 1 | Mention→Mention (1) | did encompass more traditional vulnerability research such as | [S40] sprints → manual code review |
| 804 | `did test` | 1 | Mention→Mention (1) | did test | [S10] we → this |
| 805 | `diffed` | 1 | Mention→Patch/update (1) | diffed | [S10] team → KB5002893 |
| 806 | `differ` | 1 | Mention→Mention (1) | differ | [S50] these → attack |
| 807 | `differ as primary purpose of conditions is to mitigate attacks` | 1 | Mention→Mention (1) | differ as primary purpose of conditions is to mitigate attacks | [S50] these → attack |
| 808 | `differ emerge as consequence of execution If attacker does take action to overcome conditions` | 1 | Mention→Mention (1) | differ emerge as consequence of execution If attacker does take action to overcome conditions | [S50] these → attack |
| 809 | `differ from security-enhancing techniques/technologies` | 1 | Mention→Mention (1) | differ from security-enhancing techniques/technologies | [S50] these → attack |
| 810 | `differ on cause of` | 1 | Mention→Mention (1) | differ on cause of | [S52] reports → vulnerability |
| 811 | `digest` | 1 | Mention→Mention (1) | digest | [S08] SHA1 → value |
| 812 | `directed agencies to` | 1 | Mention→Mention (1) | directed agencies to | [S19] BOD 22-01 → remediate |
| 813 | `directed agencies to remediate` | 1 | Mention→Mention (1) | directed agencies to remediate | [S19] BOD 22-01 → aggressively |
| 814 | `disables / / explicitly` | 1 | Mention→Mention (1) | disables / / explicitly | [S08] code → signature requirements |
| 815 | `disables / / signature requirements When constructing TokenValidationParameters for` | 1 | Mention→Product (1) | disables / / signature requirements When constructing TokenValidationParameters for | [S08] code → underlying Microsoft.IdentityModel JWT library |
| 816 | `disclosed CVE-2026-59310 on` | 1 | Mention→Mention (1) | disclosed CVE-2026-59310 on | [S11] France Broadcom → July 29 |
| 817 | `discloses` | 1 | Mention→Mention (1) | discloses | [S54] vulnerability → authentication credentials |
| 818 | `discover` | 1 | Mention→Mention (1) | discover | [S08] we → target realm |
| 819 | `discusses leveraging BDC models for` | 1 | CVE→Mention (1) | discusses leveraging BDC models for | [S09] writeup of CVE-2019-1257 by ZDI research team → unsafe |
| 820 | `do align with` | 1 | Mention→Product (1) | do align with | [S53] organizations mission spaces → CISA 's decision tree |
| 821 | `do replace` | 1 | Mention→Mention (1) | do replace | [S07] actions → installing security addresses |
| 822 | `do this` | 1 | Mention→Mention (1) | do this | [S08] we → x509 certificate of STS signing certificate from target SharePoint site |
| 823 | `do use IKE For` | 1 | Mention→Mention (1) | do use IKE For | [S07] systems → systems |
| 824 | `do use to configure` | 1 | Mention→Mention (1) | do use to configure | [S45] systems → firewall rules to allow inbound traffic only from known peer addresses |
| 825 | `document BDCM schema in` | 1 | Mention→Mention (1) | document BDCM schema in | [S10] official SharePoint GitHub docs → parent-child hierarchy |
| 826 | `does change priority of` | 1 | Mention→Mention (1) | does change priority of | [S54] value of mitigation → SSVC decision mitigation information |
| 827 | `does change priority of SSVC decision mitigation information Based on` | 1 | Mention→Organization (1) | does change priority of SSVC decision mitigation information Based on | [S54] value of mitigation → CISA decision tree |
| 828 | `does have open connectivity to` | 1 | Mention→Mention (1) | does have open connectivity to | [S54] vulnerable component → internet |
| 829 | `does impact retention of` | 1 | Mention→Mention (1) | does impact retention of | [S16] setting → safety signals |
| 830 | `does take action to overcome` | 1 | Mention→Mention (1) | does take action to overcome | [S50] attacker → conditions |
| 831 | `downloaded` | 1 | Mention→Mention (1) | downloaded | [S16] they → it |
| 832 | `downloaded it from` | 1 | Mention→Mention (1) | downloaded it from | [S16] they → public repositories |
| 833 | `egress to` | 1 | Mention→Mention (1) | egress to | [S57] metadata API → → new external hosts |
| 834 | `embraces Centers` | 1 | Mention→Mention (1) | embraces Centers | [S54] that negatively impact well-being SVCC → those |
| 835 | `embraces Centers for Disease Control expansive definition of` | 1 | Mention→Mention (1) | embraces Centers for Disease Control expansive definition of | [S54] that negatively impact well-being SVCC → well-being those |
| 836 | `emerge` | 1 | Mention→Mention (1) | emerge | [S50] primary purpose of conditions → naturally |
| 837 | `emerge as` | 1 | Mention→Mention (1) | emerge as | [S50] primary purpose of conditions → consequence of deployment of vulnerable system |
| 838 | `emerge as consequence of` | 1 | Mention→Mention (1) | emerge as consequence of | [S50] primary purpose of conditions → execution |
| 839 | `emerging trends` | 1 | Mention→Mention (1) | emerging trends | [S10] we → high-fidelity insights to market |
| 840 | `employs` | 1 | Mention→Mention (1) | employs | [S51] organization → automated methods |
| 841 | `employs automated methods to` | 1 | Mention→Mention (1) | employs automated methods to | [S51] organization → comprehensively utilize Threat metric groups is listed below concept of Scope |
| 842 | `enabled anti-attribution settings on` | 1 | Mention→Mention (1) | enabled anti-attribution settings on | [S16] actor → tools |
| 843 | `enables attacker` | 1 | Mention→Mention (1) | enables attacker | [S51] virtual machine → delete |
| 844 | `enables attacker to read files on` | 1 | Mention→Mention (1) | enables attacker to read files on | [S51] virtual machine → host operating system |
| 845 | `enables authorized organization to enrich content of` | 1 | Mention→Mention (1) | enables authorized organization to enrich content of | [S38] Authorized Data Publishers CVE Program ADP role → CVE Records published by CVE Numbering Authority with additional related information |
| 846 | `enables qualified organization to enrich content of` | 1 | Mention→Mention (1) | enables qualified organization to enrich content of | [S38] Authorized Data Publishers CVE Program ADP role → CVE Records published by CVE Numbering Authority with additional related information |
| 847 | `ends at` | 1 | Mention→Mention (1) | ends at | [S16] exploitation recovered session data → point |
| 848 | `enumerates` | 1 | Mention→Mention (1) | enumerates | [S19] agency → pursuant to BOD 23-01 |
| 849 | `environment describe` | 1 | Mention→Mention (1) | environment describe | [S50] Supplemental Metrics → Finally |
| 850 | `evolves upon` | 1 | Mention→Product (1) | evolves upon | [S19] directive → CISA 's KEV Catalog |
| 851 | `examines` | 1 | Mention→Mention (1) | examines | [S12] we → potential connection to exploitation of related CVE-2026 Follow-up Investigation Published As announced in initial analysis |
| 852 | `executed hundreds of hours of manual targeting analysis in` | 1 | Mention→Mention (1) | executed hundreds of hours of manual targeting analysis in | [S16] system → mere minutes |
| 853 | `executes` | 1 | Mention→Mention (1) | executes | [S10] fully authenticated deserialization → calc process |
| 854 | `executes calc process on` | 1 | Mention→Mention (1) | executes calc process on | [S10] fully authenticated deserialization → vulnerable SharePoint server |
| 855 | `executes in` | 1 | Mention→Mention (1) | executes in | [S50] set of computing logic → environment with set of security policies |
| 856 | `executes in environment with` | 1 | Mention→Mention (1) | executes in environment with | [S50] set of computing logic → coherent function |
| 857 | `exists` | 1 | Mention→Mention (1) | exists | [S54] organization → reason |
| 858 | `exists in more components of such system technology product or solution set of` | 1 | Mention→Mention (1) | exists in more components of such system technology product or solution set of | [S50] vulnerability → security policies |
| 859 | `exists in solution set of` | 1 | Mention→Mention (1) | exists in solution set of | [S50] vulnerability → security policies |
| 860 | `exists set of` | 1 | Mention→Mention (1) | exists set of | [S50] vulnerability → security policies |
| 861 | `expands beyond` | 1 | Mention→Mention (1) | expands beyond | [S12] it → initial victim telemetry |
| 862 | `expect method to use to perform` | 1 | Mention→Mention (1) | expect method to use to perform | [S10] SharePoint → CRUD operation |
| 863 | `exploit from` | 1 | Mention→Mention (1) | exploit from | [S16] public PoC → GitHub |
| 864 | `exploit gives threat actor` | 1 | Mention→Mention (1) | exploit gives threat actor | [S19] information exposure → low stochastic opportunity for total control In context defined in Circular A-130 as information system operated about |
| 865 | `exploit gives threat actor low stochastic opportunity for` | 1 | Mention→Mention (1) | exploit gives threat actor low stochastic opportunity for | [S54] information exposure → about |
| 866 | `exploited it over multiple days with` | 1 | Mention→Mention (1) | exploited it over multiple days with | [S16] they → memory grooming parameters |
| 867 | `exploits Apache/Nginx/app servers` | 1 | Mention→Mention (1) | exploits Apache/Nginx/app servers | [S57] → optional outbound callback from host/container Adversary → loads non-standard modules |
| 868 | `expose IKE services to` | 1 | Mention→Mention (1) | expose IKE services to | [S46] patching systems → untrusted networks |
| 869 | `extracts Bearer token from` | 1 | Mention→Mention (1) | extracts Bearer token from | [S08] which → Authorization header |
| 870 | `faces` | 1 | Mention→Mention (1) | faces | [S19] United States → persistent increasingly sophisticated malicious cyber campaigns |
| 871 | `facilitating` | 1 | Mention→Mention (1) | facilitating | [S50] tireless work → CVSS SIG meetings |
| 872 | `failed` | 1 | Mention→Mention (1) | failed | [S16] initial exploitation → due to target environment 's restrictive configurations |
| 873 | `finds match` | 1 | Mention→Mention (1) | finds match | [S08] resolver → LocalLoginProvider access provider |
| 874 | `fires` | 1 | Mention→Mention (1) | fires | [S10] it → automatically moment |
| 875 | `focus` | 1 | Mention→Mention (1) | focus | [S47] you → limited remediation effort |
| 876 | `focuses on specific informational elements agreed upon with CVE Program as scope of` | 1 | Mention→Mention (1) | focuses on specific informational elements agreed upon with CVE Program as scope of | [S38] ADP → ADP 's contributions |
| 877 | `follow` | 1 | Mention→Product (1) | follow | [S19] agencies → CISA 's Internet Exposure Reduction Guidance |
| 878 | `follow CISA 's Internet Exposure Reduction Guidance to answer` | 1 | Mention→Mention (1) | follow CISA 's Internet Exposure Reduction Guidance to answer | [S19] agencies → Asset Exposure |
| 879 | `follow path of` | 1 | Mention→Mention (1) | follow path of | [S16] threat actors → least resistance |
| 880 | `follow path of least resistance For` | 1 | Mention→Mention (1) | follow path of least resistance For | [S16] threat actors → autonomous attack engine |
| 881 | `followed within` | 1 | Mention→Mention (1) | followed within | [S17] exploitation → hours |
| 882 | `follows same requirements from` | 1 | Mention→Mention (1) | follows same requirements from | [S19] supporting CSP infrastructure → directive |
| 883 | `found` | 1 | Mention→Mention (1) | found | [S43] Response Matrix ' → Fixed Version ' column |
| 884 | `framed` | 1 | Mention→Mention (1) | framed | [S52] CVSS Special Interest Group → lookup table |
| 885 | `framed lookup table by` | 1 | Mention→Mention (1) | framed lookup table by | [S52] CVSS Special Interest Group → assigning metric values |
| 886 | `framed lookup table to` | 1 | Mention→Mention (1) | framed lookup table to | [S52] CVSS Special Interest Group → real vulnerabilities |
| 887 | `gain complete control of` | 1 | Mention→Mention (1) | gain complete control of | [S46] attacker → affected system |
| 888 | `gain control over with` | 1 | Mention→Mention (1) | gain control over with | [S50] attacker → single exploitation event |
| 889 | `gets SharePoint to run` | 1 | Mention→Mention (1) | gets SharePoint to run | [S10] what → it for us just by querying list |
| 890 | `gets SharePoint to run it for` | 1 | Mention→Mention (1) | gets SharePoint to run it for | [S10] what → us |
| 891 | `gets patched` | 1 | Product→Mention (1) | gets patched | [S44] vCenter → reactively |
| 892 | `gets patched for` | 1 | Product→Mention (1) | gets patched for | [S44] vCenter → vulnerabilities |
| 893 | `goes offline simultaneously For` | 1 | Mention→Mention (1) | goes offline simultaneously For | [S17] site-to-site tunnel → organisations |
| 894 | `had applied` | 1 | Mention→Mention (1) | had applied | [S17] organisations → July patches |
| 895 | `had customized` | 1 | Mention→Mention (1) | had customized | [S16] actor → Hermes Agent |
| 896 | `had limited` | 1 | Mention→Mention (1) | had limited | [S16] observed campaign → impacts |
| 897 | `has advanced knowledge of` | 1 | Mention→Mention (1) | has advanced knowledge of | [S50] attacker → target system |
| 898 | `has been altered` | 1 | Mention→Mention (1) | has been altered | [S51] web content → maliciously |
| 899 | `has been assigned` | 1 | Mention→Mention (1) | has been assigned | [S46] vulnerability → high exploitation confidence rating |
| 900 | `has been documented` | 1 | Mention→Mention (1) | has been documented | [S17] availability disruption → 2026 's threat landscape |
| 901 | `has been expedited remote authenticated attacker details of` | 1 | Mention→CVE (1) | has been expedited remote authenticated attacker details of | [S09] timeline → CVE-2026-63520 |
| 902 | `has been provided` | 1 | Mention→Mention (1) | has been provided | [S41] following statement → Vendor statement |
| 903 | `has been provided by` | 1 | Mention→Vendor (1) | has been provided by | [S40] following statement → Microsoft |
| 904 | `has been provided by Microsoft` | 1 | Mention→Mention (1) | has been provided by Microsoft | [S41] following statement → Vendor statement |
| 905 | `has been updated to reflect` | 1 | Mention→Mention (1) | has been updated to reflect | [S41] disclosure blog → this |
| 906 | `has best understanding of` | 1 | Mention→Mention (1) | has best understanding of | [S54] analyst → plausible scenarios |
| 907 | `has capabilities running in` | 1 | Mention→Mention (1) | has capabilities running in | [S51] CVSS User space programs → lower privilege levels |
| 908 | `has colleagues at` | 1 | Mention→Mention (1) | has colleagues at | [S16] our → OpenAI |
| 909 | `has column of` | 1 | Mention→Mention (1) | has column of | [S43] Fixed Version → Response Matrix ' found below of Response Matrix ' found below Broadcom |
| 910 | `has disclosure for` | 1 | CVE→CVE (1) | has disclosure for | [S10] CVE-2026-63520 Rapid7 → CVE-2026-63520 |
| 911 | `has intelligence sharing with` | 1 | Mention→Mention (1) | has intelligence sharing with | [S16] our → team |
| 912 | `has located` | 1 | Mention→Mention (1) | has located | [S52] attacker → already |
| 913 | `has maintenance of` | 1 | Mention→Mention (1) | has maintenance of | [S16] their → 1DayNews |
| 914 | `has mapped` | 1 | Mention→Mention (1) | has mapped | [S17] attacker → environment |
| 915 | `has own STS certificate via` | 1 | Mention→Mention (1) | has own STS certificate via | [S08] SharePoint → x5t |
| 916 | `has parameterless constructor with` | 1 | Mention→Mention (1) | has parameterless constructor with | [S10] it → useful Instance Method |
| 917 | `has perfect knowledge of` | 1 | Mention→Mention (1) | has perfect knowledge of | [S50] attacker → vulnerability |
| 918 | `has provided` | 1 | Mention→CVE (1) | has provided | [S41] vendor → following updates to remediate CVE-2026-63520 KB5002893 |
| 919 | `has provided following updates to remediate CVE-2026-55040 KB5002882` | 1 | Mention→CVE (1) | has provided following updates to remediate CVE-2026-55040 KB5002882 | [S40] vendor → CVE-2026-55040 here |
| 920 | `has published full technical details for` | 1 | Organization→CVE (1) | has published full technical details for | [S40] Technical analysis Rapid7 → CVE-2026-55040 here |
| 921 | `has published in CNA container` | 1 | Mention→Mention (1) | has published in CNA container | [S38] CNA → data |
| 922 | `has published in-depth technical analysis of flaw accompanied by proof-of-concept` | 1 | Mention→Organization (1) | has published in-depth technical analysis of flaw accompanied by proof-of-concept | [S18] Stephen Fewer → Rapid7 |
| 923 | `has script for` | 1 | Mention→Mention (1) | has script for | [S09] our → authentication bypass |
| 924 | `has to return` | 1 | Mention→Mention (1) | has to return | [S10] it → collection |
| 925 | `has to return collection by` | 1 | Mention→Mention (1) | has to return collection by | [S10] it → convention |
| 926 | `has to update` | 1 | Vendor→Mention (1) | has to update | [S45] Microsoft → its advisory to flag |
| 927 | `has tracked` | 1 | Mention→Mention (1) | has tracked | [S17] DIESEC → same systematic methodology |
| 928 | `has tracked same systematic methodology throughout` | 1 | Mention→Mention (1) | has tracked same systematic methodology throughout | [S17] DIESEC → 2026 |
| 929 | `has use of` | 1 | Mention→Mention (1) | has use of | [S19] their → AI |
| 930 | `have automated vulnerability reporting through` | 1 | Mention→Mention (1) | have automated vulnerability reporting through | [S19] agencies → CDM Program |
| 931 | `have been exploited which in` | 1 | Mention→Mention (1) | have been exploited which in | [S51] vulnerabilities → the past |
| 932 | `have been generated via script for` | 1 | Mention→Mention (1) | have been generated via script for | [S09] Bearer authorization token along with X-RequestDigest token used in following requests → authentication bypass |
| 933 | `have been published technical details for` | 1 | Mention→Mention (1) | have been published technical details for | [S41] technical details for RCE vulnerability → authentication bypass vulnerability Technical analysis |
| 934 | `have been published technical details for authentication bypass vulnerability` | 1 | Mention→Mention (1) | have been published technical details for authentication bypass vulnerability | [S41] technical details for RCE vulnerability → Technical analysis |
| 935 | `have begun` | 1 | Mention→Product (1) | have begun | [S18] public Threat actors → exploiting critical Microsoft SharePoint flaw |
| 936 | `have certain information For` | 1 | Mention→Mention (1) | have certain information For | [S10] you → instance |
| 937 | `have concentrated` | 1 | Mention→Mention (1) | have concentrated | [S51] cloud service providers However → value |
| 938 | `have evidence of` | 1 | Mention→Mention (1) | have evidence of | [S28] KEV Nomination Form Potential KEV additions → exploitation |
| 939 | `have had prior knowledge of` | 1 | Mention→Mention (1) | have had prior knowledge of | [S12] attacker → vulnerability |
| 940 | `have processed` | 1 | Mention→Mention (1) | have processed | [S17] most organisations → advisory |
| 941 | `have significant impact on` | 1 | Mention→Mention (1) | have significant impact on | [S51] use of Exploit Maturity E metric Knowing which vulnerabilities have been exploited in the past → resulting score |
| 942 | `have targeted` | 1 | Mention→Mention (1) | have targeted | [S17] attackers → material |
| 943 | `have targeted material throughout` | 1 | Mention→Mention (1) | have targeted material throughout | [S17] attackers → 2026 's supply chain exploitation arc |
| 944 | `have to react between` | 1 | Mention→Mention (1) | have to react between | [S19] defenders → patch release and possible exploitation time |
| 945 | `heeft` | 1 | Mention→Mention (1) | heeft | [S14] Het NCSC → een melding ontvangen waaruit blijkt dat er actief misbruik van deze kwetbaarheid |
| 946 | `holds credentials for` | 1 | Mention→Mention (1) | holds credentials for | [S17] Metabase → business databases MLflow |
| 947 | `hone autonomous attack processes retarget without` | 1 | Mention→Mention (1) | hone autonomous attack processes retarget without | [S16] they → human intervention |
| 948 | `hops` | 1 | Mention→Mention (1) | hops | [S50] network → more |
| 949 | `identified attempted exploitation through` | 1 | Mention→Mention (1) | identified attempted exploitation through | [S16] Langflow Exploitation DeepSeek → following steps |
| 950 | `identified testing of` | 1 | Mention→Mention (1) | identified testing of | [S16] we → Western platforms |
| 951 | `identified that from` | 1 | Mention→Mention (1) | identified that from | [S10] we → this |
| 952 | `identifies new KEVs` | 1 | Organization→Mention (1) | identifies new KEVs | [S19] CISA → rate |
| 953 | `identifies value Instead of declaring decision point as` | 1 | Organization→Mention (1) | identifies value Instead of declaring decision point as | [S54] CISA → unknown |
| 954 | `identifies vulnerabilities as` | 1 | Organization→Product (1) | identifies vulnerabilities as | [S19] CISA → carrying significant risk to federal enterprise within time frame set by CISA pursuant to Directive |
| 955 | `identifies vulnerabilities through inclusion in` | 1 | Organization→Mention (1) | identifies vulnerabilities through inclusion in | [S19] CISA → KEV catalog |
| 956 | `identify as Furthermore` | 1 | Mention→Mention (1) | identify as Furthermore | [S40] they → user |
| 957 | `identify in example` | 1 | Mention→Mention (1) | identify in example | [S08] we → SharePoint user |
| 958 | `impact` | 1 | Mention→Mention (1) | impact | [S38] information → SSVC decision points |
| 959 | `impact to availability of impacted component resulting from exploited vulnerability refers` | 1 | Mention→Mention (1) | impact to availability of impacted component resulting from exploited vulnerability refers | [S52] this metric → metric measures |
| 960 | `impacts Integrity of` | 1 | Mention→Mention (1) | impacts Integrity of | [S51] it → system |
| 961 | `impacts Integrity of system along with` | 1 | Mention→Mention (1) | impacts Integrity of system along with | [S51] it → other subsequent impacts |
| 962 | `implements own validation logic in` | 1 | Mention→Mention (1) | implements own validation logic in | [S08] SharePoint → separate methods |
| 963 | `include IKEv2 Remote Access VPN with` | 1 | Mention→Mention (1) | include IKEv2 Remote Access VPN with | [S17] Affected configurations → Client Services |
| 964 | `included in` | 1 | Mention→Mention (1) | included in | [S10] Only types → farm 's BCSAllowedTypeNames |
| 965 | `includes fix for` | 1 | Mention→Mention (1) | includes fix for | [S43] which → CVE 3b |
| 966 | `includes further discussion of CVSS guidelines on glossary of terms used` | 1 | Mention→Mention (1) | includes further discussion of CVSS guidelines on glossary of terms used | [S52] User Guide → companion to Specification |
| 967 | `increases mission readiness across` | 1 | Mention→Mention (1) | increases mission readiness across | [S19] directive → federal government |
| 968 | `increases mission readiness across federal government by prioritizing high-risk vulnerabilities for` | 1 | Mention→Mention (1) | increases mission readiness across federal government by prioritizing high-risk vulnerabilities for | [S19] directive → timely action |
| 969 | `increases mission readiness across federal government while deferring action against` | 1 | Mention→Mention (1) | increases mission readiness across federal government while deferring action against | [S19] directive → low-risk vulnerabilities |
| 970 | `information exposure gives threat actor low stochastic opportunity for` | 1 | Mention→Mention (1) | information exposure gives threat actor low stochastic opportunity for | [S54] behavior of software → about |
| 971 | `inherits from` | 1 | Mention→Mention (1) | inherits from | [S09] DbTypeReflector → DotNetTypeReflector |
| 972 | `introduces` | 1 | Mention→Mention (1) | introduces | [S46] this → pathway to remote code execution |
| 973 | `introduces pathway to remote code execution within context of` | 1 | Mention→Mention (1) | introduces pathway to remote code execution within context of | [S46] this → IKE service Exploitation |
| 974 | `is For` | 1 | Mention→Organization (1) | is For | [S54] exploitation of vulnerability → CISA |
| 975 | `is System.Web.HttpApplication httpApplication out` | 1 | Organization→Mention (1) | is System.Web.HttpApplication httpApplication out | [S08] Microsoft.SharePoint.IdentityModel.dll!Microsoft.SharePoint.IdentityModel.SPApplicationAuthenticationModuleV2.ConstructIClaimsPrincipalAndSetThreadIdentity → string tokenType |
| 976 | `is able` | 1 | Mention→Mention (1) | is able | [S54] analyst → given information currently available |
| 977 | `is able to` | 1 | Mention→Mention (1) | is able to | [S54] analyst → sketch |
| 978 | `is accessible via public networks such as` | 1 | Mention→Mention (1) | is accessible via public networks such as | [S19] asset in scope of directive → internet |
| 979 | `is acting under usual capabilities of` | 1 | Mention→Mention (1) | is acting under usual capabilities of | [S51] attacker → application |
| 980 | `is administrative control plane for` | 1 | Product→Mention (1) | is administrative control plane for | [S17] vCenter → VMware vSphere |
| 981 | `is analyst need consider means` | 1 | Mention→Mention (1) | is analyst need consider means | [S50] that → vulnerability |
| 982 | `is analyzed as` | 1 | Mention→Mention (1) | is analyzed as | [S54] vulnerability with presence across multiple related systems → multiple |
| 983 | `is applicable operating systems For` | 1 | Mention→Mention (1) | is applicable operating systems For | [S51] hypothetical vulnerability → example |
| 984 | `is assigned score of` | 1 | Mention→Mention (1) | is assigned score of | [S50] highest severity vector of MacroVector → MacroVector |
| 985 | `is assigned score of MacroVector from` | 1 | Mention→Mention (1) | is assigned score of MacroVector from | [S50] highest severity vector of MacroVector → cvss_lookup |
| 986 | `is attacker know in` | 1 | Mention→Mention (1) | is attacker know in | [S40] prerequisite → advance user |
| 987 | `is available in` | 1 | Mention→Mention (1) | is available in | [S58] KEV catalog → formats NEW KEV |
| 988 | `is available through` | 1 | Mention→Mention (1) | is available through | [S12] rule → QUIRSO 's GitHub account Attacker-specific indicators |
| 989 | `is available to actors with` | 1 | Mention→Mention (1) | is available to actors with | [S17] same access vector → more targeted objectives |
| 990 | `is below` | 1 | Mention→Mention (1) | is below | [S10] team 's analysis of SharePoint RCE chain → SharePoint |
| 991 | `is buffer overflow vulnerability in` | 1 | CVE→Mention (1) | is buffer overflow vulnerability in | [S16] actor cloned public repository for CVE-2026-0300 → PAN-OS User-ID Authentication Portal |
| 992 | `is called during` | 1 | Mention→Mention (1) | is called during | [S08] GetTokenSignature → session token construction |
| 993 | `is change in` | 1 | Mention→Mention (1) | is change in | [S48] change in methodology → vulnerability itself |
| 994 | `is class For German organizations under` | 1 | Mention→Mention (1) | is class For German organizations under | [S44] hypervisor-layer compromise with confirmed unauthorized remote code execution → NIS2 |
| 995 | `is class of` | 1 | Mention→Mention (1) | is class of | [S44] hypervisor-layer compromise with confirmed unauthorized remote code execution → incident |
| 996 | `is cloud deployments into` | 1 | Mention→Mention (1) | is cloud deployments into | [S17] it → source code repositories |
| 997 | `is connected` | 1 | Mention→Mention (1) | is connected | [S17] SharePoint → environments |
| 998 | `is connected to Active Directory Federation Services` | 1 | Mention→Mention (1) | is connected to Active Directory Federation Services | [S17] SharePoint → environments |
| 999 | `is consequential in` | 1 | Mention→Mention (1) | is consequential in | [S17] JWT authentication bypass → environments |
| 1000 | `is considered as` | 1 | Mention→Mention (1) | is considered as | [S51] impact on users → impact to Subsequent System |
| 1001 | `is defined as` | 1 | Mention→Mention (1) | is defined as | [S19] Publicly Exposed → Yes |
| 1002 | `is defined as defined by subject matter expert process mentioned above equivalence class4 from` | 1 | Mention→Mention (1) | is defined as defined by subject matter expert process mentioned above equivalence class4 from | [S50] score of MacroVector → such qualitative perspective |
| 1003 | `is defined as set of` | 1 | Mention→Mention (1) | is defined as set of | [S50] system of interest for scoring vulnerability → computing logic |
| 1004 | `is defined by lookup table equivalence class4 from` | 1 | Mention→Mention (1) | is defined by lookup table equivalence class4 from | [S50] score of MacroVector → such qualitative perspective |
| 1005 | `is defined equivalence class4 from` | 1 | Mention→Mention (1) | is defined equivalence class4 from | [S50] score of MacroVector → such qualitative perspective |
| 1006 | `is deployed Default credential` | 1 | Mention→Mention (1) | is deployed Default credential | [S51] vulnerable product → environment |
| 1007 | `is deployed by` | 1 | Mention→Mention (1) | is deployed by | [S17] MLflow → data science teams |
| 1008 | `is deployed by data science teams independently of` | 1 | Mention→Mention (1) | is deployed by data science teams independently of | [S17] MLflow → central IT |
| 1009 | `is determined by` | 1 | Mention→Mention (1) | is determined by | [S50] proportion of distance → dividing severity distance of to-be-scored vector by depth of MacroVector |
| 1010 | `is equivalent to` | 1 | Mention→Mention (1) | is equivalent to | [S50] Not Defined → metric value of High list of possible values |
| 1011 | `is example of` | 1 | Mention→Mention (1) | is example of | [S51] ASLR → exploit-prevention tool |
| 1012 | `is executed with permission of Windows service` | 1 | Mention→Mention (1) | is executed with permission of Windows service | [S41] attacker 's arbitrary code → attacker-controlled OS command |
| 1013 | `is exposed to` | 1 | Mention→Mention (1) | is exposed to | [S54] vulnerable component → internet |
| 1014 | `is exposed to internet by` | 1 | Mention→Mention (1) | is exposed to internet by | [S54] vulnerable component → other operators |
| 1015 | `is first vulnerability in` | 1 | CVE→Mention (1) | is first vulnerability in | [S41] RCE vulnerability CVE-2026-63520 → chain |
| 1016 | `is form over behavior of` | 1 | Mention→Mention (1) | is form over behavior of | [S19] physical to achieve total control denial-of-service attack → vulnerable component |
| 1017 | `is important factor for` | 1 | Mention→Mention (1) | is important factor for | [S42] Remediation Level of vulnerability → prioritization Remediation Level |
| 1018 | `is in different security scope than` | 1 | Mention→Mention (1) | is in different security scope than | [S52] component → vulnerable component |
| 1019 | `is initiated outbound by` | 1 | Mention→Mention (1) | is initiated outbound by | [S44] connection → victim host |
| 1020 | `is iterating` | 1 | Mention→Mention (1) | is iterating | [S16] actor → actively |
| 1021 | `is kept up to` | 1 | Mention→Mention (1) | is kept up to | [S14] content of page → date |
| 1022 | `is known to exist with` | 1 | Mention→Mention (1) | is known to exist with | [S52] vulnerability → certainty |
| 1023 | `is larger than` | 1 | Mention→Mention (1) | is larger than | [S50] score change → uncertainty in ranking of vector groups |
| 1024 | `is larger than number of` | 1 | Mention→Mention (1) | is larger than number of | [S50] number of potential attackers for vulnerability → potential attackers |
| 1025 | `is limited to service provided by` | 1 | Mention→Mention (1) | is limited to service provided by | [S51] impact → affected server |
| 1026 | `is linked to` | 1 | Mention→Mention (1) | is linked to | [S16] disable account → campaign |
| 1027 | `is local.LocalLoginProvider out` | 1 | Mention→Mention (1) | is local.LocalLoginProvider out | [S08] TryResolveTokenCoreWithAccessProvider → token |
| 1028 | `is logic in` | 1 | Mention→Mention (1) | is logic in | [S08] token 's SigningToken → ValidateIssuer |
| 1029 | `is management plane for` | 1 | Mention→Mention (1) | is management plane for | [S44] Matters vCenter → hypervisor layer |
| 1030 | `is multiplied by proportion of` | 1 | Mention→Mention (1) | is multiplied by proportion of | [S50] maximal scoring difference → distance |
| 1031 | `is object obj out` | 1 | Organization→Mention (1) | is object obj out | [S09] Microsoft.SharePoint.Client.ServerRuntime.dll!Microsoft.SharePoint.Client.ClientMethodsProcessor.InvokeMethod → bool isVoid |
| 1032 | `is open framework for` | 1 | Mention→Mention (1) | is open framework for | [S52] Common Vulnerability Scoring System → communicating severity |
| 1033 | `is open framework for communicating characteristics of` | 1 | Mention→Mention (1) | is open framework for communicating characteristics of | [S52] Common Vulnerability Scoring System → software vulnerabilities CVSS |
| 1034 | `is other than` | 1 | Mention→Mention (1) | is other than | [S50] human user to participate in successful compromise of vulnerable system This metric determines whether vulnerability can be exploited solely at will of attacker → attacker |
| 1035 | `is outside scope of Complexity succeed include when` | 1 | Mention→Mention (1) | is outside scope of Complexity succeed include when | [S50] Refer to section for additional guidance → scoring Attack Complexity |
| 1036 | `is position in` | 1 | Mention→Mention (1) | is position in | [S17] it → organisation 's trust architecture |
| 1037 | `is potential entry point into` | 1 | Mention→Mention (1) | is potential entry point into | [S17] it → source code repositories |
| 1038 | `is reachable from` | 1 | Mention→Mention (1) | is reachable from | [S17] vCenter management interface → corporate LAN August 3 onwards |
| 1039 | `is reachable via` | 1 | Mention→Mention (1) | is reachable via | [S46] affected code path → UDP ports vulnerable system |
| 1040 | `is received` | 1 | Mention→Mention (1) | is received | [S51] malicious data → Network Vulnerabilities |
| 1041 | `is recommended for` | 1 | Mention→Mention (1) | is recommended for | [S50] Base metrics assessment → more meaningful results Generally |
| 1042 | `is reference to` | 1 | Mention→Mention (1) | is reference to | [S48] v1 in URL → API version |
| 1043 | `is released during processing of crafted IKE packets` | 1 | Mention→Mention (1) | is released during processing of crafted IKE packets | [S46] same region of memory → double free condition |
| 1044 | `is released more than once` | 1 | Mention→Mention (1) | is released more than once | [S46] same region of memory → double free condition |
| 1045 | `is reliable` | 1 | Mention→Mention (1) | is reliable | [S51] exploitation → due to exploit-prevention techniques enabled by default |
| 1046 | `is respected` | 1 | Mention→Mention (1) | is respected | [S50] ordering → Fixed |
| 1047 | `is responsibility of` | 1 | Mention→Mention (1) | is responsibility of | [S51] it → analyst |
| 1048 | `is responsible for` | 1 | Mention→Mention (1) | is responsible for | [S51] anyone → maintenance |
| 1049 | `is responsible for proper operation of` | 1 | Mention→Mention (1) | is responsible for proper operation of | [S51] anyone → system |
| 1050 | `is score of` | 1 | Mention→Mention (1) | is score of | [S50] score of vector → mean distance |
| 1051 | `is score of MacroVector i.e. score of` | 1 | Mention→Mention (1) | is score of MacroVector i.e. score of | [S50] score of vector → highest severity vector |
| 1052 | `is secure VPN within` | 1 | Mention→Mention (1) | is secure VPN within | [S50] MPLS → administrative network zone |
| 1053 | `is set of` | 1 | Mention→Mention (1) | is set of | [S45] this → additional capabilities |
| 1054 | `is shown in decompiled DotNetAssembly/DotNetAssemblySystemUtility` | 1 | Mention→Mention (1) | is shown in decompiled DotNetAssembly/DotNetAssemblySystemUtility | [S10] overload that we wanted Instance-first method selection → overload |
| 1055 | `is significant amount of` | 1 | Mention→Mention (1) | is significant amount of | [S40] engineering → work |
| 1056 | `is significant for` | 1 | Mention→Mention (1) | is significant for | [S46] impact → organisations operating VPN gateways |
| 1057 | `is significant of because` | 1 | CVE→Mention (1) | is significant of because | [S17] operational consequence of CVE-2026-20349 → what FTD appliances are Zero Trust Network Access deployments |
| 1058 | `is significant than` | 1 | CVE→Mention (1) | is significant than | [S17] operational consequence of CVE-2026-20349 → standard denial-of-service finding Zero Trust Network Access deployments |
| 1059 | `is staged for` | 1 | Mention→Mention (1) | is staged for | [S17] Babuk-derived ransomware payload → deployment |
| 1060 | `is supported by` | 1 | Mention→Mention (1) | is supported by | [S16] opportunistic → actor 's GitHub activity |
| 1061 | `is termed` | 1 | Mention→Mention (1) | is termed | [S50] Such vulnerability → greater severity |
| 1062 | `is trusted by` | 1 | Mention→Mention (1) | is trusted by | [S41] it → enterprises worldwide to store |
| 1063 | `is typical for` | 1 | Mention→Mention (1) | is typical for | [S52] it → only Base |
| 1064 | `is understood` | 1 | Mention→Mention (1) | is understood | [S46] underlying issue → well |
| 1065 | `is updated by originating CNA to provide` | 1 | Mention→Mention (1) | is updated by originating CNA to provide | [S38] CVE Record → information |
| 1066 | `is updated to provide` | 1 | Mention→Mention (1) | is updated to provide | [S38] CVE Record → information |
| 1067 | `is used in` | 1 | Mention→Mention (1) | is used in | [S52] which → formulas |
| 1068 | `is validated` | 1 | Mention→Mention (1) | is validated | [S52] vulnerability → more |
| 1069 | `is validated by other reputable sources` | 1 | Mention→Mention (1) | is validated by other reputable sources | [S52] vulnerability → more |
| 1070 | `is validated by vendor` | 1 | Mention→Mention (1) | is validated by vendor | [S52] vulnerability → more |
| 1071 | `is valuable to` | 1 | Mention→Mention (1) | is valuable to | [S51] it → law enforcement |
| 1072 | `is violated as result of` | 1 | Mention→Mention (1) | is violated as result of | [S51] system security policy → exploited vulnerability |
| 1073 | `is worse than` | 1 | Mention→Mention (1) | is worse than | [S54] workaround → fix |
| 1074 | `is x5t out` | 1 | Mention→Mention (1) | is x5t out | [S08] TryGetValue → object value |
| 1075 | `issue` | 1 | Mention→Mention (1) | issue | [S51] analyst → commands |
| 1076 | `issue commands as` | 1 | Mention→Mention (1) | issue commands as | [S51] analyst → root |
| 1077 | `it has added flaw` | 1 | Organization→Mention (1) | it has added flaw | [S45] CISA → flag |
| 1078 | `it has added flaw flag as` | 1 | Organization→Mention (1) | it has added flaw flag as | [S45] CISA → exploited |
| 1079 | `it runs` | 1 | Mention→Mention (1) | it runs | [S44] domain controller → just |
| 1080 | `know` | 1 | Mention→CVE (1) | know | [S10] we → similar structure to CVE-2026-63520 |
| 1081 | `know similar structure to CVE-2026-63520 from` | 1 | Mention→CVE (1) | know similar structure to CVE-2026-63520 from | [S10] we → implementing 2023 flaw as part of CVE-2023-29357 RCE chain |
| 1082 | `knows from` | 1 | Mention→Mention (1) | knows from | [S51] analyst → vulnerability description |
| 1083 | `lead to exploitation of` | 1 | Mention→Mention (1) | lead to exploitation of | [S51] protection mechanisms → vulnerability |
| 1084 | `lead to major loss of` | 1 | Mention→Mention (1) | lead to major loss of | [S39] should install security successful exploitation of vulnerability → confidentiality |
| 1085 | `led safety systems to` | 1 | Mention→Mention (1) | led safety systems to | [S16] continued attempts → flag |
| 1086 | `like to thank Abigail Palacios for` | 1 | Mention→Mention (1) | like to thank Abigail Palacios for | [S52] first → tireless work facilitating |
| 1087 | `like to thank Abigail Palacios from` | 1 | Mention→Mention (1) | like to thank Abigail Palacios from | [S52] first → Conrad Inc. facilitating |
| 1088 | `like to thank Grace Staley from` | 1 | Mention→Mention (1) | like to thank Grace Staley from | [S50] first → CAPS |
| 1089 | `like to thank Ian Barton of` | 1 | Mention→Mention (1) | like to thank Ian Barton of | [S43] Broadcom → CrowdStrike |
| 1090 | `like to thank Vivian Smith for` | 1 | Mention→Mention (1) | like to thank Vivian Smith for | [S52] first → tireless work facilitating |
| 1091 | `like to thank Vivian Smith from` | 1 | Mention→Mention (1) | like to thank Vivian Smith from | [S52] first → Conrad Inc. facilitating |
| 1092 | `live during` | 1 | Mention→Mention (1) | live during | [S44] campaign → IR engagement |
| 1093 | `maintained active during` | 1 | Mention→Mention (1) | maintained active during | [S16] threat actor → autonomous scan |
| 1094 | `maintains authoritative source of` | 1 | Organization→Mention (1) | maintains authoritative source of | [S58] CISA → vulnerabilities |
| 1095 | `make EPSS Exploitation activity data used in` | 1 | Mention→Mention (1) | make EPSS Exploitation activity data used in | [S47] data partners → EPSS |
| 1096 | `manages virtualisation for` | 1 | Mention→Mention (1) | manages virtualisation for | [S17] platform → tens of thousands of enterprise server |
| 1097 | `marked` | 1 | Mention→Mention (1) | marked | [S16] actor → exploit development directories |
| 1098 | `matches` | 1 | Mention→Mention (1) | matches | [S19] pace → rate |
| 1099 | `means` | 1 | Mention→Mention (1) | means | [S42] high attack complexity → time‑consuming |
| 1100 | `measure additional extrinsic attributes of` | 1 | Mention→Mention (1) | measure additional extrinsic attributes of | [S50] metrics → vulnerability |
| 1101 | `method achieved` | 1 | Mention→Mention (1) | method achieved | [S10] we → fully authenticated deserialization |
| 1102 | `modify` | 1 | Mention→Mention (1) | modify | [S38] ADP → data |
| 1103 | `narrow` | 1 | Mention→Mention (1) | narrow | [S19] use of AI → time |
| 1104 | `navigate through` | 1 | Mention→Product (1) | navigate through | [S53] Mission prevalence → CISA SSVC tree model |
| 1105 | `need` | 1 | Mention→Mention (1) | need | [S54] actor → configure specific code |
| 1106 | `need to evaluate effect of` | 1 | Mention→Mention (1) | need to evaluate effect of | [S53] Additional SSVC Decision Tree Models Organizations mission spaces → vulnerabilities |
| 1107 | `need to write` | 1 | Mention→Mention (1) | need to write | [S54] actor → themselves specific code |
| 1108 | `needed` | 1 | Mention→Mention (1) | needed | [S10] we → Class |
| 1109 | `needed Class` | 1 | Mention→Mention (1) | needed Class | [S10] we → useful gadget |
| 1110 | `needed return value` | 1 | Mention→Mention (1) | needed return value | [S10] Our method → associated External List |
| 1111 | `obtain SID of` | 1 | Mention→Mention (1) | obtain SID of | [S10] you → privileged SharePoint user |
| 1112 | `obtain user principal name of` | 1 | Mention→Mention (1) | obtain user principal name of | [S10] you → privileged SharePoint user |
| 1113 | `obtains privileged credentials` | 1 | Mention→Mention (1) | obtains privileged credentials | [S50] attacker → method |
| 1114 | `obtains privileged credentials prior to` | 1 | Mention→Mention (1) | obtains privileged credentials prior to | [S50] attacker → attack e.g. free trial accounts method |
| 1115 | `opens` | 1 | Mention→Mention (1) | opens | [S44] open-source tool → outbound SSH tunnel |
| 1116 | `opens outbound SSH tunnel from` | 1 | Mention→Mention (1) | opens outbound SSH tunnel from | [S44] open-source tool → compromised vCenter server |
| 1117 | `opens outbound SSH tunnel to` | 1 | Mention→Mention (1) | opens outbound SSH tunnel to | [S44] open-source tool → attacker-controlled infrastructure |
| 1118 | `overrides` | 1 | Mention→Mention (1) | overrides | [S50] analyst → Modified Privileges Required |
| 1119 | `pairing with CVE-2026-55040 authentication bypass achieved` | 1 | Mention→Mention (1) | pairing with CVE-2026-55040 authentication bypass achieved | [S10] we → fully authenticated deserialization |
| 1120 | `passes` | 1 | Mention→Mention (1) | passes | [S08] SharePoint 's own STS certificate via x5t → issuer validation |
| 1121 | `patched CVE-2026-65400 on` | 1 | Vendor→Mention (1) | patched CVE-2026-65400 on | [S17] Apple → August 6 |
| 1122 | `patched vCenter 's Syslog server on` | 1 | Mention→Mention (1) | patched vCenter 's Syslog server on | [S44] Broadcom → July 29 |
| 1123 | `peaked` | 1 | Mention→Mention (1) | peaked | [S12] campaign → the following day |
| 1124 | `perform In` | 1 | Mention→Mention (1) | perform In | [S54] organization → contrast to non-essential functions |
| 1125 | `perform arbitrary operations such as` | 1 | Mention→Mention (1) | perform arbitrary operations such as | [S41] NET gadget chain → executing attacker-controlled OS command |
| 1126 | `perform during` | 1 | Mention→Mention (1) | perform during | [S54] organization → disruption to normal operations |
| 1127 | `permits attacker to exhaust shared system resource such as` | 1 | Mention→Mention (1) | permits attacker to exhaust shared system resource such as | [S51] Subsequent System vulnerability → filling up file system |
| 1128 | `points` | 1 | Mention→Mention (1) | points | [S48] not EPSS version single stable URL → API version |
| 1129 | `points to the current day 's complete file` | 1 | Mention→Mention (1) | points to the current day 's complete file | [S48] not EPSS version single stable URL → API version |
| 1130 | `possess before exploiting vulnerability` | 1 | Mention→Mention (1) | possess before exploiting vulnerability | [S42] attacker → privileges |
| 1131 | `possess to exploiting vulnerability` | 1 | Mention→Mention (1) | possess to exploiting vulnerability | [S50] attacker → privileges |
| 1132 | `pour Mac bloque les menaces et protège votre système Mac et des fichiers personnels de hackers` | 1 | Mention→Mention (1) | pour Mac bloque les menaces et protège votre système Mac et des fichiers personnels de hackers | [S13] besoin de protection Malwarebytes Premium Security → Les Mac ont aussi |
| 1133 | `pour fonctionner de manière cohérente sur toutes les versions` | 1 | Mention→Mention (1) | pour fonctionner de manière cohérente sur toutes les versions | [S13] conçue par Apple → utilisez la fonctionnalité Mise à jour de logiciels |
| 1134 | `pour l' éteindre Vérifiez également la gestion à distance sur` | 1 | Mention→Mention (1) | pour l' éteindre Vérifiez également la gestion à distance sur | [S13] cliquez dessus → coloré |
| 1135 | `prefer` | 1 | Mention→Mention (1) | prefer | [S51] we → global consensus |
| 1136 | `prevents vulnerability from` | 1 | Mention→Mention (1) | prevents vulnerability from | [S54] that → being wormable |
| 1137 | `progress from` | 1 | Mention→Mention (1) | progress from | [S52] code available → proof-of-concept demonstration to exploit code |
| 1138 | `provide additional detection` | 1 | Mention→Mention (1) | provide additional detection | [S12] it → intrusion also |
| 1139 | `provide copy of policies If requested by` | 1 | Mention→Organization (1) | provide copy of policies If requested by | [S19] agencies → CISA |
| 1140 | `provide direct access into` | 1 | Mention→Mention (1) | provide direct access into | [S46] compromise at layer → internal infrastructure Operational disruption |
| 1141 | `provide investigation guidance` | 1 | Mention→Mention (1) | provide investigation guidance | [S12] it → intrusion also |
| 1142 | `provide procedures If requested by` | 1 | Mention→Organization (1) | provide procedures If requested by | [S19] agencies → CISA |
| 1143 | `provide public reporting of` | 1 | Mention→Mention (1) | provide public reporting of | [S54] Sources → active exploitation |
| 1144 | `provides exploitability assessment for vulnerability at` | 1 | Mention→Mention (1) | provides exploitability assessment for vulnerability at | [S39] following table → time of original publication security feature over network Exploitability |
| 1145 | `provides exploitability assessment for vulnerability security feature over` | 1 | Mention→Mention (1) | provides exploitability assessment for vulnerability security feature over | [S39] following table → network Exploitability |
| 1146 | `provides likelihood of` | 1 | Mention→Mention (1) | provides likelihood of | [S54] this metric → exploitation |
| 1147 | `provides through CISA 's Vulnrichment Program` | 1 | Organization→Mention (1) | provides through CISA 's Vulnrichment Program | [S19] CISA → elements |
| 1148 | `provides to CVE database` | 1 | Organization→Mention (1) | provides to CVE database | [S19] CISA → elements |
| 1149 | `publish updates at` | 1 | Mention→Mention (1) | publish updates at | [S19] it → pace |
| 1150 | `published PoC for` | 1 | Product→CVE (1) | published PoC for | [S10] Rapid7 's Stephen Fewer → CVE-2026-55040 |
| 1151 | `published PoC for CVE-2026-55040 on` | 1 | Product→Mention (1) | published PoC for CVE-2026-55040 on | [S10] Rapid7 's Stephen Fewer → August 11 Honeypot providers |
| 1152 | `published to` | 1 | Mention→Mention (1) | published to | [S47] Scores → community |
| 1153 | `publishes technical details for` | 1 | Organization→CVE (1) | publishes technical details for | [S40] Rapid7 → CVE-2026-55040 |
| 1154 | `ranges to identify` | 1 | Mention→Mention (1) | ranges to identify | [S16] affected version → exploitable targets |
| 1155 | `reach` | 1 | Mention→Mention (1) | reach | [S44] attackers → call out infrastructure reuse |
| 1156 | `read from` | 1 | Mention→Mention (1) | read from | [S10] last request → it |
| 1157 | `reduce specific elements from` | 1 | Mention→Mention (1) | reduce specific elements from | [S38] approach → updated CVE Record |
| 1158 | `refers to preventing access unauthorized ones for` | 1 | Mention→Mention (1) | refers to preventing access unauthorized ones for | [S50] impact to confidentiality of information managed by system due to successfully exploited vulnerability Confidentiality → vulnerable system |
| 1159 | `reflect characteristics of thing As` | 1 | Mention→Mention (1) | reflect characteristics of thing As | [S50] Exploitability metrics → previously mentioned |
| 1160 | `reflect properties of` | 1 | Mention→Mention (1) | reflect properties of | [S50] Exploitability metrics → vulnerability |
| 1161 | `refused` | 1 | Mention→Mention (1) | refused | [S16] provider-side safeguards → requests |
| 1162 | `relates to` | 1 | Mention→Mention (1) | relates to | [S51] vulnerability in library → incoming data |
| 1163 | `remain` | 1 | Mention→Mention (1) | remain | [S10] we → committed to surfacing critical intelligence on vulnerability exploitation high-fidelity insights to market |
| 1164 | `remediates` | 1 | Mention→Mention (1) | remediates | [S54] official patch → vulnerability Workaround |
| 1165 | `remove` | 1 | Organization→Mention (1) | remove | [S38] CISA ADP → assessed metrics for specific elements from updated CVE Record |
| 1166 | `renamed` | 1 | Mention→Mention (1) | renamed | [S51] Exploit Code Maturity → Exploit Maturity |
| 1167 | `renamed to` | 1 | Mention→Mention (1) | renamed to | [S51] Temporal Metric Group → Threat Metric Group Remediation Level |
| 1168 | `represents boundary between` | 1 | Mention→Mention (1) | represents boundary between | [S50] which equivalence set of vectors p in ordering of vectors → qualitative severity scores |
| 1169 | `represents boundary between qualitative severity scores to be` | 1 | Mention→Mention (1) | represents boundary between qualitative severity scores to be | [S50] which equivalence set of vectors p in ordering of vectors → backwards compatible with qualitative severity score boundaries from CVSS v3.x |
| 1170 | `represents calling application` | 1 | Mention→Mention (1) | represents calling application | [S08] actor token → actortoken claim |
| 1171 | `represents intrinsic characteristics of` | 1 | Mention→Mention (1) | represents intrinsic characteristics of | [S51] CVSS Base Score → vulnerability |
| 1172 | `require closer monitoring for` | 1 | Mention→Mention (1) | require closer monitoring for | [S53] specific characteristics → changes |
| 1173 | `requires future events` | 1 | Mention→Mention (1) | requires future events | [S54] Such approach → prior events |
| 1174 | `requires read-only permissions prior to being` | 1 | Mention→Mention (1) | requires read-only permissions prior to being | [S50] vulnerability → able to exploit vulnerability After successful exploitation |
| 1175 | `requires reliable historical evidence` | 1 | Mention→Mention (1) | requires reliable historical evidence | [S54] Such approach → prior events |
| 1176 | `resembles standard SSVC Coordinator tree For` | 1 | Product→Mention (1) | resembles standard SSVC Coordinator tree For | [S53] CISA SSVC decision tree model → organizations |
| 1177 | `resides If vulnerability discloses authentication credentials to system` | 1 | Mention→Mention (1) | resides If vulnerability discloses authentication credentials to system | [S54] vulnerability → affected component |
| 1178 | `resides If vulnerability discloses authorization credentials to system` | 1 | Mention→Mention (1) | resides If vulnerability discloses authorization credentials to system | [S54] vulnerability → affected component |
| 1179 | `resolved usable Instance type to use as` | 1 | Mention→Mention (1) | resolved usable Instance type to use as | [S10] Class → exploit |
| 1180 | `resolves arbitrary assembly-qualified type names from` | 1 | Mention→Mention (1) | resolves arbitrary assembly-qualified type names from | [S09] DbTypeReflector class → BDC model XML |
| 1181 | `resolves arbitrary assembly-qualified type names without` | 1 | Mention→Mention (1) | resolves arbitrary assembly-qualified type names without | [S09] DbTypeReflector class → safety enforcement |
| 1182 | `returned on subsequent attempts` | 1 | Mention→Mention (1) | returned on subsequent attempts | [S16] actor → attempts |
| 1183 | `returned with proxy anonymization` | 1 | Mention→Mention (1) | returned with proxy anonymization | [S16] actor → attempts |
| 1184 | `returns X509SecurityToken wrapping that certificate At is actor token 's signature` | 1 | Mention→Mention (1) | returns X509SecurityToken wrapping that certificate At is actor token 's signature | [S08] resolver → LocalLoginProvider access provider |
| 1185 | `reverse` | 1 | Mention→Mention (1) | reverse | [S41] we → engineering |
| 1186 | `reverse engineering to provide` | 1 | Mention→Mention (1) | reverse engineering to provide | [S41] we → additional context |
| 1187 | `reviewed` | 1 | Mention→Mention (1) | reviewed | [S16] we → evidence of batch exploitation against unknown number of hosts |
| 1188 | `run with` | 1 | Mention→Mention (1) | run with | [S51] library → normal privileges |
| 1189 | `runs macOS Screen` | 1 | Mention→Mention (1) | runs macOS Screen | [S17] daemon → Sharing |
| 1190 | `récentes Voici les étapes à suivre` | 1 | Mention→Mention (1) | récentes Voici les étapes à suivre | [S13] utilisez la fonctionnalité Mise à jour de logiciels → Installez la mise à jour La meilleure façon de protéger votre Mac consiste à installer la mise à jour Pour mettre à jour macOS sur n'importe quel Mac pris en charge |
| 1191 | `s introduire sur ce réseau Un attaquant pourrait visualiser et contrôler le Mac à distance` | 1 | Mention→Mention (1) | s introduire sur ce réseau Un attaquant pourrait visualiser et contrôler le Mac à distance | [S13] mais les attaquants devraient alors → accessibles uniquement depuis un réseau interne restent potentiellement exposés |
| 1192 | `said of` | 1 | Mention→Mention (1) | said of | [S51] authorized human person For CVSS → person authorized to access vulnerable system affected by vulnerability being scored Vendor |
| 1193 | `satisfy` | 1 | Mention→Mention (1) | satisfy | [S50] MacroVectors → EQ1 |
| 1194 | `scored vector` | 1 | Mention→Mention (1) | scored vector | [S50] severity distance of to-be → lower MacroVector |
| 1195 | `scored vector from highest severity vector in` | 1 | Mention→Mention (1) | scored vector from highest severity vector in | [S50] severity distance of to-be → same MacroVector lower MacroVector |
| 1196 | `see in Mittelstand environments` | 1 | Mention→Mention (1) | see in Mittelstand environments | [S44] we → pattern |
| 1197 | `send trivial crafted request to` | 1 | Mention→Mention (1) | send trivial crafted request to | [S51] local low-privileged user → operating system |
| 1198 | `sends JWT with` | 1 | Mention→Mention (1) | sends JWT with | [S08] attacker → alg |
| 1199 | `sends crafted HTTP/S input to` | 1 | Mention→Mention (1) | sends crafted HTTP/S input to | [S57] adversary → Internet-facing app |
| 1200 | `served` | 1 | Mention→Mention (1) | served | [S16] Autonomous Attack Cycle DeepSeek operating through Hermes Agent framework → OpenAI 's safety systems AI tool configurations DeepSeek/Hermes Agent |
| 1201 | `served as actor 's primary offensive AI tool` | 1 | Mention→Mention (1) | served as actor 's primary offensive AI tool | [S16] Autonomous Attack Cycle DeepSeek operating through Hermes Agent framework → OpenAI 's safety systems AI tool configurations DeepSeek/Hermes Agent |
| 1202 | `served as reasoning engine for` | 1 | Mention→Mention (1) | served as reasoning engine for | [S16] DeepSeek → code generation |
| 1203 | `serves as identity hub` | 1 | Mention→Mention (1) | serves as identity hub | [S17] SharePoint → environments |
| 1204 | `serves purpose from` | 1 | Mention→Mention (1) | serves purpose from | [S50] solution → consumer 's perspective |
| 1205 | `set` | 1 | Mention→Mention (1) | set | [S19] federal government networks → forth |
| 1206 | `set CreateNoWindow to` | 1 | Mention→Mention (1) | set CreateNoWindow to | [S09] we → true |
| 1207 | `set in` | 1 | Mention→Mention (1) | set in | [S19] federal government networks → Executive Order |
| 1208 | `sets Base Metric Privileges Required to` | 1 | Mention→Mention (1) | sets Base Metric Privileges Required to | [S50] provider → Low to High |
| 1209 | `sets actor token 's x5t header to thumbprint of` | 1 | Mention→Mention (1) | sets actor token 's x5t header to thumbprint of | [S08] attacker → SharePoint 's STS certificate |
| 1210 | `shift` | 1 | Mention→Mention (1) | shift | [S19] action → required timeline |
| 1211 | `shift required timeline for` | 1 | Mention→Mention (1) | shift required timeline for | [S19] action → further action |
| 1212 | `shift required timeline such as` | 1 | Mention→Mention (1) | shift required timeline such as | [S19] action → remediation |
| 1213 | `showed identifying as` | 1 | Mention→Mention (1) | showed identifying as | [S08] testing → local service |
| 1214 | `sit at boundary between external networks Always On` | 1 | Mention→Mention (1) | sit at boundary between external networks Always On | [S46] impact → VPN deployments systems |
| 1215 | `sit at boundary between internal networks Always On` | 1 | Mention→Mention (1) | sit at boundary between internal networks Always On | [S46] impact → VPN deployments systems |
| 1216 | `stack` | 1 | Mention→Mention (1) | stack | [S08] call → shows |
| 1217 | `started HTTP file server from` | 1 | Mention→Mention (1) | started HTTP file server from | [S16] the Operation Hermes Agent responding to Telegram command → actor 's home directory |
| 1218 | `suggests` | 1 | Mention→Mention (1) | suggests | [S12] strong correlation between time of disclosure and exploitation → disclosure as initial starting point for campaign Reverse |
| 1219 | `suggests level of technical knowledge available to would-be attackers` | 1 | Mention→Mention (1) | suggests level of technical knowledge available to would-be attackers | [S52] this metric → certainty also |
| 1220 | `supersedes risk of` | 1 | Mention→Mention (1) | supersedes risk of | [S19] directive → cyber incidents |
| 1221 | `supplement` | 1 | Mention→Mention (1) | supplement | [S52] Consumers of CVSS → Base Score |
| 1222 | `supports MEFs for` | 1 | Mention→Mention (1) | supports MEFs for | [S54] vulnerable component → more entities vulnerable component Support |
| 1223 | `systèmes` | 1 | Mention→Mention (1) | systèmes | [S13] les → les |
| 1224 | `take for` | 1 | Mention→Mention (1) | take for | [S50] it → attacker to succeed |
| 1225 | `take for attacker to succeed` | 1 | Mention→Mention (1) | take for attacker to succeed | [S50] it → e.g. race condition |
| 1226 | `targeted government entity in` | 1 | Mention→Mention (1) | targeted government entity in | [S16] actor → Malaysia |
| 1227 | `this metric refers` | 1 | Mention→Mention (1) | this metric refers | [S52] impact to availability of impacted component resulting from successfully exploited vulnerability → metric measures |
| 1228 | `this metric refers to loss of availability of impacted component itself such as networked service` | 1 | Mention→Mention (1) | this metric refers to loss of availability of impacted component itself such as networked service | [S52] impact to availability of impacted component resulting from successfully exploited vulnerability → metric measures |
| 1229 | `to bind` | 1 | Mention→Mention (1) | to bind | [S10] MethodInstance inside Deserialize method → them |
| 1230 | `to bind together` | 1 | Mention→Mention (1) | to bind together | [S10] MethodInstance inside Deserialize method → them |
| 1231 | `to compute` | 1 | Mention→Mention (1) | to compute | [S17] GPU → resources |
| 1232 | `told` | 1 | Mention→Mention (1) | told | [S10] this → us |
| 1233 | `update FAQ post for` | 1 | Mention→Mention (1) | update FAQ post for | [S11] emergency → additional information |
| 1234 | `use CVSS information` | 1 | Mention→Mention (1) | use CVSS information | [S52] consumers → organizational environment |
| 1235 | `use CVSS information as` | 1 | Mention→Mention (1) | use CVSS information as | [S52] consumers → input to organizational vulnerability management process organizational environment |
| 1236 | `use conceptual model of system of interest When establishing boundaries for` | 1 | Mention→Mention (1) | use conceptual model of system of interest When establishing boundaries for | [S50] assessment providers → Vulnerable System metric values |
| 1237 | `use string AAAA In` | 1 | Mention→Mention (1) | use string AAAA In | [S08] we → example |
| 1238 | `used Following compromise` | 1 | Mention→Mention (1) | used Following compromise | [S12] SSH → campaign Reverse |
| 1239 | `used Hermes Agent with DeepSeek for attack phase of` | 1 | Mention→Mention (1) | used Hermes Agent with DeepSeek for attack phase of | [S16] actor → campaign |
| 1240 | `used during execution of` | 1 | Mention→Mention (1) | used during execution of | [S51] asset → process |
| 1241 | `used for persistence` | 1 | Mention→Mention (1) | used for persistence | [S12] SSH → campaign Reverse |
| 1242 | `uses ADP container to provide` | 1 | Mention→Product (1) | uses ADP container to provide | [S38] CVE Program → additional CVE information for record Access for more information about CVE Program Container The CISA ADP |
| 1243 | `uses following decision points for` | 1 | Product→Mention (1) | uses following decision points for | [S54] vulnerability 's scope RELEVANT DECISION POINTS CISA → making vulnerability scoring decisions |
| 1244 | `uses nested JWT structure` | 1 | Mention→Mention (1) | uses nested JWT structure | [S08] tokens SharePoint 's S2S authentication → Bearer service-to-service |
| 1245 | `uses type reflectors to` | 1 | Mention→Mention (1) | uses type reflectors to | [S09] BDC subsystem → resolve |
| 1246 | `verify` | 1 | Mention→Mention (1) | verify | [S16] we → actual usage |
| 1247 | `views associated External List` | 1 | Mention→Mention (1) | views associated External List | [S10] someone → moment |
| 1248 | `voor` | 1 | Mention→Mention (1) | voor | [S14] Zie bijgevoegde referenties → meer informatie |
| 1249 | `wanted` | 1 | Mention→Mention (1) | wanted | [S10] we → Instance-first method selection |
| 1250 | `wanted static method that After failing with` | 1 | Mention→Mention (1) | wanted static method that After failing with | [S10] we → Process.Start |
| 1251 | `warrants` | 1 | Mention→Mention (1) | warrants | [S50] number of potential attackers for vulnerability → greater severity |
| 1252 | `was added to` | 1 | Mention→Mention (1) | was added to | [S10] flaw → VulnCheck KEV |
| 1253 | `was added to VulnCheck KEV before` | 1 | Mention→Product (1) | was added to VulnCheck KEV before | [S10] flaw → being added to CISA KEV on August 18 |
| 1254 | `was added to VulnCheck KEV on` | 1 | Mention→Mention (1) | was added to VulnCheck KEV on | [S10] flaw → August 12 |
| 1255 | `was created for` | 1 | Mention→Mention (1) | was created for | [S43] supplemental FAQ → clarification |
| 1256 | `was developed as entry for` | 1 | Mention→Mention (1) | was developed as entry for | [S40] exploit chain → recent Pwn2Own Berlin hacking competition |
| 1257 | `was discovered by Senior Principal Security Researcher at` | 1 | Mention→Organization (1) | was discovered by Senior Principal Security Researcher at | [S41] vulnerability → Rapid7 |
| 1258 | `was helpful when` | 1 | Mention→Mention (1) | was helpful when | [S09] that → conducting research |
| 1259 | `was identified In addition` | 1 | Mention→Mention (1) | was identified In addition | [S50] vulnerability → means |
| 1260 | `was made` | 1 | CVE→Mention (1) | was made | [S17] proof-of-concept exploit for CVE-2026-55040 → available |
| 1261 | `was prevented by` | 1 | Mention→Mention (1) | was prevented by | [S16] exploitation → target-side configuration requirements |
| 1262 | `was scheduled` | 1 | CVE→CVE (1) | was scheduled | [S09] remote code execution vulnerability affecting Microsoft SharePoint Today we are publishing technical analysis of CVE-2026-63520 analysis → CVE-2026-63520 |
| 1263 | `was shipped as part of` | 1 | Mention→Product (1) | was shipped as part of | [S17] fix → Microsoft 's July 2026 security updates |
| 1264 | `was undertaken through` | 1 | Mention→Mention (1) | was undertaken through | [S40] engineering → agent |
| 1265 | `was uploaded in` | 1 | Mention→Mention (1) | was uploaded in | [S10] model → previous request POST / |
| 1266 | `were listed in file deleted by` | 1 | Mention→Mention (1) | were listed in file deleted by | [S16] hosts → actor |
| 1267 | `were listed in file deleted by actor to` | 1 | Mention→Mention (1) | were listed in file deleted by actor to | [S16] hosts → prior analysis |
| 1268 | `write arbitrary code` | 1 | Mention→Mention (1) | write arbitrary code | [S42] unauthenticated attacker → execute |
| 1269 | `write arbitrary code In` | 1 | Mention→Mention (1) | write arbitrary code In | [S42] unauthenticated attacker → network-based attack |
| 1270 | `write arbitrary code to inject` | 1 | Mention→Mention (1) | write arbitrary code to inject | [S42] unauthenticated attacker → code remotely on SharePoint Server According to CVSS metric |
| 1271 | `write to even when running under` | 1 | Mention→Mention (1) | write to even when running under | [S51] they → operating system administrator privileges vulnerability |
| 1272 | `à une application hautement spécialisés` | 1 | Mention→Mention (1) | à une application hautement spécialisés | [S13] notamment pour le minage de Monero Les criminels ont probablement choisi le minage de Monero car il ne dépend pas de circuits intégrés spécifiques → car |

## Section 2 — Prédicats canoniques dérivés des assertions structurées (NVD/EPSS)

33 prédicats canoniques distincts, 259 edges au total.

| # | predicate_canonical | volume | domain→range (count) | derived_from | exemples (source_id, subject → object) |
|---|---|---|---|---|---|
| 1 | `has affected version bound` | 39 | Product→Version (39) | has affected version bound | [S02] Windows 10 Version 1607 → 10.0.14393.9060<br>[S02] Windows 10 Version 1809 → 10.0.17763.8644<br>[S02] Windows 10 Version 21H2 → 10.0.19044.7184 |
| 2 | `has affected product` | 29 | CVE→Product (29) | has affected product | [S02] CVE-2026-33824 → Windows 10 Version 1607<br>[S02] CVE-2026-33824 → Windows 10 Version 1809<br>[S02] CVE-2026-33824 → Windows 10 Version 21H2 |
| 3 | `has vendor` | 29 | Product→Vendor (29) | has vendor | [S02] Windows 10 Version 1607 → Microsoft<br>[S02] Windows 10 Version 1809 → Microsoft<br>[S02] Windows 10 Version 21H2 → Microsoft |
| 4 | `references` | 19 | CVE→URL (19) | references | [S02] CVE-2026-33824 → https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33824<br>[S02] CVE-2026-33824 → https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/<br>[S02] CVE-2026-33824 → https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-33824 |
| 5 | `has description` | 6 | CVE→Description (6) | has description | [S02] CVE-2026-33824 → Double free in Windows IKE Extension allows an unauthorized attacker to execute code over a network<br>[S02] CVE-2026-33824 → Doble liberación en la extensión IKE de Windows permite a un atacante no autorizado ejecutar código a través de una red<br>[S03] CVE-2026-55040 → Weak authentication in Microsoft Office SharePoint allows an unauthorized attacker to bypass a security feature over a network |
| 6 | `has EPSS percentile` | 5 | EPSS observation→Probability (5) | has EPSS percentile | [S21] EPSS observation for CVE-2026-33824 on 2026-08-28 → 0.994190000<br>[S22] EPSS observation for CVE-2026-55040 on 2026-08-28 → 0.985550000<br>[S23] EPSS observation for CVE-2026-59310 on 2026-08-28 → 0.987510000 |
| 7 | `has EPSS probability` | 5 | EPSS observation→Probability (5) | has EPSS probability | [S21] EPSS observation for CVE-2026-33824 on 2026-08-28 → 0.726950000<br>[S22] EPSS observation for CVE-2026-55040 on 2026-08-28 → 0.396520000<br>[S23] EPSS observation for CVE-2026-59310 on 2026-08-28 → 0.458780000 |
| 8 | `has SSVC automatable` | 5 | CVE→Observation (5) | has SSVC automatable | [S02] CVE-2026-33824 → yes<br>[S03] CVE-2026-55040 → yes<br>[S04] CVE-2026-59310 → yes |
| 9 | `has SSVC exploitation` | 5 | CVE→Observation (5) | has SSVC exploitation | [S02] CVE-2026-33824 → active<br>[S03] CVE-2026-55040 → active<br>[S04] CVE-2026-59310 → active |
| 10 | `has SSVC technicalImpact` | 5 | CVE→Observation (5) | has SSVC technicalImpact | [S02] CVE-2026-33824 → total<br>[S03] CVE-2026-55040 → total<br>[S04] CVE-2026-59310 → total |
| 11 | `has attackComplexity` | 5 | CVE→Metric (5) | has attackComplexity | [S02] CVE-2026-33824 → LOW<br>[S03] CVE-2026-55040 → LOW<br>[S04] CVE-2026-59310 → LOW |
| 12 | `has attackVector` | 5 | CVE→Metric (5) | has attackVector | [S02] CVE-2026-33824 → NETWORK<br>[S03] CVE-2026-55040 → NETWORK<br>[S04] CVE-2026-59310 → NETWORK |
| 13 | `has availabilityImpact` | 5 | CVE→Metric (5) | has availabilityImpact | [S02] CVE-2026-33824 → HIGH<br>[S03] CVE-2026-55040 → NONE<br>[S04] CVE-2026-59310 → HIGH |
| 14 | `has baseScore` | 5 | CVE→Metric (5) | has baseScore | [S02] CVE-2026-33824 → 9.8<br>[S03] CVE-2026-55040 → 9.1<br>[S04] CVE-2026-59310 → 9.8 |
| 15 | `has baseSeverity` | 5 | CVE→Metric (5) | has baseSeverity | [S02] CVE-2026-33824 → CRITICAL<br>[S03] CVE-2026-55040 → CRITICAL<br>[S04] CVE-2026-59310 → CRITICAL |
| 16 | `has confidentialityImpact` | 5 | CVE→Metric (5) | has confidentialityImpact | [S02] CVE-2026-33824 → HIGH<br>[S03] CVE-2026-55040 → HIGH<br>[S04] CVE-2026-59310 → HIGH |
| 17 | `has exploitabilityScore` | 5 | CVE→Metric (5) | has exploitabilityScore | [S02] CVE-2026-33824 → 3.9<br>[S03] CVE-2026-55040 → 3.9<br>[S04] CVE-2026-59310 → 3.9 |
| 18 | `has impactScore` | 5 | CVE→Metric (5) | has impactScore | [S02] CVE-2026-33824 → 5.9<br>[S03] CVE-2026-55040 → 5.2<br>[S04] CVE-2026-59310 → 5.9 |
| 19 | `has integrityImpact` | 5 | CVE→Metric (5) | has integrityImpact | [S02] CVE-2026-33824 → HIGH<br>[S03] CVE-2026-55040 → HIGH<br>[S04] CVE-2026-59310 → HIGH |
| 20 | `has last modified date` | 5 | CVE→Date (5) | has last modified date | [S02] CVE-2026-33824 → 2026-08-19T04:16:58.560<br>[S03] CVE-2026-55040 → 2026-08-19T04:17:23.540<br>[S04] CVE-2026-59310 → 2026-08-19T04:17:24.940 |
| 21 | `has observation date` | 5 | EPSS observation→Date (5) | has observation date | [S21] EPSS observation for CVE-2026-33824 on 2026-08-28 → 2026-08-28<br>[S22] EPSS observation for CVE-2026-55040 on 2026-08-28 → 2026-08-28<br>[S23] EPSS observation for CVE-2026-59310 on 2026-08-28 → 2026-08-28 |
| 22 | `has privilegesRequired` | 5 | CVE→Metric (5) | has privilegesRequired | [S02] CVE-2026-33824 → NONE<br>[S03] CVE-2026-55040 → NONE<br>[S04] CVE-2026-59310 → NONE |
| 23 | `has published date` | 5 | CVE→Date (5) | has published date | [S02] CVE-2026-33824 → 2026-04-14T18:17:34.767<br>[S03] CVE-2026-55040 → 2026-07-14T18:18:15.413<br>[S04] CVE-2026-59310 → 2026-07-30T13:16:53.993 |
| 24 | `has scope` | 5 | CVE→Metric (5) | has scope | [S02] CVE-2026-33824 → UNCHANGED<br>[S03] CVE-2026-55040 → UNCHANGED<br>[S04] CVE-2026-59310 → UNCHANGED |
| 25 | `has source identifier` | 5 | CVE→Value (5) | has source identifier | [S02] CVE-2026-33824 → secure@microsoft.com<br>[S03] CVE-2026-55040 → secure@microsoft.com<br>[S04] CVE-2026-59310 → security@vmware.com |
| 26 | `has userInteraction` | 5 | CVE→Metric (5) | has userInteraction | [S02] CVE-2026-33824 → NONE<br>[S03] CVE-2026-55040 → NONE<br>[S04] CVE-2026-59310 → NONE |
| 27 | `has vectorString` | 5 | CVE→Metric (5) | has vectorString | [S02] CVE-2026-33824 → CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H<br>[S03] CVE-2026-55040 → CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N<br>[S04] CVE-2026-59310 → CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H |
| 28 | `has vulnerability status` | 5 | CVE→Value (5) | has vulnerability status | [S02] CVE-2026-33824 → Analyzed<br>[S03] CVE-2026-55040 → Analyzed<br>[S04] CVE-2026-59310 → Analyzed |
| 29 | `has weakness` | 5 | CVE→CWE (5) | has weakness | [S02] CVE-2026-33824 → CWE-415<br>[S03] CVE-2026-55040 → CWE-1390<br>[S04] CVE-2026-59310 → CWE-22 |
| 30 | `observes` | 5 | EPSS observation→CVE (5) | observes | [S21] EPSS observation for CVE-2026-33824 on 2026-08-28 → CVE-2026-33824<br>[S22] EPSS observation for CVE-2026-55040 on 2026-08-28 → CVE-2026-55040<br>[S23] EPSS observation for CVE-2026-59310 on 2026-08-28 → CVE-2026-59310 |
| 31 | `has CISA action due date` | 4 | CVE→Date (4) | has CISA action due date | [S02] CVE-2026-33824 → 2026-08-21<br>[S03] CVE-2026-55040 → 2026-08-21<br>[S04] CVE-2026-59310 → 2026-08-21 |
| 32 | `has CISA exploit addition date` | 4 | CVE→Date (4) | has CISA exploit addition date | [S02] CVE-2026-33824 → 2026-08-18<br>[S03] CVE-2026-55040 → 2026-08-18<br>[S04] CVE-2026-59310 → 2026-08-18 |
| 33 | `has CISA required action` | 4 | CVE→Mitigation (4) | has CISA required action | [S02] CVE-2026-33824 → Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines<br>[S03] CVE-2026-55040 → Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines<br>[S04] CVE-2026-59310 → Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines |

## Section 3 — Signaux structurels observés (non corrigés, non décidés)

Cette section liste des observations factuelles issues de la lecture de `canonical_kg/edges.json`. 
Aucun regroupement, renommage ou fusion n'a été appliqué à partir de ces observations.

### 3.1 — Typage domain/range non résolu (`Mention`)

Sur les 1272 prédicats canoniques dérivés d'OpenIE :

| Catégorie | Nombre de prédicats | Part |
|---|---|---|
| Tous les edges du prédicat ont subject=`Mention` **et** object=`Mention` | 1122 | 88.2% |
| Tous les edges du prédicat ont subject et object typés (ni l'un ni l'autre `Mention`) | 14 | 1.1% |
| Mixte (au moins un edge typé, au moins un edge avec un côté `Mention`) | 136 | 10.7% |

Observation : les 14 prédicats "entièrement typés des deux côtés" ne sont pas les plus fiables pour autant — leur volume est de 1 ou 2 chacun, et plusieurs sont visiblement des mésanalyses MinIE (ex. `be patched by Microsoft in next update cycle for August 2026 Common Weakness Enumeration of` : CVE→CWE typé correctement par coïncidence, mais le prédicat lui-même est un fragment de phrase entière, pas une relation). Liste complète :

| predicate_canonical | volume | domain→range | exemple |
|---|---|---|---|
| `released security updates for` | 2 | Vendor→CVE | [S46] Microsoft → CVE-2026-33824 Applying updates Mitigation |
| `was scheduled` | 1 | CVE→CVE | [S09] remote code execution vulnerability affecting Microsoft SharePoint Today we are publishing technical analysis of CVE-2026-63520 analysis → CVE-2026-63520 |
| `published PoC for` | 1 | Product→CVE | [S10] Rapid7 's Stephen Fewer → CVE-2026-55040 |
| `has disclosure for` | 1 | CVE→CVE | [S10] CVE-2026-63520 Rapid7 → CVE-2026-63520 |
| `be Tracked as` | 1 | CVE→CVE | [S18] CVE-2026-55040 → CVE-2026-55040 |
| `identifies vulnerabilities as` | 1 | Organization→Product | [S19] CISA → carrying significant risk to federal enterprise within time frame set by CISA pursuant to Directive |
| `Process` | 1 | Organization→Organization | [S38] CISA ADP → CISA ADP |
| `be patched by` | 1 | CVE→CWE | [S40] authentication bypass vulnerability CVE-2026-55040 → Microsoft Common Weakness Enumeration of CWE-1390 are disclosing first vulnerability in chain |
| `be patched by Microsoft in next update cycle for August 2026 Common Weakness Enumeration of` | 1 | CVE→CWE | [S40] authentication bypass vulnerability CVE-2026-55040 → CWE-1390 |
| `be patched by Microsoft for August 2026 Common Weakness Enumeration of` | 1 | CVE→CWE | [S40] authentication bypass vulnerability CVE-2026-55040 → CWE-1390 |
| `be patched by Microsoft Common Weakness Enumeration of` | 1 | CVE→CWE | [S40] authentication bypass vulnerability CVE-2026-55040 → CWE-1390 |
| `has published full technical details for` | 1 | Organization→CVE | [S40] Technical analysis Rapid7 → CVE-2026-55040 here |
| `publishes technical details for` | 1 | Organization→CVE | [S40] Rapid7 → CVE-2026-55040 |
| `be block ongoing attacks When` | 1 | CVE→CVE | [S45] patching CVE-2026-33824 security flaw → asked for more information on attacks actively targeting CVE-2026-33824 vulnerability |

### 3.2 — Longue traîne de clusters à occurrence unique

866 des 1272 prédicats canoniques dérivés d'OpenIE (68.1%) n'ont qu'une seule assertion. Cela reflète directement la validation en masse des 1419/1423 clusters d'origine (tous acceptés en bloc, documenté au point 3 de l'audit précédent) : un cluster à 1 membre reste "accepté" sans qu'aucune fusion n'ait pu être envisagée faute de second membre à comparer. Ni un bug ni une preuve de mauvaise qualité en soi — juste un rappel que le clustering (seuil Jaccard 0.80) ne peut agir que sur des formulations qui se répètent ; une relation vraie mais rare restera dans un cluster à 1 membre autant qu'une mésanalyse rare.

### 3.3 — Paires de prédicats candidates à une relation inverse (même fait, sens contraire)

Cas identifiés par lecture directe, dans la même veine que le cas déjà documenté `affects`/`is affected by`. Les deux prédicats de chaque famille restent des clusters canoniques séparés — aucune fusion ni normalisation de voix (actif/passif) n'a été appliquée (cf. point 3 de l'audit précédent, décision explicitement renvoyée à toi).

**Famille "exploit"** — sens `X exploite Y` vs `Y est exploité (par/dans...)` :

| predicate_canonical | volume | domain→range dominant | exemple |
|---|---|---|---|
| `exploit` | 19 | Mention→Mention | [S07] attacker → vulnerability |
| `be exploited` | 12 | Mention→Mention | [S07] vulnerability → solely |
| `is being exploited in` | 2 | Mention→Mention | [S11] recently patched critical vulnerability in VMware vCenter Syslog Server → active campaign to deploy reverse SSH tool for persistence |
| `has been exploited in` | 2 | Mention→Mention | [S18] bug → wild |

Note de qualité : contrairement à `has affected product`/`has affected version bound` (structurés, propres), les 4 prédicats de cette famille proviennent tous d'OpenIE et leurs sujets/objets sont presque tous `Mention` non résolus (ex. `vulnerability`, `solely`, `wild`) — la relation sémantique "inverse" est plausible à la lecture mais ne s'appuie pas sur des entités canoniques propres des deux côtés.

**Famille "affected by"** — à comparer avec la famille structurée `has affected product`/`has affected version bound` :

| predicate_canonical | volume | origine | domain→range dominant | exemple |
|---|---|---|---|---|
| `are affected by` | 2 | openie | Mention→Mention | [S43] to execute code on host Non VMXNET3 virtual adapters → issue |
| `be affected by` | 1 | openie | Mention→Mention | [S51] vulnerable system → vulnerability being scored Vendor |
| `has affected product` | 29 | structured | CVE→Product | [S02] CVE-2026-33824 → Windows 10 Version 1607 |
| `has affected version bound` | 39 | structured | Product→Version | [S02] Windows 10 Version 1607 → 10.0.14393.9060 |

**Quasi-doublons non fusionnés (même sens, formulation différente)** :

| predicate_canonical | volume | exemple |
|---|---|---|
| `be chained to` | 2 | [S40] authentication bypass → additional vulnerabilities within authenticated attack surface of target site Rapid7 Labs |
| `be chained with` | 1 | [S51] other types of related vulnerabilities → vulnerabilities being assessed Specifically |

`be chained to` et `be chained with` n'ont pas été fusionnés par le clustering Jaccard (seuil 0.80) : normalisés en tokens, `{chain, to}` vs `{chain, with}` ont un indice de Jaccard de 1/3 ≈ 0.33, bien en dessous du seuil. C'est un exemple concret de faux-négatif de fusion mentionné en principe au point 3 de l'audit précédent, ici documenté avec ses deux clusters réels.

### 3.4 — Appendice : paires actif/passif détectées par heuristique lexicale (non vérifiées)

Détection automatique et non filtrée : pour chaque prédicat commençant par `be`/`is`/`are`/`was`/`were`, recherche d'un prédicat sans cet auxiliaire et de forme proche parmi les 1272 prédicats OpenIE. La plupart sont du bruit de verbe générique (MinIE), pas des relations métier — fournies ici à l'état brut, sans tri de pertinence, pour ne rien filtrer par anticipation de ce qui "semblerait pertinent".

| predicate A | volume A | predicate B | volume B |
|---|---|---|---|
| `be use in` | 1 | `use` | 13 |
| `be use as` | 1 | `use` | 13 |
| `be prevent` | 9 | `prevent` | 2 |
| `be implement` | 5 | `implement` | 3 |
| `be make` | 1 | `make` | 7 |
| `be identified by` | 4 | `identified` | 3 |
| `added` | 6 | `was added to` | 1 |
| `be read` | 2 | `read` | 5 |
| `Based on` | 4 | `be based on` | 3 |
| `be perform` | 4 | `perform` | 2 |
| `be install` | 2 | `install` | 3 |
| `be protect against` | 1 | `protect` | 4 |
| `be identified in` | 2 | `identified` | 3 |
| `be determine` | 3 | `determine` | 2 |
| `achieve` | 1 | `be achieve` | 3 |
| `be found` | 3 | `found` | 1 |
| `be integrated` | 2 | `integrated` | 2 |
| `be requiring` | 1 | `requiring` | 3 |
| `be patched by` | 1 | `patched` | 2 |
| `be found below` | 2 | `found` | 1 |
| `change` | 2 | `is change in` | 1 |
| `be create` | 1 | `create` | 2 |
| `be integrated with` | 1 | `integrated` | 2 |
| `assume` | 2 | `be assume` | 1 |
| `be stack below` | 1 | `stack` | 1 |
| `be found inside` | 1 | `found` | 1 |
| `be needed to` | 1 | `needed` | 1 |
| `Process` | 1 | `be process` | 1 |
| `be compute` | 1 | `compute` | 1 |
| `deployed` | 1 | `is deployed by` | 1 |
| `be set by` | 1 | `set` | 1 |
| `be set` | 1 | `set` | 1 |
| `is set of` | 1 | `set` | 1 |
| `be set How` | 1 | `set` | 1 |
| `be included in` | 1 | `included in` | 1 |
