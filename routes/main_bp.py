from pprint import pprint

from flask import Blueprint, render_template, request

from models.user import User

HTTP_NOT_FOUND = 404
main_bp = Blueprint("main_bp", __name__)


def get_user_details(username):
    return User.query.get(username)


#  API / Endpoint
@main_bp.get("/")
def home_page():
    return render_template("home.html")
