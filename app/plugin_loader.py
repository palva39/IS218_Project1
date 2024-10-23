import importlib
import os

class PluginLoader:
    def __init__(self, plugin_dir='app/plugins'):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_plugin(self, plugin_name):
        try:
            plugin_module = importlib.import_module(f'app.plugins.{plugin_name}')
            self.plugins[plugin_name] = plugin_module
        except ImportError:
            raise ImportError(f"Plugin '{plugin_name}' not found.")

    def get_plugins(self):
        return list(self.plugins.keys())
