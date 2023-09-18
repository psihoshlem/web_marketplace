from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

from functions.db_models import User, engine, Friendship, Buyer
# from db_models import User, engine, Friendship, Buyer


session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_user(login: str, password: str):
    if is_user_exist(login):
        return False
    with session() as db:
        db.add(User(login=login, password=password))
        db.commit()
    return True

def is_user_exist(login):
    with session() as db:
        user = db.query(User).filter(User.login == login).first()
    if user:
        return True
    else:
        return False

def auth_user(login: str, password: str):
    with session() as db:
        user = db.query(User).filter(User.login == login).first()
    if not user:
        return False
    if password == user.password:
        return True
    

def get_user_from_id(id: int):
    with session() as db:
        user = db.query(User).filter(User.id == id).first()
    return user

def get_user_from_login(login: str):
    with session() as db:
        user = db.query(User).filter(User.login == login).first()
    return user

def add_friendship(user: str, friend: str):
    user_id = get_user_from_login(user).id
    friend_id = get_user_from_login(friend).id
    new_friendship = Friendship(user_id=user_id, friend_id=friend_id)
    with session() as db:
        db.add(new_friendship)
        db.commit()

def get_user_friends(login):
    user_id = get_user_from_login(login).id
    friends = []
    with session() as db:
        friendships = db.query(Friendship).filter_by(user_id=user_id).all()
        for friendship in friendships:
            friend = friendship.friend
            friend_data = {
                "fullname": friend.buyer.name + " " + friend.buyer.lastname,
                "login": friend.login
            }
            friends.append(friend_data)
    return friends

def create_buyer(data):
    user_id = get_user_from_login(data["login"]).id
    buyer = Buyer(
        user_id = user_id,
        name = data["name"],
        lastname = data["lastname"],
        age = data["age"],
        height = data["height"],
        weight = data["weight"],
        personality_type = data["personality_type"]
    )
    with session() as db:
        db.add(buyer)
        db.commit()
        buyer_id = db.query(Buyer).where(Buyer.user_id == user_id).first().id
        db.execute(update(User).where(User.id == user_id).values(buyer_id = buyer_id))
        db.commit()


def get_user_info_from_db(login: str):
    with session() as db:
        user = db.query(User).filter(User.login == login).first()
        buyer = user.buyer
    info = {
        "login": login,
        "name": buyer.name,
        "lastname": buyer.lastname,
        "age": buyer.age,
        "height": buyer.height,
        "weight": buyer.weight,
        "personality_type": buyer.personality_type 
    }
    return info

if __name__=="__main__":
    with session() as db:
        records = db.query(User).filter_by(id=1).first()
        print(records.buyer_id)
        records = db.query(User).filter_by(id=2).first()
        print(records.buyer_id)