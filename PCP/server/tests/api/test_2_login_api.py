import json
import unittest

import requests
from ..test_utils import *

class LoginApiTestCase(unittest.TestCase):
    
    BASE_URL = 'http://localhost:5000/login'
        
    def test_1_successful_login(self):
        new_user = {
            "username": "la3679",
            "hashed_password": "Vishulk1234",
        }
        response = requests.post(self.BASE_URL, json=new_user)
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
