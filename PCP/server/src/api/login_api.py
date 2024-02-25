from flask_restful import Resource
from flask import jsonify
from flask_restful import request
from flask_restful import reqparse
import json
from src.utilities.swen_344_db_utils import *
from src.api.login import *
import hashlib

class AddUserAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str,required=True, location='json')
        parser.add_argument('password', type=str,required=True, location='json')
        parser.add_argument('email', type=str,required=True, location='json')
        parser.add_argument('firstname',type=str,required=True, location='json')
        parser.add_argument('lastname',type=str,required=True, location='json')
        parser.add_argument('role', type=str,required=True, location='json')
        args = parser.parse_args()
        response = user_details(**args)
        return jsonify(response)

class LoginAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, location='json')
        parser.add_argument('password', type=str, required=True, location='json')
        args = parser.parse_args()

        # Hash the password the same way it's hashed when a user is created
        hashed_password = hashlib.sha224(args['password'].encode()).hexdigest()

        user_id = check_user_credentials(args['username'], hashed_password)
        print("it is :",user_id)
        if user_id:
            return jsonify(user_id)
            
        else:
            # If credentials are incorrect, return an error message
            return jsonify("Invalide Creds"), 401
         
    
    


