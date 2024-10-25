import math

def factorial(number):
    """Calculate the factorial of a given number."""
    try:
        # Convert input to integer if it's a valid number
        number = int(number)
    except (ValueError, TypeError):
        raise ValueError("Input must be a non-negative integer.")

    if number < 0:
        raise ValueError("Cannot calculate the factorial of a negative number.")

    return math.factorial(number)
