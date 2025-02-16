from fastapi import Depends

from app.model.embeddings.base_embedding import BaseEmbeddingModel
from app.model.similarity.base_similarity import BaseSimilarityMetric
from app.services.movie_service import MovieService


def get_embedding_model() -> BaseEmbeddingModel:
    """Returns the embedding model"""
    return None


def get_similarity_service() -> BaseSimilarityMetric:
    """Returns the similarity metric"""
    return None


def get_movie_service(embedding_model=Depends(get_embedding_model),
                      similarity_metric=Depends(get_similarity_service)) -> MovieService:
    """Returns the movie service"""
    return MovieService(embedding_model, similarity_metric)
