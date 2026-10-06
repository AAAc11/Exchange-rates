from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")

DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@localhost:5432/{DB_NAME}"

def write_to_db(clean_df):
    try:
        engine = create_engine(DB_URL)
        clean_df.to_sql("exchange_rates", con=engine, if_exists="append", index=False)
        print("Data saved to database")
    except Exception as e:
        print(f"Error occured: {e}")
