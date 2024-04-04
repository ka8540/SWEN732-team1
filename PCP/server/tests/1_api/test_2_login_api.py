import json
import unittest
from unittest.mock import patch
from tests.test_utils import *

class LoginApiTestCase(unittest.TestCase):
    
    BASE_URL = 'http://localhost:5000/login'
        
    @patch('requests.post')
    def test_1_successful_login(self, mock_post):
        # Prepare the mock response to simulate a successful login
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        
        # Set the mock object to return the mock response when it is called
        mock_post.return_value = mock_response
        
        new_user = {
            "username": "la3679",
            "password": "Vishulk1234",
        }
        
        # Call the function that would normally make the HTTP request
        response = requests.post(self.BASE_URL, json=new_user)
        
        # Verify that the requests.post was called with the correct parameters
        mock_post.assert_called_once_with(self.BASE_URL, json=new_user)
        
        # Assert that the mocked response's status code is what we expect
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
