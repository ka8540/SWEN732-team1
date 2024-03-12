import psycopg2
import yaml
import os
import pandas as pd
import numpy as np
import sys
import os
from api.login_api import *
from utilities.swen_344_db_utils import *
import hashlib
import secrets



def list_info_items():
    result = exec_get_all('''SELECT * FROM user_authentication''')
    return result

def user_signup(**kwargs):
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
    if user_exists:
        print("user_exist")
        # If user exists, return immediately with an appropriate message and status
        return {"message": "User already exists"}, 409  # HTTP 409 Conflict

    # If the user does not exist, proceed to insert the new user
    tuple_to_insert = (firstname, lastname, username, password, email)
    query_insert = 'INSERT INTO user_authentication (firstname, lastname, username, hashed_password, email) VALUES (%s, %s, %s, %s, %s);'
    exec_commit(query_insert, tuple_to_insert)

    # Return a success message (consider also returning an appropriate status code)
    return {"message": "User registered successfully"}, 200