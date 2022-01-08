# https://github.com/gothinkster/flask-realworld-example-app/blob/master/conduit/user/views.py

from flask import Blueprint

blueprint = Blueprint('users', __name__, url_prefix='/users')

@blueprint.route("/", methods=('GET',))
def get_user_list():
    return {"message": "Get List of Users."}

@blueprint.route("/", methods=('POST',))
def create_user():
    return {"message": "Create a User."}