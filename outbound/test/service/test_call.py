import unittest
from unittest.mock import patch
from service.call import Caller

class TestService(unittest.TestCase):

    _config = {}

    @classmethod
    def setUpClass(cls):
        pass

    @patch('service.call.Caller.execute_call', return_value='Fine')
    def test_execute_call(self, mock_outbound_call):
        self._config['account_sid'] = 'a'
        self._config['auth_token'] = 'b'
        caller = Caller(self._config)
        return_val = caller.execute_call('', 'a custom message')
        self.assertTrue(mock_outbound_call.called)
        self.assertEquals(return_val, 'Fine')

    @classmethod
    def tearDownClass(cls):
        cls._config = None

if __name__ == '__main__':
    unittest.main()