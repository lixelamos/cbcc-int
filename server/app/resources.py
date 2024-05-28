from flask_restful import Resource, reqparse
from app import db
from models import UserProfile

class RegisterResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', required=True)
        parser.add_argument('last_name', required=True)
        parser.add_argument('age', required=True)
        parser.add_argument('phone_number', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('gprs_location', required=True)
        parser.add_argument('profile_picture', required=False)  
        args = parser.parse_args()

        user = UserProfile(
            first_name=args['first_name'],
            last_name=args['last_name'],
            age=args['age'],
            phone_number=args['phone_number'],
            email=args['email'],
            gprs_location=args['gprs_location'],
            profile_picture=args.get('profile_picture')  
        )
        db.session.add(user)
        db.session.commit()
        return {'message': 'User profile created successfully'}, 201

class ProfileListResource(Resource):
    def get(self):
        users = UserProfile.query.all()
        return [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'age': user.age,
                 'phone_number': user.phone_number, 'email': user.email, 'gprs_location': user.gprs_location,
                 'profile_picture': user.profile_picture} for user in users]
