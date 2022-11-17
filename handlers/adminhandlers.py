from datetime import date
from fastapi import APIRouter, Depends
from env import get_token_header
from models.pydanticSchemes import GameBase
from db import games, sales


router = APIRouter(dependencies=[Depends(get_token_header)],
                   responses={404: {"description": "Not found"}}, )


@router.post("/games", response_model=GameBase)
async def create_game(game: GameBase):
    genres = ",".join(game.categories)
    games.create_game(game.name, game.price, genres,)
    return game


@router.put("/games", response_model=GameBase)
async def update_game(gid: int, game: GameBase):
    genres = ",".join(game.categories)
    games.update_game(gid, game.name, game.price, genres)
    return game



@router.delete("/games")
async def delete_game(gid: int):
    games.del_by_id(gid)



@router.get("/list")
async def get_salelist(start_date: date, end_date: date):
    return sales.get_list(start_date, end_date)


@router.get("/stats")
async def get_salestats(start_date: date, end_date: date):
    return sales.get_stats(start_date,end_date)



