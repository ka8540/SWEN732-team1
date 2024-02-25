import psycopg2
import yaml
import os
import pandas as pd
import numpy as np
import sys
import os
from PCP.server.src.api.login_api import *
from PCP.server.src.utilities.swen_344_db_utils import *
import hashlib
import secrets


def rebuild_tables():
    exec_sql_file('UserDetail.sql')

def list_info_items():
    """Fetches all records from the User table."""
    result = exec_get_all('''SELECT * FROM user_authentication''')
    return result

def check_user_credentials(username, hashed_password):
    query = '''SELECT username, session_key FROM users WHERE username = %s AND session_key = %s;'''
    result = exec_get_all(query, (username,hashed_password))
    print(result,"result of query to check user")
    return len(result) > 0

def user_details(id,username,password,role):
    password=hashlib.sha224(password.encode()).hexdigest()
    print("Password:",password)
    print("UserName:",username)
    tuple= (id,username,password,role)
    query= 'SELECT * FROM users WHERE id = %s AND username = %s AND hashed_password = %s AND role = %s;'
    catch_return=exec_get_all(query,tuple)
    print("catch empty:",catch_return)
    if (len(catch_return)==0):
        tuple_1= (id,username,password,role)
        print("creds:",tuple_1)
        result= 'INSERT INTO users (id,username,hashed_password,role) VALUES (%s,%s, %s,%s);'
        catch_return=exec_commit(result,tuple_1)
        print(catch_return)
        return result
    else:
        return "The user already axists",401


def insert_info_item(**kwargs):
    sql = '''INSERT INTO user_authentication (username, hashed_password, email, role) VALUES (%s, %s, %s, %s) RETURNING id;'''
    args = (kwargs.get('username'), kwargs.get('hashed_password'), kwargs.get('email'), kwargs.get('role'))
    inserted_id = exec_commit(sql, args)
    return inserted_id

# Updates an existing item in the InfoDetail table.
# Conceptually, this could be seen as modifying an 'element' before it receives further 'visits' by operations.
def update_info_item(**kwargs):
    """
    Updates details of an existing information item in the database.
    
    Args:
        **kwargs: New details for the item along with its ID.
    
    Returns:
        The ID of the updated item, ensuring it can still be identified for any 'visits'.
    """
    sql = '''UPDATE InfoDetail SET firstname=%s, lastname=%s, email=%s, uid=%s, mobileNum=%s WHERE id=%s RETURNING id;'''
    args = (kwargs['firstname'], kwargs['lastname'], kwargs['email'], kwargs['uid'], kwargs['mobilenumber'], kwargs['item_id'])
    updated_item = exec_commit(sql, args)
    return updated_item

# Deletes an item from the InfoDetail table.
# This could be viewed as removing an 'element' from the pool of items that can be 'visited'.
def delete_info_item(item_id):
    """
    Deletes an information item from the database.
    
    Args:
        item_id: The ID of the item to be deleted.
    
    Returns:
        The result of the delete operation, typically confirmation of deletion.
    """
    result = exec_commit('''DELETE FROM InfoDetail WHERE id = %s;''', (item_id,))
    return result
