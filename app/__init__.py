from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myobj = Flask(__name__)
myobj.config.from_mapping(SECRET_KEY='password123')

db = SQLAlchemy(myapp_obj)
from app import routes, models
