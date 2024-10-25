"""
Unit tests for the HistoryManager class.
"""

import pytest
from app.history_manager import HistoryManager

@pytest.fixture
def history_manager(tmp_path):
    """Fixture to create a HistoryManager instance with a temporary file."""
    # Use a temporary path for the CSV file
    temp_file = tmp_path / "temp_calculation_history.csv"
    return HistoryManager(history_file=str(temp_file))

def test_record_and_save(history_manager):
    """Test recording and saving a calculation to the history."""
    record = {'operation': 'add', 'a': 1, 'b': 2, 'result': 3}
    history_manager.record(record)

    # Check if the history is updated
    history = history_manager.get_history()
    assert 'add' in history
    assert '1' in history
    assert '2' in history
    assert '3' in history

def test_clear_history(history_manager):
    """Test clearing the history records."""
    # Add a record first
    record = {'operation': 'subtract', 'a': 5, 'b': 3, 'result': 2}
    history_manager.record(record)

    # Clear the history and verify it's empty
    history_manager.clear_history()

    # Check if the DataFrame is truly empty
    assert history_manager.history.empty

def test_load_and_save_history(history_manager):
    """Test loading and saving history from a file."""
    # Test loading and saving functionality
    record = {'operation': 'multiply', 'a': 2, 'b': 3, 'result': 6}
    history_manager.record(record)

    # Reload the history manager to simulate loading from file
    new_history_manager = HistoryManager(history_file=history_manager.history_file)
    history = new_history_manager.get_history()
    assert 'multiply' in history
    assert '2' in history
    assert '3' in history
    assert '6' in history

def test_load_and_save_history(history_manager):
    """Test loading and saving history from a file."""
    # Test loading and saving functionality
    record = {'operation': 'divide', 'a': 12, 'b': 2, 'result': 6}
    history_manager.record(record)

    # Reload the history manager to simulate loading from file
    new_history_manager = HistoryManager(history_file=history_manager.history_file)
    history = new_history_manager.get_history()
    assert 'divide' in history
    assert '12' in history
    assert '2' in history
    assert '6' in history

def test_invalid_record(history_manager):
    """Test attempting to record an invalid calculation entry."""
    # An invalid record should not raise errors, but should not be saved
    invalid_record = {'operation': 'add', 'a': 1, 'b': None, 'result': None}
    history_manager.record(invalid_record)

    # The history should not contain the invalid record
    history = history_manager.get_history()
    assert 'None' not in history
