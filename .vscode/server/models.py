# app/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gps_location = db.Column(db.String(100), nullable=False)
    profile_picture = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<UserProfile %r>' % self.email
