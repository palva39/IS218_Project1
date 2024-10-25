"""
Unit tests for the Calculator class.
"""

import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance."""
    return Calculator()

def test_add(calculator):
    """Test the addition functionality of the Calculator."""
    assert calculator.add(3, 2) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(3.5, 2.5) == 6.0

def test_subtract(calculator):
    """Test the subtraction functionality of the Calculator."""
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(-1, -1) == 0
    assert calculator.subtract(3.5, 1.5) == 2.0

def test_multiply(calculator):
    """Test the multiplication functionality of the Calculator."""
    assert calculator.multiply(3, 2) == 6
    assert calculator.multiply(-1, 2) == -2
    assert calculator.multiply(1.5, 2) == 3.0

def test_divide(calculator):
    """Test the division functionality of the Calculator."""
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-6, 3) == -2
    assert calculator.divide(1.5, 0.5) == 3.0

    # Check division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)
