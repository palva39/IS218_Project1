import math

def factorial(number):
    """Calculate the factorial of a given number."""
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("Input must be a non-negative integer.")
    if number < 0:
        raise ValueError("Cannot calculate the factorial of a negative number.")
    return math.factorial(number)
