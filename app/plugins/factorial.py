import math

def factorial(number):
    """Calculate the factorial of a given number."""
    number = int(number)
    if number < 0:
        raise ValueError("Cannot calculate the factorial of a negative number.")
    return math.factorial(number)
