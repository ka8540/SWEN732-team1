import unittest

import requests

# from db import login
try:
    from ...src.db.logout import user_logout
    from ...src.utilities.swen_344_db_utils import exec_commit
    from ...src.db.logout import user_logout
except:
    from src.db.logout import user_logout
    from src.utilities.swen_344_db_utils import exec_commit
    from src.db.logout import user_logout
    


class MyTestCase(unittest.TestCase):
    def test_a_user_logout(self):
        # This test case verifies the functionality of the user_logout function, which is responsible for logging out a user by invalidating their session key.
        session_key = 'a318928a5e47a62d205133f6aac0401a'  # Input data: a valid session key
        expected_result = {"message": "User Logout Successfully!"}  # Expected result after logout
        actual_result, status_code = user_logout({"session_key": session_key})  # Calling the function under test
        # Asserting the expected outcome
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(status_code, 200)


if __name__ == '__main__':
    unittest.main()
