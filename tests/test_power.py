"""
Unit tests for the power function in the power plugin.
"""

import pytest
from app.plugins.power import power

def test_power():
    """Test the power function for various inputs."""
    # Test positive base and exponent
    assert power(2, 3) == 8.0  # 2^3
    assert power(5, 2) == 25.0  # 5^2

    # Test zero base
    assert power(0, 3) == 0.0  # 0^3

    # Test zero exponent
    assert power(5, 0) == 1.0  # 5^0

    # Test negative base and positive exponent
    assert power(-2, 3) == -8.0  # (-2)^3

    # Test negative exponent
    assert power(2, -2) == 0.25  # 2^-2

    # Test edge case with large numbers
    assert power(10, 6) == 1e6  # 10^6

    # Test string input should raise an error
    with pytest.raises(ValueError):
        power("base", "exponent")
