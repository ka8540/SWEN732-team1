import psycopg2
import yaml
import os
import pandas as pd
import numpy as np
import sys
import os
from src.api.login_api import *
from src.utilities.swen_344_db_utils import *
from src.model.user import *
import hashlib
import secrets


def rebuild_tables():
    exec_sql_file('UserDetail.sql')

def list_user_detail(username):
    print('User entered to get the detail!!')
    # Updated query to filter by username using parameterized queries for security
    query = '''SELECT firstname, lastname, username, email FROM user_authentication WHERE username = %s;'''
    users = exec_get_all(query, (username,))  # Note the comma after username to make it a tuple
    print(users, 'user detail!!')
    
    if users:
        user_details = [{'firstname': user[0], 'lastname': user[1], 'username': user[2], 'email': user[3]} for user in users]
    else:
        user_details = []
    
    return user_details
def verify_session_key(session_key):
    # Implement the logic to verify session key and return the associated username
    # This is a placeholder for your SQL query to find the username with the given session_key
    query = '''SELECT username FROM user_authentication WHERE session_key = %s;'''
    result = exec_get_all(query, (session_key,))
    if result:
        return result[0][0]  # Assuming exec_get_all returns a list of tuples
    return None

def list_info_items():
    """Fetches all records from the User table."""
    result = exec_get_all('''SELECT * FROM user_authentication''')
    return result

def check_user_credentials(username, hashed_password):
    # Query to check if the username exists
    query_username = '''SELECT username FROM user_authentication WHERE username = %s;'''
    result_username = exec_get_all(query_username, (username,))
    
    # Query to check if the username and hashed password combination is correct
    query_credentials = '''SELECT username FROM user_authentication WHERE username = %s AND hashed_password = %s;'''
    result_credentials = exec_get_all(query_credentials, (username, hashed_password))
    
    if not result_username:
        # Username does not exist
        return {"message": "Login Creds are Incorrect", "sessionKey": None}, 410
    elif result_username and not result_credentials:
        # Username exists, but password is incorrect
        # Here, we should not attempt to generate or use a session key since login failed.
        return {"message": "Password Invalid", "sessionKey": None}, 411
    else:
        # Correct credentials; proceed with session key generation and update.
        session_key = generate_session_key()
        update_session_key_query = '''UPDATE user_authentication SET session_key = %s WHERE username = %s;'''
        exec_commit(update_session_key_query, (session_key, username))
        # Return success with the session key.
        return {"message": "Login Creds are Correct", "sessionKey": session_key}, 200



def user_details(**kwargs):
    firstname = kwargs.get('firstname')
    lastname = kwargs.get('lastname')
    username = kwargs.get('username')
    password_kwargs = kwargs.get('password')
    email = kwargs.get('email')
    password = hashlib.sha224(password_kwargs.encode()).hexdigest()

    # Check if user already exists based on username
    user_exists_query = 'SELECT username FROM user_authentication WHERE username = %s;'
    user_exists = exec_get_all(user_exists_query, (username,))
    print(user_exists,'username !!')
    result = check_username(user_exists)
    if result is not None:
        return result

    # If the user does not exist, proceed to insert the new user
    tuple_to_insert = (firstname, lastname, username, password, email)
    query_insert = 'INSERT INTO user_authentication (firstname, lastname, username, hashed_password, email) VALUES (%s, %s, %s, %s, %s);'
    exec_commit(query_insert, tuple_to_insert)

    # Return a success message (consider also returning an appropriate status code)
    return {"message": "User registered successfully"}, 200



