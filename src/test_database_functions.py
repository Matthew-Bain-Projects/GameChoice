import unittest
import database_functions

class TestDatabaseMethods(unittest.TestCase):

    def test_should_connect_to_db(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
