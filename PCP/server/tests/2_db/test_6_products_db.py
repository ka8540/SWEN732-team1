import unittest
from unittest.mock import patch

try:
    from ...src.db.products import get_all_products, get_product_by_id, search_products
except:
    from src.db.products import get_all_products, get_product_by_id, search_products

class MyTestCase(unittest.TestCase):
    @patch('src.db.products.exec_get_all')
    def test_a_get_all_products(self, mock_exec_get_all):
        expected_product = [
            (1, 'Laptop', 'Electronics', 2, 'image.url')
        ]
        mock_exec_get_all.return_value = expected_product
        # Call the get_all_categories function
        result = get_all_products()

        # Assert that the result matches the expected categories
        self.assertEqual(result, expected_product)

    @patch('src.db.products.exec_get_one')
    def test_b_get_product_by_id(self, mock_exec_get_one):
        # Simulate an existing product with ID 42
        existing_product = {"ProductID": 42, "ProductName": "Widget"}
        mock_database = [existing_product]

        mock_exec_get_one.return_value = existing_product

        # Call get_product_by_id with an existing product ID
        result = get_product_by_id(42)

        # Check if the returned product matches the expected values
        self.assertEqual(result, existing_product)

    @patch('src.db.products.exec_get_one')
    def test_c_get_product_by_id_non_existing(self, mock_exec_get_one):
        # Mock the database query and return None
        mock_exec_get_one.return_value = None
        # Call the get_product_by_id function with a non-existing product ID
        result = get_product_by_id(99)
        self.assertIsNone(result)

    @patch('src.db.products.exec_get_all')
    def test_d_search_products(self, mock_exec_get_all):
        existing_product = {"ProductID": 42, "ProductName": "Widget"}

        # Mock the database query and return the expected categories
        mock_exec_get_all.return_value = existing_product

        # Call the search_categories function with the search query 'Electronics'
        result = search_products('Widget')

        # Assert that the result matches the expected categories
        self.assertEqual(result, existing_product)


if __name__ == '__main__':
    unittest.main()
