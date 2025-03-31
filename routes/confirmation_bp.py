from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
confirmation_bp = Blueprint("confirmation_bp", __name__)


#  API / Endpoint
@confirmation_bp.get("/")
def hello_world():
    return render_template("confirmation.html")
