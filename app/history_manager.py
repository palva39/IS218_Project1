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
        try:
            self.history = pd.read_csv(self.history_file)
        except Exception as e:
            print(f"Error loading history: {e}")

    def save_history(self):
        try:
            self.history.to_csv(self.history_file, index=False)
        except Exception as e:
            print(f"Error saving history: {e}")

    def record(self, record):
        # Check if the record is valid
        if all(key in record for key in ['operation', 'a', 'b', 'result']) and not any(pd.isna(value) for value in record.values()):
            try:
                # Create a DataFrame from the record and add it to the history
                new_record = pd.DataFrame([record])
                self.history = pd.concat([self.history, new_record], ignore_index=True)
                self.save_history()
            except Exception as e:
                print(f"Error recording history: {e}")

    def get_history(self):
        return self.history.to_string(index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'a', 'b', 'result'])
        self.save_history()
