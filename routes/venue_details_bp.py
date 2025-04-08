from pprint import pprint

from flask import Blueprint, render_template, request
from flask_login import login_required

from models.venue import Venue

HTTP_NOT_FOUND = 404
venue_details_bp = Blueprint("venue_details_bp", __name__)


@venue_details_bp.get("/venue-details/<venue_id>")
@login_required
def venue_details_page(venue_id):
    venue = Venue.query.get(venue_id)

    venue_data = venue.to_dict()

    return render_template("venue_details.html", venue=venue_data)
