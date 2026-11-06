from app.embeddings.embedding import EmbeddingModel
from app.retrieval.similarity import cosine_similarity


class SemanticSearch:

    def __init__(
        self,
        documents: list[str]
    ):

        self.embedding_model = EmbeddingModel()

        self.documents = documents

        self.embeddings = (
            self.embedding_model.generate_batch(
                documents
            )
        )

    def search(
        self,
        query: str,
        top_k: int = 3
    ):

        query_embedding = (
            self.embedding_model.generate(query)
        )

        results = []

        for document, embedding in zip(
            self.documents,
            self.embeddings
        ):

            score = cosine_similarity(
                query_embedding,
                embedding
            )

            results.append({
                "text": document,
                "score": score
            })

        results.sort(
            key=lambda result: result["score"],
            reverse=True
        )

        return results[:top_k]