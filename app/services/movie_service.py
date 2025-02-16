from app.model.embeddings.base_embedding import BaseEmbeddingModel
from app.model.similarity.base_similarity import BaseSimilarityMetric
from app.repository.movie_repository import get_movies_dataset


class MovieService:
    """Implements the business logic for movies"""

    def __init__(self, embedding_model: BaseEmbeddingModel, similarity_metric: BaseSimilarityMetric):
        self.embedding_model = embedding_model
        self.similarity_metric = similarity_metric
        self.movies_df = get_movies_dataset(self.embedding_model)

    def find_similar_movies(self, query: str, top_n: int = 5):
        """Find the most similar movies to a given query."""
        query_embedding = self.embedding_model.encode_text(query)
        self.movies_df["similarity"] = self.movies_df["embedding"].apply(
            lambda emb: self.similarity_metric.compute_similarity(query_embedding, emb)
        )
        results = self.movies_df.sort_values(by="similarity", ascending=False).head(top_n)
        return (results[["title", "overview", "release_date", "popularity", "vote_average", "vote_count", "similarity"]]
                .to_dict(orient="records"))
