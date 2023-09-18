from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///marketplace.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)
    buyer_id = Column(Integer, ForeignKey("buyers.id"), nullable=True)
    buyer = relationship("Buyer", foreign_keys=[buyer_id])


class Shop(Base):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cost = Column(Float)

class Buyer(Base):
    __tablename__ = 'buyers'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    personality_type = Column(String)
    user = relationship("User", foreign_keys=[user_id])

class Friendship(Base):
    __tablename__ = 'friendships'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    friend_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user = relationship("User", foreign_keys=[user_id])
    friend = relationship("User", foreign_keys=[friend_id])
    def __init__(self, user_id, friend_id):
        self.user_id = user_id
        self.friend_id = friend_id

        
Base.metadata.create_all(bind=engine)