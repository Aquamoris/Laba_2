import sqlite3

con = sqlite3.connect("meal-ration.sqlite")

cursor = con.cursor()

query = """"""

# query_create_1 = """
# CREATE TABLE IF NOT EXISTS category (
#     id INTEGER PRIMARY KEY,
#     category_name VARCHAR(255) NOT NULL
# );"""
#
# query_create_2 = """CREATE TABLE IF NOT EXISTS product (
#     name VARCHAR(255) PRIMARY KEY,
#     id_category INTEGER,
#     FOREIGN KEY (id_category) REFERENCES category (id)
# );"""
#
# query_create_3 = """CREATE TABLE IF NOT EXISTS meal (
#     date DATE PRIMARY KEY,
#     product_id VARCHAR(255),
#     FOREIGN KEY (product_id) REFERENCES product (name)
# );"""

# cursor.execute("""
# INSERT INTO product (name, id_category)
# VALUES
#     ('Яблоко', 1),
#     ('Молоко', 2),
#     ('Хлеб', 3),
#     ('Банан', 1),
#     ('Яйцо', 2),
#     ('Сыр', 3),
#     ('Огурец', 1),
#     ('Картошка', 2),
#     ('Мясо', 3),
#     ('Мандарин', 1),
#     ('Гречка', 2),
#     ('Творог', 3),
#     ('Киноа', 3),
#     ('Омлет', 3),
#     ('Сырники', 3),
#     ('Руккола', 3),
#     ('Пармезан', 3),
#     ('Лапша', 3),
#     ('Доширак', 3),
#     ('Киви', 3),
#     ('Протеин', 3),
#     ('Козеин', 3),
#     ('Козинак', 3),
#     ('Оладьи', 3),
#     ('Чипсы', 3),
#     ('Картошка', 3),
#     ('Изюм', 3),
#     ('Виноград', 3),
#     ('Соль', 3),
#     ('Сахар', 3),
#     ('Булка', 3),
#     ('Буханка', 3),
#     ('Рожок', 3),
#     ('Творожок', 3),
#
# INSERT INTO meal (date, product_id)
# SELECT
#     date('now', '-' || abs(random() % 365) || ' days'),
#     (SELECT name FROM product ORDER BY random() LIMIT 1)
# FROM
#     sqlite_master
# WHERE
#     type='table'
# LIMIT 50;
# """)

# Два запроса на выборку для связанных таблиц с условиями и сортировкой;
# Выборка всех продуктов в категории "Категория 1" с датами приема пищи в заданном диапазоне и сортировкой по дате
# Выборка всех продуктов в категории "Категория 2" с общей оплатой за услуги более 1000 рублей и сортировкой по общей оплате по убыванию
# cursor.execute("""
# SELECT
#     p.name AS product_name,
#     c.category_name,
#     m.date AS meal_date
# FROM
#     product p
# JOIN
#     category c ON p.id_category = c.id
# JOIN
#     meal m ON p.name = m.product_id
# WHERE
#     c.category_name = 'Категория 1'
#     AND m.date BETWEEN '2023-01-01' AND '2023-01-31'
# ORDER BY
#     m.date DESC;
#
# SELECT
#     p.name AS product_name,
#     c.category_name,
#     SUM(sb.price) AS total_payment
# FROM
#     product p
# JOIN
#     category c ON p.id_category = c.id
# LEFT JOIN
#     meal m ON p.name = m.product_id
# LEFT JOIN
#     service_booking sb ON m.date = sb.service_start_date
# WHERE
#     c.category_name = 'Категория 2'
# GROUP BY
#     p.name, c.category_name
# HAVING
#     total_payment > 1000
# ORDER BY
#     total_payment DESC;
#
# """)

# Два запроса с группировкой и групповыми функциями;
# Группировка по категориям и подсчет количества продуктов в каждой категории
# Группировка по датам приема пищи и подсчет количества продуктов в каждую дату
# cursor.execute("""
# SELECT
#     c.category_name,
#     COUNT(p.name) AS count_products
# FROM
#     category c
# JOIN
#     product p ON c.id = p.id_category
# GROUP BY
#     c.category_name;
#
# SELECT
#     m.date AS meal_date,
#     COUNT(m.product_id) AS count_products
# FROM
#     meal m
# JOIN
#     product p ON m.product_id = p.name
# JOIN
#     category c ON p.id_category = c.id
# GROUP BY
#     m.date;
# """)

# Два запроса со вложенными запросами или табличными выражениями;
# Запрос с вложенным подзапросом для получения списка продуктов в каждой категории с указанием их общего количества
# Вывести информацию о количестве приемов пищи для каждого продукта в каждой категории
# cursor.execute("""
# SELECT
#     c.category_name,
#     p.name AS product_name,
#     (SELECT COUNT(m.product_id)
#      FROM meal m
#      WHERE m.product_id = p.name) AS count_in_category
# FROM
#     category c
# JOIN
#     product p ON c.id = p.id_category;
#
# WITH ProductCategoryMealCount AS (
#     SELECT
#         c.category_name,
#         p.name AS product_name,
#         COUNT(m.product_id) AS meal_count
#     FROM
#         category c
#     JOIN
#         product p ON c.id = p.id_category
#     LEFT JOIN
#         meal m ON p.name = m.product_id
#     GROUP BY
#         c.category_name, p.name
# )
#
# SELECT
#     category_name,
#     product_name,
#     COALESCE(meal_count, 0) AS meal_count
# FROM
#     ProductCategoryMealCount
# ORDER BY
#     category_name, product_name;
#
# """)

# Два запроса корректировки данных (обновление, добавление, удаление и пр)
# cursor.execute("""
# UPDATE product
# SET id_category = (
#     SELECT id FROM category WHERE category_name = 'Категория 2'
# )
# WHERE name = 'Яблоко';
#
# INSERT INTO product (name, id_category)
# VALUES ('Груша', (SELECT id FROM category WHERE category_name = 'Категория 1'));
#
# DELETE FROM product
# WHERE name = 'Молоко';
# """)

cursor.execute(query);

con.close()