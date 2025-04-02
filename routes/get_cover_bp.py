from pprint import pprint

from flask import Blueprint, flash, redirect, render_template, request, url_for

from extensions import db
from models.insurance_cover import InsureCover
from models.venue import Venue
from models.wedding import Wedding

HTTP_NOT_FOUND = 404
get_cover_bp = Blueprint("get_cover_bp", __name__)


@get_cover_bp.get("/")
def get_cover_bp_page():
    venue = Venue.query.all()
    covers = InsureCover.query.all()
    return render_template("get-cover.html", venue=venue, covers=covers)


@get_cover_bp.post("/")
def create_cover():
    data = {
        "no_guests": request.form.get("no_guests"),
        "wed_date": request.form.get("wed_date"),
        "venue_name": request.form.get("venue_name"),
        "selected_cover": request.form.getlist("covers"),
    }

    total_price = 0

    for cover_name in data["selected_cover"]:
        cover = InsureCover.query.get(cover_name)
        if cover:
            total_price += cover.cover_price

    try:
        new_cover = Wedding(
            no_guests=data["no_guests"],
            wed_date=data["wed_date"],
            venue_name=data["venue_name"],
            total_price=total_price,
        )
        db.session.add(new_cover)
        db.session.commit()

        return redirect(
            url_for("confirmation_bp.confirmation_page", total_price=total_price)
        )
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return redirect(url_for("get_cover_bp.create_cover"))
