from datetime import datetime, date
from fastapi import APIRouter, Depends, HTTPException
from pony.orm import db_session
from env import get_token_header
from db.connection import Game, Sale
from models.pydanticSchemes import GameBase

router = APIRouter(dependencies=[Depends(get_token_header)],
                   responses={404: {"description": "Not found"}}, )


@router.post("/games", response_model=GameBase)
async def create_game(game: GameBase):
    genres = ",".join(game.categories)
    with db_session:
        Game(add_date=datetime.now(), edit_date=datetime.now(), title=game.name, price=game.price,
             categories=genres)
    return game


@router.put("/games", response_model=GameBase)
async def update_game(gid: int, game: GameBase):
    genres = ",".join(game.categories)
    with db_session:
        data = Game[gid]
        if game.name is not None:
            data.title = game.name
        if game.price is not None:
            data.price = game.price
        if game.categories is not None:
            data.categories = genres
        data.edit_date = datetime.now()

    return game


@router.delete("/games")
async def delete_game(gid: int):
    with db_session:
        data = Game[gid]
        data.delete()


@router.get("/list")
async def get_salelist(start_date: date, end_date: date):
    lst = []
    with db_session:
        for data in Sale.select(lambda p: p.date >= start_date and p.date <= end_date):
            sale = {"id": data.id, "date": data.date, "price": data.s_price, "card": data.user_card}
            lst.append(sale)
    return lst


@router.get("/stats")
async def get_salestats(start_date: date, end_date: date):
    with db_session:
        query = Sale.select(lambda p: p.date >= start_date and p.date <= end_date)
        total_sales = query.count()
        sum_of_sales = sum(s.s_price for s in query)

    return {"total": total_sales, "sum": sum_of_sales}


# sum(s.gpa for s in Student if s.group.number == 101)

"""
@db_session
def add_examples():
    g1 = Game(add_date='2022-11-10 22:41:51', edit_date='2022-11-10 22:41:51', title='UFC4', price=19.99, categories='Action')
    g2 = Game(add_date='2022-11-10 22:41:51', edit_date='2022-11-10 22:41:51', title='GTA5', price=15.99, categories='Action')
    g3 = Game(add_date='2022-11-10 22:41:51', edit_date='2022-11-10 22:41:51', title='DOTA2', price=9.99, categories='Strategy')
    
add_examples()
"""
