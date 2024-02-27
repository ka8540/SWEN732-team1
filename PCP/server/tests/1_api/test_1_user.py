import unittest
from tests.utilities.requests_utils import post_rest_call

class UserTest(unittest.TestCase):
    
    def test_0_create_user(self):
        request_body = {
            "id": "love",
            "first_name": "Love",
            "last_name": "Ahir",
            "email": "la3679@rit.edu",
            "phone_number": "8980387432",
            "username": "la3679",
            "password": "1234567"
        }
        # Make the POST request using the utility function
        results, status_code = post_rest_call(self, 'http://localhost:5000/users', json=request_body)
        
        # Check if the request was successful (status code 201)
        self.assertEqual(status_code, 201, "User creation failed")
        
if __name__ == '__main__':
    unittest.main()
