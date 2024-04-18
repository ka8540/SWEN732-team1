import requests
import unittest
from unittest.mock import patch, MagicMock

import requests
from tests.test_utils import *


class UserDetailApiTestCase(unittest.TestCase):
    SignUp_URL = 'http://localhost:5000/signUp'
    Login_URL = 'http://localhost:5000/login'
    UserDetail_URL = 'http://localhost:5000/userdetail'

    @patch('requests.post')
    def setUp(self, mock_post):
        # Creating a mock response object for  user registration and user login with a session key
        mock_sign_up_response = MagicMock(status_code=200)
        mock_login_response = MagicMock(status_code=200,
                                        json=MagicMock(return_value={'sessionKey': 'mock_session_key'}))

        # Setting the side effect of the mock to return the different responses
        mock_post.side_effect = [mock_sign_up_response, mock_login_response]

        # Simulating user registration
        test_user = {
            "username": "ss3679",
            "password": "SS12345",
            "email": "ss3679@rit.edu",
            "firstname": "Shridhar",
            "lastname": "Shinde"
        }
        requests.post(self.SignUp_URL, json=test_user)

        # Simulating user login to get a session key
        login_credentials = {
            "username": "ss3679",
            "password": "SS12345",
        }
        response = requests.post(self.Login_URL, json=login_credentials)
        login_response_data = response.json()
        self.session_key = login_response_data.get('sessionKey')

    @patch('requests.get')
    def test_1_user_detail_retrieval(self, mock_get):
        self.assertIsNotNone(self.session_key, "Session key should not be None")

        # Mock response for user detail retrieval
        mock_user_detail_response = MagicMock(status_code=200, json=MagicMock(return_value=[{
            'firstname': 'Shridhar',
            'lastname': 'Shinde',
            'username': 'ss3679',
            'email': 'ss3679@rit.edu'
        }]))
        mock_get.return_value = mock_user_detail_response

        # Request (mocked) user details using the session key
        headers = {'X-Session-Key': self.session_key}
        response = requests.get(self.UserDetail_URL, headers=headers)

        self.assertEqual(response.status_code, 200)

        # Verifying the mocked user details
        user_details = response.json()
        self.assertIsInstance(user_details, list, "User details should be a list")
        self.assertGreater(len(user_details), 0, "User details list should not be empty")
        self.assertIn('firstname', user_details[0], "First name should be present in user details")
        self.assertIn('lastname', user_details[0], "Last name should be present in user details")
        self.assertIn('username', user_details[0], "Username should be present in user details")
        self.assertIn('email', user_details[0], "Email should be present in user details")
        self.assertEqual(user_details[0]['username'], 'ss3679', "Username in user details should match the test user")

        # Mock Assertion 
        mock_get.assert_called_once_with(self.UserDetail_URL, headers=headers)


if __name__ == '__main__':
    unittest.main()
