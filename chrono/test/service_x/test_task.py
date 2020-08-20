import unittest
from unittest.mock import patch
from service import task

class TestService(unittest.TestCase):

    def test_check_date_format(self):
        date_str = '15:46 08/18/2020'
        self.assertTrue(task.validate_datetime(date_str))

    def test_check_date_format_fail(self):
        date_str = '15:46 18/18/2020'
        self.assertFalse(task.validate_datetime(date_str))

if __name__ == '__main__':
    unittest.main()