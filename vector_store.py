# src/vector_store.py
import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.chunks = []

    def add(self, vectors, chunks):
        self.index.add(vectors.astype('float32'))
        self.chunks.extend(chunks)

    def search(self, query_vector, top_k=3):
        distances, indices = self.index.search(query_vector.astype('float32'), top_k)
        results = [self.chunks[i] for i in indices[0]]
        return results
