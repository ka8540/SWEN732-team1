from flask import make_response
from flask import jsonify
from flask_restful import Resource, reqparse, request
from db import example
from db.utils import * 
import hashlib

from db.utils import exec_get_all

class signupapi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('firstname', type=str, help='firstname of the user', required=True)
        parser.add_argument('lastname', type=str, help='lastname of the user', required=True)
        parser.add_argument('username', type=str, help='Username of the user', required=True)
        parser.add_argument('password', type=str, help='Password for the account', required=True)
        parser.add_argument('confirmpassword', type=str, help='should enter the same password as before', required=True)
        parser.add_argument('email', type=str, help='MailID of the user', required=True)
        args = parser.parse_args()

        firstname = args['firstname']
        lastname = args['lastname']
        username = args['username']
        password = args['password']
        confirmpassword = args ['confirmpassword']
        email = args['email']

        # Check if the password and confirmpassword matches.
        if password != confirmpassword:
            return {'error': 'password and confirmpassword do not match'}, 400 # 400 - bad request

        # Hash the password using SHA-256 (consider using a secure hashing library)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Use the same table name as in your login.py
        query = "INSERT INTO users (firstname, lastname, username, password, email) VALUES (%s, %s, %s, %s, %s);"
        values = (firstname, lastname, username, hashed_password, email)

        count = exec_commit(query, values)

        if count == 1:
            return {'message': 'User successfully registered', 'username': username}, 201 # 201 - OK
        else:
            return {'error': 'Failed to register user'}, 500 # 500 - Internal server error


