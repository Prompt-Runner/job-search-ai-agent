from App.database.faiss_db import load_faiss
from App.services.embedding_service import generate_embeddings
import numpy as np


def retrieve_context(query, top_k=3):
    """
    Retrieve the most relevant resume chunks for a query.
    """

    # Load FAISS index and stored chunks
    index, chunks = load_faiss()

    # Generate embedding for the query
    query_embedding = generate_embeddings([query])[0]

    # Convert to NumPy float32 array
    query_embedding = np.array([query_embedding]).astype("float32")

    # Search FAISS
    distances, indices = index.search(query_embedding, top_k)

    # Get matching chunks
    retrieved_chunks = []

    for idx in indices[0]:
        if 0 <= idx < len(chunks):
            retrieved_chunks.append(chunks[idx])

    return retrieved_chunks