import unittest
from unittest.mock import patch

try:
    from ...src.db.logout import user_logout
except:
    from src.db.logout import user_logout


class MyTestCase(unittest.TestCase):
    @patch('src.db.logout.exec_commit')
    def test_logout(self, mock_exec_commit):
        # Set up mock session key
        session_key = "mock_session_key"

        # Call the function under test
        result, status_code = user_logout({'session_key': session_key})

        # Assert that the exec_commit function was called with the correct parameters
        mock_exec_commit.assert_called_once_with(
            '''UPDATE user_authentication SET session_key = NULL WHERE session_key = %s;''', (session_key,))

        # Assert the expected outcome
        expected_result = {"message": "User Logout Successfully!"}
        expected_status_code = 200
        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, expected_status_code)


if __name__ == '__main__':
    unittest.main()
