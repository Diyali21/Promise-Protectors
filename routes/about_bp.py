from pprint import pprint

from flask import Blueprint, render_template, request
from flask_login import login_required

HTTP_NOT_FOUND = 404
about_bp = Blueprint("about_bp", __name__)


@about_bp.get("/")
@login_required
def about_bp_page():
    return render_template("about.html")
