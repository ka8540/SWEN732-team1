import requests
import unittest
from unittest.mock import patch, MagicMock

import requests
from tests.test_utils import requests


class TestCategoriesAPI(unittest.TestCase):
    BASE_URL = 'http://localhost:5000/categories'
    CATEGORY_BY_ID_URL = '/categories/<int:category_id>'
    CATEGORY_SEARCH_URL = 'http://localhost:5000/categories/search?query={query}'

    @patch('requests.get')
    def test_get_all_categories(self, mock_get):
        # Creating a mock response object for getting all categories
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'id': 1, 'name': 'Electronics'}, {'id': 2, 'name': 'Books'}]
        mock_get.return_value = mock_response

        response = requests.get(self.BASE_URL)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        mock_get.assert_called_once_with(self.BASE_URL)

    @patch('requests.get')
    def test_get_category_by_id(self, mock_get):
        category_id = 1  # Assuming category ID 1 exists
        url = f'http://localhost:5000/categories/{category_id}'

        # Creating a mock response object for getting a category by ID
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'id': category_id, 'name': 'Electronics'}
        mock_get.return_value = mock_response

        response = requests.get(url)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        mock_get.assert_called_once_with(url)

    @patch('requests.get')
    def test_category_search(self, mock_get):
        query = 'phone'
        url = self.CATEGORY_SEARCH_URL.format(query=query)

        # Creating a mock response object for category search
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'id': 3, 'name': 'Smartphones'}]
        mock_get.return_value = mock_response

        response = requests.get(url)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        mock_get.assert_called_once_with(url)


if __name__ == '__main__':
    unittest.main()
