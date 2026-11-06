from app.tokenization.tokenizer import Tokenizer


def test_tokenization():

    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize(
        "How can I get a refund?"
    )

    assert len(tokens) > 0

    print(tokens)