class Command:
    """Base class for all commands."""
    def execute(self, *args):
        raise NotImplementedError("Command must implement an execute method.")

class AddCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, a, b):
        return self.calculator.add(float(a), float(b))

class SubtractCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, a, b):
        return self.calculator.subtract(float(a), float(b))

class MultiplyCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, a, b):
        return self.calculator.multiply(float(a), float(b))

class DivideCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, a, b):
        return self.calculator.divide(float(a), float(b))
