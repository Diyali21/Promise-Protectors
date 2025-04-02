from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
login_bp = Blueprint("login_bp", __name__)


#  API / Endpoint
@login_bp.get("/")
def hello_world():
    return render_template("login.html")
