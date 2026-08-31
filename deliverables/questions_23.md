# Réponses préparées — questions §23

*Réponses courtes, appuyées sur une preuve du dépôt. À dire, pas à lire.*

---

**1. Un KG complet garantit-il une réponse correcte ?**

Non, et nous l'avons mesuré dans les deux sens. Avec le KG complet, l'exactitude passe de
3/9 à 9/9 — donc le graphe compte. Mais retirer une relation ne dégrade la réponse que
dans 2 cas sur 9 : quand cette relation est le seul porteur du fait. Un graphe peut donc
être « complet » sur le papier et fragile sur un fait précis, ou incomplet et robuste par
redondance. La complétude est une propriété du graphe ; la fiabilité est une propriété du
couple graphe-question.

---

**2. Comment évitez-vous d'ajouter de fausses relations dans le graphe ?**

Rien ne devient canonique sans décision humaine explicite. Aujourd'hui : 944 groupes
acceptés, 11 rejetés, 2 scindés, 1 154 encore en attente — et cette portion en attente est
*exclue* du graphe, pas incluse par défaut. Le mécanisme de scission est reject-par-défaut :
une formulation non assignée ne passe pas. Et une décision est ancrée à la composition
exacte sur laquelle elle a été prise : si elle change, la décision repasse en attente.

---

**3. À partir de quel moment une connaissance peut-elle être persistée ?**

Quand un humain l'a acceptée **et** que ce sur quoi il s'est prononcé n'a pas changé
depuis. C'est le point qui nous a coûté le plus de travail. Une décision porte sur un
groupe de formulations ; si le pipeline évolue et modifie ce groupe, la décision n'est ni
conservée ni jetée : elle est remise en attente, l'ancienne est préservée, un différentiel
est écrit, et il faut une reconfirmation explicite. Re-saisir la même décision ne suffit
pas — le format ne permettrait pas de distinguer « toujours valide » de « re-sauvegardé
sans regarder ».

---

**4. Quelle métrique pourrait donner un faux sentiment de fiabilité ?**

La nôtre : la précision de notre jeu d'évaluation est de 0,026. Lue telle quelle, elle
suggère un pipeline catastrophique. C'est un artefact : 8 triplets annotés confrontés à
304 prédits. Seul le rappel y est interprétable. Nous la citons parce que c'est exactement
le piège — un chiffre calculé correctement sur un protocole mal dimensionné. Plus
généralement, un taux de grounding élevé rassure à tort : nos configurations KG-aware sont
à 551/556, mais cela mesure la traçabilité, pas la vérité.

---

**5. Quelle suggestion de l'IA avez-vous rejetée ?**

Plusieurs, mais la plus importante : une première passe avait validé en bloc ~940 groupes
de relations. Résultat, les deux plus grosses « relations » du graphe étaient des copules
vides — `is` et `has`. Nous avons repris la passe et ajouté un filtre. Rejeté aussi : la
conclusion que le chaînage SharePoint n'avait pas d'importance parce que son retrait ne
changeait rien. Elle était fausse, et c'est le décompte de porteurs qui l'a montré.

---

**6. Quelle relation est la plus critique dans votre graphe ?**

Ce n'est pas la question que nous nous posons — « critique » n'est pas une propriété de la
relation seule. Nous mesurons combien d'arêtes portent un fait. Les faits à porteur unique
sont les points de fragilité : le statut d'exploitation macOS, les références de correctif.
Le chaînage SharePoint, qui *paraît* le plus critique, a 12 porteurs : le retirer ne change
rien.

---

**7. Comment distinguez-vous une réponse fausse due au LLM d'une réponse fausse due à la connaissance disponible ?**

Par construction du protocole. La configuration 1 (aucun contexte) isole le comportement
propre du modèle : elle choisit la mauvaise CVE en raisonnant que le numéro le plus élevé
est le plus récent — erreur de raisonnement pur. Les configurations KG-aware partagent le
même prompt : tout écart entre elles vient du contexte, pas du modèle. Et l'arbre de
classification tranche ensuite : le fait était-il dans le corpus, dans les extractions,
dans le graphe ?

---

**8. Comment distinguez-vous un problème de retrieval d'un problème de graphe ?**

Il n'y a pas de retrieval ici — le sous-graphe est construit par filtre déterministe, pas
par recherche sémantique. C'est un choix : cela supprime une variable. Tout écart observé
est donc imputable au graphe ou au modèle, jamais à un classement de pertinence. Le prix à
payer est que la méthode ne dit rien du retrieval ; c'est une extension, pas une omission.

---

**9. Comment détecteriez-vous une relation implicitement présente mais non extraite ?**

C'est exactement ce que fait le décompte de porteurs, en sens inverse. Un fait exprimé dans
un texte-preuve mais absent du graphe sous une étiquette exploitable apparaît comme un
porteur partiel sans porteur explicite. Cas réel : le correctif vCenter est énoncé dans S17
et n'existe sous aucune arête. C'est une lacune d'extraction, détectée mécaniquement.

---

**10. Quelle baseline pourrait battre votre approche ?**

Un RAG documentaire simple, sur nos tâches factuelles. Les références KB, les scores CVSS,
les dates d'échéance sont dans le texte source : un bon retrieval les retrouverait sans
graphe. Le graphe reprend l'avantage là où la réponse dépend d'une relation entre entités
distantes ou d'un constat d'absence — dire « aucun contournement n'est documenté » suppose
d'avoir cherché exhaustivement, ce qu'un top-k ne garantit pas. Nous n'avons pas exécuté
cette baseline : c'est une limite du travail, et le premier comparatif de la roadmap.

---

**11. Pourquoi la cybersécurité et pas la santé, le droit ou la finance ?**

Parce que décider y mobilise cinq mécanismes relationnels simultanés qu'aucun document
isolé ne porte : une relation (le chaînage 55040 → 63520), une condition (l'exposition de
l'actif), une échéance datée (CISA, 2026-08-21), une contradiction entre signaux
concurrents (CVE-2026-63520 : CVSS 8,1 mais EPSS 0,029) et une absence (aucun contournement
vCenter documenté). Le domaine offre aussi une fraîcheur extrême et des sources qui se
contredisent en quelques jours. Ce n'est pas le sujet, c'est le terrain : la méthode ne
présuppose aucun schéma et se transpose telle quelle.

---

**12. Quelle source est la plus fiable ? La plus fragile ?**

Les plus fiables sont NVD et FIRST EPSS — 12/12 dans notre grille : officielles, primaires,
accessibles par API versionnée, donc reproductibles. Les plus fragiles sont les deux
sources DIESEC (S17, S44), seules classées `commercial`, score le plus bas en autorité. Et
ce n'est pas théorique : c'est précisément S17 qui porte la date de PoC contredisant
VulnCheck, et c'est aussi S17 qui énonce le correctif vCenter que notre pipeline n'a pas
su extraire. La source la plus fragile est celle sur laquelle nous dépendons le plus pour
les faits que le graphe rate.

---

**13. Que feriez-vous pendant les 90 premiers jours ?**

Généraliser le décompte de porteurs en une métrique de complétude indépendante du domaine —
aujourd'hui il s'appuie sur le texte-preuve d'un corpus cyber, ce qui n'est pas une
définition transposable. En parallèle, corriger la résolution d'entités, qui est la limite
bloquante (2 fusions sur 3 699 mentions) et qui est la raison même pour laquelle le
décompte doit passer par le texte plutôt que par la structure du graphe. Et formaliser le
protocole d'ablation comme méthode reproductible, avec son pré-enregistrement, plutôt que
comme un montage propre à ce cas.

---

**14. Après la démonstration interactive : « vos configurations 5 et 8 donnent des réponses opposées, non ? »**

Oui, et c'est à double tranchant. Elles reçoivent un contexte identique à une seule phrase
près — le signalement d'incomplétude — et aboutissent à « urgent » contre « peut attendre ».
Côté positif, c'est la preuve directe que le modèle **lit le contexte** au lieu de réciter
une réponse mémorisée : une phrase change la décision. Côté honnête, cela veut dire que
**la formulation du signalement est elle-même une variable qui influence la décision, et
nous ne l'avons jamais mesurée comme telle** — nous avons testé la présence du signalement,
pas sa formulation. C'est une limite découverte en construisant l'outil de démonstration,
pas un résultat du protocole des 45 cellules.

---

## Réserve à trois autres questions probables

**« Le LLM valide-t-il une vérité ou une plausibilité ? »** — Une plausibilité. C'est
pourquoi aucun modèle ne note aucune réponse dans notre protocole.

**« Une connaissance manquante impacte-t-elle toutes les questions de la même manière ? »**
— Non, et c'est notre résultat principal : cela dépend du nombre de porteurs, pas de la
question.

**« Quelle information avez-vous décidé de ne pas persister ? »** — 1 154 groupes de
relations non revus, et 11 rejetés explicitement, dont `exploit` : il contenait 6 faits
réels mais mêlés à 53 triplets partageant les mêmes formulations, sans séparation possible
au niveau de la phrase. Nous avons préféré perdre 6 faits que d'en faire entrer 47 douteux.
