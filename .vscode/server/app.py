# app.py

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_profiles.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    gprs_location = db.Column(db.String(100), nullable=False)
    profile_picture = db.Column(db.String(100), nullable=False)

class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        parser.add_argument('age', type=int, required=True)
        parser.add_argument('phone_number', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('gprs_location', type=str, required=True)
        parser.add_argument('profile_picture', type=str, required=True)
        args = parser.parse_args()

        user = UserProfile(
            first_name=args['first_name'],
            last_name=args['last_name'],
            age=args['age'],
            phone_number=args['phone_number'],
            email=args['email'],
            gprs_location=args['gprs_location'],
            profile_picture=args['profile_picture']
        )
        db.session.add(user)
        db.session.commit()
        return {'message': 'User registered successfully'}, 201

class Profiles(Resource):
    def get(self):
        users = UserProfile.query.all()
        profiles = []
        for user in users:
            profile = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'age': user.age,
                'phone_number': user.phone_number,
                'email': user.email,
                'gprs_location': user.gprs_location,
                'profile_picture': user.profile_picture
            }
            profiles.append(profile)
        return {'profiles': profiles}, 200

api.add_resource(Register, '/api/register')
api.add_resource(Profiles, '/api/profiles')

if __name__ == '__main__':
 app.run(port=5555)
