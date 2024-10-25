from app.pandas_facade import PandasFacade

class HistoryManager:
    def __init__(self, history_file='data/calculation_history.csv'):
        self.history_file = history_file
        self.history = PandasFacade.load_csv(self.history_file)

    def load_history(self):
        self.history = PandasFacade.load_csv(self.history_file)

    def save_history(self):
        PandasFacade.save_csv(self.history, self.history_file)

    def record(self, record):
        if all(key in record for key in ['operation', 'a', 'b', 'result']) and not any(pd.isna(value) for value in record.values()):
            self.history = PandasFacade.concat_dataframes(self.history, record)
            self.save_history()

    def get_history(self):
        return PandasFacade.get_dataframe_string(self.history)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'a', 'b', 'result'])
        self.save_history()
