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
    
    # Run the REPL and handle SystemExit gracefully
    try:
        repl.start()  # This will run the REPL once with "add 3 4"
    except SystemExit:
        pass

    # History should have the add command
    history = repl.history_manager.get_history()
    assert 'add' in history
    assert '3' in history
    assert '4' in history
    assert '7' in history  # 3 + 4 = 7

def test_load_plugin_command(repl, monkeypatch):
    """Test loading a plugin and running a command from it in the REPL."""
    # Ensure the 'example_plugin.py' file exists in 'app/plugins'
    plugin_file = "app/plugins/example_plugin.py"
    with open(plugin_file, "w") as f:
        f.write("""
def square(number):
    return float(number) ** 2
""")

    # Mock user input to load a plugin and run a command
    inputs = iter(["load_plugin example_plugin", "square 3", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the REPL and handle SystemExit gracefully
    try:
        repl.start()  # This will load the plugin and use a command from it
    except SystemExit:
        pass

    # Check if the result is stored in the history
    history = repl.history_manager.get_history()
    assert 'square' in history
    assert '3' in history
    assert '9' in history  # 3 squared is 9
