from flask import Flask
from config import Config

from database.database import db
from database.models import User

app = Flask(__name__)

# Load Configuration
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

# Create Tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "<h1>VisionCare AI Backend Running Successfully!</h1>"


if __name__ == "__main__":
    app.run(debug=True)