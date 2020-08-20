from __future__ import print_function
import configparser
import os

config_loader = Loader('dev')
# config = config_loader.load_config()

def lambda_handler(event, _):
        
    for record in event['Records']:
        print(record['eventID'])
        print(record['eventName'])

    print('Successfully processed %s records.' % str(len(event['Records'])))


class Loader(object):

    _resource_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..', 'resources'))

    def __init__(self, env_suffix):

        if 'dev' not in env_suffix:
            print('Config file not found to start app')
            return -1
        self.env_suffix = env_suffix
