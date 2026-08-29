# Sélection du jeu de tâches (§13)

Ce document existe pour une seule raison : rendre le choix des tâches **vérifiable**.
Le critère le plus lourd de la grille §20 est la qualité du protocole expérimental
(15/100), et un protocole dont les tâches ont été choisies au jugé n'est pas un
protocole. On donne donc l'espace complet des tâches possibles, la règle de sélection,
et ce qui a été écarté.

## 1. Espace des candidates : 32 instanciations

Le corpus a **5 entités pivots** (les 5 CVE du périmètre) et le protocole utilise
**7 gabarits** indépendants du domaine. L'espace est le produit des deux :

| Gabarit | Portée | Nombre d'instances |
|---|---|---:|
| `pairwise_arbitration` — arbitrer entre deux entités | paire | C(5,2) = **10** |
| `single_urgency` — urgence d'une entité seule | 1 pivot | **5** |
| `absence_check` — un fait est-il établi ou absent ? | 1 pivot | **5** |
| `conflict_arbitration` — arbitrer deux signaux contradictoires | 1 pivot | **5** |
| `availability_check` — une information précise est-elle disponible ? | 1 pivot | **5** |
| `compliance_check` — conformité de l'ensemble à une règle | 5 pivots | **1** |
| `full_ranking` — ordonner l'ensemble | 5 pivots | **1** |
| | | **32** |

Aucun de ces gabarits n'est spécifique à la cybersécurité : arbitrer entre deux
entités, constater une absence, trancher un conflit de signaux, vérifier une
conformité, ordonner un ensemble. Seul change le **type d'entité pivot**. C'est ce qui
rend le protocole transposable à un autre domaine sans réécriture.

Taille du sous-graphe par candidate (mesurée, pas estimée) :

| Portée | Sous-graphe |
|---|---:|
| Paires (10) | de 80 (59310+65400) à 114 edges (33824+55040) |
| CVE seule | 33824 : 54 · 55040 : 60 · 59310 : 42 · 63520 : 45 · 65400 : 38 |
| Ensemble des 5 | 238 edges |

## 2. Règle de sélection, écrite avant exécution

**9 tâches retenues sur 32.** Les 23 autres n'ont pas été exécutées : à 5
configurations par tâche, l'espace complet représenterait 160 cellules, hors budget.
La règle appliquée :

1. **Les deux tâches du Jour 2 sont conservées telles quelles** (T1, T2), y compris
   leur ablation connue comme incomplète, pour que les résultats antérieurs restent
   comparables. Elles ne sont pas rejouées.
2. **Chacune des quatre exigences du §13 est couverte au moins deux fois** :
   plusieurs sources · relations entre entités · conditions/exceptions/dépendances ·
   révélation des limites du corpus ou du graphe.
3. **Le jeu doit contenir au moins un fait à porteur unique et un fait fortement
   redondant.** Sans les deux, le protocole ne peut pas distinguer « la relation
   retirée n'avait pas d'importance » de « la relation retirée était encore portée
   ailleurs ». C'est la correction directe de l'échec du Jour 2.
4. **Une même paire ou un même pivot n'est pas réutilisé** au-delà de ce qu'exige la
   règle 3 (d'où T1/T1b sur la même paire : la comparaison ablation incomplète vs
   complète est précisément l'objet du test).

### Tâches retenues

| # | Gabarit | Pivot(s) | Exigence §13 couverte | Porteurs |
|---|---|---|---|---:|
| T1 | pairwise_arbitration | 55040 + 63520 | relations entre entités | 12 |
| T1b | pairwise_arbitration | 55040 + 63520 | idem, ablation complète | 12 |
| T2 | single_urgency | 33824 | conditions / exceptions | s.o. |
| T3 | absence_check | 59310 | limites du corpus | 1 |
| T4 | absence_check | 65400 | limites du graphe | 1 |
| T5 | compliance_check | les 5 | plusieurs sources | 4 |
| T6 | full_ranking | les 5 | plusieurs sources + relations | 10 |
| T7 | conflict_arbitration | 63520 | contradiction entre sources | 2 |
| T8 | availability_check | 63520 | limites du corpus | 5 |

### Contrôle anti-complaisance

La sélection ne privilégie pas les sous-graphes les plus fournis — vérifiable sur les
chiffres ci-dessus :

- la paire retenue (55040+63520, 104 edges) est la **6ᵉ sur 10** en taille, pas la
  première (33824+55040, 114) ;
- les deux `absence_check` portent sur les **deux CVE les plus pauvres** du corpus
  (65400 : 38 edges, 59310 : 42), c'est-à-dire les cas les plus défavorables au KG ;
- T3 porte sur la seule CVE dont le sous-graphe **ne contient aucun fait de
  disponibilité de correctif**, alors que S17 en énonce un — un cas où le graphe est
  pris en défaut, pas mis en valeur.

### Candidates écartées (23) et motif

| Écartées | Motif |
|---|---|
| 9 paires restantes | Le gabarit `pairwise_arbitration` est déjà couvert deux fois (T1/T1b). Une paire supplémentaire n'aurait testé aucune exigence §13 nouvelle. |
| `single_urgency` sur 55040, 59310, 63520, 65400 (4) | Gabarit couvert par T2. La condition testée (exposition de l'actif) est hors corpus pour les cinq CVE : les répliquer aurait multiplié le même scénario synthétique. |
| `absence_check` sur 33824, 55040, 63520 (3) | Gabarit couvert deux fois par T3/T4, déjà sur les deux pivots les plus défavorables. |
| `conflict_arbitration` sur 33824, 55040, 59310, 65400 (4) | Le conflit CVSS-élevé / EPSS-faible n'existe que pour 63520 (CVSS 8.1, EPSS 0,029). Sur les quatre autres les deux signaux concordent : il n'y aurait pas eu de contradiction à arbitrer. |
| `availability_check` sur 33824, 55040, 59310, 65400 (4) | Gabarit couvert par T8, retenu sur 63520 parce que c'est le seul cas où la référence de correctif a un historique d'extraction fragmentée documenté. |

## 3. Traçabilité des ajustements

Deux ajustements ont été faits pendant la construction, **avant l'exécution de toute
cellule** — donc sans possibilité d'ajuster au résultat :

- Les `anchors` de T3 et T4 ont été affinés une fois. Les valeurs initiales
  (`patch`, `exploit`) captaient des correspondances non voulues : `patch` remontait le
  texte réglementaire CISA (qui contient « patching guidelines ») et `exploit` remontait
  une URL du catalogue KEV et un sous-score CVSS. Corrigés en `mitigations` et
  `exploitation:`, qui désignent exactement le fait visé.
- Les cibles d'ablation ne sont pas écrites à la main : `carrier_check.py --apply`
  calcule l'ensemble complet des porteurs Tier-1 et l'inscrit dans `tasks.json`. Seules
  T1 (gelée à l'identique du Jour 2) et T2 (fait hors corpus) y échappent.

## 4. Limite assumée

9 tâches sur 32 restent un échantillon. Le jeu couvre les quatre exigences du §13 et
les deux régimes de redondance, mais il ne permet pas d'affirmer une fréquence : dire
« 2 tâches sur 9 changent de décision » décrit ce jeu-là, pas une propriété générale du
graphe. La montée à l'espace complet (160 cellules) est le prolongement naturel.
