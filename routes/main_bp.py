from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required

from extensions import db
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
        return render_template("not-found.html")

    policy = PolicyUser.query.filter_by(wed_id=wedding.wed_id).first()

    if not policy:
        return render_template("not-found.html")
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
        wed_id=wed_id,
    )


@main_bp.get("/get-cover-edit")
def get_cover_edit_page():
    wed_id = request.args.get("wed_id")
    wedding = Wedding.query.get(wed_id)
    venue = Venue.query.all()
    covers = InsureCover.query.all()

    policy = PolicyUser.query.filter_by(wed_id=wed_id).first()

    policy_covers = PolicyCover.query.filter_by(policy_id=policy.policy_id).all()

    covers_policy = []

    for pc in policy_covers:
        cover = InsureCover.query.get(pc.cover_id)

        if cover:
            covers_policy.append(pc.cover_id)

    return render_template(
        "get-cover-edit.html",
        venue=venue,
        covers=covers,
        wedding=wedding,
        policy=policy,
        covers_policy=covers_policy,
    )


@main_bp.post("/get-cover-edit")
def update_page():
    wedd_id = request.form.get("wed_id")

    policy_user = PolicyUser.query.filter_by(wed_id=wedd_id).first()

    policy_cover = PolicyCover.query.filter_by(policy_id=policy_user.policy_id).all()

    if not policy_user:
        return render_template("not-found.html")

    pu = policy_user.to_dict()

    if not policy_cover:
        return render_template("not-found.html")

    for pc in policy_cover:
        db.session.delete(pc)
    db.session.commit()

    selected_cover = request.form.getlist("covers")

    for sc in selected_cover:
        new_policy_cover = PolicyCover(policy_id=policy_user.policy_id, cover_id=sc)
        db.session.add(new_policy_cover)
    db.session.commit()

    flash("Details updated successfully", "success")

    return render_template("about.html")
