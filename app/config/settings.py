import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "word2vec")
    SIMILARITY_METRIC: str = os.getenv("SIMILARITY_METRIC", "cosine")
