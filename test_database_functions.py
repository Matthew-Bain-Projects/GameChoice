import unittest
import database_functions


class TestDatabaseMethods(unittest.TestCase):

    def test_should_connect_to_db(self):
        conn = database_functions.connect_database()
        conn.close()


if __name__ == '__main__':
    unittest.main()
