import sqlite3
import unittest

class TestUM(unittest.TestCase):
    def setUp(self):
        connection=sqlite3.connect('products.db')
        self.cursor = connection.cursor()
    def test_get_emails(self):
        self.assertTrue(get_emails_and_names_of_customers(self.cursor),"Empty result")
    def test_quantity_is_correct(self):
        res=get_quantity_of_products(self.cursor)
        for el in res:
            self.assertTrue(isinstance(el[2],int),"Type of quantity data is incorrect")
    def test_get_types(self):
        self.assertTrue(get_types_of_ordered_products(self.cursor),"Empty result")


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

for line in req2:
    print(*line)

if __name__ == '__main__':
    unittest.main()

connection.close()