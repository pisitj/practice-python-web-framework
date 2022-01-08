# https://github.com/gothinkster/flask-realworld-example-app/blob/master/conduit/user/views.py

from flask import Blueprint

blueprint = Blueprint('items', __name__, url_prefix='/items')

@blueprint.route("/", methods=('GET',))
def get_item_list():
    return {"message": "Get List of Items."}

@blueprint.route("/", methods=('POST',))
def create_item():
    return {"message": "Create a Item."}