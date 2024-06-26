from app.adapters.whisper_adapter import WhisperAdapter
from app.use_cases.transcribe_audio import TranscribeAudio

class TranscriptorService:
    def __init__(self):
        self.transcriptor_adapter = WhisperAdapter()
        self.transcribe_audio = TranscribeAudio(self.transcriptor_adapter)