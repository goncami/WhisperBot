import os

import requests


class AudioHandler:
    def __init__(self, request):
        self.request = request

    def get_audio_content(self):
        audio_url = self.get_audio_url()
        return requests.get(audio_url).content

    def get_audio_url(self):
        return self.request.values.get('MediaUrl0', '')

    def get_extension(self):
        media_type = self.get_media_type()
        return media_type.split('/')[1]

    def get_media_type(self):
        return self.request.values.get('MediaContentType0', '')

    def save_audio(self, binary_content, extension):
        file_path = f'input_audio.{extension}'
        with open(file_path, "wb") as f:
            f.write(binary_content)
        return file_path

    def print_file_size(self, file, destino):
        file_size = os.path.getsize(file)
        print(f"File Size is : {file_size} bytes to phone number: {destino}")
