from flask import Flask
from flask_restful import Resource, Api
from api.login import user_details 
from api.signup import signupapi
from api.login import loginAPI
from api.management import *
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Init, '/manage/init') #Management API for initializing the DB

api.add_resource(Version, '/manage/version') #Management API for checking DB version

api.add_resource(user_details, '/')
api.add_resource(signupapi, '/signup')
api.add_resource(loginAPI, '/login')


if __name__ == '__main__':
    rebuild_tables()
    app.run(debug=True)