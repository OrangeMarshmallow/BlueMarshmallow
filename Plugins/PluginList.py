from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var


class PluginList(base):
    def __init__(self):
        super().__init__()
        self.name = 'Список плагинов'
        self.description = 'Возвращает список плагинов'
        self.words = ["плагины", "команды", "plugins", "commands"]

    def func(self):
        try:
            _str = ''
            count_plugins = 0
            for plugin in var.plugins:
                name = str(plugin)
                name = name[name.find('.') + 1:len(name)]
                name = name[0:name.find('.')]
                if not 'Base' in name and not plugin.hide:
                    if self.ulvl in plugin.level:
                        count_plugins += 1
                        if plugin.debug:
                            _str += '$' + name + ' (' + plugin.words[0] + ', ...)\n'
                        else:
                            if plugin.job:
                                _str += name + ' (' + plugin.words[0] + ', ...)\n'
                            else:
                                _str += '*' + name + ' (' + plugin.words[0] + ', ...)\n'
            _str = f'* - плагин не работает.\n$ - плагин в режиме дебага\n[{count_plugins}/{len(var.plugins)}]\n' + _str
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
