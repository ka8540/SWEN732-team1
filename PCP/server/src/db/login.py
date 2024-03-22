import psycopg2
import yaml
import os
import pandas as pd
import numpy as np
import sys
import os
from api.login_api import *
from utilities.swen_344_db_utils import *
from model.user import *
import hashlib
import secrets


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



