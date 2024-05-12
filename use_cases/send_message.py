from interfaces.sender_api import SenderInterface


class SendMessage:
    def __init__(self, message_adapter: SenderInterface):
        self.message_adapter = message_adapter

    def execute(self, destiny, message):
        return self.message_adapter.send_message(destiny, message)
