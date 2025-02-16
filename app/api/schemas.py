from typing import Optional

from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str
    top_n: Optional[int] = 5
