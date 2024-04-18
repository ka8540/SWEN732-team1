import unittest
from unittest.mock import patch


try:
    from ...src.db.prices import get_prices_by_product, get_all_prices
except ImportError:
    from src.db.prices import get_prices_by_product, get_all_prices


class TestPricesDB(unittest.TestCase):

    @patch('src.db.prices.exec_get_all')
    def test_get_all_prices(self, mock_exec_get_all):
        # Mock data for exec_get_all when get_all_prices
        mock_data = [
            (1, 1, 1, 'USD', 29.99, 'Amazon', 'https://www.amazon.com/'),
            (2, 1, 2, 'USD', 49.99, 'BestBuy', 'https://www.bestbuy.com/')
        ]
        mock_exec_get_all.return_value = mock_data

        # Call the function under test
        result = get_all_prices()

        # Perform assertions
        self.assertEqual(result, mock_data)
        mock_exec_get_all.assert_called_once()

    @patch('src.db.prices.exec_get_all')
    def test_get_prices_by_product(self, mock_exec_get_all):
        product_id = 1
        # Mock data for exec_get_all when get_prices_by_product when called with a specific product_id
        mock_data = [
            (1, product_id, 1, 'USD', 29.99, 'Amazon', 'https://www.amazon.com/')
        ]
        mock_exec_get_all.return_value = mock_data

        # Call the function under test
        result = get_prices_by_product(product_id)

        # Perform assertions
        self.assertEqual(result, mock_data)
        mock_exec_get_all.assert_called_once_with("""
    SELECT Prices.*, Retailers.RetailerName, Retailers.WebsiteURL
    FROM Prices
    JOIN Retailers ON Prices.RetailerID = Retailers.RetailerID
    WHERE ProductID = %s;
    """, (product_id,))


if __name__ == '__main__':
    unittest.main()
