import math

def square_root(number):
    """Calculate the square root of a given number."""
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(float(number))
