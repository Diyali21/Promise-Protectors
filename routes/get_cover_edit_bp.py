from pprint import pprint

from flask import Blueprint, render_template, request
from flask_login import login_required

from extensions import db
from models.policy_cover import PolicyCover
from models.policy_user import PolicyUser
from models.wedding import Wedding

HTTP_NOT_FOUND = 404
get_cover_edit_bp = Blueprint("get_cover_edit_bp", __name__)
