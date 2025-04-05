from pprint import pprint

from flask import Blueprint, render_template, request
from flask_login import login_required

HTTP_NOT_FOUND = 404
venue_details_bp = Blueprint("venue_details_bp", __name__)


@venue_details_bp.get("/")
@login_required
def venue_details_bp_page():
    return render_template("venue-details.html")
