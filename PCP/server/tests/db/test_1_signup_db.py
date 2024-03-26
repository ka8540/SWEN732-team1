import hashlib
import json
import unittest
from flask_restful import Resource
from src.utilities.swen_344_db_utils import exec_get_all, exec_commit
from ..test_utils import *
try:
    from ...src.api.signup_api import list_info_items
    from ...src.api.signup_api import user_signup
except:
    from src.api.signup_api import list_info_items
    from src.api.signup_api import user_signup
    


class SignUpDBTestCase(unittest.TestCase):
    def test_a_list_info_items(self):
        printing_response = list_info_items()  # Call the function to list all user records
        print(printing_response)  # Print the response for inspection

    # This function verifies the functionality of the user_signup function
    def test_b_new_user_registration(self):
        # # Input data for a new user registration
        user_data = {
            'firstname': 'bharathi',
            'lastname': 'pandurangan',
            'username': 'bp61980',
            'password': 'password123',
            'email': 'bp6191@rit.com'
        }
        # Call the user_signup function to register a new user
        response, status_code = user_signup(**user_data)
        self.assertEqual(status_code,
                         200)  # Assert that the registration was successful (status code 200 and appropriate message)
        self.assertEqual(response['message'], 'User registered successfully')

        # This function verifies the functionality of the user_signup function when trying to register a user with a username that already exists in the database.

    # def test_c_existing_user(self):
    #     # Attempt to register with an existing username
    #     userdata = {
    #         'firstname': 'bharathi',
    #         'lastname': 'pandurangan',
    #         'username': 'bp6191',
    #         'password': 'Secret123',
    #         'email': 'bp6191@example.com'
    #     }
    #     # Attempt to register a user with an existing username
    #     response, status_code = user_signup(**userdata)
    #     self.assertEqual(status_code,
    #                      409)  # Assert that the registration failed due to an existing user (status code 409)
    #     self.assertEqual(response['message'], 'User already exists')


if __name__ == '__main__':
    unittest.main()
