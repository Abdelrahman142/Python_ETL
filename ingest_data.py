import pandas as pd

def ingest_data(file_path):
        print("Ingesting data...")
        df = pd.read_csv(file_path)
        return df
