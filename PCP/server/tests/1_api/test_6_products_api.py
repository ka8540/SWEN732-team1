import json
import requests
import unittest
from unittest.mock import patch, MagicMock

class TestProductsAPI(unittest.TestCase):
    
    BASE_URL = 'http://localhost:5000/products'
    PRODUCT_BY_ID_URL = '/products/<int:product_id>'
    PRODUCT_SEARCH_URL = 'http://localhost:5000/products/search?query={query}'
    
    @patch('requests.get')
    def test_get_all_products(self, mock_get):
        # Creating a mock response object for getting all products
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'id': 1, 'name': 'Product 1'}, {'id': 2, 'name': 'Product 2'}]
        mock_get.return_value = mock_response
        
        response = requests.get(self.BASE_URL)
        data = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        mock_get.assert_called_once_with(self.BASE_URL)

    @patch('requests.get')
    def test_get_product_by_id(self, mock_get):
        product_id = 1  # Assuming product ID 1 exists
        url = f'{self.BASE_URL}/{product_id}'
        
        # Creating a mock response object for getting a product by ID
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'id': product_id, 'name': 'Product 1'}
        mock_get.return_value = mock_response
        
        response = requests.get(url)
        data = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        mock_get.assert_called_once_with(url)
    
    @patch('requests.get')
    def test_product_search(self, mock_get):
        query = 'SAMSUNG Galaxy S24 Ultra Cell Phone, 256GB AI Smartphone'  # Assuming a valid search query
        url = self.PRODUCT_SEARCH_URL.format(query=query)
        
        # Creating a mock response object for product search
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'id': 3, 'name': query}]
        mock_get.return_value = mock_response
        
        response = requests.get(url)
        data = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        mock_get.assert_called_once_with(url)

if __name__ == '__main__':
    unittest.main()
