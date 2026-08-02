from App.services.parser_service import extract_text
from App.utils.chunking import create_chunks

# Replace with your resume filename
file_path = "Assets/resumes/Pranavi_Datta_Kasbe.pdf"

text = extract_text(file_path)

chunks = create_chunks(text)

print("=" * 60)
print(f"Total Chunks: {len(chunks)}")
print("=" * 60)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print("-" * 60)
    print(chunk)