from twilio.rest import Client

class Caller(object):

    def __init__(self, config):
        self._client = Client(config['account_sid'], config['auth_token'])

    def execute_call(self, to_number, msg):
        call = self._client.calls.create(
                            twiml=f'<Response><Say>{msg}</Say></Response>',
                            to='+447718215606',
                            from_='+12058988592')
        return call.sid


