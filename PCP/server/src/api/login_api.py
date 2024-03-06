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
from src.utilities.swen_344_db_utils import *  # Importing database utilities
from src.db.login import *  # Importing login functions
import hashlib  # Importing hashlib module for password hashing

class AddUserAPI(Resource):

    """
    API endpoint to add a new user.
    """
    def get(self):
        return jsonify(list_info_items())

    def post(self):
        """
        Handles POST requests to create a new user.

        Expects JSON payload with the following parameters:
        - username (str): Username of the new user.
        - password (str): Password of the new user.
        - email (str): Email address of the new user.
        - firstname (str): First name of the new user.
        - lastname (str): Last name of the new user.

        Returns:
            JSON response with details of the newly created user.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, location='json')
        parser.add_argument('password', type=str, required=True, location='json')
        parser.add_argument('email', type=str, required=True, location='json')
        parser.add_argument('firstname', type=str, required=True, location='json')
        parser.add_argument('lastname', type=str, required=True, location='json')
        args = parser.parse_args()

        # Call user_details function to create the user
        response, status_code = user_details(**args)
        
        
        # Return JSON response with user details
        return make_response(jsonify(response), status_code)

class LoginAPI(Resource):
    """
    API endpoint for user login.
    """

    def post(self):
        """
        Handles POST requests for user login.

        Expects JSON payload with the following parameters:
        - username (str): Username of the user.
        - password (str): Password of the user.

        Returns:
            JSON response with user ID if login is successful, otherwise returns an error message.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, location='json')
        parser.add_argument('password', type=str, required=True, location='json')
        args = parser.parse_args()

        # Hash the password using SHA-224 algorithm
        hashed_password = hashlib.sha224(args['password'].encode()).hexdigest()

        # Check user credentials
        response, status_code = check_user_credentials(args['username'], hashed_password)
        
        if response:
            # If credentials are correct, return JSON response with user ID
            return make_response(jsonify(response),status_code)
        else:
            # If credentials are incorrect, return an error message
            return make_response(jsonify(response),status_code)
