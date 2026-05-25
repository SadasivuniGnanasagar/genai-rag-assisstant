from sklearn.metrics.pairwise import cosine_similarity
from app.services.embedding_service import generate_embedding
from app.vectorstore.store import vector_db
import numpy as np

THRESHOLD = 0.5

def retrieve_chunks(query, top_k=3):

    query_embedding = generate_embedding(query)

    results = []

    for item in vector_db:

        score = cosine_similarity(
            [query_embedding],
            [item["embedding"]]
        )[0][0]

        results.append({
            "text": item["text"],
            "title": item["title"],
            "score": score
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    best_score = results[0]["score"]

    if best_score < THRESHOLD:
        return []

    return results[:top_k]