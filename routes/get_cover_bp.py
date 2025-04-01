from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
get_cover_bp = Blueprint("get_cover_bp", __name__)


@get_cover_bp.get("/")
def get_cover_bp_page():
    return render_template("get-cover.html")
