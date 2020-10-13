from enum import Enum
import os

from envparse import env
env.read_envfile()


class TTSSource(Enum):
    Web = 'web'
    Local = 'local'

SERVER_PORT = env.int('SERVER_PORT')
BROKER_URL = env('BROKER_URL')

TTS_SOURCE = TTSSource(env('TTS_SOURCE'))

TMPDIR_PATH = env('TMPDIR_PATH')
if not os.path.exists(TMPDIR_PATH):
    os.mkdir(TMPDIR_PATH)

TMPDIR_CLEAN_INTERVAL_M = env.int('TMPDIR_CLEAN_INTERVAL_M')