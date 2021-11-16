import os.path
import os
from datetime import timedelta


from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from finalproject.config import BaseConfig, ProductionConfig

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
else:
    app.config.from_object(BaseConfig())


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'final_proj_jwt.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['JWT_TOKEN_LOCATION'] = ['headers']
# app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
# app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)
api = Api(app, title="Movies API", authorizations=authorizations, security='Bearer', errors=Flask.errorhandler)
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
