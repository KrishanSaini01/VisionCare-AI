from flask import (
    Blueprint,
    render_template,
    request
)

from flask_login import login_required

from ai.chatbot import ask_medical_ai

chat = Blueprint(
    "chat",
    __name__
)


@chat.route("/chat", methods=["GET", "POST"])
@login_required
def medical_chat():

    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        answer = ask_medical_ai(question)

    return render_template(
        "chat.html",
        answer=answer
    )