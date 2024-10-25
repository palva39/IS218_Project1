import logging
from app.calculator import Calculator
from app.history_manager import HistoryManager
from app.plugin_loader import PluginLoader
from app.command_factory import CommandFactory
from app.logging_config import setup_logging  # Ensure logging is set up

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.history_manager = HistoryManager()
        self.plugin_loader = PluginLoader()
        setup_logging()  # Setup logging based on configuration

        # Command mappings
        self.commands = {
            'history': self._show_history,
            'clear_history': self._clear_history,
            'load_plugin': self._load_plugin,
            'menu': self._menu,
            'quit': self._quit
        }

    def start(self):
        logging.info("Starting the REPL application.")
        print("Advanced Python Calculator - Type 'menu' to see available commands.")
        while True:
            user_input = input(">> ").strip().split()
            if not user_input:
                continue
            command_name = user_input[0].lower()
            args = user_input[1:]

            # Check if it's a calculator command, if not handle other commands
            if command_name in ['add', 'subtract', 'multiply', 'divide']:
                try:
                    command = CommandFactory.create(command_name, self.calculator)
                    logging.info(f"Executing command: {command_name} with arguments {args}")
                    result = command.execute(*args)
                    if result is not None:
                        self._record_and_print(command_name, args[0], args[1], result)
                except Exception as e:
                    logging.error(f"Error executing command '{command_name}': {e}")
                    print(f"Error: {e}")
            elif command_name in self.commands:
                try:
                    logging.info(f"Executing command: {command_name} with arguments {args}")
                    self.commands[command_name](*args)
                except Exception as e:
                    logging.error(f"Error executing command '{command_name}': {e}")
                    print(f"Error: {e}")
            else:
                logging.warning(f"Unknown command entered: {command_name}")
                print(f"Unknown command: {command_name}")

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

                    # Create a wrapper function that handles plugin operations and saves to history
                    def wrapped_func(*args, func=func, func_name=func_name):
                        try:
                            # Convert arguments to floats and execute the plugin function
                            result = func(*map(float, args))
                            
                            # Record the plugin operation to history
                            a = args[0] if len(args) > 0 else None
                            b = args[1] if len(args) > 1 else None
                            
                            # Ensure proper recording to history
                            self._record_and_print(func_name, a, b, result)
                            
                            return result
                        except Exception as e:
                            logging.error(f"Error executing plugin command '{func_name}': {e}")
                            raise
                    
                    # Use a lambda to capture the current func_name and func correctly
                    self.commands[func_name] = (lambda f=func, fn=func_name: 
                                                lambda *args: wrapped_func(*args, func=f, func_name=fn))()
                    
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
