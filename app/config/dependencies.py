from fastapi import Depends
from pydantic_settings import BaseSettings

from app.config.settings import Settings
from app.model.embeddings.base_embedding import BaseEmbeddingModel
from app.model.embeddings.transformer_embedding import TransformerEmbedding
from app.model.embeddings.word2vec_embedding import Word2VecEmbedding
from app.model.similarity.base_similarity import BaseSimilarityMetric
from app.model.similarity.cosine_similarity import CosineSimilarity
from app.services.movie_service import MovieService


def get_settings() -> BaseSettings:
    return Settings()


def get_embedding_model(app_settings=Depends(get_settings)) -> BaseEmbeddingModel:
    """Returns the embedding model"""
    if app_settings.EMBEDDING_MODEL == "word2vec":
        return Word2VecEmbedding()

    if app_settings.EMBEDDING_MODEL == "transformer":
        return TransformerEmbedding()

    return Word2VecEmbedding()


def get_similarity_service(app_settings=Depends(get_settings)) -> BaseSimilarityMetric:
    """Returns the similarity metric"""
    if app_settings.SIMILARITY_METRIC == "cosine":
        return CosineSimilarity()
    return CosineSimilarity()


def get_movie_service(embedding_model=Depends(get_embedding_model),
                      similarity_metric=Depends(get_similarity_service)) -> MovieService:
    """Returns the movie service"""
    return MovieService(embedding_model, similarity_metric)
