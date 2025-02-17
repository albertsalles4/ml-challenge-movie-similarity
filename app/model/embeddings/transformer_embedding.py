import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel

from app.model.embeddings.base_embedding import BaseEmbeddingModel


class TransformerEmbedding(BaseEmbeddingModel):
    """Bert Embedding Model"""

    _instance = None
    _tokenizer = None
    _model = None

    def __new__(cls):
        """Singleton-based pattern to prevent reloading at every request."""
        if cls._instance is None:
            cls._instance = super(TransformerEmbedding, cls).__new__(cls)
            cls._tokenizer = AutoTokenizer.from_pretrained("microsoft/MiniLM-L12-H384-uncased")
            cls._model = AutoModel.from_pretrained("microsoft/MiniLM-L12-H384-uncased")
        return cls._instance

    def encode_text(self, text: str) -> np.ndarray:
        """Encodes a text into a vector using a tranformer-based model."""
        inputs = self._tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

        with torch.no_grad():
            outputs = self._model(**inputs)

        embeddings = outputs.last_hidden_state  # Shape: (batch_size, sequence_length, hidden_size)

        # Pooling: Take the [CLS] token representation (first token)
        sentence_embedding = embeddings[:, 0, :].squeeze()  # Shape: (hidden_size, )

        return sentence_embedding.numpy()
