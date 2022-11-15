from pydantic import BaseModel
from datetime import datetime


class GameBase(BaseModel):
    name: str
    price: float
    categories: str

    class Config:
        orm_mode = True


class Transaction(BaseModel):
    exp: str
    card: str
    date: datetime

    class Config:
        orm_mode = True
