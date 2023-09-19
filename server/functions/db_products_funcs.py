from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

# from db_models import (
from functions.db_models import (
    engine,
    Shop,
    Product,
    Review
)
# from db_user_funcs import get_similarity_ratio
from functions.db_user_funcs import get_similarity_ratio

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
                rating_all = 0,
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
                    "id": product.id,
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


def get_product(id: int, login: str):
    with session() as db:
        product = db.query(Product).filter(Product.id==id).first()
        return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "rating": product.rating,
            "shop": product.shop.name,
            "reviews": get_reviews(id, login)
        }
    

def create_review(data):
    with session() as db:
        db.add(
            Review(
                user_id=data["user_id"],
                product_id=data["product_id"],
                rating=data["rating"],
                review=data["review"]
            )
        )
        db.commit()
        product = db.query(Product).filter_by(id=data["product_id"]).first()
        product.rating_all += data["rating"]
        product.reviews_count += 1
        product.rating = product.rating_all/product.reviews_count
        db.commit()


def get_reviewers(product_id: int):
    reviewers = []
    with session() as db:
        reviews = db.query(Review).filter(Review.product_id==product_id).all()
        for review in reviews:
            reviewers.append(review.user.id)
    return reviewers

def get_reviews(product_id: int, user_login):
    reviews = []
    reviewers_sort = []
    reviewers = get_reviewers(product_id)
    for reviewer in reviewers:
        reviewers_sort.append(
            {
                reviewer: get_similarity_ratio(user_login, reviewer)
            }
        )
    sorted_data = sorted(reviewers_sort, key=lambda x: list(x.values())[0], reverse=True)
    user_ids = [list(d.keys())[0] for d in sorted_data]
    for user_id in user_ids:
        with session() as db:
            review = db.query(Review).filter(and_(Review.user_id == user_id, Review.product_id == product_id)).first()
            reviews.append(
                {
                    "user": review.user.name,
                    "rating": review.rating,
                    "review": review.review
                }
            )
    return reviews

# print(get_reviews(20, 9))