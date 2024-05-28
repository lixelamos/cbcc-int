import os
from flask import current_app
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from app import db
from models import UserProfile
from flask import abort

class RegisterResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', required=True)
        parser.add_argument('last_name', required=True)
        parser.add_argument('age', required=True, choices=range(10, 16))  
        parser.add_argument('phone_number', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('gprs_location', required=True)
        parser.add_argument('profile_picture', type=FileStorage, location='files', required=False)
        args = parser.parse_args()

        # Handle profile picture upload
        profile_picture_path = None
        if args['profile_picture']:
            profile_picture = args['profile_picture']
            profile_picture_path = save_profile_picture(profile_picture)

        user = UserProfile(
            first_name=args['first_name'],
            last_name=args['last_name'],
            age=args['age'],
            phone_number=args['phone_number'],
            email=args['email'],
            gprs_location=args['gprs_location'],
            profile_picture=profile_picture_path
        )
        db.session.add(user)
        db.session.commit()
        return {'message': 'User profile created successfully'}, 201

def save_profile_picture(profile_picture):
    static_folder = os.path.join(current_app.root_path, 'static')
    os.makedirs(static_folder, exist_ok=True)

    # Generate a unique filename
    filename = secure_filename(profile_picture.filename)
    file_path = os.path.join(static_folder, filename)
    profile_picture.save(file_path)
    return os.path.join('static', filename)