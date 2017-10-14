import os
import importlib
import sys

class Plugin(object):
    """docstring for Plugin"""
    def __init__(self, rawSend):
        self.rawSend = rawSend
        self.allowed_plugins_dict = {}
        self.allowed_plugins_mtime = {}
        self.loaded_plugins = {}
        self.loaded_modules = {}
        self.plugin_path = '/full/path/to/plugins/'
        self.package_name = self.plugin_path.split('/')[-2]
        self.listAvailablePlugins()
        self.loadPlugins(self.allowed_plugins_dict)
        sys.path.insert(0,self.plugin_path)

    def listAvailablePlugins(self):
        for path, subdirs, files in os.walk(self.plugin_path):
            for name in files:
                current_path = os.path.join(path, name)
                if current_path.startswith(tuple(self.plugin_path)) and current_path.endswith('.py'):
                    name = name[:-3]
                    self.allowed_plugins_dict[name] = name
                    self.allowed_plugins_mtime[name] = os.path.getmtime(current_path)
        return self.allowed_plugins_dict


    def reloadIfNeeded(self, plugin_name):
        full_path = os.path.join(self.plugin_path, plugin_name).replace('.', '/')+'.py'
        if os.path.getmtime(full_path) > self.allowed_plugins_mtime[plugin_name]:
            self.loadPlugins({plugin_name})
            self.allowed_plugins_mtime[plugin_name] = os.path.getmtime(full_path)

    def loadPlugins(self, lst_plugins):

        for current_plugin in lst_plugins:
            if current_plugin in self.allowed_plugins_dict.keys():
                if current_plugin in self.loaded_plugins.keys():
                    self.loaded_modules[current_plugin] = importlib.reload(self.loaded_modules[current_plugin])
                else:
                    self.loaded_modules[current_plugin] = importlib.import_module(self.package_name+'.'+self.allowed_plugins_dict[current_plugin])
                self.loaded_plugins[current_plugin] = getattr(self.loaded_modules[current_plugin], current_plugin)(self.rawSend)

        return self.loaded_plugins

    def execute(self, datas):
        plugin_name = datas['content'][1:].split(' ')[0]
        if (plugin_name in self.allowed_plugins_dict.keys()):
            self.reloadIfNeeded(plugin_name)
            try:
                self.loaded_plugins[plugin_name].execute(datas)
            except Exception as e:
                self.rawSend('PRIVMSG', 'Un poulpe est arrivé et m\'a cassé.',  datas['to'])
                print(e)
