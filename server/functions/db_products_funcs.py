from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

# from db_models import (
from functions.db_models import (
    engine,
    Shop,
    Product
)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_shop(name):
    with session() as db:
        db.add(Shop(name=name))
        db.commit()


def create_product(data: dict):
    # print(data)
    with session() as db:
        shop = db.user = db.query(Shop).filter(Shop.id == data["shop_id"]).first()
        db.add(
            Product(
                shop_id=shop.id,
                name=data["product_name"],
                description=data["description"],
                price=data["price"]
            )
        )
        db.commit()