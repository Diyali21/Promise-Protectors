from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
contact_us_bp = Blueprint("contact_us_bp", __name__)


@contact_us_bp.get("/")
def contact_us_bp_page():
    return render_template("contact-us-page.html")
