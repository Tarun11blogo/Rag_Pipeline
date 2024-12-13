import faiss
import numpy as np

def setup_faiss(documents, embed_func):
    embeddings = [embed_func(doc) for doc in documents]
    dimension = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

def retrieve_context(query, index, documents, embed_func, top_k=2):
    query_vector = embed_func(query).reshape(1, -1)
    distances, indices = index.search(query_vector, top_k)
    retrieved_docs = [documents[i] for i in indices[0]]
    return " ".join(retrieved_docs)
