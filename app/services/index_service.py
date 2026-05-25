import json
from app.services.embedding_service import generate_embedding
from app.vectorstore.store import vector_db

def load_documents():

    with open("docs.json", "r") as f:
        docs = json.load(f)

    for idx, doc in enumerate(docs):

        embedding = generate_embedding(doc["content"])

        vector_db.append({
            "id": idx,
            "title": doc["title"],
            "text": doc["content"],
            "embedding": embedding
        })

    print("Documents indexed successfully")