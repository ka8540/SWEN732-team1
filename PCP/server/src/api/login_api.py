from flask_restful import Resource, reqparse
from src.db.login import exec_get_all, exec_commit
import psycopg2
import os
from dotenv import load_dotenv
import hashlib
import secrets

# Load environment variables
load_dotenv()

# Database connection function
def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST')
    )

class LoginAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True, location='json')
        self.reqparse.add_argument('password', type=str, required=True, location='json')

    def post(self):
        args = self.reqparse.parse_args()
        username = args['username']
        password = args['password']
        
        # Hash the password
        hashed_password = hashlib.sha224(password.encode()).hexdigest()

        # Check if username exists
        user_exists_query = '''SELECT username FROM user_authentication WHERE username = %s;'''
        user_exists = exec_get_all(user_exists_query, (username,))
        
        if not user_exists:
            return {"message": "Username does not exist"}, 404

        # Check if the username and password combination is correct
        credentials_query = '''SELECT username FROM user_authentication WHERE username = %s AND hashed_password = %s;'''
        valid_credentials = exec_get_all(credentials_query, (username, hashed_password))
        
        if not valid_credentials:
            return {"message": "Invalid password"}, 401

        # Generate and update session key
        session_key = secrets.token_hex(16)
        update_session_key_query = '''UPDATE user_authentication SET session_key = %s WHERE username = %s;'''
        exec_commit(update_session_key_query, (session_key, username))
        
        return {"message": "Login successful", "session_key": session_key}, 200
