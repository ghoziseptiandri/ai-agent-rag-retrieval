import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from tools.document_loader import load_document
from tools.chunker import chunk_text
from tools.embeddings import create_embedding


document = load_document("documents/company_policy.txt")
chunks = chunk_text(document, 30)

for i, chunk in enumerate(chunks, start=1):
    vector = create_embedding(chunk)

    print(f"CHUNK {i}")
    print(f"Text: {chunk}")
    print(f"Vector dimensions: {len(vector)}")
    print(f"First 5 values: {vector[:5]}")
    print()