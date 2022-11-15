from datetime import datetime

import pymysql
from pony.orm import *

con = pymysql.connect(host='localhost', user='root', password='123456')

with con:
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS Gamesales")

db = Database()
db.bind(provider='mysql', host='localhost', user='root', passwd='123456', db='Gamesales')


class Game(db.Entity):
    id = PrimaryKey(int, auto=True)
    add_date = Required(datetime)
    edit_date = Required(datetime)
    title = Required(str)
    price = Required(float)
    categories = Required(str)
    sales = Set('Sale')


class Sale(db.Entity):
    id = PrimaryKey(int, auto=True)
    date = Required(datetime)
    game = Required('Game')
    s_price = Required(float)
    user_card = Required(str)


db.generate_mapping(create_tables=True)
