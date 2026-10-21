from google import genai

from config import GEMINI_API_KEY
from config import MODEL_NAME
from tools.retriever import retrieve_chunks


client = genai.Client(api_key=GEMINI_API_KEY)


def search_knowledge_base(question: str, top_k: int = 2) -> str:
    results = retrieve_chunks(
        question,
        top_k=top_k,
    )

    if not results:
        return "I don't have enough information in the provided documents."

    return "\n\n".join(
        chunk
        for chunk, score in results
    )

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

If the answer cannot be found in the context, say:
"I don't have enough information in the provided documents."
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text