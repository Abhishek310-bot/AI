from uuid import UUID

from app.vector_store.pgvector import get_vector_connection


class VectorRepository:

    def insert_chunk(
        self,
        chunk_id: UUID,
        document_id: UUID,
        chunk_index: int,
        content: str,
        embedding: list[float]
    ):

        with get_vector_connection() as connection:

            with connection.cursor() as cursor:

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
                        chunk_id,
                        document_id,
                        chunk_index,
                        content,
                        embedding
                    )
                )

            connection.commit()