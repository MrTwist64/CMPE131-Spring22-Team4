from app import db
from sqlalchemy import CheckConstraint, select 

class User(db.Model):
    uID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Category(db.Model):
    categoryID = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(128), nullable= False, unique=True)

    def __repr__(self):
        return '<Category {}>'.format(self.category_name)

class Items(db.Model):
    itemID = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(64))
    condition = db.Column(db.String(64))
    description = db.Column(db.String(524))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    sellerID = db.Column(db.Integer,  db.ForeignKey('user.uID'))
    categoryID = db.Column(db.Integer, nullable = False)
    CheckConstraint('price > 0', name='price_not_negative_check')
    def __repr__(self):
        return '<Items {} {} {} ${}>'.format(self.product_name, self.condition, self.price, self.quantity)

