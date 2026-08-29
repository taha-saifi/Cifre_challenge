#!/usr/bin/env python3
"""Render deliverables/resultats.md from the experiment data files.

The report is generated, never hand-typed, so no figure in it can drift from
carriers.json / scores.json / decisions.json.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "deliverables" / "resultats.md"
CONFIGS = [1, 4, 5, 7, 8]
CONFIG_LABEL = {
    1: "1 — LLM seul",
    4: "4 — KG complet",
    5: "5 — KG incomplet",
    7: "7 — KG pré-validation",
    8: "8 — KG incomplet + signalement",
}


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def main() -> int:
    tasks = load("tasks.json")
    carriers = load("carriers.json")
    scores = load("scores.json")
    decisions = load("decisions.json")

    score_by_cell = {(s["task"], s["config"]): s for s in scores["scores"]}
    lines = []
    add = lines.append

    add("# Résultats du protocole expérimental (§13)")
    add("")
    add("*Document généré par `experiments/build_report.py` depuis `carriers.json`, "
        "`scores.json` et `decisions.json`. Ne pas éditer à la main : toute correction "
        "se fait dans les données puis par régénération.*")
    add("")
    n_tasks = len(tasks["tasks"])
    add(f"**{n_tasks} tâches × {len(CONFIGS)} configurations = {n_tasks * len(CONFIGS)} cellules.** "
        "Un seul appel par cellule, aucun retry, chaque cellule exécutée par un agent isolé "
        "ne connaissant ni le protocole ni les autres cellules. Le prompt de décision est "
        "identique dans les cinq configurations d'une même tâche ; seul le contexte varie.")
    add("")

    # --- 1. Decision table -------------------------------------------------
    add("## 1. Tableau des décisions")
    add("")
    add("| Tâche | " + " | ".join(CONFIG_LABEL[c] for c in CONFIGS) + " |")
    add("|---|" + "---|" * len(CONFIGS))
    for task in tasks["tasks"]:
        tid = task["id"]
        cells = decisions["cells"].get(tid, {})
        row = [f"**{tid}**"]
        for c in CONFIGS:
            row.append(cells.get(f"c{c}", "—"))
        add("| " + " | ".join(row) + " |")
    add("")

    # --- 2. Ablation effect ------------------------------------------------
    add("## 2. Effet de l'ablation : la décision change-t-elle par rapport à la config 4 ?")
    add("")
    add("| Tâche | Porteurs du fait ablaté | Ablation complète ? | c5 ≠ c4 | c8 ≠ c4 |")
    add("|---|---:|---|---|---|")
    changed_count = 0
    for task in tasks["tasks"]:
        tid = task["id"]
        cells = decisions["cells"].get(tid, {})
        info = carriers["tasks"].get(tid, {})
        n_carriers = info.get("carrier_count", "n/a")
        complete = info.get("ablation_complete")
        complete_str = {True: "oui", False: "**non**", None: "s.o."}[complete]
        c5_diff = cells.get("c5") != cells.get("c4")
        c8_diff = cells.get("c8") != cells.get("c4")
        if c5_diff:
            changed_count += 1
        add(f"| {tid} | {n_carriers} | {complete_str} | "
            f"{'**OUI**' if c5_diff else 'non'} | {'**OUI**' if c8_diff else 'non'} |")
    add("")
    add(f"Sur {n_tasks} tâches, **{changed_count}** voient leur décision changer entre la "
        "config 4 et la config 5.")
    add("")

    # --- 3. Grounding ------------------------------------------------------
    add("## 3. Grounding et citations (calculés, sans juge LLM)")
    add("")
    add("`grounding` = part des jetons littéralement vérifiables de la réponse "
        "(identifiants CVE, références KB, identifiants de source, dates ISO, scores CVSS) "
        "que l'on retrouve dans le contexte exact fourni à cette cellule. La comparaison est "
        "faite par correspondance de chaînes, jamais par appréciation.")
    add("")
    add("| Tâche | " + " | ".join(f"c{c}" for c in CONFIGS) + " |")
    add("|---|" + "---|" * len(CONFIGS))
    for task in tasks["tasks"]:
        row = [f"**{task['id']}**"]
        for c in CONFIGS:
            s = score_by_cell.get((task["id"], c))
            if not s:
                row.append("—")
                continue
            g = s["grounding"]
            row.append(f"{g['grounded']}/{g['verifiable_tokens']}" if g["verifiable_tokens"] else "n/a")
        add("| " + " | ".join(row) + " |")
    add("")

    c1_tokens = sum(score_by_cell[(t["id"], 1)]["grounding"]["verifiable_tokens"]
                    for t in tasks["tasks"] if (t["id"], 1) in score_by_cell)
    c1_grounded = sum(score_by_cell[(t["id"], 1)]["grounding"]["grounded"]
                      for t in tasks["tasks"] if (t["id"], 1) in score_by_cell)
    kg_tokens = sum(s["grounding"]["verifiable_tokens"] for s in scores["scores"] if s["config"] != 1)
    kg_grounded = sum(s["grounding"]["grounded"] for s in scores["scores"] if s["config"] != 1)
    add(f"Agrégé : config 1 (LLM seul) **{c1_grounded}/{c1_tokens}** jetons ancrés ; "
        f"configs KG-aware **{kg_grounded}/{kg_tokens}**.")
    add("")
    add(f"Le ratio de la config 1 est trompeur pris seul : les rares jetons qu'elle ancre sont "
        f"surtout l'identifiant CVE recopié depuis la question. Le signal réel est le **volume** "
        f"de faits vérifiables produits — {c1_tokens} jetons sur {n_tasks} tâches en config 1 "
        f"contre {kg_tokens} pour les configurations KG-aware, soit un facteur "
        f"{kg_tokens / c1_tokens:.0f}×. Sans graphe, le modèle ne se trompe pas beaucoup : il "
        f"n'avance presque rien de vérifiable.")
    add("")
    add("Deux réserves sur cette métrique, à énoncer plutôt qu'à masquer. D'abord elle compte "
        "des nombres employés rhétoriquement : le « 7.0 » de T7-c1 est un seuil dans une "
        "phrase conditionnelle, pas une affirmation sur la CVE. Ensuite la config 1 n'est pas "
        "un isolement parfait — en T6-c1 le modèle cite les identifiants de source S02–S06 et "
        "S21–S25 sans avoir lu le corpus, ce que seul son environnement d'exécution peut lui "
        "avoir fourni. La baseline « LLM seul » est donc légèrement optimiste.")
    add("")

    # --- 4. Observable indicators -----------------------------------------
    add("## 4. Indicateurs observables (§14.3)")
    add("")
    add("Comptés, pas notés : *décision explicite formulée*, *incertitude nommée*, "
        "*information complémentaire demandée*, *niveau de confiance énoncé*.")
    add("")
    add("| Config | Décision explicite | Incertitude nommée | Info demandée | Confiance énoncée |")
    add("|---|---:|---:|---:|---:|")
    for c in CONFIGS:
        cells = [s for s in scores["scores"] if s["config"] == c]
        counts = {k: sum(1 for s in cells if s["indicators"][k]) for k in
                  ("explicit_decision", "names_uncertainty", "requests_more_info", "states_confidence")}
        add(f"| {CONFIG_LABEL[c]} | {counts['explicit_decision']}/{len(cells)} | "
            f"{counts['names_uncertainty']}/{len(cells)} | {counts['requests_more_info']}/{len(cells)} | "
            f"{counts['states_confidence']}/{len(cells)} |")
    add("")

    # --- 4b. Exactitude vs the pre-registered key --------------------------
    add("## 4b. Exactitude par configuration (contre la clé pré-enregistrée)")
    add("")
    add("La clé a été écrite et gelée avant l'exécution de toute cellule. Pour les tâches "
        "dont le fait testé est ablaté (T4, T8), la réponse attendue en configuration 5 "
        "et 8 est un constat explicite d'impossibilité de conclure, pas la réponse "
        "positive.")
    add("")
    add("| Configuration | Exactitude | Incertitude nommée |")
    add("|---|---:|---:|")
    matches = decisions["matches_key"]
    task_ids = [t for t in matches if not t.startswith("_")]
    for c in CONFIGS:
        correct = sum(1 for t in task_ids if matches[t].get(f"c{c}"))
        uncertain = sum(1 for s in scores["scores"]
                        if s["config"] == c and s["indicators"]["names_uncertainty"])
        add(f"| {CONFIG_LABEL[c]} | {correct}/{len(task_ids)} | {uncertain}/{len(task_ids)} |")
    add("")

    # --- 5. Gap classification --------------------------------------------
    add("## 5. Classification des écarts (§7)")
    add("")
    add(decisions["gap_classification"]["_typology"])
    add("")
    for tid, info in decisions["gap_classification"].items():
        if tid.startswith("_"):
            continue
        add(f"- **{tid} — {info['type']}.** {info['evidence']}")
    add("")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(lines)} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
