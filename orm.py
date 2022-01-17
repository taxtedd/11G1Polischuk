from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
db = SQLAlchemy(app)


class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.id} {self.name}'


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(80))
    details = db.Column(db.Integer, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey(Types.id),nullable=False)
    type = db.relationship('Types', backref=db.backref('Products', lazy=False))

    def __repr__(self):
        return f'{self.id} - Наименование: {self.name} Цена:{self.price}'

class Warehouses(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True,nullable=False)
    address = db.Column(db.String(80),nullable=False)

    def __repr__(self):
        return f'{self.id} {self.name} {self.address}'

class Warehousing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(Products.id), nullable=False)
    product = db.relationship('Products', backref=db.backref('Warehousing', lazy=True))
    warehouse_id = db.Column(db.Integer, db.ForeignKey(Warehouses.id), nullable=False)
    warehouse = db.relationship('Warehouses', backref=db.backref('Warehousing', lazy=False))
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'На складе {self.warehouse_id} {self.quantity} ед. {self.product_id}'


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    patronymic = db.Column(db.String(80))
    city = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), unique=True, nullable=False)
    registration_date = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.String(80))

    def __repr__(self):
        return f'{self.id} - {self.email}, {self.phone} - {self.surname}'


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey(Users.id), nullable=False)
    user_id = db.relationship('Users', backref=db.backref('Orders', lazy=False))
    order_date = db.Column(db.String(80), nullable=False)
    total_amount = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(Products.id), nullable=False)
    product = db.relationship('Products', backref=db.backref('Orders', lazy=False))
    quantity = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id} - Пользователь: {self.user_id} Заказ на сумму: {self.total_amount}'


db.create_all()
create_type = Types(name="Парафиновые свечи")
db.session.add(create_type)
product = Products(name="Mixed berry candle", price=500, discount=0,details="Аромат: Rich cherries start this sweet gourmand fragrance, finished with silky almonds and creamy vanilla.", type=create_type)
db.session.add(product)
warehouse = Warehouses(name="Склад 1", address="г.Москва, ул.1-я Крылатская, д.17")
db.session.add(warehouse)
create_warehousing = Warehousing(product_id=1, warehouse_id=1, quantity=50)
db.session.add(create_warehousing)
user = Users(email='ivanov@gmail.com', password='123', surname='Иванов', name='Иван', patronymic='Иванович', city='Москва', address='Балаклавский проспект, дом 6А', phone='8(916)111-11-11', registration_date='2021-05-12', birth_date='2003-04-03')
db.session.add(user)
order = Orders(user=1,order_date='2021-11-17 15:00', total_amount=1000,product_id=1,quantity=2,discount=0)
db.session.add(order)
db.session.commit()
print(Orders.query.all())