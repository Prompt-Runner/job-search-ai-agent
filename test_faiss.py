from App.services.parser_service import extract_text
from App.utils.chunking import create_chunks
from App.services.embedding_service import generate_embeddings
from App.database.faiss_db import save_to_faiss

file_path = "Assets/resumes/Pranavi_Datta_Kasbe.pdf"

text = extract_text(file_path)

chunks = create_chunks(text)

embeddings = generate_embeddings(chunks)

save_to_faiss(embeddings, chunks)

print("Database Created Successfully")