import unittest
from test_utils import get_rest_call, delete_rest_call, put_rest_call, post_rest_call

class TestSignupAPI(unittest.TestCase):

    def setUp(self):
        """Initialize DB using API call"""
        post_rest_call(self, 'http://localhost:5000/manage/init')
        print("DB Should be reset now")


        # @patch('your_module.get_rest_call')

    def test_login(self):
        # # Mock the response from the REST call
        # mock_get_rest_call.return_value = {'status': 'success', 'message': 'Login successful'}

        # Call the login function and capture the response
        actual = post_rest_call(self, 'http://localhost:5000/login')

        # Define the expected response
        expected = {'status': 'success', 'message': 'Login successful'}

        # Assert that the actual response matches the expected response
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
