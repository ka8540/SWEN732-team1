import unittest

from utilities.swen_344_db_utils import exec_sql_file

class PCPSetupDB(unittest.TestCase):
    """
    This test file contains unit test for setting up database tables and
    initial data required for testing purposes.
    """

    # Setup test data from SQL file and also sample rows
    def test_0_setup_tables(self):
        print("Setting up test data...")
        # Execute SQL commands from a specified file to set up the database schema and initial data
        result = exec_sql_file("data/UserDetail.sql")


if __name__ == '__main__':
    unittest.main()
