--Логины и фамилии всех пользователей, которые делали хотя бы один заказ
SELECT email, surname FROM users JOIN orders on users.id==orders.user_id;

--Для каждого товара вывести на каком складе он есть и в каком количестве
SELECT products.name AS 'Наименование',(SELECT warehouses.name FROM warehouses WHERE warehouses.id=warehousing.warehouse) AS 'Склад', warehousing.quantity AS 'Количество' FROM products LEFT JOIN warehousing
WHERE warehousing.product=products.id

--не доделала: Вывести пользователей, которым (меньше 18 лет) или (старше 60)
SELECT users.email FROM users WHERE (SUBSTR(CURRENT_DATE,1,4)-SUBSTR(birth_date,1,4))-(SUBSTR(CURRENT_DATE,6,5)<SUBSTR(birth_date,6,5))<18
UNION
SELECT users.email FROM users, orders WHERE (SUBSTR(CURRENT_DATE,1,4)-SUBSTR(birth_date,1,4))-(SUBSTR(CURRENT_DATE,6,5)<SUBSTR(birth_date,6,5))>60 AND orders.user_id=users.id