# Impact de la qualité d'un graphe de connaissances sur la fiabilité d'une recommandation IA

**Note de proposition — challenge CIFRE, SpotworkAI × Université Paris Cité / LIPADE**

## 1. Domaine et problème

**Priorisation de correctifs de sécurité.** Cinq vulnérabilités inscrites au catalogue
CISA KEV en août 2026 : deux failles SharePoint chaînables (CVE-2026-55040 contournement
d'authentification, CVE-2026-63520 exécution de code), une faille IKE Windows, une
vCenter, une macOS. La question opérationnelle : *nous ne pouvons appliquer qu'un seul
correctif cette semaine — lequel, et pourquoi ?*

## 2. Justification du choix

Le domaine échoue comme exercice de synthèse, ce qui est l'intérêt. Décider mobilise une
**relation** (patcher 55040 casse la chaîne qui rend 63520 exploitable), une
**condition** (l'actif est-il exposé ?), une **échéance réglementaire** (CISA, 2026-08-21),
une **contradiction** (63520 : CVSS 8,1 mais EPSS 0,029) et une **absence** (aucun
contournement documenté pour vCenter, et il faut savoir le dire). Aucune de ces cinq
choses ne se lit dans un document isolé.

## 3. Cas d'usage spécifique et méthode généralisable

Distinction centrale : **le cas d'usage est la cybersécurité, la méthode est un protocole
d'objectivation.** À chaque étape où un jugement aurait pu s'introduire, un mécanisme le
remplace.

| Étape | Mécanisme |
|---|---|
| Choix des tâches | 32 candidates énumérées, 9 retenues par règle écrite, 23 écartées avec motif |
| Choix du fait retiré | calculé : l'ablation est l'ensemble complet des porteurs, jamais une sélection |
| Construction du contexte | prompt identique dans les 5 configurations, contexte produit par script |
| Exécution | un appel par cellule, aucun retry, agent isolé ignorant le protocole |
| Décision de référence | clé pré-enregistrée avant exécution, dérivée des seuls champs structurés |
| Grounding, citations | calculés par correspondance de chaînes contre le contexte exact |
| Classification d'une lacune | arbre de décision mécanique sur les artefacts du pipeline |

Rien n'y est propre aux CVE : seuls changent le type d'entité pivot et les champs
structurés de référence. Le pipeline, lui, ne présuppose aucun schéma de relations.

## 4. Sources sélectionnées

57 sources déclarées, 56 exploitables, se ramenant à **9 familles principales** — NVD,
FIRST EPSS, CISA KEV, CISA BOD 26-04, MSRC, Rapid7, VulnCheck, Apple, Broadcom — plus un
corpus de corroboration (spécifications CVSS et SSVC, MITRE ATT&CK, presse). Le §9
recommande 5 à 10 sources principales : l'écart apparent tient à l'unité de compte, le
NVD n'étant pas cinq sources parce qu'il a été interrogé pour cinq CVE. Règle tenue de
bout en bout : **aucune source inventée ni remplacée**.

## 5. Qualité des sources

Scoring par règle unique appliquée à toutes : autorité (officiel 5 → commercial 1),
niveau de preuve (primaire 2 / secondaire 1), accessibilité (API 5 → non tentée 0). Détail
en annexe `sources.md`. Deux dimensions du §14.1 sont **identifiées mais non
instrumentées** — fraîcheur et stabilité : le seul champ temporel est un horodatage de
collecte, les scorer fabriquerait une mesure.

**Deux lacunes de source documentées.** S27 (avis Broadcom, authentification requise,
délibérément non collectée) et S58 (page KEV répondant 200 sans données par-CVE). Le cas
S58 prive le graphe de l'échéance CISA de CVE-2026-63520 et pourrait fausser une tâche de
conformité — il n'en est rien : l'enregistrement NVD de cette CVE ne contient aucun champ
`cisa*` quand les quatre autres en contiennent quatre chacun. Deux sources indépendantes
concordent : c'est une **preuve d'absence**, pas une **absence de preuve**.

**Une contradiction inter-sources conservée telle quelle**, et ce qu'elle révèle. S10
(VulnCheck) date la publication du PoC de CVE-2026-55040 au **11 août**, S17 (DIESEC) au
**13 août**. Les deux dates ont été extraites ; une seule a survécu à la validation —
l'arête canonique porte « August 11 », les trois assertions de S17 sont restées dans
`open_kg`, leur cluster n'ayant pas été accepté. **La contradiction a donc été arbitrée par
le silence**, sans que personne la constate. C'est une limite de conception à énoncer :
la porte de validation humaine protège contre les fausses relations, pas contre l'arbitrage
involontaire d'un désaccord factuel, parce qu'elle statue sur des étiquettes de relation et
jamais sur la cohérence des valeurs.

## 6. Représentation de connaissance

Pipeline **non-LLM**, auditable : OpenIE (MinIE) sur le texte libre, mappage déterministe
des champs structurés (NVD, EPSS), puis résolution d'entités, graphe ouvert, clustering
des relations découvertes, **validation humaine**, et seulement ensuite nommage canonique.

56 sources → 4 401 arêtes ouvertes → **2 123 arêtes canoniques** sur 1 867 nœuds. Chaque
assertion conserve son `source_id` et le texte exact qui la justifie.

Le brief suggère 15 à 30 nœuds ; le graphe complet est deux ordres de grandeur au-dessus —
correct pour l'audit, illisible sur une planche. Une **vue de présentation** en est
projetée par règle (les prédicats à valeur littérale deviennent des attributs du nœud,
ceux entre entités restent des arêtes) : **27 nœuds, 21 arêtes**, provenance conservée.
Ce n'est pas un second graphe, c'est une projection vérifiable du premier.

## 7. Lacunes identifiées

La typologie du §7 est rendue **mécaniquement décidable**. Pour un fait donné : est-il
dans le corpus ? sinon → **lacune de source**. Sinon, dans les assertions extraites ?
sinon → **lacune d'extraction**. Sinon, dans le graphe sous une étiquette exploitable ?
sinon → **lacune de relation**.

Exemples tracés : *source* — S27 inaccessible. *Extraction* — S17 énonce « Broadcom
released patches for CVE-2026-59310 » et le sous-graphe vCenter n'en contient aucune
trace. *Relation* — le chaînage SharePoint existe sous trois étiquettes distinctes et neuf
porteurs partiels, donc jamais sous une forme unique interrogeable.

## 8. Relations critiques

Une relation est critique non parce qu'elle paraît importante, mais parce que **son
retrait change une décision** — ce qui suppose de savoir combien d'arêtes portent le même
fait. D'où la notion de **porteur** : arête dont le texte-preuve mentionne toutes les
entités du fait (porteur explicite), ou une partie et le vocabulaire des porteurs
explicites (porteur partiel, seuil déclaré, sensibilité testée). Profil mesuré : de
**1 porteur** (statut d'exploitation macOS) à **12** (chaînage SharePoint).

## 9. Expérimentation

**9 tâches × 5 configurations = 45 cellules.** Configurations §13 : (1) LLM seul,
(4) KG complet, (5) KG incomplet, (7) KG avant validation humaine, (8) KG incomplet avec
signalement d'incertitude. Un appel par cellule, aucun retry, agent isolé ignorant le
protocole ; prompt identique dans les cinq configurations, **seul le contexte varie**.
Les tâches couvrent les quatre exigences du §13 et ne sont pas toutes factuelles :
arbitrage, classement, conformité, constat d'absence, refus de conclure.

## 10. Métriques et baselines

**Baseline** : configuration 1, le LLM sans contexte. Le §21 fait du « LLM-as-a-Judge sans
contrôle » un critère éliminatoire : **aucun modèle ne note aucune réponse ici.** Deux
dimensions sont calculées par correspondance de chaînes contre le contexte exact —
**grounding** (part des jetons littéralement vérifiables retrouvés) et **citations
correctes**. Quatre autres sont des **indicateurs binaires observables** (décision
explicite, incertitude nommée, information demandée, confiance énoncée), comptés et non
notés. Seule l'**exactitude** demande un humain : c'est une comparaison à une clé
**pré-enregistrée** avant exécution, dérivée par règle fixe des seuls champs structurés.

## 11. Résultats

| Configuration | Exactitude | Incertitude nommée |
|---|---:|---:|
| 1 — LLM seul | 3/9 | 6/9 |
| 4 — KG complet | **9/9** | 3/9 |
| 5 — KG incomplet | 7/9 | 5/9 |
| 7 — KG avant validation | 8/9 | 4/9 |
| 8 — KG incomplet + signalement | 7/9 | **8/9** |

**Le graphe ne rend pas le modèle moins faux, il le rend vérifiable.** Sans contexte : 16
jetons vérifiables sur 9 tâches ; avec le graphe : 556 — facteur 35. La configuration 1 ne
se trompe pas beaucoup, elle n'avance presque rien de contrôlable ; sur l'arbitrage
SharePoint elle choisit la mauvaise CVE au motif que le numéro le plus élevé serait le
plus récent.

**Le retrait d'une relation ne change une décision que si elle est le seul porteur du
fait.** Sur 9 tâches, 2 changent : les observations EPSS (classement) et les références de
correctif. Le chaînage SharePoint, lui, ne bouge pas — même en retirant l'intégralité de
ses porteurs explicites, parce que neuf porteurs partiels subsistent, dont
`Patching CVE-2026-55040 break exploit chain` que la réponse cite mot pour mot. Ce
résultat vient d'un échec : la première ablation retirait deux arêtes sur trois en croyant
retirer une relation. **On ne peut pas évaluer l'impact d'une relation manquante sans
d'abord mesurer combien de fois elle est présente.**

**Le signalement d'incertitude fonctionne.** À information égale (config 5 vs 8) et à
exactitude égale (7/9), l'incertitude nommée passe de 5 à 8 réponses sur 9.

*Réserves* : la métrique de grounding compte des nombres employés rhétoriquement ; et la
baseline « LLM seul » n'est pas un isolement parfait — sur une tâche le modèle a cité des
identifiants de source qu'il ne pouvait tenir que de son environnement. Elle est donc
légèrement flatteuse.

**Deux observations issues de l'outil de démonstration interactif, à ne pas confondre avec
le protocole.** Elles proviennent d'une exécution de l'explorateur (`demo_server/`,
modèles gratuits via OpenRouter) sur une question *hors des 9 tâches* ; elles illustrent le
mécanisme et ne sont pas comparables en exactitude aux 45 cellules.

- **Le mécanisme généralise au-delà du jeu de tâches figé.** Sur cette question inédite, la
  configuration sans contexte produit **0 jeton vérifiable**, la configuration RAG
  sémantique **6/6** — la récupération fonctionne réellement, elle n'est pas décorative.
- **Un effet de cadrage, découvert et non prévu.** Les configurations 5 et 8 reçoivent un
  contexte identique à une seule phrase près (le signalement d'incomplétude) et aboutissent
  à des décisions **opposées** : « urgent » contre « peut attendre ». Le modèle lit donc
  bien le contexte plutôt que de réciter, mais cela signifie aussi que **la formulation du
  signalement est une variable qui influence la décision et que nous n'avons jamais
  mesurée comme telle**. À énoncer au même titre que la précision de 0,026 : avant qu'un
  jury ne le trouve.

## 12. Persistance et amélioration continue

Une connaissance entre dans le graphe canonique parce qu'un humain l'a acceptée, non parce
qu'elle a été extraite. Cycle de vie : `new` → `pending` → `confirmed` →
`needs_reconfirmation`. Chaque décision est **ancrée à la composition exacte** du groupe
de formulations sur laquelle elle portait ; si une évolution du pipeline la modifie, la
décision **repasse en attente** — jamais conservée ni supprimée silencieusement :
l'ancienne est préservée, un différentiel explicite est écrit, et seule une reconfirmation
humaine la referme. Re-saisir la même décision ne suffit pas, le format ne distinguerait
pas « toujours valide » de « re-sauvegardé sans voir le différentiel ».

Conséquence : **une arête n'existe que tant qu'une décision humaine reste ancrée à ce sur
quoi elle portait.** C'est ce qui sépare connaissance *extraite* et connaissance
*persistée*. État : 944 acceptés, 11 rejetés, 2 scindés, **1 154 en attente** sur 2 111.
Réserve : ce mécanisme est implémenté mais **jamais déclenché à ce jour**.

## 13. Composant produit

**Un détecteur de redondance relationnelle** : pour un fait donné, combien d'arêtes le
portent, sous quelles étiquettes, et que resterait-il en retirant la principale ? Deux
usages constatés : **avant génération**, un fait à porteur unique est un point de
fragilité ; **avant expérimentation**, toute évaluation par ablation sur un graphe
d'extraction ouverte est ininterprétable sans ce décompte. Ce n'est pas une esquisse : le
composant a été construit, appliqué aux 9 tâches, et c'est lui qui a corrigé une
conclusion erronée que nous allions tirer.

## 14. Généralisation

Transfert par construction : aucun schéma présupposé, le décompte de porteurs ne dépend
que d'un couple d'entités et d'un texte-preuve, l'arbre de classification n'interroge que
les artefacts du pipeline. Santé — une recommandation dépend d'une contre-indication ;
droit — une obligation dépend d'une exception ; finance — un ratio d'une méthode datée ;
éducation — un parcours d'un prérequis. Même question opératoire : *cette relation
critique est-elle représentée, et combien de fois ?*

**Limite, et ce qui la lève.** Cette généralisation est **argumentée, pas démontrée** :
aucun second domaine n'a été traité. Et un obstacle précis reste à franchir avant qu'elle
le soit — le décompte de porteurs s'appuie aujourd'hui sur le *texte-preuve*, pas sur la
structure du graphe, faute de résolution d'entités fiable. C'est ce qui rend la §15
nécessaire plutôt que décorative : les 0–6 mois lèvent l'obstacle en dégageant une
définition du porteur indépendante du corpus, et les 6–12 mois transforment l'argument en
résultat sur un second domaine. Le présent point dit *pourquoi la méthode devrait
transférer* ; la roadmap dit *quand et comment on le vérifiera*.

## 15. Roadmap CIFRE

La trajectoire remonte les cinq niveaux du projet : cas d'usage → décision métier →
problème expérimental → question scientifique → question de thèse. Le décompte de porteurs
et la typologie des trois lacunes ne sont pas le point d'arrivée : ils sont l'amorce
empirique d'une **méthode d'évaluation de la complétude d'un graphe**, qui est la question
de thèse.

**0–6 mois — de l'artefact au concept.** Généraliser le décompte de porteurs en une
**métrique de complétude indépendante du domaine** : formaliser « porteur » sans recourir
au texte-preuve d'un corpus cyber, et caractériser ce qu'elle mesure face aux mesures
existantes de complétude de KG. Élargir l'ancrage bibliographique au-delà de RAG/GraphRAG
déjà couverts — littérature sur la complétude et la qualité des graphes, la calibration et
la quantification d'incertitude. Formaliser le protocole d'ablation consciente de la
redondance comme **méthode reproductible**, avec sa procédure de pré-enregistrement, plutôt
que comme un montage propre à ce cas. Exploiter le score d'autorité désormais porté par
chaque arête : pondérer la sélection de contexte par fiabilité de source et mesurer si cela
déplace une décision — sur un protocole ré-enregistré, jamais en repondérant après coup les
45 cellules déjà exécutées.

**6–12 mois — répondre à la généralisation au lieu de l'argumenter.** Premier test sur un
second domaine, idéalement **un cas ou des données fournis par SpotWorkAI** plutôt qu'un
second cas cyber choisi par nous : c'est la seule façon de transformer le §14 d'argument en
résultat. Benchmark comparant RAG documentaire, GraphRAG et KG-aware sous le même protocole
d'ablation. Première publication méthodologique sur la métrique de complétude et sur le
résultat négatif qui la motive — l'ablation naïve ne mesure pas ce qu'elle prétend mesurer.

**12–24 mois — du rétrospectif au prédictif.** Aujourd'hui la fragilité d'un fait se
constate *après* ablation ; l'objectif est de l'**identifier avant génération**, comme
signal d'alerte sur une réponse en train de se construire. Confrontation aux stratégies
d'enrichissement de l'état de l'art (GraphRAG, complétion de graphe façon OMNIA, apport de
sources externes) : enrichir un graphe et mesurer sa complétude sont deux faces du même
problème. Intégrer une évaluation **LLM-as-a-Judge** de la fiabilité des recommandations —
non comme juge unique, ce que le §21 exclut, mais confrontée aux mesures calculées de ce
travail, la question de recherche étant précisément *quand* un juge modèle est fiable.

**24–36 mois — retour au terrain industriel.** Validation à l'échelle sur des cas réels et
des bases de connaissances SpotWorkAI ; transfert du détecteur de redondance en composant
intégrable à leur plateforme, en amont de la génération ; comparaison finale à l'état de
l'art ; rédaction et publications.

## 16. Limites et risques

1. **Résolution d'entités quasi inopérante** — 3 699 mentions pour 3 697 entités, soit 2
   fusions. Limite la plus sérieuse : elle explique la traîne de 946 relations canoniques
   dont 535 uniques, et pourquoi `Patching CVE-2026-55040` est une entité distincte de
   `CVE-2026-55040`.
2. **1 154 groupes de relations sur 2 111 jamais revus.**
3. **Jeu d'évaluation brouillon** : sa précision de 0,026 n'est pas un échec mais un
   artefact (8 triplets annotés contre 304 prédits). Seul le rappel y est interprétable —
   c'est la métrique qui donnerait un faux sentiment de fiabilité si on la citait telle
   quelle.
4. **La crédibilité des sources atteint le graphe, mais rien ne s'en sert encore.**
   Rang, catégorie et score d'autorité (règle unique de `build_source_quality.py`) sont
   désormais copiés de `corpus/raw/` vers `corpus/clean/` puis **joints sur `source_id`**
   sur les 2 123 arêtes canoniques — et par héritage sur `demo_kg/`. On peut donc trier
   et filtrer les arêtes par fiabilité. Ce qui reste ouvert : ce poids n'entre **ni dans
   le protocole des 45 cellules** (enregistré avant cette propagation, non repondéré a
   posteriori) **ni dans la sélection de contexte**, qui traite encore toutes les arêtes
   à poids égal. Un billet commercial et le NVD pèsent toujours autant *dans la réponse*,
   même si l'écart est maintenant visible *dans la donnée*. Repondération et mesure de
   son effet : feuille de route, pas résultat.
5. **87 identifiants de nœuds dupliqués** (identifiant insensible à la casse, libellé
   non) : sans effet sur les arêtes, mais le libellé affiché dépend de l'ordre de lecture.
6. **Actif et passif non fusionnés** au clustering.
7. **Mécanisme de re-validation jamais déclenché** en conditions réelles.
8. **Aucune couche actif/exposition dans le graphe.** Le KG n'a ni type d'entité `Asset` ni
   prédicat d'exposition : la condition d'exposition est **une phrase de contexte**
   préfixée `[Scénario expérimental, non issu du corpus]`, injectée dans 2 des 45
   contextes. Le marquage est donc dans la donnée transmise au modèle, pas seulement dans
   cette note — mais il ne faut pas parler de « deux couches du graphe », il n'y en a
   qu'une.
9. **Graphe non ré-extractible sur la machine de rédaction** (ni Java ni MinIE) : il est
   gelé, ce qui garantit la cohérence des 45 cellules mais interdit une reproduction
   complète de bout en bout.

**Risque principal pour la thèse** : que la redondance relationnelle soit propre aux
extractions ouvertes et non aux graphes construits sur schéma. C'est ce que la comparaison
multi-domaines des 6–12 mois doit trancher.

---

## AI Usage & Verification Log

Assistance IA (Claude Code) pour : pipeline d'extraction, harnais expérimental, scripts de
mesure, exécution des 45 cellules par agents isolés, rédaction. Chaque chiffre de cette
note est régénérable depuis les données du dépôt.

**Corrections apportées à des sorties d'IA, après vérification humaine :**

- **Deux sources déclarées à tort inexistantes**, retrouvées manuellement (DIESEC). Une
  troisième (DTIC) redirigeait bien vers une page de maintenance : **retirée plutôt que
  fabriquée**. S27, inaccessible sans authentification, est enregistrée comme telle.
- **~940 clusters validés en bloc** lors d'une première passe : les deux plus grosses
  « relations » du graphe étaient les copules vides `is` et `has`. Passe reprise, filtre ajouté.
- **Deux bugs détruisant silencieusement du travail de validation** : décision de scission
  perdue à chaque ré-export, cache de graphe non recalculé. Trouvés parce que les compteurs
  avant/après divergeaient.
- **L'ablation initiale ne mesurait rien** — deux arêtes retirées sur trois. Conclusion
  **retirée, pas réécrite** ; c'est ce qui a produit le décompte de porteurs.
- **Deux artefacts de mesure corrigés** avant interprétation (date fournie dans la question
  comptée comme non ancrée ; identifiant en minuscules dans une URL).

**Écarts de l'outil de démonstration, déclarés plutôt que lissés.** MinIE étant
indisponible, le graphe de démo est une **projection** du graphe canonique, pas une
ré-extraction : un rejeu heuristique remplaçait `break` par `exploit` — cluster déjà
rejeté — et aurait fabriqué un faux signal « lacune » là où il n'y a qu'un changement
d'extracteur. L'outil appelle l'API OpenRouter alors que les 45 cellules venaient de
sous-agents isolés : **transport différent**, et une chaîne de modèles gratuits **jamais
comparés entre eux** — ses réponses illustrent le mécanisme, elles ne sont pas comparables
en exactitude à `resultats.md`. Son **template de prompt diverge aussi** : il exige une
décision, une justification et la citation des éléments utilisés, là où les 45 cellules
demandaient seulement décision + justification. Le template reste identique entre les cinq
configurations — la contrainte méthodologique est préservée — mais il n'est pas celui du
protocole enregistré, et `experiments/` comme `resultats.md` sont inchangés. Quatre défauts trouvés en le
construisant : fuite de raisonnement malgré l'instruction d'exclusion, troncature par budget
de jetons, réponses non conclusives, erreur de syntaxe JS.
