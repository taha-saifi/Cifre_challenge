# Explorateur KG — serveur local

Outil d'exploration pour **les 40 minutes de discussion**, pas pour le pitch minuté.

> **Ne remplace pas `deliverables/demo.html`.** La page statique reste la démonstration
> scriptée de 3 minutes (`deliverables/demo_script.md`) : hors ligne, déjà testée, aucun
> risque d'appel réseau en direct. Ce serveur sert au cas que la page statique ne couvre
> pas — une question inventée par le jury sur le moment.

## Démarrage

```bash
.venv/Scripts/python demo_server/app.py
```

Deux pages, sur `127.0.0.1` uniquement :

| Page | Rôle |
|---|---|
| **http://127.0.0.1:5000** | comparaison de 5 configurations sur une question, graphe `demo_kg/` |
| **http://127.0.0.1:5000/live** | ingestion de sources (URLs, fichiers) → extraction → graphe interactif |

Prérequis : `.venv` avec `flask`, `requests`, `python-dotenv`, et un fichier `.env` à la
racine contenant `OPENROUTER_API_KEY` (déjà en place, et **ignoré par git**). Sans clé, le
serveur démarre quand même et chaque colonne affiche « configuration indisponible ».

L'index d'embeddings est construit au premier appel RAG et mis en cache dans
`rag_index.json`. Pour le reconstruire : `.venv/Scripts/python demo_server/rag.py`.

## Ce que fait l'outil

Une question, jusqu'à cinq configurations exécutées **en parallèle**, réponses côte à côte.
La question et la consigne de décision sont **identiques dans toutes les colonnes** ; seul
le contexte change. C'est le même contrat méthodologique que les 45 cellules.

| Config | Contexte transmis |
|---|---|
| 1 — LLM seul | aucun |
| 2 — RAG documentaire | top-5 passages de `demo_corpus/` par similarité cosinus sur embeddings réels |
| 4 — KG-aware complet | sous-graphe complet autour des pivots, via le même filtre que `build_contexts.py` |
| 5 — KG incomplet | idem, moins les porteurs Tier-1 **calculés** par `carrier_check.py` |
| 8 — KG incomplet + signalement | idem 5, plus la phrase de signalement d'incomplétude |

La case « retirer le porteur principal » n'agit que sur les configurations 5 et 8, et
appelle `carrier_check.find_carriers()` — les arêtes retirées sont donc **calculées, jamais
désignées à la main**, exactement comme dans le protocole enregistré.

## Ce qui est réutilisé, et ce qui ne peut pas l'être

**Réutilisé tel quel** : le filtre de sous-graphe et le rendu
`sujet prédicat objet [source: Sxx]` (`experiments/build_contexts.py`), la détection de
porteurs (`experiments/carrier_check.py`), la règle de jetons vérifiables du grounding
(`experiments/score.py`).

**Ce qui diffère, et qu'il faut dire tel quel à l'oral** : les 45 cellules enregistrées ont
été produites par des agents Claude Code isolés, un appel chacun, sans retry. Un serveur web
ne peut pas en lancer. Ce client appelle **OpenRouter** — c'est un *transport différent*.
Ce qui est préservé, c'est le contrat qui porte la méthode : prompt identique entre
configurations, seul le contexte varie. Dire que cet outil « rejoue » les cellules
enregistrées serait faux.

## Modèles

Chaîne de repli **fixe**, sur la disponibilité et non sur la qualité — aucune comparaison
entre modèles n'est faite ni suggérée :

1. `nvidia/nemotron-3.5-lightning:free`
2. `poolside/laguna-s-2.1:free`
3. `inclusionai/ling-3.0-flash-fin:free`

Embeddings (récupération uniquement, pas de chat) : `liquid/lfm-2.5-embedding-350m:free`.

Le passage au modèle suivant se déclenche sur : erreur réseau, HTTP ≠ 200, **429
(rate-limit)**, contenu vide, raisonnement sans conclusion, sortie encore délibérative, ou
réponse tronquée (budget épuisé). « Configuration indisponible » ne s'affiche que si les
**trois** échouent, avec le détail des tentatives.

Note vérifiée sur ces modèles : les trois émettent une chaîne de raisonnement. Le premier
l'écrit dans `content` et ignore toute consigne contraire (testé, y compris avec
`reasoning.exclude=true`). Le préambule est donc retiré à l'affichage, la sortie brute reste
consultable dans un dépliant sous chaque réponse, et rien n'est supprimé silencieusement.

## Test manuel documenté

Question **hors des 9 tâches du protocole**, pour montrer que l'outil généralise et n'est
pas un rejeu déguisé :

> « Un serveur SharePoint 2019 non exposé à internet mais accessible depuis le réseau
> interne : faut-il appliquer le correctif de CVE-2026-63520 en urgence ou peut-on attendre
> le prochain cycle ? »

Pivot `CVE-2026-63520`, ablation activée, 5 configurations. Résultat complet dans
`test_run.json` (101,7 s) :

| Config | Contexte | Décision obtenue | Grounding |
|---|---|---|---:|
| 1 — LLM seul | aucun | appliquer au cycle courant | aucun jeton vérifiable |
| 2 — RAG | 5 passages (S10, S18, S40, S41) | **urgent** | 6/6 |
| 4 — KG complet | 45 triplets | **rapidement** | 4/5 |
| 5 — KG incomplet | 36 triplets, −9 porteurs | **urgent** | 3/3 |
| 8 — KG incomplet + signalement | 36 triplets, −9 porteurs | **peut attendre** | 7/7 |

Deux observations exploitables à l'oral. D'abord la colonne RAG est réellement distincte de
« LLM seul » : elle récupère 5 passages de 4 sources et passe de 0 à 6 jetons vérifiables —
si la récupération ne fonctionnait pas, les deux colonnes seraient identiques. Ensuite les
configurations 5 et 8 partagent **exactement le même contexte** à la phrase de signalement
près, et aboutissent à des décisions opposées : c'est une illustration en direct de l'effet
du cadrage, obtenue sur une question que le jury pourrait poser.

## Limites

- Dépend d'un appel réseau en direct. C'est pourquoi il ne remplace pas la démo scriptée.
- Le graphe interrogé est `demo_kg/`, une **projection** du graphe figé sur 10 sources — pas
  une ré-extraction (voir `demo_server/build_demo_kg.py` et `demo_corpus/SELECTION.md`).
- Les modèles gratuits sont lents (≈ 100 s pour 5 configurations en parallèle) et peuvent
  être limités en débit ; la chaîne de repli existe pour ça.
- Les réponses sortent tantôt en français tantôt en anglais selon le modèle qui répond.


---

# Page `/live` — ingestion et visualisation

Coller des URLs et/ou déposer des fichiers (`.txt`, `.md`, `.html`, `.pdf`), les faire
passer par le pipeline existant, et explorer le graphe obtenu.

## Rien n'est réimplémenté

| Étape | Fonctions réutilisées |
|---|---|
| Collecte HTTP | `build_corpus.request_with_retry` (retry 5/15/30 s) |
| HTML → texte | `build_corpus.html_to_text` (trafilatura, repli readability-lxml) |
| Repli navigateur | `build_corpus.fetch_via_playwright` |
| PDF | `build_corpus.extract_pdf` (pdfplumber) |
| Contrôle qualité | `build_corpus.is_suspect` |
| Nettoyage | `preprocess_corpus.filter_noise`, `normalize_whitespace`, `chunk_text` |
| Extraction → graphe | `pipeline_lib.extract_structured/extract_openie/extract_entities/resolve_entities/build_open_kg` |

Les fonctions du pipeline ne prennent aucun argument et lisent tous leurs chemins dans
`config`. `live_pipeline.redirected_config()` rebind ces chemins vers `live_kg/` le temps
du run, sous verrou, et les restaure toujours — un run live **ne peut pas** écrire dans
`extraction_pipeline/`. Les sources sont numérotées à partir de `S901` pour ne jamais se
confondre avec le corpus figé (S01–S58).

## Isolation

Sortie dans `live_corpus/` et `live_kg/`, **jamais fusionnée avec `demo_kg/`** ni avec
`corpus/`. Les deux répertoires sont régénérés à chaque ingestion et sont gitignorés : ils
contiennent du texte tiers récupéré sur le web, qui n'a pas à entrer dans le dépôt.

## Deux limites affichées en grand, pas en petits caractères

1. **Extraction heuristique.** MinIE exige Java et un JAR construit, absents ici — rien
   n'écoute sur `127.0.0.1:8080`. Le backend est **sondé une fois** au début du run
   (`live_pipeline.minie_available()`) et `config.OPENIE_BACKEND` est réglé sur ce qui
   existe réellement. Laissé sur `minie` alors que le service est mort, `extract_openie`
   réessaie une fois par lot **et** une fois par phrase : plusieurs centaines de tentatives
   réseau pour une seule page longue, ce qui faisait passer une ingestion de 13 s à plus de
   10 minutes. Le bandeau de la page donne un exemple mesuré de l'écart de qualité.
2. **Graphe pré-validation.** Ce qui s'affiche est `open_kg`, pas le graphe canonique. Dans
   ce projet aucune arête ne devient canonique sans qu'un humain accepte son cluster de
   relation ; cette étape n'est pas dans l'outil, donc le canonique serait vide. Afficher
   l'ouvert en le disant est la seule option honnête.

## Dégradation propre

Chaque source a son propre statut ; un échec n'affecte qu'elle. Vérifié :

| Cas | Résultat |
|---|---|
| Page HTML normale (openwall) | `ok`, 12 253 car., `html_trafilatura`, 2,6 s |
| SPA sans contenu serveur (NVD) | `failed` — « aucun texte extrait » + raison du repli navigateur (`chromium executable doesn't exist`) |
| Hôte injoignable | `failed` — « réseau : Échec après 4 tentatives » |
| Fichier texte | `ok`, `text_direct` |

La requête renvoie toujours HTTP 200 avec les statuts par source, pour que la page affiche
ce qui a fonctionné.

## Test manuel documenté

2 URLs (openwall + Wikipédia XZ backdoor) via l'interface : **2 sources exploitées, 40
assertions OpenIE, 77 nœuds, 40 arêtes**, extracteurs `heuristic=303`, pastille
« pré-validation » affichée. Un clic sur une arête restitue la chaîne de provenance
complète — triplet, `source_id`, URL cliquable, méthode d'extraction, et le texte-preuve
verbatim :

```
backdoor in upstream xz/liblzma — leading to → ssh server compromise
S901 · https://www.openwall.com/lists/oss-security/2024/03/29/4
heuristic
« Subject: backdoor in upstream xz/liblzma leading to ssh server compromise »
```

`vis-network` est vendoré dans `static/vendor/` : aucune dépendance CDN à l'exécution.
