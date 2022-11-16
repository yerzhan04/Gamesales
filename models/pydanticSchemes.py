from typing import List

from pydantic import BaseModel, Field


class GameBase(BaseModel):
    name: str = Field(..., max_length=150)
    price: float
    categories: List[str]


class Transaction(BaseModel):
    id: int
    exp: str
    card: str = Field(..., min_length=16, max_length=16)
    cvv: str = Field(..., min_length=3, max_length=3)