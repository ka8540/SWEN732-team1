import unittest
from unittest.mock import patch
from src.db.login import check_user_credentials  # Assuming this is the correct import path

class MyTestCase(unittest.TestCase):

    @patch('src.utilities.swen_344_db_utils.exec_get_one')
    @patch('src.utilities.swen_344_db_utils.exec_commit')
    @patch('src.db.login.generate_session_key')  # Assuming generate_session_key is a function you have
    def test_a_validCredentials(self, mock_generate_session_key, mock_exec_commit, mock_exec_get_one):
        # Configure the mocks
        mock_exec_get_one.side_effect = [True, True]  # Simulates both username existence and password correctness
        mock_generate_session_key.return_value = 'new_session_key'

        username = 'bp61980'
        hashed_password = '3d45597256050bb1e93bd9c10aee4c8716f8774f5a48c995bf0cf860'
        expected_message = "Login Creds are Correct"

        actual_result, status_code = check_user_credentials(username, hashed_password)

        self.assertEqual(actual_result["message"], expected_message)
        self.assertEqual(status_code, 200)
        self.assertEqual(actual_result["sessionKey"], 'new_session_key')

    @patch('src.utilities.swen_344_db_utils.exec_get_one')
    def test_b_username_not_found(self, mock_exec_get_one):
        # Configure the mock to simulate username not found
        mock_exec_get_one.return_value = False

        username = 'nonexistent_user'
        hashed_password = '3d45597256050bb1e93bd9c10aee4c8716f8774f5a48c995bf0cf860'
        expected_message = {"message": "Login Creds are Incorrect", "sessionKey": None}

        actual_result, status_code = check_user_credentials(username, hashed_password)

        self.assertEqual(actual_result, expected_message)
        self.assertEqual(status_code, 410)

    @patch('src.utilities.swen_344_db_utils.exec_get_one')
    def test_c_invalidPassword(self, mock_exec_get_one):
        # Configure the mock to first return True for username existence, then False for password correctness
        mock_exec_get_one.side_effect = [True, False]

        username = 'existing_username'
        hashed_password = 'wrong_password'
        expected_message = {"message": "Login Creds are Incorrect", "sessionKey": None}

        actual_result, status_code = check_user_credentials(username, hashed_password)
        
        self.assertEqual(actual_result, expected_message)
        self.assertEqual(status_code, 410)

if __name__ == '__main__':
    unittest.main()
