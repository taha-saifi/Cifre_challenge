# Script de démonstration — 2 min 40

*À dérouler après la slide 6. Chronométré. Le démonstrateur est une page autonome, sans
réseau : rien ne peut échouer en direct.*

---

## 0:00 — 0:20 · Poser le dispositif

> « Même question, même modèle, même consigne. La seule chose qui change, c'est le
> graphe : je retire un fait, et je relance. »

Montrer le bandeau haut, puis la bascule **KG complet / KG amputé**. Ne pas encore
cliquer.

---

## 0:20 — 1:10 · Cas A — le résultat contre-intuitif

Question à l'écran : arbitrer entre les deux CVE SharePoint.

> « À gauche, les triplets réellement transmis au modèle. Les trois surlignés portent le
> chaînage entre les deux failles — c'est l'information censée décider. À droite, la
> réponse : patcher CVE-2026-55040. »

**Cliquer « KG amputé ».**

> « Je retire les trois. La décision ne bouge pas. »

Laisser deux secondes de silence.

> « Notre première lecture a été : cette relation n'a pas d'importance. C'était faux. »

---

## 1:10 — 1:50 · Cas A — l'explication

Descendre au panneau **« Pourquoi la décision ne bouge pas »**.

> « Neuf autres arêtes portaient le même fait sous d'autres étiquettes. Celle-ci » —
> pointer `Patching CVE-2026-55040 break exploit chain` — « la réponse la cite mot pour
> mot, y compris après ablation. L'information n'a jamais quitté le graphe. »

> « C'est ce qui nous a conduits à mesurer, avant toute ablation, **combien d'arêtes
> portent un fait**. Sans ce décompte, une ablation ne mesure pas ce qu'elle prétend
> mesurer. »

---

## 1:50 — 2:30 · Cas B — le contre-exemple

**Cliquer l'onglet « Cas B ».** Question : quel correctif pour CVE-2026-63520 ?

> « Ici, cinq arêtes portent les références KB — et rien d'autre dans le graphe ne
> véhicule ce fait. Zéro porteur partiel. »

Réponse à droite : la liste des KB.

**Cliquer « KG amputé ».**

> « Je retire les cinq. Cette fois la décision bascule : “référence indisponible”. Et le
> modèle n'invente pas de numéro de KB — il constate l'absence et le dit. »

---

## 2:30 — 2:40 · La phrase de sortie

> « Deux cas, deux régimes. Ce n'est pas l'importance apparente de la relation qui
> détermine l'impact de son absence, c'est le nombre de porteurs. Et ce nombre, on peut
> le calculer avant de générer quoi que ce soit. »

---

## Questions anticipées

**« Pourquoi le retrait de la relation n'a-t-il rien changé au cas A ? »**
Parce que la relation n'était pas seule à porter le fait. Neuf arêtes le portaient encore
sous d'autres étiquettes — c'est mesuré, pas supposé, et le cas B montre le comportement
inverse quand le porteur est unique.

**« N'avez-vous pas simplement mal retiré la relation ? »**
Si, la première fois : deux arêtes retirées sur trois. C'est précisément ce que le
décompte de porteurs a révélé. La seconde version en retire l'intégralité — et la
décision ne bouge toujours pas, à cause des porteurs partiels.

**« Le modèle ne récite-t-il pas simplement ses connaissances préalables ? »**
La configuration sans graphe est dans le protocole : elle choisit la mauvaise CVE et
produit 16 faits vérifiables contre 556. Les connaissances préalables ne suffisent pas.

**« Ces triplets sont-ils réels ? »**
Ce sont exactement ceux transmis au modèle, au format du contexte. Chacun garde son
identifiant de source et son texte-preuve dans le graphe canonique.

**« Et la couche exposition d'actif ? »**
Synthétique, et signalée comme telle **dans le contexte lui-même** : aucune source du
corpus ne documente un actif client concret. Elle n'est pas utilisée dans cette démo.
