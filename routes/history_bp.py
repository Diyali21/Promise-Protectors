from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
history_bp = Blueprint("history_bp", __name__)


@history_bp.get("/")
def history_bp_page():
    return render_template("history.html")
