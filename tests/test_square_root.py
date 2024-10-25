"""
Unit tests for the square_root function in the square_root plugin.
"""

import pytest
from app.plugins.square_root import square_root

def test_square_root_positive_numbers():
    """Test the square_root function with positive numbers."""
    # Test positive numbers
    assert square_root(4) == 2.0  # sqrt(4) = 2
    assert square_root(9) == 3.0  # sqrt(9) = 3
    assert square_root(2.25) == 1.5  # sqrt(2.25) = 1.5
    assert square_root(16) == 4.0  # sqrt(16) = 4

def test_square_root_large_numbers():
    """Test the square_root function with large numbers."""
    assert square_root(1e6) == 1000.0  # sqrt(1e6) = 1000
    assert square_root(1e12) == 1e6  # sqrt(1e12) = 1e6

def test_square_root_zero():
    """Test the square_root function with zero."""
    assert square_root(0) == 0.0  # sqrt(0) = 0

def test_square_root_negative_numbers():
    """Test the square_root function with negative numbers."""
    # Test negative number should raise an error
    with pytest.raises(ValueError, match="Cannot calculate the square root of a negative number."):
        square_root(-4)

def test_square_root_string_input():
    """Test the square_root function with a string input."""
    # Test string input should raise an error
    with pytest.raises(ValueError, match="Input must be a numeric value."):
        square_root("not a number")

def test_square_root_non_numeric_input():
    """Test the square_root function with non-numeric input."""
    # Test non-numeric inputs like list or dict should raise an error
    with pytest.raises(ValueError, match="Input must be a numeric value."):
        square_root([1, 2, 3])

    with pytest.raises(ValueError, match="Input must be a numeric value."):
        square_root({"number": 4})
