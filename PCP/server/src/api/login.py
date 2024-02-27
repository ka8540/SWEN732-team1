import psycopg2
import yaml
import os
import pandas as pd
import numpy as np
import sys
import os
from src.api.login_api import *
from src.utilities.swen_344_db_utils import *
import hashlib
import secrets


def rebuild_tables():
    exec_sql_file('UserDetail.sql')

def list_info_items():
    """Fetches all records from the User table."""
    result = exec_get_all('''SELECT * FROM user_authentication''')
    return result

def check_user_credentials(username, hashed_password):
    query = '''SELECT username FROM user_authentication WHERE username = %s AND hashed_password = %s;'''
    result = exec_get_all(query, (username, hashed_password))
    print(result, "result of query to check user")
    
    # If the result is not empty, credentials are correct
    if len(result)>0:
        return True 
    return False

def user_details(**kwargs):
    firstname = kwargs.get('firstname')
    lastname = kwargs.get('lastname')
    username = kwargs.get('username')
    password_kwargs = kwargs.get('password')
    email = kwargs.get('email')
    password = hashlib.sha224(password_kwargs.encode()).hexdigest()

    # Log statements (useful for debugging, but should be removed or commented out in production)
    print("Password:", password)
    print("UserName:", username)
    
    # Prepare the tuple with the correct number of arguments
    tuple_to_check = (username, password)
    tuple_to_insert = (firstname, lastname, username, password, email)
    
    # Check if user already exists
    query_check = 'SELECT * FROM user_authentication WHERE username = %s AND hashed_password = %s;'
    catch_return = exec_get_all(query_check, tuple_to_check)
    
    print("catch empty:", catch_return)
    
    # If the user does not exist, insert the new user
    if len(catch_return) == 0:
        print("creds:", tuple_to_insert)
        query_insert = 'INSERT INTO user_authentication (firstname, lastname, username, hashed_password, email) VALUES (%s,%s, %s, %s, %s);'
        catch_return = exec_commit(query_insert, tuple_to_insert)
        print(catch_return)
        return catch_return
    else:
        return "The user already exists", 400


