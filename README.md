# NBP Exchange Rates ETL Pipeline (V 1.0)
Automated ETL pipeline extracting daily exchange rates from the NBP API. After data cleansing and transformation, records are loaded into a local database.

## Architecture (ETL Process)
Project has modules, which are responsible for different stages.

- Extract: Data loaded from NBP API with *requests* library and saved to JSON file

- Transform: Parsing data with *Pandas* to DataFrame and handling Null columns, changing to correct data type

- Load: Clean data is loaded into local *SQLite* database using *SQLAlchemy*

## Technologies Used

- Python 3.12
- Pandas
- SQLAlchemy
- SQLite
- Git

## Project Structure

- main.py - main file for orchestration

- load_data.py - script for getting raw data from API

- transform_data.py - puts data into data frame and corrects data types and puts date row

- export_to_sql.py - exports data into database

## How to Run Locally

1. Clone the repository.
   ```
   git clone https://github.com/AAAc11/Exchange-rates.git
   ```
  

2. Create and activate a virtual environment.
   ```
   python -m venv venv
   venv/Scripts/activate
   ```
    
3. Install required packages.
   ```
   pip install pandas sqlalchemy requests
   ```

4. Run python main.py in your terminal.
   ```
   python main.py
   ```

## Roadmap (V 2.0)

Migration from local SQLite to a Cloud/Dockerized PostgreSQL database.

Containerization of the application using Docker.

Orchestration and scheduling using Apache Airflow or Prefect.

Storing raw extracted data in a Cloud Data Lake (e.g., AWS S3).
