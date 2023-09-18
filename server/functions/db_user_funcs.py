from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

from functions.db_models import User, engine, Friendship
# from db_models import User, engine, Friendship


session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


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
                "fullname": friend.name + " " + friend.lastname,
                "login": friend.login
            }
            friends.append(friend_data)
    return friends

def create_user(data):
    if is_user_exist(data.login):
        return False
    buyer = User(
        login = data.login,
        password = data.password,
        address = data.address,
        name = data.name,
        lastname = data.lastname,
        age = data.age,
        height = data.height,
        weight = data.weight,
        personality_type = data.personality_type
    )
    with session() as db:
        db.add(buyer)
        db.commit()
    return True


def get_user_info_from_db(login: str):
    with session() as db:
        user = db.query(User).filter(User.login == login).first()
    info = {
        "login": login,
        "name": user.name,
        "lastname": user.lastname,
        "age": user.age,
        "height": user.height,
        "weight": user.weight,
        "personality_type": user.personality_type 
    }
    return info

if __name__=="__main__":
    pass