from app import myobj
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