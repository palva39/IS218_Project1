"""
Unit tests for the square_root function in the square_root plugin.
"""

import pytest
from app.plugins.square_root import square_root

def test_square_root():
    """Test the square_root function for various inputs."""
    # Test positive numbers
    assert square_root(4) == 2.0  # sqrt(4) = 2
    assert square_root(9) == 3.0  # sqrt(9) = 3

    # Test zero
    assert square_root(0) == 0.0  # sqrt(0) = 0

    # Test large number
    assert square_root(1e6) == 1000.0  # sqrt(1e6) = 1000

    # Test negative number should raise an error
    with pytest.raises(ValueError):
        square_root(-4)

    # Test string input should raise an error
    with pytest.raises(ValueError):
        square_root("not a number")
