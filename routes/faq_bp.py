from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
faq_bp = Blueprint("faq_bp", __name__)


@faq_bp.get("/")
def sample_bp_page():
    return render_template("faq.html", active_page="faq")
