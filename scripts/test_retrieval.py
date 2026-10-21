import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from tools.document_loader import load_document
from tools.chunker import chunk_text
from tools.retriever import retrieve_chunks


document = load_document("documents/company_policy.txt")
chunks = chunk_text(document, 30)

question = "How long does a refund take?"

results = retrieve_chunks(
    question,
    top_k=2,
)

print(f"Question: {question}")
print()

for i, (chunk, score) in enumerate(results, start=1):
    print(f"RESULT {i}")
    print(f"Similarity: {score:.4f}")
    print(f"Text: {chunk}")
    print()