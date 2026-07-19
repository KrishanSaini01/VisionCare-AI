import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:"
    f"{quote_plus(os.getenv('MYSQL_PASSWORD'))}@"
    f"{os.getenv('MYSQL_HOST')}/"
    f"{os.getenv('MYSQL_DB')}"
)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = "uploads"

    MODEL_PATH = "model/cnn_model.keras"

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")