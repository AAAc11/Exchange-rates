from load_data import get_raw_data
from transform_data import data_transformation
from export_to_sql import write_to_db

def main():
    try:
        print("Initializing")
        get_raw_data()
        clean_df = data_transformation()
        write_to_db(clean_df)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
