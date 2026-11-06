from app.embeddings.embedding import EmbeddingModel


def test_embedding():

    model = EmbeddingModel()

    embedding = model.generate(
        "How can I get a refund?"
    )

    print("Dimension:", len(embedding))
    print("First 10 values:", embedding[:10])

    assert len(embedding) == 384