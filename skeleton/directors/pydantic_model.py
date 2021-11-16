from pydantic import BaseModel


class DirectorRequestModel(BaseModel):
    name: str
    gender: int
    uid: int
    department: str
