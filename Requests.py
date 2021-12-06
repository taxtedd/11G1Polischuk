import sqlite3


# Логины и имена всех пользователей, которые делали хотя бы один заказ
def get_emails_and_names_of_customers(cursor):
    cursor.execute('SELECT email, name FROM users JOIN orders on users.id==orders.user_id GROUP BY users.id;')
    return cursor.fetchall()

# Для каждого товара вывести на каком складе он есть и в каком количестве
def get_quantity_of_products(cursor):
    cursor.execute('SELECT products.name,(SELECT warehouses.name FROM warehouses WHERE warehouses.id=warehousing.warehouse), warehousing.quantity FROM products LEFT JOIN warehousing WHERE warehousing.product=products.id')
    return cursor.fetchall()

# Вывести категории товаров, которые покупали польователи (только если они хотя бы раз делали заказ)
def get_types_of_ordered_products(cursor):
    cursor.execute('SELECT users.email, (SELECT types.name FROM types WHERE types.id = (SELECT products.type FROM products WHERE products.id = orders.id)) FROM users JOIN  orders ON orders.user_id=users.id;')
    return cursor.fetchall()


connection=sqlite3.connect('products.db')
cursor = connection.cursor()

req1 = get_emails_and_names_of_customers(cursor)
req2 = get_quantity_of_products(cursor)
req3 = get_types_of_ordered_products(cursor)

for line in req1:
    print(*line)

connection.close()