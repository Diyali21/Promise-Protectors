from flask import Blueprint, flash, redirect, render_template, request, url_for
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
    fullname = request.form.get("name")
    email = request.form.get("email")
    contact_no = request.form.get("contact_no")
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
            "fullname": fullname,
            "email": email,
            "contact_no": contact_no,
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


@auth_bp.post("/login")
def submit_login_page():
    username = request.form.get("username")
    password = request.form.get("password")  # abc@123
    try:
        # 🛡️ Validations
        if not username:
            raise ValueError("Username must be filled")

        if not password:
            raise ValueError("Password must be filled")

        # Select * from users
        #   where username = 'Ethan'
        #   Limit 1;
        user_from_db = User.query.filter_by(username=username).first()

        if not user_from_db:
            raise ValueError("Credentials are invalid")

        if not check_password_hash(user_from_db.password, password):
            raise ValueError("Credentials are invalid")

        return redirect(url_for("main_bp.home_page"))

    except Exception as e:
        print(user_from_db, username, password)
        print(e)
        db.session.rollback()
        return redirect(url_for("auth_bp.submit_login_page"))


@auth_bp.get("/logout")
def logout_page():
    logout_user()
    return redirect(url_for("auth_bp.submit_login_page"))
