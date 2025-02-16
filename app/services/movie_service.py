from app.api.schemas import MovieFilter
from app.model.embeddings.base_embedding import BaseEmbeddingModel
from app.model.similarity.base_similarity import BaseSimilarityMetric
from app.repository.movie_repository import get_movies_dataset


class MovieService:
    """Implements the business logic for movies"""

    def __init__(self, embedding_model: BaseEmbeddingModel, similarity_metric: BaseSimilarityMetric):
        self.embedding_model = embedding_model
        self.similarity_metric = similarity_metric
        self.movies_df = get_movies_dataset(self.embedding_model)

    def find_similar_movies(self, query: str, top_n: int = 5, filters: MovieFilter = None):
        """Find the most similar movies to a given query."""
        query_embedding = self.embedding_model.encode_text(query)
        movies_df = self._filter_movies(filters)
        movies_df["similarity"] = movies_df["embedding"].apply(
            lambda emb: self.similarity_metric.compute_similarity(query_embedding, emb)
        )
        results = movies_df.sort_values(by="similarity", ascending=False).head(top_n)
        return (results[["title", "overview", "release_date", "popularity", "vote_average", "vote_count", "similarity"]]
                .to_dict(orient="records"))

    def _filter_movies(self, filters: MovieFilter = None):
        """Filters the movies based on the given filters."""
        if filters is None:
            return self.movies_df

        movies_df = self.movies_df.copy()
        if filters.min_release_date is not None:
            movies_df = movies_df[movies_df["release_date"].dt.date >= filters.min_release_date]

        if filters.min_vote_average is not None:
            movies_df = movies_df[movies_df["vote_average"] >= filters.min_vote_average]

        if filters.min_vote_count is not None:
            movies_df = movies_df[movies_df["vote_count"] >= filters.min_vote_count]

        return movies_df
