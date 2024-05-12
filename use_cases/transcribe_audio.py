from interfaces.transcriber_api import TranscriberInterface


class TranscribeAudio:
    def __init__(self, transcript_adapter: TranscriberInterface):
        self.transcriber_adapter = transcript_adapter

    def execute(self, audio_file):
        return self.transcriber_adapter.transcribe(audio_file)
