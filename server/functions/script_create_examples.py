from db_user_funcs import (
    create_user, 
    add_friendship
)
from db_products_funcs import (
    create_shop,
    create_product
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
    "ГаджетГалактика",
    "УютныйДом",
    "ДетскийМир",
    "МодныйШик",
    "ЗеленыйУголок",
    "КнижныйМир",
    "РукодельнаяМастерская",
    "ЗаботаОПитомцах",
    "СпортЛидер",
    "ЗдоровоиКрасиво"
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
