# app/core/data_cleaner.py
class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()

    def clean_data(self):
        self.df.drop_duplicates(inplace=True)
        self.df.dropna(inplace=True)  # You can handle this more smartly if needed
        self.df.reset_index(drop=True, inplace=True)
        return self.df
