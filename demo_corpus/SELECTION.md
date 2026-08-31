# Corpus de démonstration — sélection des sources

Sous-ensemble dédié au démonstrateur interactif. **Le corpus complet
(`corpus/`, 57 sources déclarées / 56 exploitables) et ses dérivés — note, deck,
`resultats.md` — ne sont pas modifiés.** Les 10 fichiers ci-dessous sont des copies
octet-pour-octet des originaux (vérifié par empreinte SHA-256).

## Règle de sélection

La sélection n'est pas un choix éditorial : elle est **calculée**. Sont retenues
exactement les sources dont le `source_id` apparaît dans au moins une arête des
sous-graphes des deux cas du démonstrateur actuel, obtenus par la même fonction de
filtrage que `experiments/build_contexts.py` :

- **T1 / T1b** — chaînage SharePoint, pivots `CVE-2026-55040` + `CVE-2026-63520` → 104 arêtes, 10 sources
- **T8** — références de correctif, pivot `CVE-2026-63520` → 45 arêtes, 6 sources

Union des deux : **10 sources**. Aucune source n'a été ajoutée ni retirée à la main.

> **Note de périmètre.** La demande initiale désignait le second cas comme « correctifs
> vCenter T8 ». T8 porte en réalité sur les **références de correctif SharePoint de
> CVE-2026-63520** ; le cas vCenter (`CVE-2026-59310`) est **T3**, qui n'est pas un des
> deux cas du démonstrateur actuel. La sélection suit les deux cas réellement présents
> dans `deliverables/demo.html`. Si le cas vCenter doit être ajouté, il faudra y joindre
> les sources du sous-graphe T3 (S04, S11, S12, S17, S23, S43, S44).

## Sources retenues

| Source | Tâches qui la justifient | Rang | Catégorie | Nom | Porteuse |
|---|---|---|---|---|---|
| S03 | T1, T1b | primary | official | NVD : CVE-2026-55040 | ✔ |
| S06 | T1, T1b, T8 | primary | official | NVD : CVE-2026-63520 | |
| S10 | T1, T1b, T8 | primary | researcher | VulnCheck : SharePoint unsafe type RCE | ✔ |
| S18 | T1, T1b, T8 | secondary | journalistic | Help Net Security : PoC CVE-2026-55040 | ✔ |
| S22 | T1, T1b | primary | official | FIRST EPSS : CVE-2026-55040 | |
| S25 | T1, T1b, T8 | primary | official | FIRST EPSS : CVE-2026-63520 | |
| S39 | T1, T1b | primary | publisher | MSRC : CVE-2026-55040 | |
| S40 | T1, T1b | primary | researcher | Rapid7 : JWT bypass CVE-2026-55040 | ✔ |
| S41 | T1, T1b, T8 | primary | researcher | Rapid7 : RCE CVE-2026-63520 | ✔ |
| S42 | T1, T1b, T8 | primary | publisher | MSRC : CVE-2026-63520 | |

**Porteuse** = la source fournit au moins un porteur (Tier-1 ou Tier-2) d'un des faits
démontrés, d'après `experiments/carriers.json`. Les 5 sources porteuses — S03, S10, S18,
S40, S41 — sont celles dont le retrait casserait la démonstration. Les 5 autres
fournissent le contexte décisionnel (scores NVD, EPSS, statuts MSRC) sans porter les
faits ablatés.

Familles représentées : NVD, FIRST EPSS, Rapid7, MSRC, VulnCheck, Help Net Security —
6 des 9 familles principales du corpus complet.

## Faits que ce sous-ensemble doit pouvoir reproduire

| Cas | Fait ablaté | Porteurs | Résultat attendu | Méthode d'extraction |
|---|---|---:|---|---|
| T1 | chaînage SharePoint (ablation d'origine, incomplète) | 12 | décision **inchangée** | `minie` ×2 |
| T1b | chaînage SharePoint (tous porteurs Tier-1) | 12 | décision **inchangée** | `minie` ×3 |
| T8 | références KB de CVE-2026-63520 | 5 | décision **bascule** | `structured` ×5 |

## Statut du graphe de démonstration (`demo_kg/`)

**Non produit à ce stade — blocage technique constaté, pas une omission.**

Le graphe figé a été extrait avec MinIE pour 3246 assertions et l'extracteur heuristique
de repli pour 405 seulement (`extraction_pipeline/data/openie_run_metadata.json`). Or
MinIE **ne peut pas tourner sur cette machine** : ni Java, ni JAR construit, et le service
local répond `(None, 'urlerror')` — rien n'écoute sur `127.0.0.1:8080`.

Rejouer le pipeline sur ce sous-ensemble utiliserait donc l'extracteur heuristique pour
100 % du texte libre. Mesuré directement sur la phrase la plus importante de la
démonstration (S40) :

```
MinIE (graphe figé)  : Patching CVE-2026-55040 | break        | exploit chain
Heuristique (repli)  : Patching CVE-2026-55040 will successfully break this | exploit | chain
```

Le prédicat deviendrait `exploit` — qui fait partie des **11 clusters rejetés** à la
validation humaine. L'arête serait donc exclue du graphe canonique, et la démonstration
T1/T1b s'effondrerait. **Cette divergence ne signalerait pas la perte d'un porteur dans
le sous-ensemble** — elle refléterait un changement d'extracteur, un diagnostic tout
autre. La produire en l'état reviendrait à fabriquer un faux signal.

T8 n'est pas affecté : ses 5 arêtes sont `structured`, issues d'un extracteur regex à
portée fixe qui n'utilise pas MinIE.

Deux voies possibles, à trancher :

1. **Installer Java 21 + Maven, construire MinIE, puis rejouer le pipeline** — seule voie
   conforme à la demande (« mêmes scripts que pour le corpus complet »). Coût : une
   installation système.
2. **Dériver `demo_kg/` en projetant le graphe figé sur les 10 sources retenues** —
   déterministe, reproductible, préserve exactement les deux résultats validés, mais ce
   n'est **pas** un rejeu du pipeline : c'est une projection, du même type que
   `experiments/build_presentation_view.py`. À décrire comme telle, jamais comme une
   ré-extraction.
