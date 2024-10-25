"""
Unit tests for trigonometric functions in the trigonometry plugin.
"""

import pytest
import math
from app.plugins.trig import sine, cosine, tangent

def test_sine():
    """Test the sine function for various angles."""
    assert math.isclose(sine(0), 0.0, rel_tol=1e-9)  # sin(0) = 0
    assert math.isclose(sine(30), 0.5, rel_tol=1e-9)  # sin(30) = 0.5
    assert math.isclose(sine(90), 1.0, rel_tol=1e-9)  # sin(90) = 1

    # Test negative angles
    assert math.isclose(sine(-30), -0.5, rel_tol=1e-9)  # sin(-30) = -0.5

    # Test non-numeric input should raise an error
    with pytest.raises(ValueError):
        sine("not a number")

def test_cosine():
    """Test the cosine function for various angles."""
    assert math.isclose(cosine(0), 1.0, rel_tol=1e-9)  # cos(0) = 1
    assert math.isclose(cosine(60), 0.5, rel_tol=1e-9)  # cos(60) = 0.5
    assert math.isclose(cosine(90), 0.0, rel_tol=1e-9)  # cos(90) = 0

    # Test negative angles
    assert math.isclose(cosine(-60), 0.5, rel_tol=1e-9)  # cos(-60) = 0.5

    # Test non-numeric input should raise an error
    with pytest.raises(ValueError):
        cosine("not a number")

def test_tangent():
    """Test the tangent function for various angles."""
    assert math.isclose(tangent(0), 0.0, rel_tol=1e-9)  # tan(0) = 0
    assert math.isclose(tangent(45), 1.0, rel_tol=1e-9)  # tan(45) = 1

    # Test angle approaching undefined value (90 degrees)
    with pytest.raises(ValueError):
        tangent(90)  # tan(90) is undefined (infinity)

    # Test non-numeric input should raise an error
    with pytest.raises(ValueError):
        tangent("not a number")
