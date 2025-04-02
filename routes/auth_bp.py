from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db
from models.user import User

HTTP_NOT_FOUND = 404
auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.get("/register")
def register_page():
    return render_template("register.html")


@auth_bp.get("/login")
def login_page():
    return render_template("login.html")


@auth_bp.post("/register")
def submit_register_page():
    username = request.form.get("username")
    password = request.form.get("password")
    confirm = request.form.get("confirm")
    try:
        # 🛡️ Validations
        if not username:
            raise ValueError("Username must be filled")

        if not password:
            raise ValueError("Password must be filled")

        if password != confirm:
            raise ValueError("Password does not match")

        # Only when all validation passes
        hashed_password = generate_password_hash(password)
        data = {
            "username": username,
            "password": hashed_password,
        }

        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("auth_bp.login_page"))
    except Exception as e:
        print(e)
        db.session.rollback()
        return redirect(url_for("auth_bp.submit_register_page"))
