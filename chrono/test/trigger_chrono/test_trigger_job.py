import unittest
from unittest.mock import patch
import json
import os
from trigger_chrono import trigger_job

class TestTrigger(unittest.TestCase):

    _config = None
    _event = None
    _resource_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../../../', 'resources'))

    @classmethod
    def setUpClass(cls):
        pass

    @patch('service.task.create_job', return_value=True)
    def test_execute_call(self, mock_task_creation):
        with open(f'{self._resource_dir}/dynamo_trigger.json') as json_file:
            _event = json.load(json_file)
        errors = trigger_job.lambda_handler(_event, '')
        self.assertTrue(mock_task_creation.called)
        self.assertEquals(len(errors), 0)

    @patch('service.task.validate_datetime', return_value=False)
    @patch('service.task.create_job', return_value=True)
    def test_execute_call_fail_bad_time_format(self, mock_task_createjob, mock_task_datetime):
        with open(f'{self._resource_dir}/dynamo_trigger.json') as json_file:
            _event = json.load(json_file)
        errors = trigger_job.lambda_handler(_event, '')
        self.assertTrue(mock_task_datetime.called)
        self.assertFalse(mock_task_createjob.called)
        self.assertEquals(len(errors), 1)

    @classmethod
    def tearDownClass(cls):
        cls._config = None

if __name__ == '__main__':
    unittest.main()