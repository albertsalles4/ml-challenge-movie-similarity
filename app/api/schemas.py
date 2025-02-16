import datetime
from typing import Optional

from pydantic import BaseModel


class MovieFilter(BaseModel):
    min_release_date: Optional[datetime.date] = None
    min_vote_average: Optional[float] = None
    min_vote_count: Optional[int] = None


class SearchRequest(BaseModel):
    query: str
    top_n: Optional[int] = 5
    filters: Optional[MovieFilter] = None
