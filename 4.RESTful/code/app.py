from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'something123*()'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # creates a new endpoint /auth

items = []

# Resource accesed with a get method


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be empty!"
    )

    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # returns the first item that match
        item = next(filter(lambda x: x['name'] == name, items), None)
        # item = list(filter(lambda x: x['name'] == name, items)) # returns the list of items that match condition
        # same as - 200 if item is not None else 404
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # Error first aproach
        
        if next(filter(lambda x: x['name'] == name, items), None):
            # 400 = bad request
            return {'message': "item with name: '{}' is allready in DB!".format(name)}, 400

        # only 'price' is passed, any other fields are dropped
        # data = request.get_json() # replaced by parser
        data = Item.parser.parse_args()

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items  # use items global variable to initialise local variable
        if next(filter(lambda x: x['name'] == name, items), None):
            items = list(filter(lambda x: x['name'] != name, items))
            return {'message': 'Item deleted'}, 201
        return {'message': "Not deleted, item with name:'{}' was not found".format(name)}, 400

    def put(self, name):
        # il mutam la nivel de obiect

        # parser = reqparse.RequestParser()
        # parser.add_argument(
        #     'price',
        #     type=float,
        #     required=True,
        #     help="This field cannot be empty!"
        # )

        # only 'price' is passed, any other fields are dropped
        # data = request.get_json() # replaced by parser
        # data = parser.parse_args()

        Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
            return item, 201
        else:
            item.update(data)
            return item, 200


class ItemList(Resource):
    def get(self):
        return {'items': items}, 200


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


app.run(port=5000, debug=True)
