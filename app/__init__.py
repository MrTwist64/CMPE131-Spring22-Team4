from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# what is the directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

myobj = Flask(__name__)

myobj.config.from_mapping(
    SECRET_KEY='password123',
    # where to store app.db (database file)
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db')
)

myobj.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(myobj)

from app import routes, models
