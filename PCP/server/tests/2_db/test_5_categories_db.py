import unittest
from unittest.mock import patch

try:
    from ...src.db.categories import get_all_categories, get_category_by_id, search_categories
except ImportError:
    from src.db.categories import get_all_categories, get_category_by_id, search_categories


class MyTestCase(unittest.TestCase):
    @patch('src.db.categories.exec_get_one')
    def test_a_get_category_by_id(self, mock_exec_get_one):
        expected_category = {'CategoryID': 1, 'CategoryName': 'Phones'}
        mock_exec_get_one.return_value = expected_category

        result = get_category_by_id(1)
        # Assert that the result is not None
        self.assertIsNotNone(result)

        self.assertEqual(result, expected_category)

    @patch('src.db.categories.exec_get_one')
    def test_b_get_category_by_id_non_existing(self, mock_exec_get_one):
        # Mock the database query and return None (no category found)
        mock_exec_get_one.return_value = None
        # Call the get_category_by_id function with a non-existing category ID
        result = get_category_by_id(99)
        self.assertIsNone(result)

    @patch('src.db.categories.exec_get_all')
    def test_c_get_all_categories(self, mock_exec_get_all):
        # Set up the expected result (mocked category data)
        expected_categories = [
            (1, 'Electronics'),
            (2, 'Clothing'),
            (3, 'Home Decor')
        ]

        # Mock the database query and return the expected categories
        mock_exec_get_all.return_value = expected_categories

        # Call the get_all_categories function
        result = get_all_categories()

        # Assert that the result matches the expected categories
        self.assertEqual(result, expected_categories)

    @patch('src.db.categories.exec_get_all')
    def test_d_search_categories(self, mock_exec_get_all):
        expected_categories = [
            (1, 'Electronics'),
        ]

        # Mock the database query and return the expected categories
        mock_exec_get_all.return_value = expected_categories

        # Call the search_categories function with the search query 'Electronics'
        result = search_categories('Electronics')

        # Assert that the result matches the expected categories
        self.assertEqual(result, expected_categories)


if __name__ == '__main__':
    unittest.main()
