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
            # Convert the record into a DataFrame with the correct types
            try:
                # Create a DataFrame row using the correct types
                new_record = pd.DataFrame([{
                    'operation': str(record['operation']),
                    'a': float(record['a']),
                    'b': float(record['b']),
                    'result': float(record['result'])
                }])

                # Concatenate only if the new record is valid
                self.history = pd.concat([self.history, new_record], ignore_index=True)
                self.save_history()

            except (ValueError, TypeError) as e:
                print(f"Error processing record: {e}")

    def get_history(self):
        return self.history.to_string(index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'a', 'b', 'result'])
        self.save_history()
