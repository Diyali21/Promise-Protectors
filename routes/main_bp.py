from datetime import datetime

from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required

from models.insurance_cover import InsureCover
from models.policy_cover import PolicyCover
from models.policy_user import PolicyUser
from models.user import User
from models.venue import Venue
from models.wedding import Wedding

HTTP_NOT_FOUND = 404
main_bp = Blueprint("main_bp", __name__)


def get_user_details(username):
    if not username:
        return redirect(url_for("auth_bp.login_page"))
    return User.query.get(username)


#  API / Endpoint
@main_bp.get("/")
def home_page():
    username = session.get("username")
    user = get_user_details(username)

    if not user:
        return redirect(url_for("auth_bp.login_page"))
    now = datetime.now()
    weddings = (
        Wedding.query.filter(Wedding.wed_date > now)
        .order_by(Wedding.wed_date.asc())
        .all()
    )


@main_bp.get("/<venue_id>")
@login_required
def venue_details_page(venue_id):
    venue = Venue.query.get(venue_id)

    if not venue:
        return render_template("home.html")

    venue_data = venue.to_dict()

    return render_template("venue_details.html", venue=venue_data)
=======
    user_wedding = Wedding.query.filter_by(username=username)

    user_wedding = []

    for wed in weddings:
        user_wedding.append(wed.username)

    venue_details = Venue.query.all()

    return render_template(
        "home.html",
        weddings=weddings,
        venue_details=venue_details,
        user_wedding=user_wedding,
        now=now,
    )


@main_bp.get("/<wed_id>")
def profile_page(wed_id):
    wedding = Wedding.query.filter_by(
        wed_id=wed_id, username=current_user.username
    ).first()

    if not wedding:
        return "You have no upcoming events"

    policy = PolicyUser.query.filter_by(wed_id=Wedding.wed_id).first()

    if not policy:
        return "You have no upcoming events"
    policy_covers = PolicyCover.query.filter_by(policy_id=policy.policy_id).all()

    covers = []

    for pc in policy_covers:
        cover = InsureCover.query.get(pc.cover_id)

        if cover:
            covers.append(cover)

        venue_details = Venue.query.all()

    return render_template(
        "profile.html",
        wedding=wedding,
        policy=policy,
        covers=covers,
        venue_details=venue_details,
    )

