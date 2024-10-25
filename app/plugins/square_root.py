
import math

def square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(float(number))
