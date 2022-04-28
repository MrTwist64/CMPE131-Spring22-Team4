import os
basedir = os.path.abspath(os.path.dirname(__file__))
#Sets a path to the database
app.config.from_mapping(
    SECRET_KEY = ‘you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False)
