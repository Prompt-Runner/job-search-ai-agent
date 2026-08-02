from App.services.retrieval_service import retrieve_context

query = "What programming languages do I know?"

results = retrieve_context(query)

print("=" * 60)

for i, chunk in enumerate(results, start=1):
    print(f"\nChunk {i}")
    print("-" * 60)
    print(chunk)