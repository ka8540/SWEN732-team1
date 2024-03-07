import json
import unittest
from tests.test_utils import *

class SignUpApiTestCase(unittest.TestCase):
    
    BASE_URL = 'http://localhost:5000/signup'
    
    def test_user_list(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        
    def test_successful_signup(self):
        new_user = {
            "username": "la3679",
            "password": "Vishulk1234",
            "email": "la3679@rit.edu",
            "firstname": "Love",
            "lastname": "Ahir"
        }
        response = requests.post(self.BASE_URL, json=new_user)
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
