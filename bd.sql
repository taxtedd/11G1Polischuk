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
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("warehouse") REFERENCES "warehouses"("id"),
	FOREIGN KEY("product") REFERENCES "products"("id")
);
CREATE TABLE IF NOT EXISTS "orders" (
	"id"	INTEGER,
	"user_id"	INTEGER NOT NULL,
	"order_date"	TEXT NOT NULL,
	"total_amount"	INTEGER NOT NULL,
	"product"	INTEGER,
	"quantity"	INTEGER NOT NULL,
	"discount"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	FOREIGN KEY("product") REFERENCES "product"("id")
);
CREATE TABLE IF NOT EXISTS "types" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
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
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("type") REFERENCES "types"("id")
);
INSERT INTO "warehouses" VALUES (1,'Склад 1','г.Москва, ул.1-я Крылатская, д.17');
INSERT INTO "warehouses" VALUES (2,'Склад 2','г.Москва, ул.Церковная Горка, д.91');
INSERT INTO "warehouses" VALUES (3,'Склад 3','г.Москва, ул.Декабристов, д.174');
INSERT INTO "types" VALUES (1,'Парафиновые свечи');
INSERT INTO "types" VALUES (2,'Гелевые свечи');
INSERT INTO "types" VALUES (3,'Восковые свечи');
INSERT INTO "users" VALUES (1,'ivanov@gmail.com','123','Иванов','Иван','Иванович','Москва','Балаклавский проспект, дом 6А','8(916)111-11-11');
INSERT INTO "users" VALUES (2,'rubkin@gmail.com','222','Рыбкин','Василий','Иванович','Москва','Балаклавский проспект, дом 5А','8(916)222-22-22');
INSERT INTO "users" VALUES (3,'petrovil@gmail.com','321','Петров','Илья','Ильич','Москва','Балаклавский проспект, дом 3А','8(916)333-33-33');
INSERT INTO "products" VALUES (1,'Mixed berry candle',500,0,NULL,'Аромат: Rich cherries start this sweet gourmand fragrance, finished with silky almonds and creamy vanilla.',NULL);
INSERT INTO "products" VALUES (2,'White jasmine candle',500,0,NULL,'Аромат: A pretty floral bouquet with white lily, honeysuckle and jasmine notes.',NULL);
INSERT INTO "products" VALUES (3,'Pure lilen candle',500,0,NULL,'Аромат: A clean and refreshing scent with marine notes and soft musks.',NULL);
INSERT INTO "products" VALUES (4,'Island spa candle',500,0,NULL,'Аромат: An aromatic accord of eucalyptus, bergamot and green tea above a soft woody base.',NULL);
COMMIT;
