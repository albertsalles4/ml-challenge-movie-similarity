from abc import ABC, abstractmethod

import numpy as np


class BaseSimilarityMetric(ABC):
    """Abstract base class for similarity computation strategies."""

    @abstractmethod
    def compute_similarity(self, emb1: np.ndarray, emb2: np.ndarray) -> float:
        """Computes similarity between two vectors."""
        pass
