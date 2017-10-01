from flask import Flask

app = Flask(__name__)

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}

# GET /store/<string:name>
# GET /store
# POST /store/<string:name>/item {name:, price}
# GET /store/<string:name>/item


app.run(port=5000)