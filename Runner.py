from Log import Log
from Bot import Main
import datetime
from Engine import Engine

if __name__ == "__main__":
    cmd = "python -u bot.py"
    p = None
    start = False
    auto = True

    while auto:
        try:
            if not start:
                f = open('DB\\LOG.txt', 'a')
                f.write(f'\n:--===Starting Bot: {datetime.datetime.now()}===--:\n')
                f.close()
                Log.show_service('Инициализация плагинов:')
                Engine().initialize()
                Log.show_info('Запуск бота')
                start = True
            else:
                Log.show_info('Перезапуск бота')
            Main.start()
        except KeyboardInterrupt:
            try:
                Log.show_service('Остановка бота')
                exit()
            except SystemExit:
                import traceback
                Log.show_service('Отключение автозапуска')
                auto = False
        except SystemExit:
            Log.show_service('Бот остановлен')
        except Exception as e:
            Log.show_error(e)
        Log.show_service('Бот остановлен')
