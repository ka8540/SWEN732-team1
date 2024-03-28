import psycopg2
import yaml
import pandas as pd
import numpy as np
import sys
import os
try:
    from src.api.user_favorites_api import *
    from src.utilities.swen_344_db_utils import *
except:
    from api.user_favorites_api import *
    from utilities.swen_344_db_utils import *
    

def get_user_favorites(user_id):
    sql = """
    SELECT Products.*, UserFavorites.FavoriteID
    FROM UserFavorites
    JOIN Products ON UserFavorites.ProductID = Products.ProductID
    WHERE UserFavorites.user_id = %s;
    """
    return exec_get_all(sql, (user_id,))


def add_user_favorite(user_id, product_id):
    """Adds a new favorite product for a user."""
    sql = "INSERT INTO UserFavorites (user_id, ProductID) VALUES (%s, %s);"
    exec_commit(sql, (user_id, product_id))
