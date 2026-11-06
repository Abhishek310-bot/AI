from uuid import uuid4

from app.embeddings.embedding import EmbeddingModel
from app.vector_store.pgvector import get_vector_connection


def test_vector_search():

    embedding_model = EmbeddingModel()

    documents = [
        "Customers can request a full refund within 30 days.",
        "Standard shipping usually takes 5 to 7 business days.",
        "All electronic products include a one year warranty."
    ]

    document_id = uuid4()

    with get_vector_connection() as connection:

        with connection.cursor() as cursor:

            for index, text in enumerate(documents):

                embedding = embedding_model.generate(text)

                cursor.execute(
                    """
                    INSERT INTO document_chunks
                    (
                        id,
                        document_id,
                        chunk_index,
                        content,
                        embedding
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        uuid4(),
                        document_id,
                        index,
                        text,
                        embedding
                    )
                )

        connection.commit()

    print("Inserted", len(documents), "documents")