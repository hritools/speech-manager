import requests


class Url:
    def __init__(self, hostname, app_path=''):
        self.hostname = hostname
        self.app_path = app_path

    def __str__(self):
        return ''.join((self.hostname, self.app_path))

    def __add__(self, arg):
        return str(self) + arg


TTS_URL = Url('https://robolab.innopolis.university', '/ttsrec')


def get_audio_path(text):
    response = requests.post(TTS_URL + '/tts/', data={'text': text})
    if response.status_code != 200:
        print(response)
        return
    audio_url = TTS_URL.hostname + response.json()['url']
    return audio_url