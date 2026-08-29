"""Run each non-LLM extraction stage in dependency order."""
from pipeline_lib import (inspect_corpus, extract_structured, extract_openie, extract_entities,
    resolve_entities, build_open_kg, build_relation_inventory, normalize_relations,
    cluster_relations, export_clusters_for_review, build_canonical_kg, evaluate_pipeline,
    extraction_report, final_report)

if __name__ == "__main__":
    inspect_corpus(); extract_structured(); extract_openie(); extract_entities(); resolve_entities()
    build_open_kg(); build_relation_inventory(); normalize_relations(); cluster_relations()
    export_clusters_for_review(); build_canonical_kg(); evaluate_pipeline(); extraction_report(); final_report()
