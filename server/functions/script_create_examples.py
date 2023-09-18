from db_user_funcs import (
    create_user, 
    create_buyer,
    add_friendship
)

USERS = [
    ["senks", "1234"],
    ["imadji", "4567"],
    ["aemlnt", "qwer"],
    ["miro", "asdd"],
    ["krut", "dfsf"],
    ["groot", "asdf"],
    ["kreeper", "asdf"],
    ["buster", "1234"],
    ["zhoos", "zxvc"],
    ["popicona", "zvxc"],
]

BUYERS = [
    {
        "login": "senks",
        "name": "Арсений",
        "lastname": "Ильин",
        "age": 21,
        "height": 170,
        "weight": 59,
        "personality_type": "Сангвиник" 
    },
    {
        "login": "imadji",
        "name": "Иван",
        "lastname": "Ежов",
        "age": 21,
        "height": 170,
        "weight": 59,
        "personality_type": "Холерик" 
    },
    {
        "login": "aemlnt",
        "name": "Артём",
        "lastname": "Сидоров",
        "age": 29,
        "height": 175,
        "weight": 65,
        "personality_type": "Сангвиник" 
    },
    {
        "login": "miro",
        "name": "Данила",
        "lastname": "Вошняев",
        "age": 21,
        "height": 173,
        "weight": 65.5,
        "personality_type": "Сангвиник" 
    },
    {
        "login": "krut",
        "name": "Петр",
        "lastname": "Максимов",
        "age": 25,
        "height": 180,
        "weight": 70,
        "personality_type": "Флегматик"
    },
    {
        "login": "groot",
        "name": "Полина",
        "lastname": "Анисимова",
        "age": 30,
        "height": 160,
        "weight": 55,
        "personality_type": "Меланхолик"
    },
    {
        "login": "kreeper",
        "name": "Влад",
        "lastname": "Валунов",
        "age": 22,
        "height": 175,
        "weight": 68,
        "personality_type": "Холерик"
    },
    {
        "login": "buster",
        "name": "Станислав",
        "lastname": "Андреев",
        "age": 26,
        "height": 165,
        "weight": 60,
        "personality_type": "Сангвиник"
    },
    {
        "login": "zhoos",
        "name": "Виктория",
        "lastname": "Романова",
        "age": 24,
        "height": 178,
        "weight": 72,
        "personality_type": "Холерик"
    },
    {
        "login": "popicona",
        "name": "Анна",
        "lastname": "Тронова",
        "age": 27,
        "height": 163,
        "weight": 58,
        "personality_type": "Меланхолик"
    }
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
    create_user(user[0], user[1])

# UPLOAD USERS INFO
for buyer in BUYERS:
    create_buyer(buyer)

# ADD FRIENDS
for friends in FRIENDSHIPS:
    add_friendship(friends[0], friends[1])