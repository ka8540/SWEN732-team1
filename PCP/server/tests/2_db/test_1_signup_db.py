# import unittest
# from unittest.mock import patch
# from src.api.signup_api import list_info_items, user_signup
# from src.utilities.swen_344_db_utils import exec_get_all, exec_commit

# class SignUpDBTestCase(unittest.TestCase):

#     def setUp(self):
#         # Setup your test database or clean it
#         pass

#     def tearDown(self):
#         # Teardown your test database or clean it
#         pass

#     @patch('src.utilities.swen_344_db_utils.exec_get_all')
#     def test_a_list_info_items(self, mock_exec_get_all):
#         # Mock the exec_get_all to return expected data
#         mock_exec_get_all.return_value = [{'username': 'testuser', 'email': 'test@example.com'}]
        
#         printing_response = list_info_items()
#         print(printing_response)  # This will show the mocked response
#         # You can add assertions here to check the printing_response content if it's structured

#     @patch('src.utilities.swen_344_db_utils.exec_commit')
#     def test_b_new_user_registration(self, mock_exec_commit):
#         # Mock the exec_commit to simulate database insert without actually inserting
#         mock_exec_commit.return_value = None  # Adjust based on your actual function's return value on success

#         user_data = {
#             'firstname': 'bharathi',
#             'lastname': 'pandurangan',
#             'username': 'bp61980',
#             'password': 'password123',
#             'email': 'bp6191@rit.com'
#         }
#         response, status_code = user_signup(**user_data)
#         self.assertEqual(status_code, 200)
#         self.assertEqual(response['message'], 'User registered successfully')

#     @patch('src.utilities.swen_344_db_utils.exec_commit')
#     def test_c_existing_user(self, mock_exec_commit):
#         # First call to exec_commit simulates successful user registration
#         # Second call simulates a database error due to unique constraint, for example
#         mock_exec_commit.side_effect = [None, Exception("Unique constraint failed")]

#         userdata_1 = {
#             'firstname': 'bharathi',
#             'lastname': 'pandurangan',
#             'username': 'bp6191',
#             'password': 'Secret123',
#             'email': 'bp6191@example.com'
#         }

#         # First user registration should succeed
#         response, status_code = user_signup(**userdata_1)
#         self.assertEqual(status_code, 200)

#         # Second registration with the same username should fail
#         response, status_code = user_signup(**userdata_1)
#         self.assertEqual(status_code, 409)
#         self.assertEqual(response['message'], 'User already exists')

# if __name__ == '__main__':
#     unittest.main()
