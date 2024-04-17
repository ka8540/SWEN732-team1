import unittest
from unittest.mock import patch

# from db.signup import user_signup
try:
    from ...src.db.signup import list_info_items, user_signup
except:
    from src.db.signup import list_info_items, user_signup


class TestPricesDB(unittest.TestCase):

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
