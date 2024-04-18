try:
    from src.utilities.swen_344_db_utils import exec_get_all, exec_commit
except ImportError:
    from utilities.swen_344_db_utils import exec_get_all, exec_commit
    

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


def delete_user_favorite(user_id, product_id):
    """Deletes a favorite product for a user."""
    sql = "DELETE FROM UserFavorites WHERE user_id = %s AND ProductID = %s;"
    exec_commit(sql, (user_id, product_id))