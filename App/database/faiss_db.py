import faiss
import numpy as np
import pickle
import os

VECTOR_DB_PATH = "Assets/vector_db"

os.makedirs(VECTOR_DB_PATH, exist_ok=True)


def save_to_faiss(embeddings, chunks):

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(index, f"{VECTOR_DB_PATH}/index.faiss")

    with open(f"{VECTOR_DB_PATH}/metadata.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("FAISS database saved successfully.")


def load_faiss():

    index = faiss.read_index(f"{VECTOR_DB_PATH}/index.faiss")

    with open(f"{VECTOR_DB_PATH}/metadata.pkl", "rb") as f:
        chunks = pickle.load(f)

    return index, chunks