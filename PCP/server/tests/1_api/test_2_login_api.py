import json
import unittest
from unittest.mock import patch
from tests.test_utils import *

class LoginApiTestCase(unittest.TestCase):
    
    BASE_URL = 'http://localhost:5000/login'
        
    @patch('requests.post')
    def test_1_successful_login(self, mock_post):
        # Creating a mock response object for login
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        
        # Configuring the mock return values
        mock_post.return_value = mock_response
        
        new_user = {
            "username": "la3679",
            "password": "Vishulk1234",
        }
        
        # Calling the function
        response = requests.post(self.BASE_URL, json=new_user)
        
        # Mock Assertion
        mock_post.assert_called_once_with(self.BASE_URL, json=new_user)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
