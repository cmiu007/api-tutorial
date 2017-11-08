from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'something123*()'
api = Api(app)
 
jwt = JWT(app, authenticate, identity)  # creates a new endpoint /auth

api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

<<<<<<< HEAD
if name == '__main__':
=======
if __name__ == '__main__':
>>>>>>> 75ce8ce148052c7fa0f09287a481d72c687b114f
    app.run(port=5000, debug=True)
