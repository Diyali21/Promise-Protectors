from pprint import pprint

from flask import Blueprint, render_template, request

from models import venue
from models.venue import Venue

HTTP_NOT_FOUND = 404
confirmation_bp = Blueprint("confirmation_bp", __name__)


#  API / Endpoint
@confirmation_bp.get("/")
def confirmation_page():
    total_price = request.args.get("total_price")
    wed_date = request.args.get("wed_date")
    coverage_name = request.args.getlist("coverage_name")
    coverage_price = request.args.getlist("coverage_price")
    venue_name = request.args.get("venue_name")
    venues = Venue.query.all()

    return render_template(
        "confirmation.html",
        total_price=total_price,
        wed_date=wed_date,
        coverage_name=coverage_name,
        coverage_price=coverage_price,
        venue_name=venue_name,
        venues=venues,
    )
