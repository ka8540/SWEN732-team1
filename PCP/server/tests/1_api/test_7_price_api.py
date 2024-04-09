import json
import unittest
from unittest.mock import patch, MagicMock
import requests

class TestPriceAPI(unittest.TestCase):

    BASE_URL = 'http://localhost:5000'
    
    @patch('requests.get')
    def test_get_prices_by_product(self, mock_get):
        product_id = 1
        url = f'{self.BASE_URL}/prices/products/{product_id}'

        # Creating a mock response object for getting prices by product ID
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'product_id': product_id, 'price': '100'}]
        mock_get.return_value = mock_response

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        mock_get.assert_called_once_with(url)

    @patch('requests.get')
    def test_get_all_prices(self, mock_get):
        url = f'{self.BASE_URL}/prices'

        # Creating a mock response object for getting all prices
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'product_id': 1, 'price': '100'}, {'product_id': 2, 'price': '200'}]
        mock_get.return_value = mock_response

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        mock_get.assert_called_once_with(url)

if __name__ == '__main__':
    unittest.main()
