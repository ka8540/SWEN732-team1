try:
    from src.utilities.swen_344_db_utils import exec_get_all, exec_commit
except ImportError:
    from utilities.swen_344_db_utils import exec_get_all, exec_commit


def get_cart_contents(user_id):
    """Fetches all items in the user's cart."""
    sql = """
    SELECT p.ProductID, p.ProductName, p.ProductDescription, p.ImageURL, c.Quantity, pr.Price 
    FROM Cart c
    JOIN Products p ON c.ProductID = p.ProductID
    JOIN Prices pr ON p.ProductID = pr.ProductID
    WHERE c.UserID = %s;
    """
    result = exec_get_all(sql, (user_id,))
    return result


def add_item_to_cart(user_id, product_id, quantity):
    """Adds a new item or updates the quantity of an existing item in the cart."""
    sql = """
    INSERT INTO Cart (UserID, ProductID, Quantity)
    VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE Quantity = Quantity + VALUES(Quantity);
    """
    result = exec_commit(sql, (user_id, product_id, quantity))
    return result


def remove_item_from_cart(user_id, product_id):
    """Removes an item from the cart."""
    sql = "DELETE FROM Cart WHERE UserID = %s AND ProductID = %s;"
    exec_commit(sql, (user_id, product_id))
