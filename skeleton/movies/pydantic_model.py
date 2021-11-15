from pydantic import BaseModel


class MovieRequestModel(BaseModel):
    original_title: str
    budget: int
    popularity: int
    release_date: str
    revenue: int
    title: str
    vote_average: float
    vote_count: int
    overview: str
    tagline: str
    uid: int
    director_id: int
