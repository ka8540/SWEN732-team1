import psycopg2
import yaml
import pandas as pd
import numpy as np
import sys
import os
try:
    from src.api.retailer_api import *
    from src.utilities.swen_344_db_utils import *
except:
    from api.retailer_api import *
    from utilities.swen_344_db_utils import *
    

def get_all_retailers():
    sql = "SELECT * FROM Retailers;"
    return exec_get_all(sql)

def get_retailer_by_id(retailer_id):
    sql = "SELECT * FROM Retailers WHERE RetailerID = %s;"
    return exec_get_one(sql, (retailer_id,))
