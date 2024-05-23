import os
import threading
import time
from dotenv import load_dotenv
from app.adapters.audio_handler import AudioHandler
from app.services.transcriptor_service import TranscriptorService
from app.services.messages_service import MessagesService


class TranscriptorBot:
    def __init__(self):
        load_dotenv()
        self.messages_service = MessagesService(os.getenv('ACCOUNT_SID'), os.getenv('AUTH_TOKEN'))
        self.transcriptor_service = TranscriptorService()

    def process_request(self, request):
        try:
            destiny = request.values.get('From', '')
            audio_handler = AudioHandler(request)

            if not audio_handler.get_media_type():
                response_text = 'Por favor, envía un archivo de audio.'
                return

            content = audio_handler.get_audio_content()
            file = audio_handler.save_audio(content, audio_handler.get_extension())
            audio_handler.print_file_size(file, destiny)
            t1 = threading.Thread(target=self.async_transcribe, args=[file, destiny])
            t1.start()
            response_text = 'Espera mientras se transcribe...'
        except Exception as e:
            print(f"Se produjo una excepción: {e}")
            response_text = 'Se ha producido un error, ' + 'vuelve a intentarlo gracias'
        finally:
            return self.messages_service.send_message.execute(destiny, response_text)

    def async_transcribe(self, file, from_number):
        print(f"Inside async_transcribe: {threading.current_thread().name}")
        print(f"Comenzando la transcripción del audio: {threading.current_thread().name}")
        start_time = time.time()

        text_result = self.transcriptor_service.transcribe_audio.execute(file)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Transcripción completada en {elapsed_time} segundos")

        self.messages_service.send_message.execute(from_number, text_result)
