from flask import make_response
from flask import jsonify
from flask_restful import Resource, reqparse, request
from db import example
from db.utils import * 
import hashlib

from db.utils import exec_get_all

# class HelloWorld(Resource):
#     def get(self):
#         return dict(example.list_examples())

class user_details(Resource):
    def get(self):
        # Assuming user_details table has columns id, username, password, mailID
        result = exec_get_all('SELECT * FROM users')
        return result

# Login APIs
class loginAPI(Resource):
    def post(self):
        # Create a request parser
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='Username of the user', required=True)
        parser.add_argument('password', type=str, help='Password for the account', required=True)
        args = parser.parse_args()

        # Extract data from the parsed arguments
        username = args['username']
        password = args['password']

        # Hash the provided password for comparison with the stored hashed password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # query = "SELECT user_id, username, password FROM users WHERE username = %s;"
        query = "SELECT username, password FROM users WHERE username = %s;"
        result = exec_get_one(query, (username,))

        if result:
            stored_username, stored_password = result

            # Check if the hashed password matches the stored hashed password
            if hashed_password == stored_password:
                return {'message': 'Login successful', 'username': stored_username}, 200
            else:
                return {'error': 'Invalid credentials'}, 401
        else:
            return {'error': 'User not found'}, 404
