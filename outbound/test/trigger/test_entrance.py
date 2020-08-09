import unittest
from unittest.mock import patch
import json

from trigger import entrance

class TestTrigger(unittest.TestCase):

    _config = None
    _event = None

    @classmethod
    def setUpClass(cls):
        pass

    @patch('service.call.Caller.execute_call', return_value='Fine')
    def test_trigger(self, mock_outbound_call):

        with open('test/resources/dynamo_trigger.json') as json_file:
            _event = json.load(json_file)
        entrance.lambda_handler(_event, '')
        self.assertTrue(mock_outbound_call.called)

    @classmethod
    def tearDownClass(cls):
        cls._config = None

if __name__ == '__main__':
    unittest.main()