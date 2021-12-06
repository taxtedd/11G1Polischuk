--Логины и имена всех пользователей, которые делали хотя бы один заказ
SELECT email, name FROM users JOIN orders on users.id==orders.user_id GROUP BY users.id;

--Для каждого товара вывести на каком складе он есть и в каком количестве
SELECT products.name AS 'Наименование',(SELECT warehouses.name FROM warehouses WHERE warehouses.id=warehousing.warehouse) AS 'Склад', warehousing.quantity AS 'Количество' FROM products LEFT JOIN warehousing
WHERE warehousing.product=products.id

--Вывести категории товаров, которые покупали польователи (только если они хотя бы раз делали заказ)
SELECT users.email AS 'e-mail', (SELECT types.name FROM types WHERE types.id=
	(SELECT products.type FROM products WHERE products.id = orders.id)) AS 'Тип товара' 
FROM users JOIN  orders ON orders.user_id=users.id;