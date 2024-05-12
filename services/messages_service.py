from adapters.twilio_adapter import TwilioAdapter
from use_cases.send_message import SendMessage


class MessagesService:
    def __init__(self, account_sid, auth_token):
        self.twilio_adapter = TwilioAdapter(account_sid, auth_token)
        self.send_message = SendMessage(self.twilio_adapter)