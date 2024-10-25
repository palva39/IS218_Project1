"""
Unit tests for the CommandFactory class in command_factory.py.
"""

import pytest
from app.calculator import Calculator
from app.command_factory import CommandFactory
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance."""
    return Calculator()

def test_create_add_command(calculator):
    """Test creating an AddCommand using the CommandFactory."""
    command = CommandFactory.create('add', calculator)
    assert isinstance(command, AddCommand)
    result = command.execute(10, 5)
    assert result == 15.0  # 10 + 5 = 15

def test_create_subtract_command(calculator):
    """Test creating a SubtractCommand using the CommandFactory."""
    command = CommandFactory.create('subtract', calculator)
    assert isinstance(command, SubtractCommand)
    result = command.execute(10, 5)
    assert result == 5.0  # 10 - 5 = 5

def test_create_multiply_command(calculator):
    """Test creating a MultiplyCommand using the CommandFactory."""
    command = CommandFactory.create('multiply', calculator)
    assert isinstance(command, MultiplyCommand)
    result = command.execute(10, 5)
    assert result == 50.0  # 10 * 5 = 50

def test_create_divide_command(calculator):
    """Test creating a DivideCommand using the CommandFactory."""
    command = CommandFactory.create('divide', calculator)
    assert isinstance(command, DivideCommand)
    result = command.execute(10, 2)
    assert result == 5.0  # 10 / 2 = 5

def test_create_invalid_command(calculator):
    """Test creating an invalid command using the CommandFactory."""
    with pytest.raises(ValueError, match="Unknown command: invalid"):
        CommandFactory.create('invalid', calculator)
