import json
import unittest
from tests.test_utils import *

class SignUpApiTestCase(unittest.TestCase):
    
    BASE_URL = 'http://localhost:5000/login'
        
    def test_2_successful_login(self):
        new_user = {
            "username": "la3679",
            "password": "Vishulk1234",
        }
        response = requests.post(self.BASE_URL, json=new_user)
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
