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