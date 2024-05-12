import os
import threading

from flask import Flask, request, jsonify
from dotenv import load_dotenv

from adapters.audio_handler import AudioHandler
from adapters.twilio_adapter import TwilioAdapter
from adapters.whisper_adapter import WhisperAdapter
from use_cases.send_message import SendMessage
from use_cases.transcribe_audio import TranscribeAudio

print(f"In flask global level: {threading.current_thread().name}")
load_dotenv()
MODEL_SIZE = os.getenv('MODEL_SIZE')
#IS_PRODUCTION = os.getenv('IS_MAINTENNANCE')
IS_MAINTENNANCE = os.getenv("IS_MAINTENNANCE", 'False').lower() in ('true', '1', 't')
ADMIN_PHONE_NUMBER = os.getenv('ADMIN_PHONE_NUMBER')
app = Flask(__name__)


twilio_adapter = TwilioAdapter(os.getenv('ACCOUNT_SID'), os.getenv('AUTH_TOKEN'))
send_message = SendMessage(twilio_adapter)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=['POST'])
def bot():
    try:
        destiny = request.values.get('From', '')
        audio_handler = AudioHandler(request)

        if not audio_handler.get_media_type():
            return send_message.execute(destiny, 'Por favor, envía un archivo de audio.')

        content = audio_handler.get_audio_content()
        file = audio_handler.save_audio(content, audio_handler.get_extension())
        audio_handler.print_file_size(file, destiny)

        t1 = threading.Thread(target=async_transcribe, args=[file, destiny])
        t1.start()
        response_text = 'Espera mientras se transcribe...'
    except Exception as e:
        print(f"Se produjo una excepción: {e}")
        response_text = 'Se ha producido un error, ' + 'vuelve a intentarlo gracias'
    finally:
        return send_message.execute(destiny, response_text)


def async_transcribe(file, from_number):
    print(f"Inside async_transcribe: {threading.current_thread().name}")
    transcriptor = TranscribeAudio(WhisperAdapter())
    text_result = transcriptor.execute(file)
    send_message.execute(from_number, text_result)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
