from __future__ import print_function
import configparser
import os
from service import task

class Loader(object):

    _resource_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..', 'resources'))
    def __init__(self, env_suffix):

        if 'dev' not in env_suffix:
            print('Config file not found to start app')
            return -1
        self.env_suffix = env_suffix

config_loader = Loader('dev')
# config = config_loader.load_config()

def lambda_handler(event, _):
    
    errors = {}
    for record in event['Records']:
        idx = record['id']
        date_str = record['datetime']
        if not task.validate_datetime(date_str):
            errors[idx] = 'task not made'
        else:
            print(f'creating new job for id {idx}')
            task.create_job(idx, date_str)

    print('Successfully processed %s records.' % str(len(event['Records'])))
    return errors



