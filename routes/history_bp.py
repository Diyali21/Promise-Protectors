from flask import Blueprint, render_template, request
from flask_login import current_user

from models.user import User
from models.wedding import Wedding

HTTP_NOT_FOUND = 404
history_bp = Blueprint("history_bp", __name__)


@history_bp.get("/")
def history_bp_page():
    wedding = Wedding.query.all()
    return render_template("history.html", wedding=wedding)
