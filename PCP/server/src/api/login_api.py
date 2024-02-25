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
        print(args['password'],'lol kush ')
        print(args['email'])
        response = user_details(**args)
        return jsonify(response)

    
    
    


