import os

from dotenv import load_dotenv

from interfaces.transcriber_api import TranscriberInterface
import whisper

load_dotenv()
MODEL_SIZE = os.getenv('MODEL_SIZE')


class WhisperAdapter(TranscriberInterface):
    def transcribe(self, audio_file):
        print(f"Whisper MODEL_SIZE: {MODEL_SIZE}")
        model = whisper.load_model(MODEL_SIZE)

        # load the entire audio file
        audio = whisper.load_audio(audio_file)

        options = {
            "language": "es",  # input language, if omitted is auto detected
            "task": "transcribe"  # translate or "transcribe" if you just want transcription
        }
        result = whisper.transcribe(model, audio, **options)
        text = result["text"]

        return "*Transcripción:* " + text
