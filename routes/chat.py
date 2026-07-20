from flask import Blueprint, render_template
chat = Blueprint("chat", __name__)

@chat.route("/chat")
def medical_chat():
    return render_template("chat.html")