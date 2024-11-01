import math

def square_root(number):
    """Calculate the square root of a given number."""
    try:
        # Ensure the input can be converted to a float
        number = float(number)
    except (ValueError, TypeError):
        raise ValueError("Input must be a numeric value.")
    
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    
    return math.sqrt(number)
