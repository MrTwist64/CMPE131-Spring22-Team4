from app import db

from sqlalchemy import CheckConstraint, UniqueConstraint
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    securityQuestion = db.Column(db.String(128))
    question_answer_hash = db.Column(db.String(128))

    def set_security_answer(self, securityQuestionAnswer):
        self.question_answer_hash = generate_password_hash(securityQuestionAnswer)

    def check_security_answer(self, securityQuestionAnswer):
        return check_password_hash(self.question_answer_hash, securityQuestionAnswer)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Category(db.Model):
    categoryID = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(128), nullable=False, unique=True)

    def __repr__(self):
        return '<Category {}>'.format(self.category_name)


class Items(db.Model):
    itemID = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(64))
    condition = db.Column(db.String(64))
    description = db.Column(db.String(524))
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer)
    sellerID = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    categoryID = db.Column(db.Integer, nullable=False)
    CheckConstraint('price > 0', name='price_not_negative_check')
    CheckConstraint('quantity > 0', name='quantity_not_negative_check')

    def __repr__(self):
        return '<Items {} {} {} ${}>'.format(self.product_name, self.condition, self.price, self.quantity)

class Cart(db.Model):
    cartID = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    itemID = db.Column(db.Integer, db.ForeignKey('items.itemID', ondelete='CASCADE'))
    quantity = db.Column(db.Integer, nullable= False)
    createdAt = db.Column(db.DateTime, server_default=func.now())
    modifiedAt = db.Column(db.DateTime, onupdate=func.now())
    
    UniqueConstraint('id', 'cartID', 'itemID')
    
    CheckConstraint('quantity > 0', name='quantity_not_negative_check')
    CheckConstraint('quantity > 0', name='modifiedAt_not_earlier_check')
    def __repr__(self):
        return '<Cart {} {} {} {}>'.format(self.cartID, self.id, self.itemID, self.quantity)

