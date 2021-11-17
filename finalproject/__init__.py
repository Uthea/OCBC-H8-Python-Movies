import os


from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from finalproject.config import BaseConfig, ProductionConfig, TestConfig

basedir = os.path.dirname(os.path.realpath(__file__))

authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Bearer {token}'
    }
}

app = Flask(__name__)
print(f"ENV : {os.getenv('FLASK_ENV')}")
if os.getenv('FLASK_ENV') == "production":
    app.config.from_object(ProductionConfig())
elif os.getenv('FLASK_ENV') == "test":
    app.config.from_object(TestConfig())
else:
    app.config.from_object(BaseConfig())


jwt = JWTManager(app)
api = Api(app, title="Movies API", authorizations=authorizations, security='Bearer')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from finalproject.auth.routes import api as ns1
from finalproject.movies.routes import api as ns2
from finalproject.directors.routes import api as ns3

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)

if __name__ == '__main__':
    app.run(debug=True)
