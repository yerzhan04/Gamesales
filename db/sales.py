from datetime import datetime

from db.connection import Sale, Game, db_session


def buy_game(gid, card):
    with db_session:
        game = Game[gid]
        Sale(date=datetime.now(), game=game.id, s_price=game.price * 1.05, user_card=card)


def get_list(start_date, end_date):
    lst = []
    with db_session:
        for data in Sale.select(lambda p: p.date >= start_date and p.date <= end_date):
            sale = {"id": data.id, "date": data.date, "price": data.s_price, "card": data.user_card}
            lst.append(sale)
    return lst


def get_stats(start_date, end_date):
    with db_session:
        query = Sale.select(lambda p: p.date >= start_date and p.date <= end_date)
        total_sales = query.count()
        sum_of_sales = sum(s.s_price for s in query)

    return {"total": total_sales, "sum": sum_of_sales}