from datetime import datetime

from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

from models.user import User
from models.venue import Venue
from models.wedding import Wedding

HTTP_NOT_FOUND = 404
history_bp = Blueprint("history_bp", __name__)


@history_bp.get("/")
@login_required
def history_bp_page():
    now = datetime.now()
    venue_details = Venue.query.all()
    history = Wedding.query.filter(Wedding.wed_date < now).all()

    return render_template(
        "history.html", user=current_user, history=history, venue_details=venue_details
    )
