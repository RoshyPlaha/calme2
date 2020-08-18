import unittest
from unittest.mock import patch
from service import task

class TestService(unittest.TestCase):


    # @patch('service.call.Caller.execute_call', return_value='Fine')
    # def test_execute_call(self, mock_outbound_call):
    #     caller = Caller(self._config)
    #     return_val = caller.execute_call('', 'a custom message')
    #     self.assertTrue(mock_outbound_call.called)
    #     self.assertEquals(return_val, 'Fine')

    def test_check_date_format(self):
        date_str = '15:46 08/18/2020'
        self.assertTrue(task.validate_datetime(date_str))

    def test_check_date_format_fail(self):
        date_str = '15:46 18/18/2020'
        self.assertFalse(task.validate_datetime(date_str))

if __name__ == '__main__':
    unittest.main()