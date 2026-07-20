from flask import Flask

from config import Config

from extensions import db
from extensions import bcrypt
from extensions import login_manager

from database.models import User

from routes.main import main
from routes.auth import auth
from routes.prediction import prediction
from routes.history import history
from routes.chat import chat

app = Flask(__name__)

app.config.from_object(Config)

# Initialize Extensions
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Register Blueprints
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(prediction)
app.register_blueprint(history)
app.register_blueprint(chat)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)