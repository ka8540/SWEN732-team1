import unittest
from db.user_details import list_user_detail, verify_session_key


class user_details(unittest.TestCase):
    def test_a_existing_user(self):
        # Testing with the user 'bp6191' which exists in the database
        expected_user = {
            'firstname': 'bharathi',
            'lastname': 'pandurangan',
            'username': 'bp6191',
            'email': 'bp6191@rit.edu'
        }
        # Fetch actual user details for the user 'bp6191'
        actual_users = list_user_detail('bp6191')
        # Assert that the actual user details match the expected user details
        self.assertEqual(actual_users, [expected_user])

    def test_non_existing_user(self):
        # Testing with 'bhara'. The username which does not exist in the database
        actual_users = list_user_detail('bhara')
        # Assert that the actual user details are empty (as no user with username 'bhara' exists)
        self.assertEqual(actual_users, [])


if __name__ == '__main__':
    unittest.main()
