from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
reviews_bp = Blueprint("reviews_bp", __name__)


@reviews_bp.get("/")
def reviews_bp_page():
    return render_template("reviews.html", active_page="reviews")
