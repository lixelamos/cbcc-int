from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api


app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from models import UserProfile
from resources import RegisterResource, ProfileListResource

api.add_resource(RegisterResource, '/api/register/')
api.add_resource(ProfileListResource, '/api/profiles/')

if __name__ == '__main__':
    app.run(port=5555)
