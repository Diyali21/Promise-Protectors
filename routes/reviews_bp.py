from pprint import pprint

from flask import Blueprint, render_template, request
from flask_login import login_required

HTTP_NOT_FOUND = 404
reviews_bp = Blueprint("reviews_bp", __name__)


@reviews_bp.get("/")
@login_required
def reviews_bp_page():
    return render_template("reviews.html")
