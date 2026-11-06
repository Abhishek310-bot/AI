from transformers import AutoTokenizer

from app.config.settings import settings


class Tokenizer:

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            settings.EMBEDDING_MODEL
        )

    def tokenize(self, text: str):
        return self.tokenizer.tokenize(text)

    def encode(self, text: str):
        return self.tokenizer.encode(text)

    def encode_with_attention_mask(self, text: str):
        return self.tokenizer(
            text,
            return_tensors="pt"
        )