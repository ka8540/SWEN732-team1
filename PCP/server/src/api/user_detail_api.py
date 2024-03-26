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
from src.db.user_details import *  # Importing login functions
import hashlib  # Importing hashlib module for passwo

class UserDetail(Resource):
    def get(self):
        # Extract session key from the request headers
        session_key = request.headers.get('X-Session-Key')
        print('session_key',session_key)

        if not session_key:
            return {"message": "No session key provided."}, 401
        
        # Verify the session key and get the associated username
        username = verify_session_key(session_key)
        
        if not username:
            return {"message": "Invalid session key."}, 401
        
        # Fetch user details with the username
        user_details = list_user_detail(username)
        print(user_details, "details of the user!!")
        return jsonify(user_details)
    

