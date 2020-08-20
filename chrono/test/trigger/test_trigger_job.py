import unittest
from unittest.mock import patch
import json
import os
from trigger import trigger_job

class TestTrigger(unittest.TestCase):

    _config = None
    _event = None
    _resource_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../../../', 'resources'))

    @classmethod
    def setUpClass(cls):
        pass

    def test_trigger(self):
        with open(f'{self._resource_dir}/dynamo_trigger.json') as json_file:
            _event = json.load(json_file)
        trigger_job.lambda_handler(_event, '')
        self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        cls._config = None

if __name__ == '__main__':
    unittest.main()