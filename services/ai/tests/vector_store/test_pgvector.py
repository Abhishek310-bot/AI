from uuid import uuid4

from app.embeddings.embedding import EmbeddingModel
from app.vector_store.repository import VectorRepository


def test_insert_embedding():

    embedding_model = EmbeddingModel()
    repository = VectorRepository()

    text = (
        "Customers can request a full refund "
        "within 30 days."
    )

    embedding = embedding_model.generate(text)

    repository.insert_chunk(
        chunk_id=uuid4(),
        document_id=uuid4(),
        chunk_index=0,
        content=text,
        embedding=embedding
    )

    print("Inserted vector dimension:", len(embedding))

    assert len(embedding) == 384