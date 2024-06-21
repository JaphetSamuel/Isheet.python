# Models
from pydantic import BaseModel


class User(BaseModel):
    """    Class   User   """
    username: str
    email: str
    password: str


class Token(BaseModel):
    """Toke"""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """TokenData"""
    username: str | None = None


class Client(BaseModel):
    """Client"""
    name: str
