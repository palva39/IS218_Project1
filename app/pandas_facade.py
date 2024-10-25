import pandas as pd

class PandasFacade:
    """A Facade for simplified Pandas data manipulation."""

    @staticmethod
    def load_csv(file_path):
        """Load data from a CSV file."""
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return pd.DataFrame()

    @staticmethod
    def save_csv(dataframe, file_path):
        """Save a DataFrame to a CSV file."""
        try:
            dataframe.to_csv(file_path, index=False)
        except Exception as e:
            print(f"Error saving CSV file: {e}")

    @staticmethod
    def concat_dataframes(existing_df, new_data):
        """Concatenate a new record to an existing DataFrame."""
        try:
            new_record = pd.DataFrame([new_data])
            if not new_record.dropna(how='all').empty:
                return pd.concat([existing_df, new_record], ignore_index=True)
        except Exception as e:
            print(f"Error concatenating data: {e}")
        return existing_df

    @staticmethod
    def get_dataframe_string(dataframe):
        """Get a string representation of a DataFrame."""
        return dataframe.to_string(index=False)
