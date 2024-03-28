import json
import unittest
import requests

class TestRetailerAPI(unittest.TestCase):

    BASE_URL = 'http://localhost:5000'
    
    def test_get_all_retailers(self):
        url = f'{self.BASE_URL}/retailers'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

    def test_get_retailer_by_id(self):
        retailer_id = 1  # Assuming retailer ID 1 exists in the database
        url = f'{self.BASE_URL}/retailers/{retailer_id}'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        
        
if __name__ == '__main__':
    unittest.main()