from pprint import pprint

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from extensions import db
from models.insurance_cover import InsureCover
from models.policy_cover import PolicyCover
from models.policy_user import PolicyUser
from models.venue import Venue
from models.wedding import Wedding

HTTP_NOT_FOUND = 404
get_cover_bp = Blueprint("get_cover_bp", __name__)


@get_cover_bp.get("/")
@login_required
def get_cover_bp_page():
    venue = Venue.query.all()
    covers = InsureCover.query.all()
    return render_template("get-cover.html", venue=venue, covers=covers)


@get_cover_bp.post("/")
def create_cover():
    data = {
        "no_guests": request.form.get("no_guests"),
        "wed_date": request.form.get("wed_date"),
        "venue_id": request.form.get("venue_id"),
        "selected_cover": request.form.getlist("covers"),
    }

    total_price = 0
    coverage_name = []
    coverage_price = []
    cover_id = []

    for cover_details in data["selected_cover"]:
        cover = InsureCover.query.get(cover_details)
        if cover:
            total_price += cover.cover_price
            coverage_name.append(cover.cover_name)
            coverage_price.append(cover.cover_price)
            cover_id.append(cover.cover_id)

    try:
        new_cover = Wedding(
            no_guests=data["no_guests"],
            wed_date=data["wed_date"],
            total_price=total_price,
            username=current_user.username,
            venue_id=data["venue_id"],
        )

        new_policy_user = PolicyUser(username=current_user.username)

        db.session.add(new_cover)
        db.session.add(new_policy_user)
        db.session.commit()

        return redirect(
            url_for(
                "confirmation_bp.confirmation_page",
                total_price=total_price,
                wed_date=data["wed_date"],
                coverage_name=coverage_name,
                coverage_price=coverage_price,
                venue_id=data["venue_id"],
                cover_id=cover_id,
                policy_id=new_policy_user.policy_id,
            ),
        )

    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return redirect(url_for("get_cover_bp.create_cover"))
