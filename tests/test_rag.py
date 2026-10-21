import tools.vector_store as vector_store


def test_save_and_load_vectors(tmp_path):
    test_file = tmp_path / "vectors.json"

    vector_store.VECTOR_STORE = test_file

    vectors = [
        {
            "text": "Refunds take 5 business days.",
            "embedding": [0.1, 0.2, 0.3],
        }
    ]

    vector_store.save_vectors(vectors)

    loaded = vector_store.load_vectors()

    assert loaded == vectors

def test_load_vectors_when_file_does_not_exist(tmp_path):
    vector_store.VECTOR_STORE = tmp_path / "missing.json"

    assert vector_store.load_vectors() == []