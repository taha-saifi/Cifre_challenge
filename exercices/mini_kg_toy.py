"""
Mini-KG : magasin de triples, requete simple, regle naive de "lien manquant probable"
"""

# 1. Le magasin de triples : une simple liste de tuples (sujet, relation, objet)
triples = [
    ("Terre", "orbite_autour_de", "Soleil"),
    ("Lune", "orbite_autour_de", "Terre"),
    ("Soleil", "a_pour_satellite", "Terre"),
    # -> remarque : le lien inverse de "Lune orbite_autour_de Terre"
    #    (c'est-a-dire "Terre a_pour_satellite Lune") N'EST PAS present.
    #    C'est volontaire, pour tester la regle de detection plus bas.
    ("Mars", "orbite_autour_de", "Soleil"),
    ("Soleil", "a_pour_satellite", "Mars"),  # celui-ci est complet dans les deux sens
]


# 2. Index pour interroger facilement : sujet -> liste de (relation, objet)
def build_index(triples):
    index = {}
    for s, r, o in triples:
        index.setdefault(s, []).append((r, o))
    return index


index = build_index(triples)


def query(subject, relation=None):
    """Renvoie tous les objets lies a `subject`, filtre par relation si fournie."""
    results = index.get(subject, [])
    if relation:
        results = [(r, o) for r, o in results if r == relation]
    return results


# --- Requetes simples ---
print("Ce que la Terre orbite :", query("Terre", "orbite_autour_de"))
print("Tous les liens de la Lune :", query("Lune"))

# 3. Regle naive de detection de lien manquant : relations inverses connues.
#    Si on sait que "orbite_autour_de" et "a_pour_satellite" sont inverses
#    l'une de l'autre, alors pour chaque triple (A, orbite_autour_de, B), on
#    DEVRAIT trouver (B, a_pour_satellite, A) dans le graphe. Si absent :
#    lien manquant probable.

inverse_relations = {
    "orbite_autour_de": "a_pour_satellite",
    "a_pour_satellite": "orbite_autour_de",
}


def detect_missing_inverse_links(triples, inverse_relations):
    triple_set = set(triples)
    missing = []
    for s, r, o in triples:
        inverse_r = inverse_relations.get(r)
        if inverse_r is None:
            continue  # on ne connait pas de relation inverse pour celle-ci
        expected_triple = (o, inverse_r, s)
        if expected_triple not in triple_set:
            missing.append({
                "triple_existant": (s, r, o),
                "lien_manquant_probable": expected_triple,
            })
    return missing


print("\n--- Liens manquants probables (regle : relations inverses connues) ---")
gaps = detect_missing_inverse_links(triples, inverse_relations)
if not gaps:
    print("  Aucun lien manquant detecte.")
for gap in gaps:
    print(f"  Triple existant      : {gap['triple_existant']}")
    print(f"  -> Manque probablement : {gap['lien_manquant_probable']}\n")
