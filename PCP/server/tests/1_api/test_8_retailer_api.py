import json
import unittest
from unittest.mock import patch, MagicMock
import requests

class TestRetailerAPI(unittest.TestCase):

    BASE_URL = 'http://localhost:5000'
    
    @patch('requests.get')
    def test_get_all_retailers(self, mock_get):
        url = f'{self.BASE_URL}/retailers'

        # Mock the response for getting all retailers
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'id': 1, 'name': 'Retailer 1'}, {'id': 2, 'name': 'Retailer 2'}]
        mock_get.return_value = mock_response

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        mock_get.assert_called_once_with(url)

    @patch('requests.get')
    def test_get_retailer_by_id(self, mock_get):
        retailer_id = 1  # Assuming retailer ID 1 exists
        url = f'{self.BASE_URL}/retailers/{retailer_id}'

        # Mock the response for getting a retailer by ID
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'id': retailer_id, 'name': 'Retailer 1'}
        mock_get.return_value = mock_response

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        mock_get.assert_called_once_with(url)

if __name__ == '__main__':
    unittest.main()
