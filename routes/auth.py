from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from extensions import db
from extensions import bcrypt
from database.models import User

from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
# OR use bcrypt.check_password_hash() as shown below

from flask_login import login_user, logout_user, login_required


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


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):

            login_user(user)

            flash("Login Successful", "success")

            return redirect(url_for("main.dashboard"))

        else:

            flash("Invalid Email or Password", "danger")

            return redirect(url_for("auth.login"))

    return render_template("login.html")


from flask_login import login_required

@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged out successfully.", "success")

    return redirect(url_for("main.home"))