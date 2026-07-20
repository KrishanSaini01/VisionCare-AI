from flask import Blueprint, render_template
from flask_login import login_required, current_user

from database.models import Prediction

history = Blueprint(
    "history",
    __name__
)

@history.route("/history")
def history_page():
    return render_template("history.html")