import json
import requests
import unittest
from tests.test_utils import *  # Make sure this contains any common setup or utility functions you need


class TestCategoriesAPI(unittest.TestCase):
    
    BASE_URL = 'http://localhost:5000/categories'
    CATEGORY_BY_ID_URL = '/categories/<int:category_id>'
    CATEGORY_SEARCH_URL = 'http://localhost:5000/categories/search?query={query}'
    
    def test_get_all_categories(self):
        response = requests.get(self.BASE_URL)
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        
    def test_get_category_by_id(self):
        category_id = 1  # Assuming category ID 1 exists in the database
        url = f'http://localhost:5000/categories/{category_id}'
        response = requests.get(url)
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        
    def test_category_search(self):
        query = 'phone'
        url = self.CATEGORY_SEARCH_URL.format(query=query)
        response = requests.get(url)
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        
        
if __name__ == '__main__':
    unittest.main()