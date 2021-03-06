BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "warehouses" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	"address"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "warehousing" (
	"id"	INTEGER,
	"product"	INTEGER NOT NULL,
	"warehouse"	INTEGER NOT NULL,
	"quantity"	INTEGER NOT NULL,
	FOREIGN KEY("warehouse") REFERENCES "warehouses"("id"),
	FOREIGN KEY("product") REFERENCES "products"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "types" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "products" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL,
	"price"	INTEGER NOT NULL,
	"discount"	INTEGER NOT NULL,
	"photo"	BLOB,
	"details"	TEXT NOT NULL,
	"type"	INTEGER,
	FOREIGN KEY("type") REFERENCES "types"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "orders" (
	"id"	INTEGER,
	"user_id"	INTEGER NOT NULL,
	"order_date"	TEXT NOT NULL,
	"total_amount"	INTEGER NOT NULL,
	"product"	INTEGER,
	"quantity"	INTEGER NOT NULL,
	"discount"	INTEGER,
	FOREIGN KEY("product") REFERENCES "products"("id"),
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER,
	"email"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"surname"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"patronymic"	TEXT,
	"city"	TEXT NOT NULL,
	"address"	TEXT NOT NULL,
	"phone"	TEXT NOT NULL UNIQUE,
	"registration_date"	STRING,
	"birth_date"	STRING,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "warehouses" VALUES (1,'Склад 1','г.Москва, ул.1-я Крылатская, д.17');
INSERT INTO "warehouses" VALUES (2,'Склад 2','г.Москва, ул.Церковная Горка, д.91');
INSERT INTO "warehouses" VALUES (3,'Склад 3','г.Москва, ул.Декабристов, д.174');
INSERT INTO "warehousing" VALUES (1,1,1,50);
INSERT INTO "warehousing" VALUES (2,2,1,50);
INSERT INTO "warehousing" VALUES (3,3,2,50);
INSERT INTO "warehousing" VALUES (4,4,3,55);
INSERT INTO "types" VALUES (1,'Парафиновые свечи');
INSERT INTO "types" VALUES (2,'Гелевые свечи');
INSERT INTO "types" VALUES (3,'Восковые свечи');
INSERT INTO "products" VALUES (1,'Mixed berry candle',500,0,NULL,'Аромат: Rich cherries start this sweet gourmand fragrance, finished with silky almonds and creamy vanilla.',1);
INSERT INTO "products" VALUES (2,'White jasmine candle',500,0,NULL,'Аромат: A pretty floral bouquet with white lily, honeysuckle and jasmine notes.',1);
INSERT INTO "products" VALUES (3,'Pure lilen candle',500,0,NULL,'Аромат: A clean and refreshing scent with marine notes and soft musks.',1);
INSERT INTO "products" VALUES (4,'Island spa candle',500,0,NULL,'Аромат: An aromatic accord of eucalyptus, bergamot and green tea above a soft woody base.',1);
INSERT INTO "orders" VALUES (1,1,'2021-11-17 15:00',1000,3,2,0);
INSERT INTO "orders" VALUES (2,2,'2021-10-27 19:15',500,1,1,0);
INSERT INTO "orders" VALUES (3,3,'2021-11-16 16:25',500,2,1,0);
INSERT INTO "users" VALUES (1,'ivanov@gmail.com','123','Иванов','Иван','Иванович','Москва','Балаклавский проспект, дом 6А','8(916)111-11-11','2021-05-12','2003-04-03');
INSERT INTO "users" VALUES (2,'rubkin@gmail.com','222','Рыбкин','Василий','Иванович','Москва','Балаклавский проспект, дом 5А','8(916)222-22-22','2021-10-22','2003-07-28');
INSERT INTO "users" VALUES (3,'petrovil@gmail.com','321','Петров','Илья','Ильич','Москва','Балаклавский проспект, дом 3А','8(916)333-33-33','2021-09-25','2000-12-19');
COMMIT;
