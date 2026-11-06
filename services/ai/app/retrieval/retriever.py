from app.retrieval.semantic_search import SemanticSearch


class Retriever:

    def __init__(
        self,
        documents: list[str]
    ):

        self.search_engine = SemanticSearch(
            documents
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ):

        return self.search_engine.search(
            query,
            top_k
        )