import os
from .utils import *

def rebuild_tables():
    exec_sql_file('src/db/schema.sql')
    # exec_sql_file('src/db/test_data.sql')

    