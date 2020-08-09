from __future__ import print_function
import configparser

from service import call
from resources import loader

config_loader = loader.Loader('dev')
config = config_loader.load_config()

def lambda_handler(event, _):
    
    for record in event['Records']:
        print(record['eventID'])
        print(record['eventName'])
        caller = call.Caller(config)
        print(caller.execute_call('toNumber', 'msg'))

    print('Successfully processed %s records.' % str(len(event['Records'])))