"""
Comprehensive unit tests for the REPL class, covering all commands, plugins, and edge cases.
"""

import pytest
from app.repl import REPL

@pytest.fixture
def repl():
    """Fixture to create a REPL instance."""
    return REPL()

def test_add_command(repl, monkeypatch):
    """Test the 'add' command functionality in the REPL."""
    inputs = iter(["add 10 5", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    history = repl.history_manager.get_history()
    assert 'add' in history
    assert '10' in history
    assert '5' in history
    assert '15' in history  # 10 + 5 = 15

def test_subtract_command(repl, monkeypatch):
    """Test the 'subtract' command functionality in the REPL."""
    inputs = iter(["subtract 10 5", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    history = repl.history_manager.get_history()
    assert 'subtract' in history
    assert '10' in history
    assert '5' in history
    assert '5' in history  # 10 - 5 = 5

def test_multiply_command(repl, monkeypatch):
    """Test the 'multiply' command functionality in the REPL."""
    inputs = iter(["multiply 10 5", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    history = repl.history_manager.get_history()
    assert 'multiply' in history
    assert '10' in history
    assert '5' in history
    assert '50' in history  # 10 * 5 = 50

def test_divide_command(repl, monkeypatch):
    """Test the 'divide' command functionality in the REPL."""
    inputs = iter(["divide 10 2", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    history = repl.history_manager.get_history()
    assert 'divide' in history
    assert '10' in history
    assert '2' in history
    assert '5' in history  # 10 / 2 = 5

def test_divide_by_zero_command(repl, monkeypatch, capsys):
    """Test the 'divide' command with division by zero in the REPL."""
    inputs = iter(["divide 10 0", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    captured = capsys.readouterr()
    assert "Error" in captured.out
    assert "Cannot divide by zero" in captured.out

def test_load_plugin_and_execute(repl, monkeypatch):
    """Test loading various plugins and executing commands."""
    plugin_file = "app/plugins/square_root_plugin.py"
    with open(plugin_file, "w", encoding="utf-8") as f:
        f.write("""
import math

def square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(float(number))
""")

    # Load the square_root plugin and run the square_root command
    inputs = iter(["load_plugin square_root_plugin", "square_root 16", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    # Verify that the square root operation is recorded
    history = repl.history_manager.get_history()
    assert 'square_root' in history
    assert '16' in history
    assert '4.0' in history  # sqrt(16) = 4.0

def test_clear_history_command(repl, monkeypatch):
    """Test the 'clear_history' command functionality in the REPL."""
    inputs = iter(["add 5 5", "clear_history", "history", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    # Verify that the history is cleared
    history = repl.history_manager.get_history()
    assert "Empty DataFrame" in history

def test_invalid_command(repl, monkeypatch, capsys):
    """Test entering an invalid command in the REPL."""
    inputs = iter(["unknown_command", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    captured = capsys.readouterr()
    assert "Unknown command" in captured.out

def test_menu_command(repl, monkeypatch, capsys):
    """Test the 'menu' command to show available commands in the REPL."""
    inputs = iter(["menu", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    captured = capsys.readouterr()
    assert "Available Commands" in captured.out
    assert "add" in captured.out
    assert "subtract" in captured.out
    assert "multiply" in captured.out
    assert "divide" in captured.out
    assert "square_root" in captured.out
    assert "factorial" in captured.out
    assert "power" in captured.out
    assert "sine" in captured.out
    assert "cosine" in captured.out
    assert "tangent" in captured.out

def test_quit_command(repl, monkeypatch):
    """Test the 'quit' command to exit the REPL."""
    inputs = iter(["quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        repl.start()
