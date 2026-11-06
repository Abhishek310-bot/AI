from sentence_transformers import SentenceTransformer

from app.config.settings import settings


class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )

    def generate(self, text: str) -> list[float]:
        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding.tolist()

    def generate_batch(
        self,
        texts: list[str]
    ) -> list[list[float]]:

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings.tolist()

    def dimension(self) -> int:
        return self.model.get_sentence_embedding_dimension()