from flask import Flask

myobj = Flask(__name__)
myobj.config.from_mapping(SECRET_KEY='password123')

from app import routes