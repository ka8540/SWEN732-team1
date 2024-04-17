import psycopg2
import yaml
import pandas as pd
import numpy as np
import sys
import os
try:
    # from src.api.categories_api import *
    from src.utilities.swen_344_db_utils import exec_get_all, exec_get_one
except:
    # from api.categories_api import *
    from utilities.swen_344_db_utils import exec_get_all, exec_get_one
    
    
def get_all_categories():
    """Fetches all records from the produtcategories table."""
    
    sql = "SELECT * FROM ProductCategories;"
    result = exec_get_all(sql)
    return result

def get_category_by_id(category_id):
    """Fetches a single category by its ID from the ProductCategories table."""
    
    sql = "SELECT * FROM ProductCategories WHERE CategoryID = %s;"
    result = exec_get_one(sql, (category_id,))
    return result

def search_categories(query):
    """Searches for categories that match the query string."""
    
    # Using ILIKE for case-insensitive matching, % signs are wildcards in SQL LIKE expressions
    sql = "SELECT * FROM ProductCategories WHERE CategoryName ILIKE %s;"
    # The % signs around the query are wildcards that match any characters
    search_query = f"%{query}%"
    
    # exec_get_all is a function that executes the given SQL query and returns all the results
    result = exec_get_all(sql, (search_query,))
    return result
