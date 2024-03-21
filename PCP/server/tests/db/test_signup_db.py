import hashlib
import json
import unittest
from flask_restful import Resource
from utilities.swen_344_db_utils import exec_get_all, exec_commit
from ..test_utils import *
from db.signup import list_info_items
from db.signup import user_signup

class SignUpDBTestCase(unittest.TestCase):

    def test_a_list_info_items(self):
        printing_response = list_info_items()
        print(printing_response)

    def test_b_new_user_registration(self):
        # Input data
        user_data = {
            'firstname': 'bharathi',
            'lastname': 'pandurangan',
            'username': 'bp6191',
            'password': 'Secret123!',
            'email': 'bp6191@rit.edu'
        }
        response, status_code = user_signup(**user_data)
        self.assertEqual(status_code, 200)
        self.assertEqual(response['message'], 'User registered successfully')

    def test_c_existing_user(self):
        # Attempt to register with an existing username
        userdata = {
            'firstname': 'bharathi',
            'lastname': 'pandurangan',
            'username': 'bp6191',
            'password': 'Secret123!',
            'email': 'bp6191@example.com'
        }
        response, status_code = user_signup(**userdata)
        self.assertEqual(status_code, 409)
        self.assertEqual(response['message'], 'User already exists')

        # Verify that the existing user is not overwritten or duplicated

if __name__ == '__main__':
    unittest.main()
