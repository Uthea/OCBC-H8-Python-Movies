from pydantic import BaseModel, EmailStr, constr


class LoginBodyModel(BaseModel):
    email: EmailStr
    password: str


class RegisterBodyModel(BaseModel):
    email: EmailStr
    username: str
    password: constr(min_length=6)


class RefreshBodyModel(BaseModel):
    access_token: str
    refresh_token: str
