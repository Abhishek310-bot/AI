from pgvector import Vector

from app.embeddings.embedding import EmbeddingModel
from app.vector_store.pgvector import get_vector_connection


def test_vector_query():

    embedding_model = EmbeddingModel()

    query = "How can I get my money back?"

    query_embedding = embedding_model.generate(query)
    #Tells the pgvector this is vector data
    query_vector = Vector(query_embedding)

    with get_vector_connection() as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    content,
                    embedding <=> %s AS distance
                FROM document_chunks
                ORDER BY embedding <=> %s
                LIMIT 3
                """,
                (
                    query_vector,
                    query_vector
                )
            )

            results = cursor.fetchall()

    for content, distance in results:
        print()
        print("Distance:", distance)
        print("Content:", content)

    assert len(results) > 0