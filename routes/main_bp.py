from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
main_bp = Blueprint("main_bp", __name__)


#  API / Endpoint
@main_bp.get("/")
def hello_world():
    return render_template("home.html", active_page="home")
