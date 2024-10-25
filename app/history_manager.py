# app/history_manager.py
import pandas as pd
import os

class HistoryManager:
    def __init__(self, history_file='data/calculation_history.csv'):
        self.history_file = history_file
        self.history = pd.DataFrame(columns=['operation', 'a', 'b', 'result'])

        if os.path.exists(self.history_file):
            self.load_history()

    def load_history(self):
        self.history = pd.read_csv(self.history_file)

    def save_history(self):
        self.history.to_csv(self.history_file, index=False)

    def record(self, record):
        # Ensure all keys are present and values are not None
        if all(key in record for key in ['operation', 'a', 'b', 'result']) and not any(pd.isna(value) for value in record.values()):
            # Create a DataFrame from the record with specific data types
            new_record = pd.DataFrame([record], dtype=self.history.dtypes.to_dict())

            # Concatenate only if the new record is valid
            if not new_record.empty:
                self.history = pd.concat([self.history, new_record], ignore_index=True)
                self.save_history()

    def get_history(self):
        return self.history.to_string(index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'a', 'b', 'result'])
        self.save_history()
