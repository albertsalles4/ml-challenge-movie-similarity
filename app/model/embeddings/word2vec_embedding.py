import gensim.downloader as api
import nltk
import numpy as np
from nltk.tokenize import word_tokenize

from app.model.embeddings.base_embedding import BaseEmbeddingModel

# Download necessary resources
nltk.download('punkt')
nltk.download('punkt_tab')


class Word2VecEmbedding(BaseEmbeddingModel):
    """Word2Vec embedding model"""

    _instance = None
    _model = None

    def __new__(cls):
        """Singleton-based pattern to prevent reloading at every request."""
        if cls._instance is None:
            cls._instance = super(Word2VecEmbedding, cls).__new__(cls)
            cls._model = api.load("word2vec-google-news-300")
        return cls._instance

    def encode_text(self, text: str) -> np.ndarray:
        """
        Encodes a text into a vector using the word2vec model.
        Computes the average of the word vectors in the text.
        """
        tokens = word_tokenize(text.lower())
        word_vecs = [self._model[word] for word in tokens if word in self._model]

        if not word_vecs:
            return np.zeros(self._model.vector_size)

        return np.mean(word_vecs, axis=0)
