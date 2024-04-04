import unittest
from unittest.mock import patch

# Assuming the correct import paths based on your try-except blocks
from src.db.logout import user_logout  # Ensure this is the correct path to your user_logout function

class MyTestCase(unittest.TestCase):
    @patch('src.utilities.swen_344_db_utils.exec_commit')
    def test_a_user_logout(self, mock_exec_commit):
        # Setup: Define the session key and expected SQL query
        session_key = 'a318928a5e47a62d205133f6aac0401a'
        expected_query = '''UPDATE user_authentication SET session_key = NULL WHERE session_key = %s;'''
        
        # Expected result after logout
        expected_result = {"message": "User Logout Successfully!"}
        
        # Test: Call the user_logout function
        actual_result, status_code = user_logout({"session_key": session_key})
        
        # Verify: The function returns the expected result and status code
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(status_code, 200)

        # Verify: exec_commit was called once with the expected SQL query and session key
        mock_exec_commit.assert_called_once_with(expected_query, (session_key,))

if __name__ == '__main__':
    unittest.main()
