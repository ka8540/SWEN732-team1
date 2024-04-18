import unittest
from unittest.mock import patch, MagicMock

from tests.test_utils import requests


class LogOutApiTestCase(unittest.TestCase):
    SignUp_URL = 'http://localhost:5000/signUp'
    Login_URL = 'http://localhost:5000/login'
    Logout_URL = 'http://localhost:5000/logout'

    @patch('requests.post')
    def test_1_successful_logout(self, mock_post):
        # Creating a mock response object for login, signup and a mock session key for login
        mock_sign_up_response = MagicMock(status_code=200)
        mock_login_response = MagicMock(status_code=200,
                                        json=MagicMock(return_value={'sessionKey': 'mock_session_key'}))
        mock_logout_response = MagicMock(status_code=200)

        # Setting the side effect of the mock to return the different responses
        mock_post.side_effect = [mock_sign_up_response, mock_login_response, mock_logout_response]

        # Simulating user registration
        test_user = {
            "username": "ka3679",
            "password": "Vishulk123456",
            "email": "ka3679@rit.edu",
            "firstname": "Kush",
            "lastname": "Ahir"
        }
        response = requests.post(self.SignUp_URL, json=test_user)
        self.assertEqual(response.status_code, 200)

        # Simulating user login
        login_credentials = {
            "username": "ka3679",
            "password": "Vishulk123456",
        }
        response = requests.post(self.Login_URL, json=login_credentials)
        self.assertEqual(response.status_code, 200)

        # Simulating extracting session key from login response
        session_key = response.json().get('sessionKey')
        self.assertIsNotNone(session_key, "Session key should not be None")

        # Simulating logout with the session key
        logout_data = {"session_key": session_key}
        response = requests.post(self.Logout_URL, json=logout_data)
        self.assertEqual(response.status_code, 200)

        #  Mock Assertion
        mock_post.assert_any_call(self.SignUp_URL, json=test_user)
        mock_post.assert_any_call(self.Login_URL, json=login_credentials)
        mock_post.assert_any_call(self.Logout_URL, json=logout_data)


if __name__ == '__main__':
    unittest.main()
