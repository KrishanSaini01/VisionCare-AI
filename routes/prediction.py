import os
from model.predict import predict_image
from ai.gemini import generate_ai_report
from ai.fallback import fallback_report


from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from werkzeug.utils import secure_filename

from extensions import db

from database.models import Prediction

from model.predict import predict_image


prediction = Blueprint(
    "prediction",
    __name__
)


UPLOAD_FOLDER = "static/uploads"

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png"
}


def allowed_file(filename):

    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@prediction.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    if request.method == "POST":

        if "image" not in request.files:

            flash("Please select an image.", "danger")

            return redirect(request.url)

        file = request.files["image"]

        if file.filename == "":

            flash("Please choose an image.", "warning")

            return redirect(request.url)

        if not allowed_file(file.filename):

            flash("Only JPG, JPEG and PNG images are allowed.", "danger")

            return redirect(request.url)

        # -------------------------
        # Save Image
        # -------------------------

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        file.save(filepath)

        # -------------------------
        # CNN Prediction
        # -------------------------

        result = predict_image(filepath)

        disease = result["disease"]

        confidence = result["confidence"]

        # -------------------------
        # AI Medical Report
        # -------------------------

        try:

            summary = generate_ai_report(
                disease,
                confidence
            )

        except Exception:

            summary = fallback_report(
                disease,
                confidence
            )

        precautions = ""

        # -------------------------
        # Save to MySQL
        # -------------------------

        new_prediction = Prediction(

            user_id=current_user.id,

            image_path=filename,

            disease_name=disease,

            confidence_score=confidence,

            ai_summary=summary,

            precautions=precautions

        )

        db.session.add(new_prediction)

        db.session.commit()

        flash(
            "Prediction completed successfully.",
            "success"
        )

        return render_template(

            "prediction.html",

            prediction=new_prediction

        )

    return render_template("upload.html")


@prediction.route("/prediction/<int:prediction_id>")
@login_required
def view_prediction(prediction_id):

    prediction_data = Prediction.query.filter_by(
        prediction_id=prediction_id,
        user_id=current_user.id
    ).first_or_404()

    return render_template(
        "prediction.html",
        prediction=prediction_data
    )