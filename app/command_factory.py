from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class CommandFactory:
    """Factory to create command objects based on command name."""

    @staticmethod
    def create(command_name, calculator):
        if command_name == 'add':
            return AddCommand(calculator)
        elif command_name == 'subtract':
            return SubtractCommand(calculator)
        elif command_name == 'multiply':
            return MultiplyCommand(calculator)
        elif command_name == 'divide':
            return DivideCommand(calculator)
        else:
            raise ValueError(f"Unknown command: {command_name}")
