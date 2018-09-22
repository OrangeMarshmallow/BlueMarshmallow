from Settings import BotSettings as var
from colorama import Fore
import datetime
import codecs


class Log(object):
    out = True

    def __init__(self):
        self.message = 'None'
        self.mode = Log.Text.none

    class Text:
        info = "Info"
        error = "Error"
        service = "Service"
        none = "What"
        vk = "VK"
        plugin = "Plugin"

    @staticmethod
    def type(t):
        if t == Log.Text.info:
            return Fore.LIGHTGREEN_EX
        elif t == Log.Text.error:
            return Fore.LIGHTRED_EX
        elif t == Log.Text.service:
            return Fore.LIGHTYELLOW_EX
        elif t == Log.Text.vk:
            return Fore.LIGHTMAGENTA_EX
        elif t == Log.Text.plugin:
            return Fore.LIGHTBLUE_EX
        else:
            return Fore.LIGHTBLUE_EX

    @staticmethod
    def show(message, type_message):
        if Log.out:
            now = datetime.datetime.now()
            h = now.hour
            m = now.minute
            s = now.second
            if h < 10:
                h = '0' + str(h)
            if m < 10:
                m = '0' + str(m)
            if s < 10:
                s = '0' + str(s)
            if var.log_console and var.log_all:
                print(f"{Fore.LIGHTBLACK_EX}[{h}:{m}:{s}] {Log.type(type_message)}{type_message}: {Fore.CYAN}{message}")
            if var.log_text and var.log_all:
                file = codecs.open('DB\\LOG.txt', 'a', 'utf-8')
                file.write(f'[{h}:{m}:{s}] {type_message}: {message}\n')
                file.close()

    @staticmethod
    def show_info(message):
        Log.show(message, Log.Text.info)

    @staticmethod
    def show_error(message):
        Log.show(message, Log.Text.error)

    @staticmethod
    def show_service(message):
        Log.show(message, Log.Text.service)

    @staticmethod
    def show_what(message):
        Log.show(message, Log.Text.none)

    @staticmethod
    def show_vk(message):
        Log.show(message, Log.Text.vk)

    @staticmethod
    def show_plugin(message):
        Log.show(message, Log.Text.plugin)
