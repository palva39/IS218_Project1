"""
Unit tests for the command classes in commands.py.
"""

import pytest
from app.calculator import Calculator
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance."""
    return Calculator()

def test_add_command(calculator):
    """Test the AddCommand functionality."""
    add_command = AddCommand(calculator)
    result = add_command.execute(10, 5)
    assert result == 15.0  # 10 + 5 = 15

def test_subtract_command(calculator):
    """Test the SubtractCommand functionality."""
    subtract_command = SubtractCommand(calculator)
    result = subtract_command.execute(10, 5)
    assert result == 5.0  # 10 - 5 = 5

def test_multiply_command(calculator):
    """Test the MultiplyCommand functionality."""
    multiply_command = MultiplyCommand(calculator)
    result = multiply_command.execute(10, 5)
    assert result == 50.0  # 10 * 5 = 50

def test_divide_command(calculator):
    """Test the DivideCommand functionality."""
    divide_command = DivideCommand(calculator)
    result = divide_command.execute(10, 2)
    assert result == 5.0  # 10 / 2 = 5

def test_divide_by_zero(calculator):
    """Test the DivideCommand functionality for division by zero."""
    divide_command = DivideCommand(calculator)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_command.execute(10, 0)

def test_add_command_with_invalid_args(calculator):
    """Test AddCommand with invalid arguments."""
    add_command = AddCommand(calculator)
    with pytest.raises(ValueError):
        add_command.execute('invalid', 'args')

def test_subtract_command_with_invalid_args(calculator):
    """Test SubtractCommand with invalid arguments."""
    subtract_command = SubtractCommand(calculator)
    with pytest.raises(ValueError):
        subtract_command.execute('invalid', 'args')

def test_multiply_command_with_invalid_args(calculator):
    """Test MultiplyCommand with invalid arguments."""
    multiply_command = MultiplyCommand(calculator)
    with pytest.raises(ValueError):
        multiply_command.execute('invalid', 'args')

def test_divide_command_with_invalid_args(calculator):
    """Test DivideCommand with invalid arguments."""
    divide_command = DivideCommand(calculator)
    with pytest.raises(ValueError):
        divide_command.execute('invalid', 'args')
