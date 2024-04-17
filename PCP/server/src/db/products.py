try:
    from src.utilities.swen_344_db_utils import exec_get_all, exec_get_one
except:
    from utilities.swen_344_db_utils import exec_get_all, exec_get_one
    

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

