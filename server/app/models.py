from app import db

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    gprs_location = db.Column(db.String(255), nullable=False)
    profile_picture = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<UserProfile {self.first_name} {self.last_name}, {self.email}>'
