try:
    from src.utilities.swen_344_db_utils import exec_get_all, exec_commit
except ImportError:
    from utilities.swen_344_db_utils import exec_get_all, exec_commit
    

def get_cart_contents(user_id):
    sql = "SELECT ProductID, Quantity FROM Cart WHERE UserID = %s;"
    return exec_get_all(sql, (user_id,))

def add_item_to_cart(user_id, product_id, quantity):
    sql = "INSERT INTO Cart (UserID, ProductID, Quantity) VALUES (%s, %s, %s) ON CONFLICT (UserID, ProductID) DO UPDATE SET Quantity = Cart.Quantity + EXCLUDED.Quantity;"
    exec_commit(sql, (user_id, product_id, quantity))

def remove_item_from_cart(user_id, product_id):
    sql = "DELETE FROM Cart WHERE UserID = %s AND ProductID = %s;"
    exec_commit(sql, (user_id, product_id))