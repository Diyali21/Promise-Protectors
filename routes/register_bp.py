from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
register_bp = Blueprint("register_bp", __name__)


#  API / Endpoint
@register_bp.get("/")
def hello_world():
    return render_template("register.html")
