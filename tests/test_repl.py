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
    inputs = iter(["add 3 4", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    history = repl.history_manager.get_history()
    assert 'add' in history
    assert '3' in history
    assert '4' in history
    assert '7' in history

def test_invalid_command(repl, monkeypatch):
    """Test handling an invalid command in the REPL."""
    inputs = iter(["invalid_command", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

def test_menu_command(repl, monkeypatch, capsys):
    """Test the 'menu' command functionality in the REPL."""
    inputs = iter(["menu", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "add" in captured.out
    assert "subtract" in captured.out

def test_clear_history_command(repl, monkeypatch):
    """Test the 'clear_history' command functionality in the REPL."""
    inputs = iter(["add 3 4", "clear_history", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    # History should be cleared
    history = repl.history_manager.get_history()
    assert history.strip() == "Empty DataFrame\nColumns: [operation, a, b, result]\nIndex: []"

def test_load_non_existing_plugin(repl, monkeypatch, capsys):
    """Test attempting to load a non-existing plugin in the REPL."""
    inputs = iter(["load_plugin non_existing_plugin", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    captured = capsys.readouterr()
    assert "Error loading plugin" in captured.out

def test_load_plugin_command(repl, monkeypatch):
    """Test loading a plugin and running a command from it in the REPL."""
    plugin_file = "app/plugins/example_plugin.py"
    with open(plugin_file, "w") as f:
        f.write("""
def square(number):
    return float(number) ** 2
""")

    inputs = iter(["load_plugin example_plugin", "square 3", "quit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    try:
        repl.start()
    except SystemExit:
        pass

    history = repl.history_manager.get_history()
    assert 'square' in history
    assert '3' in history
    assert '9' in history
