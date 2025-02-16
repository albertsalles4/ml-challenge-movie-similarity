from fastapi import APIRouter, Depends

from app.api.schemas import SearchRequest
from app.dependencies.dependencies import get_movie_service

router = APIRouter()


@router.post("/search")
def search_endpoint(body: SearchRequest, movie_service=Depends(get_movie_service)):
    results = movie_service.find_similar_movies(body.query, body.top_n)
    return results
