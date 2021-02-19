from flask import Blueprint


auth = Blueprint('auth', __name__)
@auth.route('admin')
def admin():
    return "<h1>hello Admin</h1>"