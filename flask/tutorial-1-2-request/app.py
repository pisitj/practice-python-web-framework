# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return {"message": "Hello World."}

# path parameter - str (default)
@app.route("/users/<id>", methods=['GET'])
def get_user_by_id(id):
    return {"message": f"Get User by ID - {type(id)}"}

# path parameter - int
@app.route("/users/<int:id>", methods=['PUT'])
def update_user_by_id(id):
    return {"message": f"Update User by ID - {type(id)}"}

# query paramter
@app.route("/users", methods=['GET'])
def get_user():
    return {"firstname": request.args.get('firstname'), "lastname": request.args.get('lastname')}

# request body
@app.route("/users", methods=['POST'])
def create_user():
    return request.get_json()
