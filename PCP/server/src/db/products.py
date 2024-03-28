import psycopg2
import yaml
import pandas as pd
import numpy as np
import sys
import os
try:
    from src.api.products_api import *
    from src.utilities.swen_344_db_utils import *
except:
    from api.products_api import *
    from utilities.swen_344_db_utils import *
    

def get_all_products():
    """Fetches all records from the Products table."""
    sql = "SELECT * FROM Products;"
    result = exec_get_all(sql)
    return result

def get_product_by_id(product_id):
    """Fetches a single product by its ID from the Products table."""
    sql = "SELECT * FROM Products WHERE ProductID = %s;"
    result = exec_get_one(sql, (product_id,))
    return result

def search_products(query):
    """Searches for products that match the query string."""
    sql = "SELECT * FROM Products WHERE ProductName ILIKE %s;"
    search_query = f"%{query}%"
    result = exec_get_all(sql, (search_query,))
    return result

    