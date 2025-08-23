# src/retriever.py
import os
import faiss
import pickle
import numpy as np
import google.generativeai as genai
from src import config


genai.configure(api_key=config.GEMINI_API_KEY)

# Paths
VECTOR_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "vectorstore")
INDEX_PATH = os.path.join(VECTOR_DIR, "kb.index")
DOCS_PATH = os.path.join(VECTOR_DIR, "docs.pkl")

# Load FAISS index
index = faiss.read_index(INDEX_PATH)

# Load metadata (docs)
with open(DOCS_PATH, "rb") as f:
    metadata = pickle.load(f)

def embed_query(query: str) -> np.ndarray:
    """Embed query into same vector space as docs."""
    result = genai.embed_content(
        model=config.EMBED_MODEL,  # use value from config.py
        content=query
    )
    return np.array(result["embedding"], dtype="float32")

def retrieve(query: str, k: int = 5):
    """Return top-k most relevant documents for a query."""
    query_vector = embed_query(query).reshape(1, -1)
    distances, indices = index.search(query_vector, k)

    results = []
    for i, idx in enumerate(indices[0]):
        if idx < len(metadata):
            results.append({
                "rank": i + 1,
                "score": float(distances[0][i]),
                "content": metadata[idx]
            })
    return results

if __name__ == "__main__":
    q = "What is the claims process?"
    results = retrieve(q)
    for r in results:
        print(f"[Rank {r['rank']}] Score: {r['score']:.4f}\n{r['content']}\n")

