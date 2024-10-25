# tests/test_calculator.py

import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(3, 2) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(3.5, 2.5) == 6.0

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(-1, -1) == 0
    assert calculator.subtract(3.5, 1.5) == 2.0

def test_multiply(calculator):
    assert calculator.multiply(3, 2) == 6
    assert calculator.multiply(-1, 2) == -2
    assert calculator.multiply(1.5, 2) == 3.0

def test_divide(calculator):
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-6, 3) == -2
    assert calculator.divide(1.5, 0.5) == 3.0
    
    # Check division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)
