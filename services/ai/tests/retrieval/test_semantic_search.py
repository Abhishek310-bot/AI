from app.retrieval.semantic_search import SemanticSearch


def test_semantic_search():

    documents = [
        "Customers can request a full refund within 30 days.",
        "Standard shipping takes 5 to 7 business days.",
        "Electronic products include a one year warranty."
    ]

    search = SemanticSearch(documents)

    results = search.search(
        "How long does delivery take?",
        top_k=3
    )

    for result in results:
        print()
        print("Score:", result["score"])
        print("Text:", result["text"])

    assert len(results) == 3