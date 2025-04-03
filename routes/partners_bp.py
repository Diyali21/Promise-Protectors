from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
partners_bp = Blueprint("partners_bp", __name__)


@partners_bp.get("/")
def partners_bp_page():
    return render_template("partners.html")
