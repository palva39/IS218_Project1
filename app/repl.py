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
                    # Execute the command and check if it returns a result
                    result = self.commands[command](*args)
                    if result is not None and command not in ['history', 'clear_history', 'load_plugin', 'menu', 'quit']:
                        print(f"Result: {result}")
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
            plugin = self.plugin_loader.plugins[plugin_name]
            
            # Dynamically add plugin functions to REPL with history saving
            for func_name in dir(plugin):
                if not func_name.startswith('_'):
                    func = getattr(plugin, func_name)

                    # Create a wrapper function that handles plugin operations and saves to history
                    def wrapped_func(*args, func=func, func_name=func_name):
                        # Convert arguments to floats and execute the plugin function
                        result = func(*map(float, args))
                        # Record the plugin operation to history without printing
                        a = args[0] if len(args) > 0 else None
                        b = args[1] if len(args) > 1 else None
                        self._record_to_history(func_name, a, b, result)
                        return result  # Return the result without printing
                    
                    # Add the wrapped function to REPL commands
                    self.commands[func_name] = wrapped_func
                    
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
