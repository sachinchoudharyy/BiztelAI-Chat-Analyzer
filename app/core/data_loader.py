# app/core/data_loader.py
import pandas as pd

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self):
        try:
            df = pd.read_csv(self.file_path)
            print(f"✅ Loaded data with shape: {df.shape}")
            return df
        except Exception as e:
            raise Exception(f"❌ Failed to load data: {e}")
