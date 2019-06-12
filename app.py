from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, timedelta
from flask_cors import CORS, cross_origin

from security import authenticate, identity
from resources.contact import Contact
from resources.user import UserRegister

app = Flask(__name__)
app.secret_key = "secretkey"
api = Api(app)

cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


@app.before_first_request
def create_tables():
    db.create_all()

app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=10800)
jwt = JWT(app, authenticate, identity)

api.add_resource(Contact, '/contacts')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)