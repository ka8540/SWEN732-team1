"""
API Endpoints for user management and authentication.

These endpoints handle user registration and login functionality.
"""
from flask import make_response
from flask_restful import Resource
from flask import jsonify
from flask_restful import request
from flask_restful import reqparse
import json
from utilities.swen_344_db_utils import *  # Importing database utilities
from db.logout import *  # Importing login functions
import hashlib  # Importing hashlib module for password hashing


class LogoutAPI(Resource):
    """
    API endpoint for user logout.
    """

    def post(self):
        print("idhar aa gaya")
        print("Raw Request Data:", request.data)
        parser = reqparse.RequestParser()
        print(parser)
        parser.add_argument('session_key', type=str, required=True, location='json')
        args = parser.parse_args()
        print(args,'session_key on api')

        # Check user credentials
        response, status_code = user_logout(args)

        return make_response(jsonify(response),status_code)
    
        

