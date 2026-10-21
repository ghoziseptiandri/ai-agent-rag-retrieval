from tools.similarity import cosine_similarity


def test_identical_vectors():
    vector_a = [1, 0, 0]
    vector_b = [1, 0, 0]

    assert cosine_similarity(vector_a, vector_b) == 1.0


def test_perpendicular_vectors():
    vector_a = [1, 0, 0]
    vector_b = [0, 1, 0]

    assert cosine_similarity(vector_a, vector_b) == 0.0