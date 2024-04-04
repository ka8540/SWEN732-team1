import unittest
from unittest.mock import patch
from src.db.user_details import list_user_detail  # Ensure this is the correct import path

class UserDetailsTestCase(unittest.TestCase):
    @patch('src.utilities.swen_344_db_utils.exec_get_all')
    def test_a_existing_user(self, mock_exec_get_all):
        # Configure the mock to simulate database response for an existing user
        mock_exec_get_all.return_value = [
            ('bharathi', 'pandurangan', 'bp6191', 'bp6191@example.com')
        ]

        expected_user = {
            'firstname': 'bharathi',
            'lastname': 'pandurangan',
            'username': 'bp6191',
            'email': 'bp6191@example.com'
        }

        actual_users = list_user_detail('bp6191')
        self.assertEqual(actual_users, [expected_user])

    @patch('src.utilities.swen_344_db_utils.exec_get_all')
    def test_b_non_existing_user(self, mock_exec_get_all):
        # Configure the mock to simulate an empty database response for a non-existing user
        mock_exec_get_all.return_value = []

        actual_users = list_user_detail('bhara')
        self.assertEqual(actual_users, [])

if __name__ == '__main__':
    unittest.main()
