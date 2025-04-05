from pprint import pprint

from flask import Blueprint, flash, render_template, request
from flask_login import login_required

HTTP_NOT_FOUND = 404
contact_us_bp = Blueprint("contact_us_bp", __name__)


@contact_us_bp.get("/")
@login_required
def contact_us_bp_page():
    return render_template("contact-us.html")
