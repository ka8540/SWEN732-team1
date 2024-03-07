import psycopg2
import yaml
import os
import pandas as pd
import numpy as np
import sys
import os
from api.login_api import *
from utilities.swen_344_db_utils import *


def list_info_items():
    result = exec_get_all('''SELECT * FROM users''')
    return result

def user_login(username, hashed_password):
    query = '''SELECT username FROM users WHERE username = %s AND hashed_password = %s;'''
    result = exec_get_all(query, (username, hashed_password))
    print(result, "User Data fetched")
    
    # If the result is not empty, credentials are correct
    if len(result)>0:
        return "Login Creds are Correct",200 
    return "Login Creds are Incorrect",410