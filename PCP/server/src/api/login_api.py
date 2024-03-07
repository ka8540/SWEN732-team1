from flask import make_response
from flask_restful import Resource
from flask import jsonify
from flask_restful import request
from flask_restful import reqparse
import json
from utilities.swen_344_db_utils import*
from db.login import *
import hashlib  # Importing hashlib module for password hashing

class LoginApi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, location='json')
        parser.add_argument('password', type=str, required=True, location='json')
        args = parser.parse_args()

        hashed_password = hashlib.sha224(args['password'].encode()).hexdigest()

        response, status_code = user_login(args['username'], hashed_password)
        
        if response:
            return make_response(jsonify(response),status_code)
        else:
            return make_response(jsonify(response),status_code)
        

