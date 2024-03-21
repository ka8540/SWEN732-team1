import unittest

from db.login import check_user_credentials

class MyTestCase(unittest.TestCase):
    def test_a_validCredentials(self):
        # This test case verifies the behavior of the check_user_credentials function when valid credentials are provided.

        username = 'bp6192'
        hashed_password = '0af7a6d4a76c96a4e1f1c5c3be1560b2c6d8d9eb0082fb0a41eca348'
        expected_message = "Login Creds are Correct"
        actual_result, status_code = check_user_credentials(username, hashed_password)
        self.assertEqual(actual_result["message"], expected_message)
        self.assertEqual(status_code, 200)
        self.assertIsNotNone(actual_result["sessionKey"])

    def test_b_username_not_found(self):
        #  This test case checks the behavior of the check_user_credentials function when a non-existent username is provided.

        # The username 'nonexistent_user' doesn't exist in the database
        username = 'nonexistent_user'
        hashed_password = '0af7a6d4a76c96a4e1f1c5c3be1560b2c6d8d9eb0082fb0a41eca348'
        expected_message = {"message": "Login Creds are Incorrect", "sessionKey": None}
        actual_result, status_code = check_user_credentials(username, hashed_password)

        self.assertEqual(actual_result, expected_message)
        self.assertEqual(status_code, 410)

    def test_c_invalidPassword(self):
        #  This test case verifies the behavior of the check_user_credentials function when an invalid password is provided for an existing username.
        username = 'bp6192'
        hashed_password = 'wrong_password'
        expected_message = {"message": "Password Invalid", "sessionKey": None}
        actual_result, status_code = check_user_credentials(username, hashed_password)

        self.assertEqual(actual_result, expected_message)
        self.assertEqual(status_code, 411)





if __name__ == '__main__':
    unittest.main()
