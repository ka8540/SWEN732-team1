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
        session_key = 'c8730ce3ff2fa09e74efbaed64ba7909'
        expected_result = {"message": "User Logout Successfully!"}
        actual_result, status_code = user_logout({"session_key": session_key})
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()
