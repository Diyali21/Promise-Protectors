from pprint import pprint
from webbrowser import get

from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_login import login_required

from models import wedding
from models.user import User
from models.wedding import Wedding

HTTP_NOT_FOUND = 404
main_bp = Blueprint("main_bp", __name__)


def get_user_details(username):
    if not username:
        return redirect(url_for("auth_bp.login_page"))
    return User.query.get(username)


#  API / Endpoint
@main_bp.get("/")
@login_required
def home_page():
    username = session.get("username")
    user = get_user_details(username)

    if not user:
        return redirect(url_for("auth_bp.login_page"))

    weddings = Wedding.query.filter_by(username=username)

    upcoming_events = []
    for wedding in weddings:
        upcoming_events.append(
            {
                "venue_name": wedding.venue_name,
                "wedding_date": wedding.wed_date,
                "no_guests": wedding._no_guests,
                "total_price": wedding.total_price,
            }
        )
    return render_template("home.html", user=user, upcoming_events=upcoming_events)
