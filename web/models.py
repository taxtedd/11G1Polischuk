from init import db

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    email = db.Column(db.String(80), nullable=False)
    text = db.Column(db.String(256))

    def __repr__(self):
        return f'feedback name: {self.email}'

class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.id} {self.name}'

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(80))
    details = db.Column(db.Integer, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey(Types.id),nullable=False)
    type = db.relationship('Types', backref=db.backref('Items', lazy=False))

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
    item_id = db.Column(db.Integer, db.ForeignKey(Items.id), nullable=False)
    item = db.relationship('Items', backref=db.backref('Warehousing', lazy=True))
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
        return f'{self.id} - {self.email} - {self.phone} - {self.surname}'


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey(Users.id), nullable=False)
    user_id = db.relationship('Users', backref=db.backref('Orders', lazy=False))
    order_date = db.Column(db.String(80), nullable=False)
    total_amount = db.Column(db.Integer, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey(Items.id), nullable=False)
    item = db.relationship('Items', backref=db.backref('Orders', lazy=False))
    quantity = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id} - Пользователь: {self.user_id} Заказ на сумму: {self.total_amount}'