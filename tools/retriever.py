from tools.embeddings import create_embedding
from tools.similarity import cosine_similarity
from tools.vector_store import load_vectors


def retrieve_chunks(
    question: str,
    top_k: int = 1,
    min_score: float = 0.5,
) -> list[tuple[str, float]]:
    question_vector = create_embedding(question)

    vectors = load_vectors()

    scored_chunks = []

    for item in vectors:
        score = cosine_similarity(
            question_vector,
            item["embedding"],
        )

        if score >= min_score:
            scored_chunks.append(
                (item["text"], score)
            )

    scored_chunks.sort(
        key=lambda item: item[1],
        reverse=True,
    )

    return scored_chunks[:top_k]