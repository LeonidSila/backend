"""
Задание 1

Цель практической работы:
Научиться выполнять простые запросы в MongoDB.

Что нужно сделать:
Из коллекции постов выберите документы, в которых среди топиков встречается as, идентификатор автора содержит example.ru, а score больше 100.
"""
import pymongo

# Устанавливаем соединение с MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["posts"]

# Выбираем документы, удовлетворяющие условиям
results = collection.find({"topics": "as", "author_id": {"$regex": "example.ru"}, "score": {"$gt": 100}})

# Выводим найденные документы
for result in results:
    print(result)


"""
Задание 2

Цель практической работы:
Научиться писать запросы с использованием различных структур данных в MongoDB.

Что нужно сделать:
Одним запросом добавьте два документа к коллекции posts:
creation_date — текущее время, автор — skbx@example.com, topics должен быть списком из одного элемента mongodb;
creation_date — 31 декабря 2021 года, автор — skbx@example.ru.
"""
from pymongo import MongoClient
from datetime import datetime

# Подключение к базе данных
client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['posts']

# Добавление двух документов
post1 = {
    'creation_date': datetime.now(),
    'author': 'skbx@example.com',
    'topics': ['mongodb']
}

post2 = {
    'creation_date': datetime(2021, 12, 31),
    'author': 'skbx@example.ru'
}

posts = [post1, post2]

collection.insert_many(posts)

# Вывод успешного сообщения
print("Документы успешно добавлены к коллекции posts.")

"""
Задание 3
Цель практической работы:
Научиться анализировать запросы и создавать индексы в MongoDB.

Что нужно сделать:
Создайте композитный индекс для коллекции users, в него войдут поля first_name и last_name. Приведите запросы: на создание индекса и на проверку, что индекс используется.
"""

import pymongo

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["users"]

# Создание композитного индекса
collection.create_index([("first_name", pymongo.ASCENDING), ("last_name", pymongo.ASCENDING)])

# Проверка использования индекса
index_information = collection.index_information()
print(index_information)


"""
Задание 4

Цель практической работы:
Научиться писать аналитические запросы в MongoDB.

Что нужно сделать:
Посчитайте сумму кармы по первым буквам имён пользователей для тех пользователей, у которых больше 300 визитов.
Советы и указания
Для выбора первой буквы имени используйте ключевое слово substr.

"""
import pymongo

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
users_collection = db["users"]

# Найти пользователей с более чем 300 визитами
users_with_more_than_300_visits = users_collection.find({"visits": {"$gt": 300}})

# Инициализация словаря для хранения суммы кармы по первым буквам имён
karma_sum_by_initial = {}

# Обход пользователей с более чем 300 визитами
for user in users_with_more_than_300_visits:
    name = user["name"]
    # Получение первой буквы имени
    first_letter = name[0]
    # Получение кармы пользователя
    karma = user.get("karma", 0)
    # Обновление суммы кармы для соответствующей первой буквы имени
    karma_sum_by_initial[first_letter] = karma_sum_by_initial.get(first_letter, 0) + karma

# Вывод результатов
for initial, karma_sum in karma_sum_by_initial.items():
    print(f"Сумма кармы для пользователей с именами на букву '{initial}': {karma_sum}")


"""
Задание 5

Цель практической работы:
Научиться писать хранимые процедуры в MongoDB.

Что нужно сделать:
Создайте хранимую функцию shuffle, которая принимает один параметр — строку и возвращает строку со случайно переставленными символами.

Советы и указания:
Используйте встроенный в JavaScript метод Math.random() для сортировки символов в строке.
"""

# javascript
# // Создание хранимой функции shuffle
# db.system.js.save({
#     _id: "shuffle",
#     value: function(inputString) {
#         // Преобразование строки в массив символов
#         var characters = inputString.split('');
        
#         // Перемешивание массива символов
#         for (var i = characters.length - 1; i > 0; i--) {
#             var j = Math.floor(Math.random() * (i + 1));
#             var temp = characters[i];
#             characters[i] = characters[j];
#             characters[j] = temp;
#         }
        
#         // Объединение перемешанных символов в строку
#         var shuffledString = characters.join('');
        
#         // Возвращение результата
#         return shuffledString;
#     }
# });

from pymongo import MongoClient
import random
import string

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']

# Вызов хранимой функции shuffle
def call_shuffle(input_string):
    result = db.eval('shuffle', input_string)
    return result

# Пример использования
input_string = 'Hello World!'
shuffled_string = call_shuffle(input_string)
print("Input String:", input_string)
print("Shuffled String:", shuffled_string)