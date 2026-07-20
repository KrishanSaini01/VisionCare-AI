from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from extensions import db
from extensions import bcrypt
from database.models import User

from flask_bcrypt import generate_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]

        email = request.form["email"]

        password = request.form["password"]

        confirm = request.form["confirm_password"]

        if password != confirm:

            flash("Passwords do not match", "danger")

            return redirect(url_for("auth.register"))

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:

            flash("Email already registered", "warning")

            return redirect(url_for("auth.register"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)

        db.session.commit()

        flash("Registration Successful", "success")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route("/login")
def login():

    return render_template("login.html")


@auth.route("/logout")
def logout():

    return "Logout"