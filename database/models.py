from flask_login import UserMixin
from extensions import db


class User(UserMixin,db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )
     
from datetime import datetime

class Prediction(db.Model):

    __tablename__ = "predictions"

    prediction_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    image_path = db.Column(
        db.String(255),
        nullable=False
    )

    disease_name = db.Column(
        db.String(100),
        nullable=False
    )

    confidence_score = db.Column(
        db.Float,
        nullable=False
    )
    
    ai_summary = db.Column(
    db.Text,
    nullable=True
    )

    precautions = db.Column(
        db.Text,
        nullable=True
    )

    prediction_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    report_path = db.Column(
        db.String(255)
    )
    

    user = db.relationship(
        "User",
        backref="predictions"
    )  
    ai_summary = db.Column(db.Text)

    precautions = db.Column(db.Text)
    
    
    
    def __repr__(self):
        return f"<Prediction {self.prediction_id} - {self.disease_name}>"
    
