from app import myobj, db
from app.models import User, Category, Items
from flask import flash, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

@myobj.route('/', methods=['GET', 'POST'])
@myobj.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@myobj.route('/about.html', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@myobj.route('/login.html', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@myobj.route('/all_items.html', methods=['GET', 'POST'])
def all_items():
    items = Items.query.all()
    categories = Category.query.all()
    return render_template('all_items.html', items=items, categories=categories)

@myobj.route('/i/<int:itemID>', methods=['GET', 'POST'])
def view_item(itemID):
    item = Items.query.get(itemID)
    category = Category.query.get(item.categoryID).category_name
    seller = User.query.get(item.sellerID).username
    return render_template('item.html', item=item, category=category, seller=seller)