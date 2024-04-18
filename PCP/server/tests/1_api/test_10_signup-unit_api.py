import unittest
from unittest.mock import patch, MagicMock


# Try to import the SignUpApi class from the expected path
try:
    from ...src.db.signup import SignUpApi,list_info_items, user_signup
except:
    from src.db.signup import SignUpApi,list_info_items, user_signup

class TestSignUpAPI(unittest.TestCase):
    
    @patch('src.db.signup.list_info_items')
    def test_get_info_items(self, mock_list_info_items):
        # Setup mock data for list_info_items
        mock_data = [
            {'username': 'user1', 'email': 'user1@example.com'},
            {'username': 'user2', 'email': 'user2@example.com'}
        ]
        mock_list_info_items.return_value = mock_data

        # Call the SignUpApi get method
        api = SignUpApi()
        response = api.get()

        # Assert the get method returns the correct response
        self.assertEqual(response.json, mock_data)
        mock_list_info_items.assert_called_once()

    @patch('src.db.signup.user_signup')
    def test_post_successful_signup(self, mock_user_signup):
        # Setup mock response for a successful signup
        mock_user_signup.return_value = {'message': 'User created successfully'}, 201

        # Prepare mock request data
        data = {
            'username': 'new_user',
            'password': 'new_pass',
            'email': 'new_user@example.com',
            'firstname': 'New',
            'lastname': 'User'
        }

        # Call the SignUpApi post method
        api = SignUpApi()
        with patch('flask_restful.request.json', data):
            response = api.post()

        # Assert the post method returns the correct status code and message
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'User created successfully')
        mock_user_signup.assert_called_once_with(**data)

    @patch('src.db.signup.user_signup')
    def test_post_existing_user(self, mock_user_signup):
        # Setup mock response for an existing user
        mock_user_signup.side_effect = ValueError("User already exists")

        # Prepare mock request data
        data = {
            'username': 'existing_user',
            'password': 'existing_pass',
            'email': 'existing_user@example.com',
            'firstname': 'Existing',
            'lastname': 'User'
        }

        # Call the SignUpApi post method
        api = SignUpApi()
        with patch('flask_restful.request.json', data):
            response = api.post()

        # Assert the post method returns the correct status code and message for existing user
        self.assertEqual(response.status_code, 400)
        self.assertIn("User already exists", response.json['message'])

    # Add more tests to cover missing required fields and other potential error cases

if __name__ == '__main__':
    unittest.main()
