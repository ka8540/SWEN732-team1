import psycopg2
import yaml
import os
import pandas as pd
import numpy as np
import sys
import os
try:
    # from src.api.logout_api import *
    from src.utilities.swen_344_db_utils import exec_commit
    # from src.model.user import *
except:
    # from api.logout_api import *
    from utilities.swen_344_db_utils import exec_commit
    # from model.user import
import hashlib
import secrets

def user_logout(kwargs):
    session_key = kwargs.get('session_key')
    logout_query = '''UPDATE user_authentication SET session_key = NULL WHERE session_key = %s;'''
    exec_commit(logout_query, (session_key,))
    return {"message":"User Logout Successfully!"},200
