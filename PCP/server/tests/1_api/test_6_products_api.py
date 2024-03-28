import json
import requests
import unittest

class TestProductsAPI(unittest.TestCase):
    
    BASE_URL = 'http://localhost:5000/products'
    PRODUCT_BY_ID_URL = '/products/<int:product_id>'
    PRODUCT_SEARCH_URL = 'http://localhost:5000/products/search?query={query}'
    
    def test_get_all_products(self):
        response = requests.get(self.BASE_URL)
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        
    def test_get_product_by_id(self):
        product_id = 1  # Assuming product ID 1 exists in the database
        url = f'http://localhost:5000/products/{product_id}'
        response = requests.get(url)
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        
    def test_product_search(self):
        query = 'SAMSUNG Galaxy S24 Ultra Cell Phone, 256GB AI Smartphone'  # Assuming a valid search query
        url = self.PRODUCT_SEARCH_URL.format(query=query)
        response = requests.get(url)
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        
        
if __name__ == '__main__':
    unittest.main()
