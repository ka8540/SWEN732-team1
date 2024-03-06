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
import hashlib  # Importing hashlib module for passwo

class UserDetail(Resource):

    """
    API endpoint to add a new user.
    """
    def get(self):
        user_details = list_user_detail()
        print(user_details,"details of the user!!")
        return jsonify(user_details)
    