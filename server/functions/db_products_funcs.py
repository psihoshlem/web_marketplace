from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

# from db_models import (
from functions.db_models import (
    engine,
    Shop,
    Product,
    Review
)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_shop(name):
    with session() as db:
        db.add(Shop(name=name))
        db.commit()


def create_product(data: dict):
    with session() as db:
        shop = db.user = db.query(Shop).filter(Shop.id == data["shop_id"]).first()
        db.add(
            Product(
                shop_id=shop.id,
                name=data["product_name"],
                description=data["description"],
                rating = 0,
                reviews_count = 0,
                price=data["price"]
            )
        )
        db.commit()

def get_all_products():
    products_info = []
    with session() as db:
        products = db.query(Product).all()
        for product in products:
            products_info.append(
                {
                    "name": product.name,
                    "shop": product.shop.name
                }
            )
    return products_info


def get_products(query: str):
    products_info = []
    with session() as db:
        query = query.capitalize()
        products = db.query(Product).filter(Product.name.contains(f"%{query}%")).all()
        query = query.lower()
        products += db.query(Product).filter(Product.name.contains(f"%{query}%")).all()
        for product in products:
            products_info.append(
                {
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "rating": product.rating,
                    "shop": product.shop.name
                }
            )
    return products_info


def get_product(id: int):
    with session() as db:
        product = db.query(Product).filter(Product.id==id).first()
        return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "rating": product.rating,
            "shop": product.shop.name,
            "reviews": []
        }
    

def get_reviewers(product_id: int):
    reviewers = []
    with session() as db:
        reviews = db.query(Review).filter(Review.product_id==product_id).all()
        for review in reviews:
            reviewers.append(review.user.login)
    return reviewers

def get_reviews(product_id: int, user_id: int):
    pass

print(get_reviewers(2))