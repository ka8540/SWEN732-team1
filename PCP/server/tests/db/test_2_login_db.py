import unittest

try:
    from ...src.api.login_api import check_user_credentials 
except:
    from src.db.login import check_user_credentials


class MyTestCase(unittest.TestCase):
    def test_a_validCredentials(self):
        # This test case verifies the behavior of the check_user_credentials function when valid credentials are provided.

        username = 'bp61980'
        hashed_password = '3d45597256050bb1e93bd9c10aee4c8716f8774f5a48c995bf0cf860'
        expected_message = "Login Creds are Correct"
        actual_result, status_code = check_user_credentials(username, hashed_password)
        self.assertEqual(actual_result["message"], expected_message)
        self.assertEqual(status_code, 200)
        self.assertIsNotNone(actual_result["sessionKey"])

    def test_b_username_not_found(self):
        #  This test case checks the behavior of the check_user_credentials function when a non-existent username is provided.

        # The username 'nonexistent_user' doesn't exist in the database
        username = 'nonexistent_user'
        hashed_password = '3d45597256050bb1e93bd9c10aee4c8716f8774f5a48c995bf0cf860'
        expected_message = {"message": "Login Creds are Incorrect", "sessionKey": None}
        actual_result, status_code = check_user_credentials(username, hashed_password)

        self.assertEqual(actual_result, expected_message)
        self.assertEqual(status_code, 410)

    def test_c_invalidPassword(self):
        #  This test case verifies the behavior of the check_user_credentials function when an invalid password is provided for an existing username.
        username = 'bp6191'
        hashed_password = 'wrong_password'
        expected_message = {"message": "Password Invalid", "sessionKey": None}
        actual_result, status_code = check_user_credentials(username, hashed_password)

        self.assertEqual(actual_result, expected_message)
        self.assertEqual(status_code, 411)


if __name__ == '__main__':
    unittest.main()
