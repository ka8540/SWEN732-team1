import json
import requests
import unittest
from tests.test_utils import *  # Make sure this contains any common setup or utility functions you need

class UserDetailApiTestCase(unittest.TestCase):
    
    SignUp_URL = 'http://localhost:5000/signUp'
    Login_URL = 'http://localhost:5000/login'
    UserDetail_URL = 'http://localhost:5000/userdetail'
    
    def setUp(self):
        # Register a user
        test_user = {
            "username": "ss3679",
            "password": "SS12345",
            "email": "ss3679@rit.edu",
            "firstname": "Shridhar",
            "lastname": "Shinde"
        }
        requests.post(self.SignUp_URL, json=test_user)

        # Login to get session key
        login_credentials = {
            "username": "ss3679",
            "password": "SS12345",
        }
        response = requests.post(self.Login_URL, json=login_credentials)
        self.assertEqual(response.status_code, 200)
        login_response_data = response.json()
        self.session_key = login_response_data.get('sessionKey')

    def test_1_user_detail_retrieval(self):
        # Ensure we have a session key
        self.assertIsNotNone(self.session_key, "Session key should not be None")

        # Request user details using the session key
        headers = {'X-Session-Key': self.session_key}
        response = requests.get(self.UserDetail_URL, headers=headers)
        self.assertEqual(response.status_code, 200)

        # Verify the user details are correct
        user_details = response.json()
        self.assertIsInstance(user_details, list, "User details should be a list")
        self.assertGreater(len(user_details), 0, "User details list should not be empty")
        self.assertIn('firstname', user_details[0], "First name should be present in user details")
        self.assertIn('lastname', user_details[0], "Last name should be present in user details")
        self.assertIn('username', user_details[0], "Username should be present in user details")
        self.assertIn('email', user_details[0], "Email should be present in user details")
        self.assertEqual(user_details[0]['username'], 'ss3679', "Username in user details should match the test user")

if __name__ == '__main__':
    unittest.main()
