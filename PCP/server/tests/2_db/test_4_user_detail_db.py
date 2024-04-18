import unittest
from unittest.mock import patch

try:
    from ...src.db.user_details import list_user_detail, verify_session_key
except ImportError:
    from src.db.user_details import list_user_detail, verify_session_key


class MyTestCase(unittest.TestCase):
    @patch('src.db.user_details.exec_get_all')
    def test_a_existing_user(self, mock_exec_get_all):
        expected_user_details = [
            ('bharathi', 'pandurangan', 'bp6191', 'bp6191@example.com'),
        ]
        # Mock the database query and return the expected user details
        mock_exec_get_all.return_value = expected_user_details

        # Call the list_user_detail function with an existing username
        username = 'bharathi'
        result = list_user_detail(username)

        # Assert that the result matches the expected user details
        self.assertEqual(result, [
            {'firstname': 'bharathi', 'lastname': 'pandurangan', 'username': 'bp6191', 'email': 'bp6191@example.com'}
        ])

    @patch('src.db.user_details.exec_get_all')
    def test_b_non_existing_user(self, mock_exec_get_all):
        mock_exec_get_all.return_value = []
        result = list_user_detail('bp6191')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
