"""
Unit tests for the square function in the square plugin.
"""

import pytest
from app.plugins.square import square

def test_square():
    """Test the square function for various inputs."""
    # Test positive numbers
    assert square(2) == 4.0
    assert square(3) == 9.0
    assert square(5.5) == 30.25

    # Test zero
    assert square(0) == 0.0

    # Test negative numbers
    assert square(-3) == 9.0
    assert square(-2.5) == 6.25

    # Test edge case with large number
    assert square(1e6) == 1e12

    # Test string input should raise an error
    with pytest.raises(ValueError):
        square("not a number")
