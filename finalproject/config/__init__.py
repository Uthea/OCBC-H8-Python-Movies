import os
from datetime import timedelta
from os.path import dirname

'''
This file contains all the flask config parameters
'''

basedir = os.path.dirname(os.path.realpath(__file__))


def get_db_url():
    db_url = os.getenv('DATABASE_URL')
    if db_url:
        return db_url.replace("postgres", "postgresql")  # heroku prefix db url with postgres instead of postgresql

    return db_url


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dirname(basedir), 'final_proj_jwt.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    JWT_TOKEN_LOCATION = ['headers']
    JWT_SECRET_KEY = "super-secret"  # Change this!
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = get_db_url()


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = get_db_url()
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    PROPAGATE_EXCEPTIONS = True
