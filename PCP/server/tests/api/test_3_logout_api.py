import json
import unittest
from tests.test_utils import *

class LogOutApiTestCase(unittest.TestCase):
    
    SignUp_URL = 'http://localhost:5000/signUp'
    Login_URL = 'http://localhost:5000/login'
    Logout_URL = 'http://localhost:5000/logout'
    
    def test_1_successful_logout(self):
        # User registration
        test_user = {
            "username": "ka3679",
            "password": "Vishulk123456",
            "email": "ka3679@rit.edu",
            "firstname": "Kush",
            "lastname": "Ahir"
        }
        response = requests.post(self.SignUp_URL, json=test_user)
        self.assertEqual(response.status_code, 200)
        
        login_credentials = {
            "username": "ka3679",
            "password": "Vishulk123456",
        }
        response = requests.post(self.Login_URL, json=login_credentials)
        self.assertEqual(response.status_code, 200)
        
        # Extract session key from login response
        login_response_data = response.json()
        session_key = login_response_data.get('sessionKey')
        print(session_key)
        self.assertIsNotNone(session_key, "Session key should not be None")
        
        # Perform logout with the session key
        logout_data = {
            "session_key": session_key
        }
        response = requests.post(self.Logout_URL, json=logout_data)
        self.assertEqual(response.status_code, 200)
        
        
if __name__ == '__main__':
    unittest.main()
