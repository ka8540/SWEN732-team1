import json
import unittest
from unittest.mock import patch
from tests.test_utils import *

class SignUpApiTestCase(unittest.TestCase):
    
    BASE_URL = 'http://localhost:5000/signUp'
    
    @patch('requests.get')
    def test_a_user_list(self, mock_get):
        # Creating a mock response object
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        
        # Configuring the mock return values
        mock_get.return_value = mock_response
        
        # Calling the function
        response = requests.get(self.BASE_URL)
        
        # Mock Assertion
        mock_get.assert_called_once_with(self.BASE_URL)
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

        # Creating a mock response object for signup
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        
        # Configuring the mock return values
        mock_post.return_value = mock_response
        
        # Calling the function
        response = requests.post(self.BASE_URL, json=new_user)
        
        # Mock Assertion
        mock_post.assert_called_once_with(self.BASE_URL, json=new_user)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
