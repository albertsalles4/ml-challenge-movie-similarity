import pandas as pd

from app.model.embeddings.base_embedding import BaseEmbeddingModel


def get_movies_dataset(embedding_model: BaseEmbeddingModel) -> pd.DataFrame:
    """Loads the dataset from the movies.csv file"""
    df = pd.read_csv("app/repository/dataset/movies.csv", index_col=0)
    df["release_date"] = pd.to_datetime(df["release_date"], format="%Y-%m-%d")
    df["embedding"] = df["overview"].apply(lambda x: embedding_model.encode_text(str(x)))
    return df
