from datetime import datetime
from pprint import pprint
from webbrowser import get

from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_login import login_required

from models import wedding
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

    weddings = Wedding.query.filter(Wedding.wed_date > now).all()

    venue_details = Venue.query.all()

    return render_template("home.html", weddings=weddings, venue_details=venue_details)
