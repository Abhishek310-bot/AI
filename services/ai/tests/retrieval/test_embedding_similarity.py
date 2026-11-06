from app.embeddings.embedding import EmbeddingModel
from app.retrieval.similarity import cosine_similarity


def test_embedding_similarity():

    model = EmbeddingModel()

    a = model.generate(
        "How can I get a refund?"
    )

    b = model.generate(
        "How can I get my money back?"
    )

    similarity = cosine_similarity(a, b)

    print("Similarity:", similarity)

    assert similarity > 0.5