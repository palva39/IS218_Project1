# app/repl.py
import logging
from app.calculator import Calculator
from app.history_manager import HistoryManager
from app.plugin_loader import PluginLoader

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.history_manager = HistoryManager()
        self.plugin_loader = PluginLoader()
        self.commands = {
            'add': self._add,
            'subtract': self._subtract,
            'multiply': self._multiply,
            'divide': self._divide,
            'history': self._show_history,
            'clear_history': self._clear_history,
            'load_plugin': self._load_plugin,
            'menu': self._menu,
            'quit': self._quit
        }
        logging.basicConfig(level=logging.INFO)

    def start(self):
        print("Advanced Python Calculator - Type 'menu' to see available commands.")
        while True:
            user_input = input(">> ").strip().split()
            if not user_input:
                continue
            command = user_input[0].lower()
            args = user_input[1:]

            if command in self.commands:
                try:
                    self.commands[command](*args)
                except Exception as e:
                    logging.error(f"Error executing command '{command}': {e}")
                    print(f"Error: {e}")
            else:
                print(f"Unknown command: {command}")

    def _add(self, a, b):
        result = self.calculator.add(float(a), float(b))
        self._record_and_print("add", a, b, result)

    def _subtract(self, a, b):
        result = self.calculator.subtract(float(a), float(b))
        self._record_and_print("subtract", a, b, result)

    def _multiply(self, a, b):
        result = self.calculator.multiply(float(a), float(b))
        self._record_and_print("multiply", a, b, result)

    def _divide(self, a, b):
        result = self.calculator.divide(float(a), float(b))
        self._record_and_print("divide", a, b, result)

    def _record_and_print(self, operation, a, b, result):
        record = {'operation': operation, 'a': a, 'b': b, 'result': result}
        self.history_manager.record(record)
        print(f"Result: {result}")

    def _show_history(self):
        print("Calculation History:")
        print(self.history_manager.get_history())

    def _clear_history(self):
        self.history_manager.clear_history()
        print("History cleared.")

    def _load_plugin(self, plugin_name):
        try:
            self.plugin_loader.load_plugin(plugin_name)
            # Add plugin commands dynamically to REPL
            plugin = self.plugin_loader.plugins[plugin_name]
            for func_name in dir(plugin):
                if not func_name.startswith('_'):
                    # Bind the plugin function to a new REPL command
                    self.commands[func_name] = getattr(plugin, func_name)
            print(f"Plugin '{plugin_name}' loaded successfully.")
        except ImportError as e:
            print(f"Error loading plugin: {e}")

    def _menu(self):
        print("Available commands:")
        for command in self.commands.keys():
            print(f"- {command}")

    def _quit(self):
        print("Goodbye!")
        exit()
