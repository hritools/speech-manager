import os
import subprocess
from uuid import uuid4

from settings import TMPDIR_PATH


def get_audio_path(text :str) -> str:
    name = uuid4().hex
    path = os.path.join(TMPDIR_PATH, name)    
    _rhvoice(text, path)
    return path


def _system_tts(text, path, params):
    txt_path = path + '.txt'
    params[params.index(None)] = txt_path
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
    proc = subprocess.Popen(params, stdin=subprocess.PIPE)
    proc.wait()


def _rhvoice(text, path):
    params = ['RHVoice-test', '-i', None, '-o', path, '-p', 'aleksandr+alan']
    _system_tts(text, path, params)
