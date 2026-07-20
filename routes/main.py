from flask import Blueprint, render_template
from flask_login import login_required, current_user

from database.models import Prediction

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/dashboard")
@login_required
def dashboard():

    predictions = Prediction.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Prediction.prediction_date.desc()
    ).all()

    total_predictions = len(predictions)
    total_uploads = len(predictions)
    total_reports = len(predictions)
    total_chats = 0

    return render_template(
        "dashboard.html",
        predictions=predictions,
        total_predictions=total_predictions,
        total_uploads=total_uploads,
        total_reports=total_reports,
        total_chats=total_chats
    )