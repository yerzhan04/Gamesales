from datetime import datetime

from db.connection import Game, db_session


def create_game(name, price, genre):
    with db_session:
        Game(add_date=datetime.now(), edit_date=datetime.now(), title=name, price=price,
             categories=genre)


def update_game(gid: int, name: None, price: None, genre: None):
    with db_session:
        data = Game[gid]
        if data.title is not None:
            data.title = name
        if data.price is not None:
            data.price = price
        if data.categories is not None:
            data.categories = genre
        data.edit_date = datetime.now()


def get_by_id(gid):
    with db_session:
        data = Game[gid]

    return {"id": data.id, "name": data.title, "price": data.price, "categories": data.categories.split(',')}


def del_by_id(gid):
    with db_session:
        data = Game[gid]
        data.delete()


def get_games(start, end):
    lst = []
    with db_session:
        for data in Game.select():
            game = {"id": data.id, "name": data.title, "price": data.price, "categories": data.categories.split(',')}
            lst.append(game)
    return lst[start:start + end]


def search_game(name, genre, minp, maxp):
    lst = []
    with db_session:
        if maxp is not None and minp is not None:
            for data in Game.select(lambda p: p.price >= minp and p.price <= maxp):
                game = {"id": data.id, "name": data.title, "price": data.price,
                        "categories": data.categories.split(',')}
                lst.append(game)
        if name is not None:
            for data in Game.select(lambda p: p.title.lower() == name.lower()):
                game = {"id": data.id, "name": data.title, "price": data.price,
                        "categories": data.categories.split(',')}
                lst.append(game)
        if genre is not None:
            for data in Game.select(lambda p: p.categories.lower() == genre.lower()):
                game = {"id": data.id, "name": data.title, "price": data.price,
                        "categories": data.categories.split(',')}
                lst.append(game)
    return lst
