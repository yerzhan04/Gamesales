from datetime import datetime

from fastapi import APIRouter
from pony.orm import db_session

from db.connection import Game, Sale
from models.pydanticSchemes import Transaction

router = APIRouter()


@router.get("/games")
async def get_all_games():
    lst = []
    with db_session:
        for data in Game.select():
            game = {"id": data.id, "name": data.title, "price": data.price, "categories": data.categories}
            lst.append(game)
    return lst


@router.get('/games/{gid}')
async def get_single_game(gid: int):
    with db_session:
        data = Game[gid]

    return {"id": data.id, "name": data.title, "price": data.price, "categories": data.categories}


@router.get('/games/search')
async def search_game(name: str = None, genre: str = None, minp: int = None, maxp: int = None):
    lst=[]
    with db_session:
        for data in Game.select(lambda p: p.price >= minp and p.price <= maxp):
            game = {"id": data.id, "name": data.title, "price": data.price, "categories": data.categories}
            lst.append(game)
    return lst


@router.post('/games/transaction', response_model=Transaction)
async def buy_game(gid: int, sale: Transaction):
    with db_session:
        game = Game[gid]
        Sale(date=datetime.now(), game=game.id, s_price=game.price * 1.05, user_card=sale.card)
    return sale


"""
s1 = Sale(date='2022-11-10 22:41:51', game=g1, s_price=g1.price*1.05,  user_card='1234567891011130')
s2 = Sale(date='2022-11-10 22:41:51', game=g2, s_price=g2.price*1.05, user_card='1234567892011130')
s3 = Sale(date='2022-11-10 22:41:51', game=g3, s_price=g3.price*1.05, user_card='1234567893031130')
"""
