import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'ak'
 # For Heroku Postgres get 'DATABASE_URL' from environment vars and if not there, get sqlite connection string
 # https://help.heroku.com/ZKNTJQSK/why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres
uri = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
jwt = JWT(app, authenticate, identity) # Creeates a new endpoint /auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    app.run(port=5000, debug=True)