import os
import sys
import time

from celery import Celery
from playsound import playsound

import settings

if settings.TTS_SOURCE == settings.TTSSource.Web:
    from tts_web_service import get_audio_path
elif settings.TTS_SOURCE == settings.TTSSource.Local:
    from tts_local import get_audio_path


app = Celery('tasks', broker=settings.BROKER_URL)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(settings.TMPDIR_CLEAN_INTERVAL_M, clean.m())


@app.task
def speak(text):
    audio = get_audio_path(text)
    playsound(audio)
    

@app.task
def clean():
    now = time.time()
    try:
        names = os.listdir(settings.TMPDIR_PATH)
        for name in names:
            path = os.path.join(settings.TMPDIR_PATH, name)
            if not os.path.isfile(path):
                continue
            create_time = os.path.getctime(path)
            if (now - create_time) > settings.TMPDIR_CLEAN_INTERVAL_M * 60:
                os.remove(path)
    except Exception as e:
        print(e)