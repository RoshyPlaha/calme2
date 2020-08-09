from twilio.rest import Client

# account_sid = 'AC6854b48e0fbd9e16aa77982bf969faaa'
# auth_token = 'd5a3fa2b06f55aa3cead2b17269d3d30'

class Caller(object):

    def __init__(self, config):
        self._client = Client(config['account_sid'], config['auth_token'])

    def execute_call(self, to_number, msg):
        call = self._client.calls.create(
                            twiml=f'<Response><Say>{msg}</Say></Response>',
                            to='+447718215606',
                            from_='+12058988592')
        return call.sid


