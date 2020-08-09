import unittest
from unittest.mock import patch
from resources.loader import Loader
from service.call import Caller

class TestService(unittest.TestCase):

    _config = None

    @classmethod
    def setUpClass(cls):
        config_loader = Loader('dev')
        config = config_loader.load_config()
        cls._config = config

    @patch('service.call.Caller.execute_call', return_value='Fine')
    def test_execute_call(self, mock_outbound_call):
        caller = Caller(self._config)
        return_val = caller.execute_call('', 'a custom message')
        self.assertTrue(mock_outbound_call.called)
        self.assertEquals(return_val, 'Fine')

    @classmethod
    def tearDownClass(cls):
        cls._config = None

if __name__ == '__main__':
    unittest.main()