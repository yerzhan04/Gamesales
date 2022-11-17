from fastapi import APIRouter

from db import games, sales
from models.pydanticSchemes import Transaction

router = APIRouter()


@router.get("/games")
async def get_all_games(start: int, end: int):
    return games.get_games(start, end)


@router.get('/games/search')
async def search_game(name: str = None, genre: str = None, minp: int = None, maxp: int = None):
    return games.search_game(name, genre, minp, maxp)


@router.get('/games/{gid}')
async def get_single_game(gid: int):
    return games.get_by_id(gid)


@router.post('/games/transaction', response_model=Transaction)
async def buy_game(sale: Transaction):
    sales.buy_game(sale.id, sale.card)
    return sale


"""
s1 = Sale(date='2022-11-10 22:41:51', game=g1, s_price=g1.price*1.05,  user_card='1234567891011130')
s2 = Sale(date='2022-11-10 22:41:51', game=g2, s_price=g2.price*1.05, user_card='1234567892011130')
s3 = Sale(date='2022-11-10 22:41:51', game=g3, s_price=g3.price*1.05, user_card='1234567893031130')
"""
