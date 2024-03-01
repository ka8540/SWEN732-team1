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
    
    # Check the results and apply logic to return the correct message
    if result_username and not result_credentials:
        # Username exists, but password is incorrect
        return check_password(query_username)
    elif not result_username:
        # Username does not exist
        return check_username_and_password([], [])  # Passing empty lists to indicate no results found
    else:
        # Username and password combination is correct
        return check_username_and_password(result_username, result_credentials)


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



