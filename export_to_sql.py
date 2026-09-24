from sqlalchemy import create_engine

def write_to_db(clean_df):
    try:
        engine = create_engine("sqlite:///nbp_exchange_rates.db")
        clean_df.to_sql("currency_rates", con=engine, if_exists="append", index=False)
        print("Data saved to database")
    except Exception as e:
        print(f"Error occured: {e}")
