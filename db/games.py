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


def search_game(name=None, genre=None, minp=None, maxp=None):
    lst = []
    lst1 = []
    with db_session:
        if not Game.select().exists():
            raise HTTPException(status_code=404, detail="Table not found")
        for data in Game.select():
            game = {"id": data.id, "name": data.title, "price": data.price, "categories": data.categories.split(',')}
            lst.append(game)

        if genre and minp and maxp:
            for data in lst:
                if maxp >= data["price"] >= minp and genre.lower() in [x.lower() for x in data["categories"]]:
                    lst1.append(data)


        elif maxp and minp:
            for data in lst:
                if maxp >= data["price"] >= minp:
                    lst1.append(data)




        elif genre and minp:
            for data in lst:
                if data["price"] >= minp and genre.lower() in [x.lower() for x in data["categories"]]:
                    lst1.append(data)


        elif genre and maxp:
            for data in lst:
                if data["price"] <= maxp and genre.lower() in [x.lower() for x in data["categories"]]:
                    lst1.append(data)


        elif name:
            for data in lst:
                if data["name"].lower() == name.lower():
                    lst1.append(data)


        elif genre:
            for data in lst:
                if genre.lower() in [x.lower() for x in data["categories"]]:
                    lst1.append(data)


        elif maxp:
            for data in lst:
                if data["price"] <= maxp:
                    lst1.append(data)


        elif minp:
            for data in lst:
                if data["price"] >= minp:
                    lst1.append(data)


        else:
            raise HTTPException(status_code=404, detail="Game not found")
    if len(lst1) == 0:
        raise HTTPException(status_code=404, detail="Game not found")
    return lst1

