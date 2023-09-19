from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///marketplace.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Shop(Base):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    shop_id = Column(Integer, ForeignKey('shops.id'))
    shop = relationship("Shop", foreign_keys=[shop_id])
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    rating_all = Column(Integer)
    reviews_count =  Column(Integer)
    rating = Column(Float)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)
    address = Column(String, nullable=False)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    personality_type = Column(String)

class Friendship(Base):
    __tablename__ = 'friendships'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    friend_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user = relationship("User", foreign_keys=[user_id])
    friend = relationship("User", foreign_keys=[friend_id])
    def __init__(self, user_id, friend_id):
        self.user_id = user_id
        self.friend_id = friend_id

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", foreign_keys=[user_id])
    review = Column(String, nullable=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", foreign_keys=[product_id])
    rating = Column(Integer)


Base.metadata.create_all(bind=engine)