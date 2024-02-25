from flask_restful import Resource
from flask import jsonify
from flask_restful import request
from flask_restful import reqparse
import json
from ..utilities.swen_344_db_utils import *
from api.login import *
import hashlib

class AddUserAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id',type=str)
        parser.add_argument('userName', type=str)
        parser.add_argument('passWord', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('role', type=str)
        args = parser.parse_args()
        id = args['user_id']
        username = args['userName']
        password = args['passWord']
        role=args['role']
        response = user_details(id,username,password,role)
        return response

    
    
    


