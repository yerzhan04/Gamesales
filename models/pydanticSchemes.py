from typing import List

from pydantic import BaseModel


class GameBase(BaseModel):
    name: str
    price: float
    categories: str


class Transaction(BaseModel):
    exp: str
    card: str
