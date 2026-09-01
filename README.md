# Branche `demo` — démonstrateur seul

Cette branche ne contient que ce qu'il faut pour **faire tourner la démonstration**.
Le travail complet (corpus de 56 sources, pipeline d'extraction, graphe canonique de
2123 arêtes, protocole des 45 cellules, note / deck / résultats) vit sur **`main`** et
n'est pas dupliqué ici.

> Branche de démonstration, pas de livraison. Ce qui est évalué — la note, le deck, les
> résultats — est sur `main`.

## Ce que la démo montre

Une même question, posée à cinq configurations qui ne diffèrent **que par le contexte
fourni** — le gabarit de prompt est identique entre les colonnes. On observe ce que la
complétude du graphe change à la décision, pas quel modèle « répond le mieux ».

| Config | Contexte fourni |
|---|---|
| 1 | aucun (LLM seul) |
| 2 | RAG documentaire (embeddings réels sur `demo_corpus/clean/`) |
| 4 | KG-aware : sous-graphe complet |
| 5 | KG amputé de ses porteurs Tier-1, **calculés** par `carrier_check` |
| 8 | idem 5, plus un signalement explicite d'incertitude |

La configuration 2 est présente parce que le cahier des charges §13 l'impose comme
**témoin**, pas comme proposition : le challenge exclut explicitement de se limiter à un
chatbot RAG (§6.2 et §21).

## Installation

Python 3.11+. Sous Linux/macOS, remplacer `.venv/Scripts/` par `.venv/bin/`.

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r demo_server/requirements.txt
```

Pour l'**ingestion live** uniquement (scraping de nouvelles sources) :

```bash
.venv/Scripts/python -m pip install -r requirements.txt
.venv/Scripts/python -m playwright install chromium
```

### Clé modèle

Le démonstrateur appelle OpenRouter. Créer un fichier `.env` à la racine — il est
gitignoré et ne doit jamais être commité :

```
OPENROUTER_API_KEY=<votre clé>
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

Sans clé, le serveur démarre quand même et chaque colonne affiche « configuration
indisponible » plutôt que d'inventer une réponse.

## Lancer

```bash
.venv/Scripts/python demo_server/app.py
```

- Comparateur : http://127.0.0.1:5000
- **Voir le graphe existant** : http://127.0.0.1:5000/graph
- Ingestion live + graphe de session : http://127.0.0.1:5000/live

La page `/graph` est en lecture seule : elle dessine `demo_kg` (ou `live_kg`) sans rien
ingérer. Sélectionner des pivots applique **le filtre de `build_contexts.py`** — ce qui
est dessiné est donc exactement l'ensemble d'arêtes qu'une configuration KG-aware
recevrait, et non une sélection propre au viewer. Un clic sur une arête affiche sa
provenance : source, méthode d'extraction, texte-preuve verbatim et score d'autorité
(`inconnue` pour une source de session, jamais un score par défaut).

## Deux exemples à faire tourner

### 1. Fait redondant — la décision ne bouge pas

- Graphe `demo_kg`, pivots **`CVE-2026-55040` + `CVE-2026-63520`** (ctrl-clic)
- Question : *« Si l'équipe ne peut appliquer qu'un seul correctif cette semaine, lequel
  prioriser entre CVE-2026-55040 et CVE-2026-63520, et pourquoi ? »*
- Configurations 1 et 4, puis **relancer avec « Ablation » coché**

Le sous-graphe fait **104 arêtes**. L'ablation retire les **3 porteurs Tier-1** du fait de
chaînage ; **9 porteurs Tier-2** subsistent, **101 arêtes** restent. La décision ne change
pas — et c'est le résultat central du travail : *on ne peut pas mesurer l'impact d'une
relation manquante sans compter combien d'arêtes portent ce fait.*

### 2. Preuves convergentes et tension entre sources

- Graphe `demo_kg`, pivot **`CVE-2026-63520`** (45 arêtes), configurations 2 et 4
- Question : *« CVE-2026-63520 est-elle activement exploitée ? Sur quelles preuves
  t'appuies-tu, et avec quel niveau de confiance ? »*

Le sous-graphe porte cinq signaux hétérogènes venant de trois sources : SSVC exploitation
**none** et automatable **no** (S06), MSRC exploited **No** mais exploitability assessment
**« Exploitation More Likely »** (S42), EPSS **0,0289** pour un percentile **0,8586**
(S25). Deux pièges : la tension MSRC / SSVC (prévision contre observation, pas une
contradiction), et le percentile lu comme une probabilité — un facteur 30.

À faire ensuite : reposer la même question avec le pivot `CVE-2026-55040`. Celui-ci porte
quatre champs `cisa*` (date d'ajout KEV, échéance, action requise) ; `CVE-2026-63520` n'en
porte **aucun**. Même système source, même schéma : c'est une **preuve d'absence**, pas une
absence de preuve. Un RAG qui ne retrouve rien ne peut pas faire cette distinction.

### Ingestion live

Sur `/live` : coller une URL ou déposer un fichier. Les sources sont numérotées à partir
de **S901**, atterrissent dans `live_corpus/` + `live_kg/` isolés, ne sont **jamais**
fusionnées dans `demo_kg/`, et la qualité d'extraction obtenue est affichée en clair.
Le graphe est ensuite explorable, puis interrogeable en basculant « Graphe interrogé »
sur `live_kg`.

## Sur la qualité d'extraction (à dire, pas à cacher)

L'extraction OpenIE utilise **MinIE** quand un service local répond sur
`127.0.0.1:8080`, sinon un extracteur heuristique de repli — et l'interface le **dit**
au lieu de laisser croire à MinIE. L'écart est réel, mesuré sur la phrase centrale de la
démonstration (S40) :

```
MinIE       : Patching CVE-2026-55040 | break   | exploit chain
heuristique : Patching CVE-2026-55040 will successfully break this | exploit | chain
```

Le prédicat devient `exploit`, qui appartient à un groupe **rejeté** à la validation
humaine : l'arête disparaîtrait du graphe canonique. C'est pourquoi `demo_kg/` est une
**projection** du graphe figé (toute arête canonique dont la source appartient au corpus
de démo) et **jamais une ré-extraction** — une ré-extraction hétérogène ferait passer un
changement d'extracteur pour une lacune du graphe.

Démarrer MinIE (JDK 21 + Maven requis, build unique de plusieurs minutes) :

```bash
cd extraction_pipeline/vendor/minie && mvn -ntp -Dmaven.repo.local=../../.m2 -DskipTests package
python extraction_pipeline/scripts/start_minie_service.py
```

Le service met ~75 s à charger les modèles CoreNLP et n'écoute que sur la boucle locale.

## Ce qui n'est délibérément pas ici

| Absent | Pourquoi | Où |
|---|---|---|
| `corpus/` (56 sources) | la démo lit `demo_corpus/` (10 sources) | `main` |
| `extraction_pipeline/` — données, graphe canonique, rapports d'audit | le graphe est **gelé** ; la démo lit la projection `demo_kg/` déjà construite | `main` |
| note, deck, `resultats.md`, `sources.md` | livrables évalués, pas des dépendances de la démo | `main` |
| `experiments/` sauf 3 fichiers | seuls `carrier_check.py`, `score.py` et `build_source_quality.py` sont importés par le serveur | `main` |

Conséquence à connaître : `demo_server/build_demo_kg.py` **ne peut pas tourner sur cette
branche** (il lit `extraction_pipeline/canonical_kg/`, absent ici). `demo_kg/` est fourni
construit. Pour le régénérer, passer sur `main`.

Le code, les commentaires et les messages de commit sont en anglais ; les livrables et
cette page sont en français.
