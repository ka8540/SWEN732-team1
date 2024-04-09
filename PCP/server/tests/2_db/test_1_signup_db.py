import unittest
from unittest.mock import patch
# from db.signup import user_signup
try:
    from ...src.db.signup import list_info_items, user_signup
except:
    from src.db.signup import list_info_items, user_signup

class TestPricesDB(unittest.TestCase):

    @patch('src.db.signup.exec_commit')
    def test_b_new_user_registration(self, mock_exec_commit):

        # Input data for a new user registration
        user_data = {
            'firstname': 'bharathi',
            'lastname': 'pandurangan',
            'username': 'bp6192',
            'password': 'password123',
            'email': 'bp6192@rit.com'
        }
        # Mocking the user_signup function to simulate user already exists scenario
        mock_exec_commit.return_value = user_data

        # Call the function under test
        result, status_code = user_signup(**user_data)
        # Check if the result message and status code match the expected values
        self.assertEqual(result["message"], "User registered successfully")
        self.assertEqual(status_code, 200)  # HTTP 200 OK

        # mock_exec_commit.assert_called_once()

    @patch('src.db.signup.exec_get_all')
    def test_c_existing_user(self, mock_exec_get_all):

        user_data = {
            'firstname': 'bharathi',
            'lastname': 'pandurangan',
            'username': 'existing_user',
            'password': 'password123',
            'email': 'bp6191@rit.com'
        }
        existing_user = {"username": "existing_user"}
        mock_database = [existing_user]

        # Call user_signup with an existing username
        result, status_code = user_signup(**user_data)
        self.assertEqual(result["message"], "User already exists")
        self.assertEqual(status_code, 409)  # HTTP 409 Conflict




if __name__ == '__main__':
    unittest.main()
