from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
reviews_bp = Blueprint("reviews_bp", __name__)


#  API / Endpoint
@reviews_bp.get("/")
def hello_world():
    return render_template("reviews_bp")
