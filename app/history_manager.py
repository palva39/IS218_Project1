from app.pandas_facade import PandasFacade
import pandas as pd

class HistoryManager:
    def __init__(self, history_file='data/calculation_history.csv'):
        self.history_file = history_file
        self.history = PandasFacade.load_csv(self.history_file)

    def load_history(self):
        self.history = PandasFacade.load_csv(self.history_file)

    def save_history(self):
        PandasFacade.save_csv(self.history, self.history_file)

    def record(self, record):
        # Ensure the record contains all required fields
        if all(key in record for key in ['operation', 'a', 'b', 'result']) and not any(pd.isna(value) for value in record.values()):
            try:
                # Use PandasFacade to handle DataFrame concatenation
                new_record = pd.DataFrame([record])
                self.history = PandasFacade.concat_dataframes(self.history, record)

                self.save_history()
            except Exception as e:
                print(f"Error recording history: {e}")

    def get_history(self):
        return PandasFacade.get_dataframe_string(self.history)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'a', 'b', 'result'])
        self.save_history()
