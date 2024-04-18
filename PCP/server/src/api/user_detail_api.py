"""
API Endpoints for user management and authentication.

These endpoints handle user registration and login functionality.
"""
from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource

# Import only necessary functions from the utilities and user_details database module
try:
    from src.utilities.swen_344_db_utils import exec_get_one
    from src.db.user_details import verify_session_key, list_user_detail
except ImportError:
    from utilities.swen_344_db_utils import exec_get_one
    from db.user_details import verify_session_key, list_user_detail

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
    

