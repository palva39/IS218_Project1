"""
Calculator module providing basic arithmetic operations.
"""

class Calculator:
    """
    A simple calculator that performs basic arithmetic operations.
    """

    def add(self, a, b):
        """
        Adds two numbers.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts the second number from the first number.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiplies two numbers.
        """
        return a * b

    def divide(self, a, b):
        """
        Divides the first number by the second number.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
