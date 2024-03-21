import unittest

import requests

from db import login
from db.logout import user_logout
from utilities.swen_344_db_utils import exec_commit
from db.logout import user_logout

class MyTestCase(unittest.TestCase):
    # def test_successful_logout(self):
    #     # Assuming 'testsessionkey' exists in the database
    #     kwargs = {'session_key': 'testsessionkey'}
    #     expected_response = {"message": "User Logout Successfully!"}
    #     actual_response, status_code = user_logout(kwargs)
    #     self.assertEqual(actual_response, expected_response)
    #     self.assertEqual(status_code, 200)

    def test_a_user_logout(self):

        test_user = {
            "username": "ka3679",
            "password": "Vishulk123456",
            "email": "ka3679@rit.edu",
            "firstname": "Kush",
            "lastname": "Ahir"
        }
        response = requests.post(self.SignUp_URL, json=test_user)
        self.assertEqual(response.status_code, 200)

        login_credentials = {
            "username": "bp6191",
            "hashed_password": "password123",
        }
        response = requests.post(login, json=login_credentials)
        self.assertEqual(response.status_code, 200)

        # Extract session key from login response
        login_response_data = response.json()
        session_key = login_response_data.get('sessionKey')
        print(session_key)
        self.assertIsNotNone(session_key, "Session key should not be None")

        # Perform logout with the session key
        logout_data = {
            "session_key": session_key
        }
        response = requests.post(self.Logout_URL, json=logout_data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
