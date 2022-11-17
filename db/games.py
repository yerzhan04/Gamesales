from datetime import datetime
from fastapi import HTTPException

from db.connection import Game, db_session


def create_game(name, price, genre):
    with db_session:
        if not Game.select().exists():
            raise HTTPException(status_code=404, detail="Table not found")
        Game(add_date=datetime.now(), edit_date=datetime.now(), title=name, price=price,
             categories=genre)
    return HTTPException(status_code=201, detail="Game created")


def update_game(gid: int, name: None, price: None, genre: None):
    with db_session:
        if not Game.select().exists():
            raise HTTPException(status_code=404, detail="Table not found")
        count = 0
        for row in Game.select():
            if row.id == gid:
                count += 1
        if count == 0:
            raise HTTPException(status_code=404, detail="Game not found")
        data = Game[gid]
        if data.title is not None:
            data.title = name
        if data.price is not None:
            data.price = price
        if data.categories is not None:
            data.categories = genre
        data.edit_date = datetime.now()
        return HTTPException(status_code=200, detail="Game updated")


def get_by_id(gid):
    with db_session:
        if not Game.select().exists():
            raise HTTPException(status_code=404, detail="Table not found")
        count = 0
        for row in Game.select():
            if row.id == gid:
                count += 1
        if count == 0:
            raise HTTPException(status_code=404, detail="Game not found")
        data = Game[gid]
        return {"id": data.id, "name": data.title, "price": data.price, "categories": data.categories.split(',')}


def del_by_id(gid):
    with db_session:
        if not Game.select().exists():
            raise HTTPException(status_code=404, detail="Table not found")
        count = 0
        for row in Game.select():
            if row.id == gid:
                count += 1
        if count == 0:
            raise HTTPException(status_code=404, detail="Game not found")
        data = Game[gid]
        data.delete()
        return HTTPException(status_code=204, detail="Game deleted")


def get_games(start, end):
    lst = []
    with db_session:
        if not Game.select().exists():
            raise HTTPException(status_code=404, detail="Table not found")
        for data in Game.select():
            game = {"id": data.id, "name": data.title, "price": data.price, "categories": data.categories.split(',')}
            lst.append(game)
    if len(lst) == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return lst[start:start + end]


def search_game(name, genre, minp, maxp):
    lst = []
    with db_session:
        if not Game.select().exists():
            raise HTTPException(status_code=404, detail="Table not found")
        if name is not None:
            for data in Game.select(lambda p: p.title.lower() == name.lower()):
                game = {"id": data.id, "name": data.title, "price": data.price,
                        "categories": data.categories.split(',')}
                lst.append(game)

        if genre is not None:
            for data in Game.select(lambda p: genre.lower() in p.categories.lower()):
                game = {"id": data.id, "name": data.title, "price": data.price,
                        "categories": data.categories.split(',')}
                lst.append(game)

        if maxp is not None:
            for data in Game.select(lambda p: p.price <= maxp):
                game = {"id": data.id, "name": data.title, "price": data.price,
                        "categories": data.categories.split(',')}
                lst.append(game)

        if minp is not None:
            for data in Game.select(lambda p: p.price >= minp):
                game = {"id": data.id, "name": data.title, "price": data.price,
                        "categories": data.categories.split(',')}
                lst.append(game)

    if len(lst) == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return lst
