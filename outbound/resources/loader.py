import configparser

class Loader(object):

    def __init__(self, env_suffix):

        if 'dev' not in env_suffix:
            print('Config file not found to start app')
            return -1
        self.env_suffix = env_suffix
        print(self.load_config())

    def load_config(self):
        config = configparser.ConfigParser()
        config.read('resources/config.ini')
        return config[f'twilio_{self.env_suffix}']