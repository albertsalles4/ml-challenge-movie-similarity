import gensim.downloader as api
import nltk
import numpy as np
from nltk.tokenize import word_tokenize

from app.model.embeddings.base_embedding import BaseEmbeddingModel

# Download necessary resources
nltk.download('punkt')
nltk.download('punkt_tab')


class Word2VecEmbedding(BaseEmbeddingModel):
    """Implements the word2vec embedding model."""

    def __init__(self, model_name: str = "word2vec-google-news-300"):
        self.word_vectors = api.load(model_name)

    def encode_text(self, text: str) -> np.ndarray:
        """
        Encodes a text into a vector using the word2vec model.
        Computes the average of the word vectors in the text.
        """
        tokens = word_tokenize(text.lower())
        word_vecs = [self.word_vectors[word] for word in tokens if word in self.word_vectors]

        if not word_vecs:
            return np.zeros(self.word_vectors.vector_size)

        return np.mean(word_vecs, axis=0)
