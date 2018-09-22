import os
import inspect
from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
from Log import Log
from VK import VK
from Utils import Engine as UEngine
import collections


class Engine(object):
    def __init__(self):
        self.plugin_dir = "Plugins"
        self.modules = []
        self.package_obj = None

    def initialize(self):
        check1 = []
        check2 = []
        check3 = []
        if not var.run:
            tr = 0
            fl = 0
            al = 0
            var.run = True
            len_plugins = len(os.listdir(self.plugin_dir)) - 4
            counter_plugins = 1
            for fname in os.listdir(self.plugin_dir):
                if fname.endswith(".py"):
                    module_name = fname[: -3]
                    if module_name != "Base" and module_name != "__init__":
                        try:
                            self.package_obj = __import__(self.plugin_dir + "." + module_name)
                            self.modules.append(module_name)
                            Log.show_service(f"[{counter_plugins}/{len_plugins}] {module_name} loaded")
                            tr += 1
                        except Exception as e:
                            Log.show_error(f"[{counter_plugins}/{len_plugins}] {module_name} not loaded: {e}")
                            fl += 1
                        al += 1
                        counter_plugins += 1
            Log.show_service(f'Loaded: {tr}/{al} ({fl} errors)')

        for module_name in self.modules:
            module_obj = getattr(self.package_obj, module_name)

            for elem in dir(module_obj):
                obj = getattr(module_obj, elem)
                if inspect.isclass(obj):
                    if issubclass(obj, base):
                        a = obj()
                        if not 'BasePlugin' in str(a):
                            var.plugins.append(a)
                            name = str(a)[str(a).find('.')+1:str(a).find(' ')]
                            name = name[name.find('.')+1:]
                            check1.append(name)
                            check3.append(a.name)
                            for word in a.words:
                                check2.append(word)
        if len(check1) != len(set(check1)):
            _mas = [item for item, count in collections.Counter(check1).items() if count > 1]
            Log.show_error('There are plugins with the same plugin name: ' + str(_mas))
            raise KeyboardInterrupt
        if len(check2) != len(set(check2)):
            _mas = [item for item, count in collections.Counter(check2).items() if count > 1]
            Log.show_error('There are plugins with the same keywords: ' + str(_mas))
            raise KeyboardInterrupt
        if len(check3) != len(set(check3)):
            _mas = [item for item, count in collections.Counter(check1).items() if count > 1]
            Log.show_error('There are plugins with the same name: ' + str(_mas))
            raise KeyboardInterrupt
        var.words = check2

    @staticmethod
    def cmd(t=None, p=None, u=None, m=None, d=None):
        md = f"{var.name} [v{var.version}]"
        var.answer = False
        var.start_now = False
        for a in var.plugins:
            res = dict()
            res['message'] = ''
            res['attachment'] = ''
            res = a.cmd(t, p, u, m, d)
            if not res is False:
                if len(str(res)) > 0:
                    p = str(a)[str(a).find('.')+1:str(a).find(' ')]
                    p = p[p.find('.')+1:]
                    Log.show_plugin(res['plugin'] + ' (' + p + ')')
                    var.answer = True
                    if not res['message'] is None or not res['attachment'] is None:
                        if res['message']:
                            res['message'] = f"{res['message']}\n{md}"
                            VK().Messages().send(message=res['message'], forward_messages=d)
                        elif res['attachment']:
                            VK().Messages().send(message=md, attachment=res['attachment'], forward_messages=d)
                    if not res['lat'] is None and not res['long'] is None:
                        var.answer = True
                        VK().Messages().send(message=md, lat=res['lat'], long=res['long'], forward_messages=d)
                    if not res['forward_messages'] is None:
                        VK().Messages().send(message=md, forward_messages=res['forward_messages'])
        if not var.answer and m != 'b' and not var.start_now:
            UEngine.what()
            Log.show_plugin('None')
