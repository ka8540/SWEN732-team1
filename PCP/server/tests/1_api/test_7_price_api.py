import json
import unittest
import requests

class TestPriceAPI(unittest.TestCase):

    BASE_URL = 'http://localhost:5000'
    
    def test_get_prices_by_product(self):
        product_id = 1
        url = f'{self.BASE_URL}/prices/products/{product_id}'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_all_prices(self):
        url = f'{self.BASE_URL}/prices'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
    
if __name__ == '__main__':
    unittest.main()