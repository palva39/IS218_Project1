"""
Unit tests for the REPL class.
"""

import pytest
from app.repl import REPL

@pytest.fixture
def repl():
    """Fixture to create a REPL instance."""
    return REPL()

def test_add_command(repl, monkeypatch):
    """Test the 'add' command functionality in the REPL."""
    # Mock user input for the REPL
    inputs = iter(["add 3 4", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    repl.start()  # This will run the REPL once with "add 3 4"
    # History should have the add command
    history = repl.history_manager.get_history()
    assert 'add' in history
    assert '3' in history
    assert '4' in history
    assert '7' in history  # 3 + 4 = 7

def test_load_plugin_command(repl, monkeypatch):
    """Test loading a plugin and running a command from it in the REPL."""
    # Mock user input to load a plugin and run a command
    inputs = iter(["load_plugin example_plugin", "square 3", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    repl.start()  # This will load the plugin and use a command from it
    # Check if the result is stored in the history
    history = repl.history_manager.get_history()
    assert 'square' in history
    assert '3' in history
    assert '9' in history  # 3 squared is 9
