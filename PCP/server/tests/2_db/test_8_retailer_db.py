import unittest
from unittest.mock import patch

from src.db.retailers import get_all_retailers, get_retailer_by_id


class TestRetailersDB(unittest.TestCase):

    @patch('src.db.retailers.exec_get_all')
    def test_get_all_retailers(self, mock_exec_get_all):
        # Mock data to be returned by exec_get_all when get_all_retailers is called
        mock_retailers_data = [
            (1, 'Amazon', 'https://www.amazon.com/'),
            (2, 'BestBuy', 'https://www.bestbuy.com/')
        ]
        mock_exec_get_all.return_value = mock_retailers_data

        # Call the function under test
        result = get_all_retailers()

        # Perform assertions
        self.assertEqual(result, mock_retailers_data)
        mock_exec_get_all.assert_called_once()

    @patch('src.db.retailers.exec_get_one')
    def test_get_retailer_by_id(self, mock_exec_get_one):
        retailer_id = 1
        # Mock data to be returned by exec_get_one when get_retailer_by_id is called with a specific retailer_id
        mock_retailer_data = (1, 'Amazon', 'https://www.amazon.com/')
        mock_exec_get_one.return_value = mock_retailer_data

        # Call the function under test
        result = get_retailer_by_id(retailer_id)

        # Perform assertions
        self.assertEqual(result, mock_retailer_data)
        mock_exec_get_one.assert_called_once_with("SELECT * FROM Retailers WHERE RetailerID = %s;", (retailer_id,))


if __name__ == '__main__':
    unittest.main()
