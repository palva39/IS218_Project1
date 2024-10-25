"""
Unit tests for the PandasFacade class.
"""

import pandas as pd
import pytest
from app.pandas_facade import PandasFacade

def test_load_csv_failure(monkeypatch):
    """Test loading a CSV file with an error."""
    def mock_read_csv(file_path):
        raise FileNotFoundError("Simulated file read error.")

    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

    # Attempt to load a non-existing CSV file
    df = PandasFacade.load_csv('non_existing_file.csv')
    assert df.empty  # Should return an empty DataFrame on error

def test_save_csv_failure(monkeypatch, capsys):
    """Test saving a CSV file with an error and verify error handling."""
    def mock_to_csv(self, file_path, index):
        raise IOError("Simulated file write error.")

    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)

    # Attempt to save a DataFrame that raises an IOError
    dataframe = pd.DataFrame({'a': [1], 'b': [2]})
    PandasFacade.save_csv(dataframe, 'test.csv')

    # Capture the standard output to verify error handling
    captured = capsys.readouterr()
    assert "Error saving CSV file: Simulated file write error." in captured.out

def test_concat_dataframes_with_empty_dataframe():
    """Test concatenating DataFrames when one is empty."""
    df1 = pd.DataFrame(columns=['a', 'b'])
    df2 = pd.DataFrame({'a': [1], 'b': [2]})

    # Should handle empty DataFrame properly
    result = PandasFacade.concat_dataframes(df1, {'a': 1, 'b': 2})
    assert not result.empty
    assert len(result) == 1
