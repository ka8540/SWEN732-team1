from flask_restful import Resource, reqparse
from src.db.login import exec_get_all, exec_commit
import psycopg2
import os
from dotenv import load_dotenv
import hashlib


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

class SignupAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('firstName', type=str, required=True, location='json')
        self.reqparse.add_argument('lastName', type=str, required=True, location='json')
        self.reqparse.add_argument('email', type=str, required=True, location='json')
        self.reqparse.add_argument('phoneNumber', type=str, location='json')
        self.reqparse.add_argument('username', type=str, required=True, location='json')
        self.reqparse.add_argument('password', type=str, required=True, location='json')
        self.reqparse.add_argument('confirmPassword', type=str, required=True, location='json')

    def post(self):
        args = self.reqparse.parse_args()

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Hash the password
        hashed_password = hashlib.sha256(args['password'].encode()).hexdigest()

        # Check if the user already exists
        cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (args['username'], args['email']))
        if cursor.fetchone():
            cursor.close()
            conn.close()
            return {'status': 'fail', 'message': 'Username or email already exists'}

        # Insert new user into the database with hashed password
        cursor.execute(
            "INSERT INTO users (first_name, last_name, email, phone_number, username, password) VALUES (%s, %s, %s, %s, %s, %s)",
            (args['firstName'], args['lastName'], args['email'], args['phoneNumber'], args['username'], hashed_password)
        )
        conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()

        return jsonify({'status': 'success', 'message': 'User created successfully'})

