from db_user_funcs import (
    create_user, 
    add_friendship
)

class User:
    def __init__(
        self,
        login: str ,
        password: str,
        address: str,
        name: str,
        lastname: str,
        age: int,
        height: float,
        weight: float,
        personality_type: str
    ):
        self.login = login
        self.password = password
        self.address = address
        self.name = name
        self.lastname = lastname
        self.age = age
        self.height = height
        self.weight = weight
        self.personality_type = personality_type

USERS = [
    User(
        "senks", 
        "1234",
        "address",
        "Арсений",
        "Ильин",
        21,
        170,
        59,
        "Сангвиник"
    ),
    User(
        "imadji",
        "1234",
        "address",
        "Иван",
        "Ежов",
        21,
        170,
        59,
        "Холерик" 
    ),
    User(
        "aemlnt",
        "1234",
        "address",
        "Артём",
        "Сидоров",
        29,
        175,
        65,
        "Сангвиник" 
    ),
    User(
        "miro",
        "1234",
        "address",
        "Данила",
        "Вошняев",
        21,
        173,
        65.5,
        "Сангвиник" 
    ),
    User(
        "krut",
        "1234",
        "address",
        "Петр",
        "Максимов",
        25,
        180,
        70,
        "Флегматик"
    ),
    User(
        "groot",
        "1234",
        "address",
        "Полина",
        "Анисимова",
        30,
        160,
        55,
        "Меланхолик"
    ),
    User(
        "kreeper",
        "1234",
        "address",
        "Влад",
        "Валунов",
        22,
        175,
        68,
        "Холерик"
    ),
    User(
        "buster",
        "1234",
        "address",
        "Станислав",
        "Андреев",
        26,
        165,
        60,
        "Сангвиник"
    ),
    User(
        "zhoos",
        "1234",
        "address",
        "Виктория",
        "Романова",
        24,
        178,
        72,
        "Холерик"
    ),
    User(
        "popicona",
        "1234",
        "address",
        "Анна",
        "Тронова", 
        27, 
        163, 
        58, 
        "Меланхолик"
    )
]

FRIENDSHIPS = [
    ["senks", "krut"],
    ["krut", "senks"],
    ["senks", "miro"],
    ["miro", "senks"],
    ["senks", "imadji"],
    ["imadji", "senks"],
    ["senks", "aemlnt"],
    ["aemlnt", "senks"],
    ["imadji", "miro"],
    ["miro", "imadji"],
    ["imadji", "popicona"],
    ["popicona", "imadji"],
    ["imadji", "kreeper"],
    ["kreeper", "imadji"],
    ["miro", "aemlnt"],
    ["aemlnt", "miro"],
    ["miro", "zhoos"],
    ["zhoos", "miro"],
    ["miro", "groot"],
    ["groot", "miro"],
]

# CREATE USERS
for user in USERS:
    create_user(user)

# ADD FRIENDS
for friends in FRIENDSHIPS:
    add_friendship(friends[0], friends[1])