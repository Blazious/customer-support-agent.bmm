# src/ingest.py
import os
import faiss
import pickle
import numpy as np  # <-- missing import
import google.generativeai as genai

from src import config

# Configure Gemini client
genai.configure(api_key=config.GEMINI_API_KEY)

# Initialize embeddings client
embedding = genai.embed_content  # alias for convenience

def load_kb():
    with open(config.KB_PATH, "r", encoding="utf-8") as f:
        return f.read().split("\n\n")  # split paragraphs

def embed_texts(texts):
    # Calls Gemini embeddings API for each chunk
    return [genai.embed_content(model=config.EMBED_MODEL, content=t)["embedding"] for t in texts]

def build_index():
    docs = load_kb()
    vectors = embed_texts(docs)

    dim = len(vectors[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors).astype("float32"))

    os.makedirs(config.INDEX_DIR, exist_ok=True)
    faiss.write_index(index, os.path.join(config.INDEX_DIR, "kb.index"))

    with open(os.path.join(config.INDEX_DIR, "docs.pkl"), "wb") as f:
        pickle.dump(docs, f)

    print(f"✅ Indexed {len(docs)} chunks from KB")

if __name__ == "__main__":
    build_index()
