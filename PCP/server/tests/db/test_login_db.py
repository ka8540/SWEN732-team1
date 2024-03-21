import unittest

from db.login import check_user_credentials


class MyTestCase(unittest.TestCase):
    def test_a_validCredentials(self):

        # # actual_result, status_code = check_user_credentials('bp6191', 'Secret123')
        # actual_result, status_code = check_user_credentials('bp6191', 'Secret123')
        # expected_result = {"message": "Login Creds are Correct", "sessionkey" : "be2281c060e06df20cf4544cfebe1a68" }, 200
        # self.assertEqual(actual_result, expected_result)
        # self.assertEqual(status_code, 200)
        username = 'bp6191'
        hashed_password = 'fb0033df5679db881cdd7fd654856ed567c5e5353b90be49479ddccf'
        expected_message = "Login Creds are Correct"
        actual_result, status_code = check_user_credentials(username, hashed_password)
        self.assertEqual(actual_result["message"], expected_message)
        self.assertEqual(status_code, 200)
        self.assertIsNotNone(actual_result["sessionKey"])

if __name__ == '__main__':
    unittest.main()
