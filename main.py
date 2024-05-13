import os
from flask import Flask, request

from app.transcriptor_bot import TranscriptorBot

app = Flask(__name__)
transcriptor_bot = TranscriptorBot()

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=['POST'])
def bot():
    return transcriptor_bot.process_request(request)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))