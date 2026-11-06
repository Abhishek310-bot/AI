from app.retrieval.similarity import cosine_similarity


def test_cosine_similarity():

    a = [1, 0, 0]
    b = [1, 0, 0]
    c = [0, 1, 0]

    print("A vs B:", cosine_similarity(a, b))
    print("A vs C:", cosine_similarity(a, c))

    assert cosine_similarity(a, b) == 1
    assert cosine_similarity(a, c) == 0