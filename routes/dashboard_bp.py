from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
dashboard_bp = Blueprint("dashboard_bp", __name__)


@dashboard_bp.get("/")
def dashboard_bp_page():
    return render_template(
        "dashboard.html",
    )
