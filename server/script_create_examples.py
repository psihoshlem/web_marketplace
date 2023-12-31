import os
db_file_path = './marketplace.db'
if os.path.exists(db_file_path):
    os.remove(db_file_path)


from functions.db_user_funcs import (
    create_user, 
    add_friendship
)
from functions.db_products_funcs import (
    create_shop,
    create_product,
    create_review
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

SHOPS = [
    "Гаджет Галактика",
    "Уютный Дом",
    "Детский Мир",
    "Забота о здоровье",
    "ТехноМастер",
    "Мир искусства",
    "Маленькая страна",
    "СпортЛидер",
    "Mr. Cabel",
    "Очаг"
]

PRODUCTS = [
    {
        "shop_id": 1,
        "product_name": "Наушники 'SuperBass'",
        "description": "Наушники с отличным качеством звука и стильным дизайном. Идеально подходят для музыки и фильмов.",
        "price": 1999
    },
    {
        "shop_id": 1,
        "product_name": "Смартфон 'GalaxyPhone'",
        "description": "Мощный смартфон с большим экраном, отличной производительностью и качественной камерой.",
        "price": 23999
    },
    {
        "shop_id": 1,
        "product_name": "Планшет 'GadgetPad'",
        "description": "Отличный планшет для работы и развлечений. Высокая производительность и долгое время работы от батареи.",
        "price": 7999
    },
    {
        "shop_id": 2,
        "product_name": "Диван 'ComfortLux'",
        "description": "Мягкий и уютный диван для вашей гостиной. Идеально вписывается в интерьер и обеспечивает комфорт.",
        "price": 14999
    },
    {
        "shop_id": 2,
        "product_name": "Кухонный стол 'Family'",
        "description": "Прочный и стильный стол для всей семьи. Подходит для совместных обедов и ужинов.",
        "price": 5499
    },
    {
        "shop_id": 2,
        "product_name": "Ковер 'SoftnessUnderFeet'",
        "description": "Добавьте уют и тепло в ваш дом с этим мягким ковром. Идеально подходит для гостиной или спальни.",
        "price": 2999
    },
    {
        "shop_id": 3,
        "product_name": "Кукла 'Лолита'",
        "description": "Очаровательная кукла с яркими нарядами и аксессуарами. Подарите радость вашей девочке!",
        "price": 799
    },
    {
        "shop_id": 3,
        "product_name": "Конструктор 'СуперСтроитель'",
        "description": "Набор для строительства и игры. Развивает логику и воображение у детей.",
        "price": 1299
    },
    {
        "shop_id": 3,
        "product_name": "Велосипед 'ДетскийГерой'",
        "description": "Яркий и безопасный велосипед для детей. Помогает развивать координацию и активность.",
        "price": 3499
    },
    {
        "shop_id": 4,
        "product_name": "Беговая дорожка 'RunnerPro'",
        "description": "Профессиональная беговая дорожка для занятий спортом. С множеством функций и режимов тренировок.",
        "price": 28999
    },
    {
        "shop_id": 4,
        "product_name": "Гантели 'StrongArm'",
        "description": "Комплект гантелей разных весов для силовых тренировок. Удобные и надежные.",
        "price": 1999
    },
    {
        "shop_id": 4,
        "product_name": "Мяч для йоги 'YogaBalance'",
        "description": "Мяч для йоги, помогает развивать гибкость и укреплять мышцы. Подходит для занятий дома или в зале.",
        "price": 599
    },
    {
        "shop_id": 5,
        "product_name": "Смартфон 'ТехноГаджет 2000'",
        "description": "Современный смартфон с высокой производительностью и камерой 64 Мп. Отличный выбор для тех, кто ценит качество!",
        "price": 18999
    },
    {
        "shop_id": 5,
        "product_name": "Ноутбук 'Пульсар Pro'",
        "description": "Мощный ноутбук для работы и развлечений. Идеально подходит для игр и тяжелых задач.",
        "price": 34999
    },
    {
        "shop_id": 5,
        "product_name": "Умные часы 'СмартВотч 3'",
        "description": "Стильные и функциональные умные часы с поддержкой множества приложений и трекером активности.",
        "price": 7999
    },
    {
        "shop_id": 6,
        "product_name": "Картина 'Абстракция'",
        "description": "Изящная картина в современном стиле, украсит интерьер вашего дома или офиса.",
        "price": 1499
    },
    {
        "shop_id": 6,
        "product_name": "Скатерть и салфетки 'Роскошь'",
        "description": "Набор изысканных скатерти и салфеток с ручной вышивкой. Прекрасный выбор для торжеств и ужинов.",
        "price": 2999
    },
    {
        "shop_id": 6,
        "product_name": "Светильник 'Луна'",
        "description": "Декоративный светильник в форме луны. Создайте уютную атмосферу в вашем доме.",
        "price": 999
    },
    {
        "shop_id": 7,
        "product_name": "Игровой набор 'Пираты Карибского моря'",
        "description": "Захватывающий игровой набор, включающий пиратский корабль, остров с кладом и пиратов. Для маленьких исследователей!",
        "price": 1999
    },
    {
        "shop_id": 7,
        "product_name": "Конструктор 'Мир Блоков'",
        "description": "Развивающий конструктор для детей. Помогает развивать логику и воображение. В комплекте 100 деталей.",
        "price": 799
    },
    {
        "shop_id": 7,
        "product_name": "Мягкая игрушка 'Плюшевый медведь'",
        "description": "Мягкая и пушистая игрушка в виде медведя. Вашему ребенку будет с кем играть и обниматься.",
        "price": 599
    },
    {
        "shop_id": 8,
        "product_name": "Велосипед 'СпортПро X5'",
        "description": "Спортивный велосипед с алюминиевой рамой и 21 скоростью. Отличный выбор для активных летних прогулок.",
        "price": 7499
    },
    {
        "shop_id": 8,
        "product_name": "Теннисная ракетка 'ПрофиТеннис'",
        "description": "Профессиональная теннисная ракетка с усиленным каркасом. Для настоящих любителей тенниса.",
        "price": 1999
    },
    {
        "shop_id": 8,
        "product_name": "Беговая дорожка 'Спортランнер 3000'",
        "description": "Современная беговая дорожка с множеством программ тренировок и датчиком пульса. Домашний фитнес на высшем уровне.",
        "price": 9999
    },
    {
        "shop_id": 9,
        "product_name": "Наушники 'SoundMaster Pro'",
        "description": "Наушники высшего качества с шумоподавлением и кристально чистым звуком. Идеальны для музыки и звонков.",
        "price": 2999
    },
    {
        "shop_id": 9,
        "product_name": "Портативная колонка 'SoundWave Mini'",
        "description": "Компактная беспроводная колонка с мощным басом. Встроенный аккумулятор для долгого воспроизведения музыки.",
        "price": 1499
    },
    {
        "shop_id": 9,
        "product_name": "USB-микрофон 'StudioSound Pro'",
        "description": "Профессиональный микрофон для записи аудио и ведения онлайн-трансляций. Качество звука на высшем уровне.",
        "price": 2499
    },
    {
        "shop_id": 10,
        "product_name": "Диван 'LuxComfort'",
        "description": "Удобный и стильный диван для вашей гостиной. Прекрасно впишется в интерьер и обеспечит комфортный отдых.",
        "price": 8999
    },
    {
        "shop_id": 10,
        "product_name": "Кофейный столик 'EcoWood'",
        "description": "Элегантный кофейный столик из натурального дерева. Прочный и экологичный выбор для вашего дома.",
        "price": 2999
    },
    {
        "shop_id": 10,
        "product_name": "Кухонный набор 'MasterChef'",
        "description": "Комплект кухонных принадлежностей высокого качества. С ним приготовление пищи станет ещё приятнее.",
        "price": 1999
    }
]

REVIEWS = [
    {"user_id": 1, "product_id": 15, "rating": 4, "review": "Отличный товар!"},
    {"user_id": 2, "product_id": 5, "rating": 2, "review": "Не понравилось."},
    {"user_id": 3, "product_id": 12, "rating": 5, "review": "Замечательно!"},
    {"user_id": 4, "product_id": 8, "rating": 3, "review": "Средний товар."},
    {"user_id": 5, "product_id": 27, "rating": 4, "review": "Хороший выбор."},
    {"user_id": 6, "product_id": 19, "rating": 1, "review": "Ужасное качество."},
    {"user_id": 7, "product_id": 7, "rating": 4, "review": "Мне понравилось."},
    {"user_id": 8, "product_id": 14, "rating": 5, "review": "Прекрасный товар!"},
    {"user_id": 9, "product_id": 23, "rating": 3, "review": "Так себе..."},
    {"user_id": 10, "product_id": 1, "rating": 2, "review": "Не рекомендую."},
    {"user_id": 1, "product_id": 20, "rating": 4, "review": "Хороший выбор."},
    {"user_id": 2, "product_id": 9, "rating": 3, "review": "Средний товар."},
    {"user_id": 3, "product_id": 6, "rating": 5, "review": "Отличный продукт!"},
    {"user_id": 4, "product_id": 25, "rating": 2, "review": "Не впечатлил."},
    {"user_id": 5, "product_id": 16, "rating": 1, "review": "Ужасно..."},
    {"user_id": 6, "product_id": 10, "rating": 4, "review": "Хорошее качество."},
    {"user_id": 7, "product_id": 30, "rating": 3, "review": "Средний выбор."},
    {"user_id": 8, "product_id": 11, "rating": 5, "review": "Отличный товар!"},
    {"user_id": 9, "product_id": 3, "rating": 2, "review": "Не понравилось."},
    {"user_id": 10, "product_id": 18, "rating": 1, "review": "Ужасное качество."},
    {"user_id": 1, "product_id": 2, "rating": 4, "review": "Мне понравилось."},
    {"user_id": 2, "product_id": 4, "rating": 5, "review": "Замечательный товар!"},
    {"user_id": 3, "product_id": 28, "rating": 3, "review": "Средний продукт."},
    {"user_id": 4, "product_id": 13, "rating": 2, "review": "Не впечатлил."},
    {"user_id": 5, "product_id": 21, "rating": 1, "review": "Ужасно..."},
    {"user_id": 6, "product_id": 17, "rating": 4, "review": "Хорошее качество."},
    {"user_id": 7, "product_id": 22, "rating": 3, "review": "Средний выбор."},
    {"user_id": 8, "product_id": 29, "rating": 5, "review": "Отличный товар!"},
    {"user_id": 9, "product_id": 26, "rating": 2, "review": "Не понравилось."},
    {"user_id": 10, "product_id": 24, "rating": 1, "review": "Ужасное качество."},
    {"user_id": 1, "product_id": 7, "rating": 4, "review": "Мне понравилось."},
    {"user_id": 2, "product_id": 16, "rating": 5, "review": "Замечательный товар!"},
    {"user_id": 3, "product_id": 9, "rating": 3, "review": "Средний продукт."},
    {"user_id": 4, "product_id": 14, "rating": 2, "review": "Не впечатлил."},
    {"user_id": 5, "product_id": 8, "rating": 1, "review": "Ужасно..."},
    {"user_id": 6, "product_id": 25, "rating": 4, "review": "Хорошее качество."},
    {"user_id": 7, "product_id": 11, "rating": 3, "review": "Средний выбор."},
    {"user_id": 8, "product_id": 23, "rating": 5, "review": "Отличный товар!"},
    {"user_id": 9, "product_id": 6, "rating": 2, "review": "Не понравилось."},
    {"user_id": 10, "product_id": 12, "rating": 1, "review": "Ужасное качество."},
    {"user_id": 1, "product_id": 3, "rating": 4, "review": "Мне понравилось."},
    {"user_id": 2, "product_id": 28, "rating": 5, "review": "Замечательный товар!"},
    {"user_id": 3, "product_id": 13, "rating": 3, "review": "Средний продукт."},
    {"user_id": 4, "product_id": 21, "rating": 2, "review": "Не впечатлил."},
    {"user_id": 5, "product_id": 10, "rating": 1, "review": "Ужасно..."},
    {"user_id": 6, "product_id": 18, "rating": 4, "review": "Хорошее качество."},
    {"user_id": 7, "product_id": 29, "rating": 3, "review": "Средний выбор."},
    {"user_id": 8, "product_id": 4, "rating": 5, "review": "Отличный товар!"},
    {"user_id": 9, "product_id": 17, "rating": 2, "review": "Не понравилось."},
    {"user_id": 10, "product_id": 26, "rating": 1, "review": "Ужасное качество."},
    {"user_id": 2, "product_id": 20, "rating": 5, "review": "Замечательное качество."},
    {"user_id": 3, "product_id": 20, "rating": 3, "review": "Средний конструктор."},
    {"user_id": 4, "product_id": 20, "rating": 4, "review": "Мне понравилось."},
    {"user_id": 5, "product_id": 20, "rating": 5, "review": "Прекрасный выбор!"},
]

# CREATE USERS
for user in USERS:
    create_user(user)

# ADD FRIENDS
for friends in FRIENDSHIPS:
    add_friendship(friends[0], friends[1])

# CREATE SHOPS
for shop in SHOPS:
    create_shop(shop)

# CREATE PRODUCTS
for product in PRODUCTS:
    create_product(product)

for review in REVIEWS:
    create_review(review)