import unittest
import requests

class TestUserFavoritesAPI(unittest.TestCase):

    BASE_URL = 'http://localhost:5000'

    def test_add_user_favorite(self):
        url = f'{self.BASE_URL}/user_favorites'
        data = {'user_id': 1, 'product_id': 1}  # Assuming user ID and product ID exist in the database
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data['message'], 'Favorite product added successfully')
        
    def test_get_user_favorites(self):
        user_id = 1  # Assuming user ID 1 exists in the database
        url = f'{self.BASE_URL}/user_favorites/{user_id}'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)


if __name__ == '__main__':
    unittest.main()
