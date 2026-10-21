import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from tools.document_loader import load_document
from tools.chunker import chunk_text
from tools.embeddings import create_embedding
from tools.vector_store import save_vectors


document = load_document("documents/company_policy.txt")
chunks = chunk_text(document, 30)

vectors = []

for chunk in chunks:
    embedding = create_embedding(chunk)

    vectors.append({
        "text": chunk,
        "embedding": embedding,
    })

save_vectors(vectors)

print(f"Indexed {len(vectors)} chunks.")