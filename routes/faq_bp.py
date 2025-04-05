from pprint import pprint

from flask import Blueprint, render_template, request
from flask_login import login_required

HTTP_NOT_FOUND = 404
faq_bp = Blueprint("faq_bp", __name__)


@faq_bp.get("/")
@login_required
def faq_bp_page():
    return render_template("faq.html")
