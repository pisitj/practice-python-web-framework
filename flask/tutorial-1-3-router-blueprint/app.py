# https://github.com/gothinkster/flask-realworld-example-app/blob/master/conduit/app.py

from flask import Flask
from items.views import blueprint as items_blueprint
from users.views import blueprint as users_blueprint

app = Flask(__name__)
app.url_map.strict_slashes = False

app.register_blueprint(items_blueprint)
app.register_blueprint(users_blueprint)

@app.route("/", methods=['GET'])
def hello():
    return {"message": "Hello World."}