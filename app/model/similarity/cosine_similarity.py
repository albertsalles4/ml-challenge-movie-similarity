import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from app.model.similarity.base_similarity import BaseSimilarityMetric


class CosineSimilarity(BaseSimilarityMetric):
    """Computes cosine similarity between two embeddings."""

    def compute_similarity(self, emb1: np.ndarray, emb2: np.ndarray) -> float:
        return cosine_similarity([emb1], [emb2])[0][0]
