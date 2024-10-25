"""
Unit tests for the REPL class, covering all basic commands.
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

def test_load_plugin_command(repl, monkeypatch):
    """Test loading a plugin and running a command from it in the REPL."""

    # Clear any previous history before starting the test
    repl.history_manager.clear_history()

    plugin_file = "app/plugins/square.py"
    with open(plugin_file, "w", encoding="utf-8") as f:
        f.write("""
def square(number):
    return float(number) ** 2
""")

    # Mock user input to load the plugin and run a command from it
    inputs = iter(["load_plugin square", "square 3", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    # Verify the plugin operation is recorded
    history = repl.history_manager.get_history()
    assert 'square' in history
    assert '3' in history
    assert '9' in history  # 3 squared is 9

def test_invalid_calculator_command(repl, monkeypatch, capsys):
    """Test handling an invalid calculator command in the REPL."""
    inputs = iter(["add invalid args", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    captured = capsys.readouterr()
    assert "Error" in captured.out
    assert "could not convert string to float" in captured.out

def test_unknown_plugin_function(repl, monkeypatch):
    """Test running an unknown function from a loaded plugin."""
    plugin_file = "app/plugins/unknown_plugin.py"
    with open(plugin_file, "w", encoding="utf-8") as f:
        f.write("""
def unknown_function(number):
    return number * 2
""")

    inputs = iter(["load_plugin unknown_plugin", "unknown_function 3", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    # Ensure unknown function handling doesn't break the REPL
    history = repl.history_manager.get_history()
    assert 'unknown_function' in history
    assert '3' in history
    assert '6' in history  # 3 * 2 = 6
