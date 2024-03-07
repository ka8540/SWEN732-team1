from flask import make_response
from flask_restful import Resource
from flask import jsonify
from flask_restful import request
from flask_restful import reqparse
import json
from utilities.swen_344_db_utils import*
from db.login import *
from db.signup import *

class SignUpApi(Resource):
    def get(self):
        return jsonify(list_info_items())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, location='json')
        parser.add_argument('password', type=str, required=True, location='json')
        parser.add_argument('email', type=str, required=True, location='json')
        parser.add_argument('firstname', type=str, required=True, location='json')
        parser.add_argument('lastname', type=str, required=True, location='json')
        args = parser.parse_args()

        response, status_code = user_signup(**args)
        return make_response(jsonify(response), status_code)
        

