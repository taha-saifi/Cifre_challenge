"""
Mini-RAG : retrieval par similarite cosinus (TF-IDF)
Objectif : voir concretement les etapes chunk -> embed -> retrieve top-k -> (generate, laisse de cote ici)
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. "Chunks" : nos petits fragments de documents (dans un vrai RAG, ca vient
#    du decoupage de documents plus longs)
chunks = [
    "Le Soleil est une etoile de type naine jaune situee au centre du systeme solaire.",
    "La Lune est le seul satellite naturel de la Terre et influence les marees.",
    "Mars est surnommee la planete rouge a cause de l'oxyde de fer present a sa surface.",
    "Jupiter est la plus grande planete du systeme solaire et possede plus de 90 lunes.",
    "Les marees sont principalement causees par l'attraction gravitationnelle de la Lune.",
    "Venus est la planete la plus chaude du systeme solaire a cause de son effet de serre.",
]

# 2. "Embed" : on vectorise les chunks avec TF-IDF (une forme simple d'embedding,
#    basee sur la frequence des mots plutot que sur du sens appris comme les
#    embeddings neuronaux, mais le principe geometrique est le meme)
vectorizer = TfidfVectorizer()
chunk_vectors = vectorizer.fit_transform(chunks)


def retrieve(question, k=2):
    # La question est vectorisee avec le MEME vectorizer -> meme espace vectoriel,
    # condition necessaire pour que la comparaison ait un sens
    question_vector = vectorizer.transform([question])

    # 3. Similarite cosinus entre la question et chaque chunk
    similarities = cosine_similarity(question_vector, chunk_vectors)[0]

    # 4. "Retrieve top-k" : on trie et on garde les k chunks les plus proches
    top_k_indices = np.argsort(similarities)[::-1][:k]

    print(f"\nQuestion : {question}")
    print(f"Top-{k} chunks recuperes :")
    for rank, idx in enumerate(top_k_indices, start=1):
        print(f"  {rank}. (score={similarities[idx]:.3f}) {chunks[idx]}")


# --- Cas simples : l'info est contenue dans un seul chunk ---
retrieve("Quelle est la planete la plus grande ?", k=2)
retrieve("Quelle planete est appelee planete rouge et pourquoi ?", k=2)

# --- Cas qui illustre une limite du RAG : retrieval purement lexical/local ---
# Repondre correctement necessite DEUX chunks : celui sur la Lune (satellite
# de la Terre) ET celui sur la cause physique des marees (attraction
# gravitationnelle). Verifions ce qui est vraiment recupere :
print("\n--- Classement complet des chunks pour cette question ---")
retrieve("Quel astre cause les marees et de quelle planete est-il le satellite ?", k=6)
# -> Constat : le chunk sur "les marees causees par l'attraction gravitationnelle
#    de la Lune" (le 2e chunk necessaire) se classe SOUS des chunks sans rapport
#    (Venus, Mars), simplement parce qu'ils partagent le mot "planete" avec la
#    question. Avec un k realiste (2 ou 3), ce chunk essentiel n'est PAS
#    recupere : le systeme repondrait avec une information incomplete, sans
#    aucun signal indiquant qu'il lui manque une partie de la reponse.
#    C'est exactement la limite "retrieval local" : la similarite mesuree
#    (ici lexicale via TF-IDF, mais le probleme se retrouve aussi avec des
#    embeddings neuronaux) ne garantit pas que TOUS les fragments pertinents
#    pour une conclusion soient recuperes ensemble.
