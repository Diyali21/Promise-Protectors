from pprint import pprint

from flask import Blueprint, render_template, request

from extensions import db
from models.policy_cover import PolicyCover
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
    venue_id = request.args.get("venue_id")
    venues = Venue.query.filter_by(venue_id=venue_id)
    cover_id = request.args.getlist("cover_id")
    policy_id = request.args.get("policy_id")

    try:
        for cover_data in cover_id:
            new_policy_cover = PolicyCover(policy_id=policy_id, cover_id=cover_data)
            db.session.add(new_policy_cover)

        db.session.commit()

        return render_template(
            "confirmation.html",
            total_price=total_price,
            wed_date=wed_date,
            coverage_name=coverage_name,
            coverage_price=coverage_price,
            venue_id=venue_id,
            venues=venues,
            cover_id=cover_id,
            policy_id=policy_id,
        )
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
