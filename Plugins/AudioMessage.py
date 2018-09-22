from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from gtts import gTTS
import os


class AudioMessagePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Аудио сообщение'
        self.description = 'Отправляет голосовое сообщение'
        self.words = ["аудио", "озвучь", "audio"]

    def func(self):
        try:
            if len(str(self.text)) > 0:
                tts = gTTS(text=str(self.text), lang='ru')
                tts.save('audio.ogg')
                self.result['attachment'] = UEngine.audio_message('audio.ogg')
                os.remove('audio.ogg')
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
