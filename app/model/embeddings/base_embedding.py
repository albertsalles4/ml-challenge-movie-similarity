from abc import ABC, abstractmethod

import numpy as np


class BaseEmbeddingModel(ABC):
    """Base class for embeddings"""

    @abstractmethod
    def encode_text(self, text) -> np.ndarray:
        """Encodes a text into a vector"""
        pass
