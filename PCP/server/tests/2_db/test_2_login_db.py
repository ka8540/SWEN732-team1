import unittest
from unittest.mock import patch
from src.db.login import list_info_items, check_user_credentials

class MyTestCase(unittest.TestCase):

    @patch('src.db.login.exec_get_all')
    def test_a_list_info_items(self, mock_exec_get_all):
        # Sample data to be returned by the mock
        sample_data = [
            (1, 'user1', 'email1@example.com'),
            (2, 'user2', 'email2@example.com')
        ]
        mock_exec_get_all.return_value = sample_data

        # Call the function under test
        result = list_info_items()

        # Assertions
        self.assertEqual(result, sample_data)
        mock_exec_get_all.assert_called_once()

    @patch('src.db.login.exec_get_one')
    def test_b_validCredentials(self, mock_exec_get_one):
        # Setup the mock to return a successful user lookup and password match
        mock_exec_get_one.side_effect = [(1,), (1,)]

        # Call the function with mocked valid credentials
        result, status_code = check_user_credentials('valid_user', 'hashed_password')

        # Assertions
        self.assertEqual(result["message"], "Login Creds are Correct")
        self.assertEqual(status_code, 200)
        self.assertIsNotNone(result.get("sessionKey"))

    # @patch('src.db.login.exec_get_one')
    # def test_c_InvalidCredentials(self, mock_exec_get_one):
    #     # Setup the mock to indicate user not found
    #     mock_exec_get_one.return_value = None

    #     # Call the function with mocked invalid credentials
    #     result, status_code = check_user_credentials('invalid_user', 'hashed_password')

    #     # Assertions
    #     self.assertEqual(result["message"], "Login Creds are Incorrect")
    #     self.assertEqual(status_code, 410)
    #     self.assertIsNone(result.get("sessionKey"))

    @patch('src.db.login.exec_get_one')
    def test_d_passwordIncorrect(self, mock_exec_get_one):
        # Setup the mock to return a successful user lookup and password mismatch
        mock_exec_get_one.side_effect = [(1,), None]

        # Call the function with mocked valid username but invalid password
        result, status_code = check_user_credentials('valid_user', 'wrong_hashed_password')

        # Assertions
        self.assertEqual(result["message"], "Password Invalid")
        self.assertEqual(status_code, 411)
        self.assertIsNone(result.get("sessionKey"))

if __name__ == '__main__':
    unittest.main()
