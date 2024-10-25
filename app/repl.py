import logging
from app.calculator import Calculator
from app.history_manager import HistoryManager
from app.plugin_loader import PluginLoader
from app.logging_config import setup_logging  # Ensure logging is set up
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.history_manager = HistoryManager()
        self.plugin_loader = PluginLoader()
        self.commands = {
              'add': AddCommand(self.calculator),
            'subtract': SubtractCommand(self.calculator),
            'multiply': MultiplyCommand(self.calculator),
            'divide': DivideCommand(self.calculator),
            'history': self._show_history,
            'clear_history': self._clear_history,
            'load_plugin': self._load_plugin,
            'menu': self._menu,
            'quit': self._quit
        }
        setup_logging()  # Setup logging based on configuration

    def start(self):
        logging.info("Starting the REPL application.")
        print("Advanced Python Calculator - Type 'menu' to see available commands.")
        while True:
            user_input = input(">> ").strip().split()
            if not user_input:
                continue
            command = user_input[0].lower()
            args = user_input[1:]

            if command in self.commands:
                try:
                    logging.info(f"Executing command: {command} with arguments {args}")
                    result = self.commands[command](*args)
                    if result is not None and command not in ['history', 'clear_history', 'load_plugin', 'menu', 'quit']:
                        print(f"Result: {result}")
                except Exception as e:
                    logging.error(f"Error executing command '{command}': {e}")
                    print(f"Error: {e}")
            else:
                logging.warning(f"Unknown command entered: {command}")
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
        try:
            result = self.calculator.divide(float(a), float(b))
            self._record_and_print("divide", a, b, result)
        except ValueError as e:
            logging.error(f"Division by zero attempted with: {a} / {b}")
            raise

    def _record_and_print(self, operation, a, b, result):
        logging.info(f"Recording operation: {operation} with operands {a}, {b} and result {result}")
        record = {'operation': operation, 'a': a, 'b': b, 'result': result}
        self.history_manager.record(record)
        print(f"Result: {result}")

    def _show_history(self):
        logging.info("Displaying calculation history.")
        print("Calculation History:")
        print(self.history_manager.get_history())

    def _clear_history(self):
        logging.info("Clearing calculation history.")
        self.history_manager.clear_history()
        print("History cleared.")

    def _load_plugin(self, plugin_name):
        try:
            logging.info(f"Loading plugin: {plugin_name}")
            self.plugin_loader.load_plugin(plugin_name)
            plugin = self.plugin_loader.plugins[plugin_name]
            
            for func_name in dir(plugin):
                if not func_name.startswith('_'):
                    func = getattr(plugin, func_name)

                    # Use the correct method to handle recording and printing
                    def wrapped_func(*args, func=func, func_name=func_name):
                        result = func(*map(float, args))
                        a = args[0] if len(args) > 0 else None
                        b = args[1] if len(args) > 1 else None
                        self._record_and_print(func_name, a, b, result)
                        return result
                    
                    self.commands[func_name] = wrapped_func
                    
            print(f"Plugin '{plugin_name}' loaded successfully.")
        except ImportError as e:
            logging.error(f"Failed to load plugin '{plugin_name}': {e}")
            print(f"Error loading plugin: {e}")

    def _menu(self):
        logging.info("Displaying available commands.")
        print("Available commands:")
        for command in self.commands.keys():
            print(f"- {command}")

    def _quit(self):
        logging.info("Exiting the REPL application.")
        print("Goodbye!")
        exit()
