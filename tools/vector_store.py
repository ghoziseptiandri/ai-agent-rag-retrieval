import json
from pathlib import Path


VECTOR_STORE = Path("data/vectors.json")


def save_vectors(vectors: list[dict]) -> None:
    VECTOR_STORE.parent.mkdir(parents=True, exist_ok=True)

    with open(VECTOR_STORE, "w", encoding="utf-8") as file:
        json.dump(vectors, file)


def load_vectors() -> list[dict]:
    if not VECTOR_STORE.exists():
        return []

    with open(VECTOR_STORE, "r", encoding="utf-8") as file:
        return json.load(file)