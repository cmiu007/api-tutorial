import sqlite3
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

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
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"

        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        print(row)
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}, 200

        return {'message': 'Item not found'}, 404

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

        data = Item.parser.parse_args()

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