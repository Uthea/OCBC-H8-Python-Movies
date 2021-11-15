from pydantic import BaseModel


class RequestBodyModel(BaseModel):
    title: str
    author: str



