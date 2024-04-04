import json
import unittest
from unittest.mock import patch
from tests.test_utils import *

class SignUpApiTestCase(unittest.TestCase):
    
    BASE_URL = 'http://localhost:5000/signUp'
    
    @patch('requests.get')
    def test_a_user_list(self, mock_get):
        # Create a mock response object, with a `status_code` property
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        
        # Configure the mock to return the mock response when called
        mock_get.return_value = mock_response
        
        # Call the function that should make a `get` request
        response = requests.get(self.BASE_URL)
        
        # Assert the mock was called correctly
        mock_get.assert_called_once_with(self.BASE_URL)
        
        # Assert the response has the status code we expect
        self.assertEqual(response.status_code, 200)
        
    @patch('requests.post')
    def test_b_successful_signup(self, mock_post):
        new_user = {
            "username": "la3679",
            "password": "Vishulk1234",
            "email": "la3679@rit.edu",
            "firstname": "Love",
            "lastname": "Ahir"
        }

        # Create a mock response object for the POST request
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        
        # Configure the mock to return the mock response when called
        mock_post.return_value = mock_response
        
        # Call the function that should make a `post` request
        response = requests.post(self.BASE_URL, json=new_user)
        
        # Assert the mock was called correctly
        mock_post.assert_called_once_with(self.BASE_URL, json=new_user)
        
        # Assert the response has the status code we expect
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
