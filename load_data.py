import requests
import json
from datetime import datetime
import os
import boto3

def upload_raw_data_to_s3(raw_data):
    bucket_name = os.getenv('AWS_S3_BUCKET')

    date_today = datetime.now().strftime('%Y-%m-%d')
    file_name = f"raw_data/nbp_raw_{date_today}.json"

    s3_client = boto3.client("s3")

    print(f"Sending {file_name} to S3")

    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(raw_data)
    )

    print("Raw data saved in Data Lake")


def get_raw_data():
    URL = "https://api.nbp.pl/api/exchangerates/tables/a/today/?format=json"

    try:
        raw_data = requests.get(URL)
        raw_data.raise_for_status()
        print("Raw data downloaded")
        raw_data_json = raw_data.json()

        upload_raw_data_to_s3(raw_data_json)

        os.makedirs("raw_data", exist_ok=True)

        today_date = datetime.now().date()
        with open(f"raw_data/{today_date}.json", "w", encoding="utf-8") as file:
            json.dump(raw_data_json, file, indent=4)
        print("Raw data loaded into JSON file")

    except Exception as e:
        print(f"Error occurred: {e}")