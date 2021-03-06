from __future__ import print_function
import configparser
import os

from service import call

def lambda_handler(event, _):
    
    config_loader = Loader('dev')
    config = config_loader.load_config()

    for record in event['Records']:
        print(record['eventID'])
        print(record['eventName'])
        caller = call.Caller(config)
        print(caller.execute_call('toNumber', 'msg'))

    print('Successfully processed %s records.' % str(len(event['Records'])))

class Loader(object):

    _resource_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..', 'resources'))

    def __init__(self, env_suffix):

        if 'dev' not in env_suffix:
            print('Config file not found to start app')
            return -1
        self.env_suffix = env_suffix

    def load_config(self):
        config = configparser.ConfigParser()
        config.read(f'{self._resource_dir}/config.ini')
        return config[f'twilio_{self.env_suffix}']