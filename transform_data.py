import pandas as pd
from datetime import datetime
import json

def data_transformation():
    try:

        today_date = datetime.now().date()

        with open(f"raw_data/{today_date}.json", "r", encoding="utf-8") as file:
            raw_data_json = json.load(file)
            rates = raw_data_json[0].get("rates")
            df = pd.DataFrame(rates)

            df.dropna(subset=["code", "mid"])
            df["currency"] = df["currency"].fillna("Unknown currency")

            df["date"] = today_date
            df["date"] = pd.to_datetime(df["date"])

            print("Data transformed")

            return df

    except Exception as e:
        print(f"Error occurred: {e}")
