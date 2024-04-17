import unittest
from unittest.mock import patch

from src.db.user_favorites import get_user_favorites, add_user_favorite


class TestUserFavoritesDB(unittest.TestCase):

    @patch('src.db.user_favorites.exec_get_all')
    def test_get_user_favorites(self, mock_exec_get_all):
        user_id = 1  # Example user ID
        mock_favorites_data = [
            (1, 'Product1', 'Description1', 'Category1', 'ImageURL1', user_id),
            (2, 'Product2', 'Description2', 'Category2', 'ImageURL2', user_id)
        ]
        mock_exec_get_all.return_value = mock_favorites_data

        # Call the function under test
        result = get_user_favorites(user_id)

        # Perform assertions
        self.assertEqual(result, mock_favorites_data)
        mock_exec_get_all.assert_called_once_with("""
    SELECT Products.*, UserFavorites.FavoriteID
    FROM UserFavorites
    JOIN Products ON UserFavorites.ProductID = Products.ProductID
    WHERE UserFavorites.user_id = %s;
    """, (user_id,))

    @patch('src.db.user_favorites.exec_commit')
    def test_add_user_favorite(self, mock_exec_commit):
        user_id = 1  # Example user ID
        product_id = 1  # Example product ID
        mock_exec_commit.return_value = None  # exec_commit does not return anything on success

        # Call the function under test
        add_user_favorite(user_id, product_id)

        # Perform assertions
        mock_exec_commit.assert_called_once_with(
            "INSERT INTO UserFavorites (user_id, ProductID) VALUES (%s, %s);",
            (user_id, product_id)
        )


if __name__ == '__main__':
    unittest.main()
