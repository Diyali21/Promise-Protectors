from pprint import pprint

from flask import Blueprint, flash, redirect, render_template, request, url_for

from extensions import db
from models.wedding import Wedding

HTTP_NOT_FOUND = 404
get_cover_bp = Blueprint("get_cover_bp", __name__)


@get_cover_bp.get("/")
def get_cover_bp_page():
    return render_template("get-cover.html")


@get_cover_bp.post("/")
def create_cover():
    data = {
        "no_guests": request.form.get("no_guests"),
        "wed_date": request.form.get("wed_date"),
        "venue_name": request.form.get("venue_name"),
    }

    new_cover = Wedding(**data)
    try:
        print(new_cover, new_cover.to_dict())
        db.session.add(new_cover)
        db.session.commit()
        flash("Success")
        return redirect(url_for("confirmation_bp.confirmation_page"))
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return redirect(url_for("get_cover_bp.create_cover"))
