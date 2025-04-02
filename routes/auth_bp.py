from pprint import pprint

from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db
from models.user import User

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.get("/login")
def login_page():
    return render_template("login.html")


@auth_bp.post("/login")
def submit_login_page():
    pass


@auth_bp.get("/register")
def register_page():
    return render_template("register.html")


@auth_bp.post("/register")
def submit_register_page():
    # Only when all validation passes
    data = {
        "username": request.form.get("username"),
        "password": request.form.get("password"),
    }

    new_user = User(**data)
    try:
        print(new_user, new_user.to_dict())
        db.session.add(new_user)
        db.session.commit()
        # Todo: Take them to login page
        return redirect(url_for("auth_bp.login_page"))
    except Exception as e:
        print(e)
        db.session.rollback()
        return redirect(url_for("auth_bp.submit_register_page"))
