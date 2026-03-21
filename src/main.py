from extract import extract_all
from transform import transform_all
from load import load_data

def run_etl():
    print("[main] strating ETL process...")
    raw_data = extract_all()
    trasformed_data = transform_all(raw_data)
    load_data(trasformed_data)
    print("[main] ETL process completed.")


if __name__ == "__main__":
    run_etl()