import requests
import json
from datetime import datetime
import os

def get_raw_data():
    URL = "https://api.nbp.pl/api/exchangerates/tables/a/today/?format=json"

    try:
        raw_data = requests.get(URL)
        raw_data.raise_for_status()
        print("Raw data downloaded")
        raw_data_json = raw_data.json()

        os.makedirs("raw_data", exist_ok=True)

        today_date = datetime.now().date()
        with open(f"raw_data/{today_date}.json", "w", encoding="utf-8") as file:
            json.dump(raw_data_json, file, indent=4)
        print("Raw data loaded into JSON file")

    except Exception as e:
        print(f"Error occurred: {e}")