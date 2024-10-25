import logging
from app.calculator import Calculator
from app.history_manager import HistoryManager
from app.plugin_loader import PluginLoader
from app.command_factory import CommandFactory
from app.logging_config import setup_logging  # Ensure logging is set up
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.history_manager = HistoryManager()
        self.plugin_loader = PluginLoader()
        setup_logging()  # Setup logging based on configuration

        # Command mappings
        self.commands = {
            'add': AddCommand(self.calculator).execute,
            'subtract': SubtractCommand(self.calculator).execute,
            'multiply': MultiplyCommand(self.calculator).execute,
            'divide': DivideCommand(self.calculator).execute,
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
        print(f"Debug: Recording operation: {operation} with operands {a}, {b} and result {result}")
        
        record = {'operation': operation, 'a': a, 'b': b, 'result': result}
        self.history_manager.record(record)
        print(f"Debug: Recorded to history: {self.history_manager.get_history()}")
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
            self.plugin_loader.load_plugin(plugin_name)
            plugin = self.plugin_loader.plugins[plugin_name]
            
            # Dynamically add plugin functions to REPL with history saving
            for func_name in dir(plugin):
                if not func_name.startswith('_'):
                    func = getattr(plugin, func_name)

                    # Use default arguments to capture current func and func_name
                    def wrapped_func(*args, func=func, func_name=func_name):
                        # Convert arguments to floats and execute the plugin function
                        logging.debug(f"Executing plugin function '{func_name}' with arguments {args}")
                        result = func(*map(float, args))
                        
                        # Ensure consistent recording data structure
                        a = args[0] if len(args) > 0 else None
                        b = args[1] if len(args) > 1 else ''  # Use empty string for plugins with a single argument
                        
                        # Debug print to ensure correct data handling
                        logging.debug(f"Recording plugin operation '{func_name}' with result {result} and operands {a}, {b}")
                        
                        # Record to history
                        self._record_and_print(func_name, a, b, result)
                        
                        return result  # Return the result instead of printing it
                    
                    # Add the wrapped function to REPL commands
                    self.commands[func_name] = wrapped_func

            print(f"Plugin '{plugin_name}' loaded successfully.")
        except ImportError as e:
            logging.error(f"Failed to load plugin '{plugin_name}': {e}")
            print(f"Error loading plugin: {e}")


    def _menu(self):
        logging.info("Displaying available commands.")
    
        print("\n=== Available Commands ===")
        
        # Basic calculation commands with usage examples
        print("\n-- Basic Calculation Commands --")
        print("add <number1> <number2>        : Add two numbers.")
        print("  Example: add 10 5            -> Result: 15.0")
        
        print("subtract <number1> <number2>   : Subtract second number from the first.")
        print("  Example: subtract 10 5       -> Result: 5.0")
        
        print("multiply <number1> <number2>   : Multiply two numbers.")
        print("  Example: multiply 10 5       -> Result: 50.0")
        
        print("divide <number1> <number2>     : Divide first number by the second.")
        print("  Example: divide 10 2         -> Result: 5.0")
        
        # Plugins with usage examples
        print("\n-- Plugin Commands --")
        print("power <base> <exponent>        : Raise a base number to the power of the exponent.")
        print("  Example: power 2 3           -> Result: 8.0 (2^3)")
        
        print("factorial <number>             : Calculate the factorial of a number.")
        print("  Example: factorial 5         -> Result: 120")
        
        print("square_root <number>           : Calculate the square root of a number.")
        print("  Example: square_root 16      -> Result: 4.0")
        
        print("sine <angle>                   : Calculate the sine of an angle (in degrees).")
        print("  Example: sine 30             -> Result: 0.5")
        
        print("cosine <angle>                 : Calculate the cosine of an angle (in degrees).")
        print("  Example: cosine 60           -> Result: 0.5")
        
        print("tangent <angle>                : Calculate the tangent of an angle (in degrees).")
        print("  Example: tangent 45          -> Result: 1.0")
        
        # Other available commands
        print("\n-- General Commands --")
        print("history                        : Display calculation history.")
        print("clear_history                  : Clear the calculation history.")
        print("load_plugin <plugin_name>      : Load a plugin by its name.")
        print("  Example: load_plugin square_root")
        print("menu                           : Show this menu.")
        print("quit                           : Exit the REPL.")
        print("\n===========================\n")

    def _quit(self):
        logging.info("Exiting the REPL application.")
        print("Goodbye!")
        exit()
