import psycopg2
import yaml
import os
import pandas as pd
import numpy as np
import sys
import os
try:
    from src.api.login_api import *
    from src.utilities.swen_344_db_utils import *
    from src.model.user import *
except:
    from api.login_api import *
    from utilities.swen_344_db_utils import *
    from model.user import *



def list_info_items():
    """Fetches all records from the User table."""
    result = exec_get_all('''SELECT * FROM user_authentication''')
    return result

def check_user_credentials(username, hashed_password):
    # Check if the username exists
    query_username_exists = '''SELECT 1 FROM user_authentication WHERE username = %s;'''
    username_exists = exec_get_one(query_username_exists, (username,))

    if not username_exists:
        # Username does not exist
        return {"message": "Login Creds are Incorrect", "sessionKey": None}, 410
    else:
        # Username exists, now check if the password is correct
        query_password_correct = '''SELECT 1 FROM user_authentication WHERE username = %s AND hashed_password = %s;'''
        password_correct = exec_get_one(query_password_correct, (username, hashed_password))

        if not password_correct:
            # Password is incorrect
            return {"message": "Password Invalid", "sessionKey": None}, 411
        else:
            # Credentials are correct
            session_key = generate_session_key()  # Make sure you have a function to generate a session key
            # Update the session key in the database
            update_session_key_query = '''UPDATE user_authentication SET session_key = %s WHERE username = %s;'''
            exec_commit(update_session_key_query, (session_key, username))
            return {"message": "Login Creds are Correct", "sessionKey": session_key}, 200





