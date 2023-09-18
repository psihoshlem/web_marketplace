from sqlalchemy.orm import sessionmaker

# from functions.db_models import User, engine, Friendship
from db_models import User, engine, Friendship, Buyer


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

def add_friend(user: str, friend: str):
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
        records = db.query(Friendship).filter_by(user_id=user_id).all()
        for record in records:
            friends.append(record.friend.login)
    return friends

def create_buyer(data):
    data["user_id"] = get_user_from_login(data["login"]).id
    buyer = Buyer(data)
    with session() as db:
        db.add(buyer)
        db.commit()


if __name__=="__main__":
    with session() as db:
        records = db.query(User).filter_by(id=1).first()
        print(records.buyer_id)
        records = db.query(User).filter_by(id=2).first()
        print(records.buyer_id)