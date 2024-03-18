import unittest
from test_utils import get_rest_call, delete_rest_call, put_rest_call, post_rest_call

class TestExample(unittest.TestCase):

    def setUp(self):  
        """Initialize DB using API call"""
        post_rest_call(self, 'http://localhost:5000/manage/init')
        print("DB Should be reset now")

    def test_login(self):
        expected = []
        actual = get_rest_call(self, 'http://localhost:5000')
        self.assertEqual(expected, actual)
