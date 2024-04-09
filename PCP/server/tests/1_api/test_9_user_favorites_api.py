import unittest
from unittest.mock import patch, MagicMock
import requests

class TestUserFavoritesAPI(unittest.TestCase):

    BASE_URL = 'http://localhost:5000'

    @patch('requests.post')
    def test_add_user_favorite(self, mock_post):
        url = f'{self.BASE_URL}/user_favorites'
        data = {'user_id': 1, 'product_id': 1}  # Assuming user ID and product ID exist in the database
        
        # Creating a mock response object to POST favorite product
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {'message': 'Favorite product added successfully'}
        mock_post.return_value = mock_response
        
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data['message'], 'Favorite product added successfully')
        mock_post.assert_called_once_with(url, json=data)

    @patch('requests.get')
    def test_get_user_favorites(self, mock_get):
        user_id = 1  # Assuming user ID 1 exists in the database
        url = f'{self.BASE_URL}/user_favorites/{user_id}'
        
        # Creating a mock response object to GET favorite product
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'user_id': 1, 'product_id': 1}]
        mock_get.return_value = mock_response
        
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        mock_get.assert_called_once_with(url)

if __name__ == '__main__':
    unittest.main()
