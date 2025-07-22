from ingest_data import ingest_data
from process_data import clean_data
from load_data import load_data

def run_etl():
    print("Running full ETL process...\n")
    df = ingest_data("massive_dataset.csv")
    cleaned_df = clean_data(df)
    load_data(cleaned_df)
    print("\nETL process completed!")

if __name__ == "__main__":
    run_etl()
