"""
Unit tests for the factorial function in the factorial plugin.
"""

import pytest
from app.plugins.factorial import factorial

def test_factorial():
    """Test the factorial function for various inputs."""
    # Test small positive numbers
    assert factorial(0) == 1  # 0! = 1
    assert factorial(1) == 1  # 1! = 1
    assert factorial(5) == 120  # 5! = 120

    # Test larger numbers
    assert factorial(10) == 3628800  # 10! = 3628800

    # Test string input that is a valid integer
    assert factorial("5") == 120  # "5" should be converted to 5

    # Test negative number should raise an error
    with pytest.raises(ValueError, match="Cannot calculate the factorial of a negative number."):
        factorial(-1)

    # Test non-integer input should raise an error
    with pytest.raises(ValueError, match="Input must be a non-negative integer."):
        factorial(3.5)

    # Test string input that is not a valid integer should raise an error
    with pytest.raises(ValueError, match="Input must be a non-negative integer."):
        factorial("not a number")
