# NBP Exchange Rates ETL Pipeline (V 2.0 - ongoing)
Automated ETL pipeline extracting daily exchange rates from the NBP API. After data cleansing and transformation, records are loaded into containerized PostgreSQL database.

## Architecture (ETL Process)
Project has modules, which are responsible for different stages.

- Extract: Data loaded from NBP API with *requests* library and saved to JSON file

- Transform: Parsing data with *Pandas* to DataFrame and handling Null columns, changing to correct data type

- Load: Clean data is loaded into a *PostgreSQL* database running in a *Docker* container using *SQLAlchemy*

- Infrastructure: The whole application is managed by *Docker Compose* and database changes are controlled by *Alembic*

## Technologies Used

- Python 3.12
- Pandas
- SQLAlchemy & Alembic
- PostgreSQL
- Docker & Docker Compose
- Git

## Project Structure

- main.py - main file for orchestration

- load_data.py - script for getting raw data from API

- transform_data.py - puts data into data frame and corrects data types and puts date row

- export_to_sql.py - exports data into database

- models.py - defines database columns

- Dockerfile - containerization instructions

- docker-compose.yml - defines the environment

## How to Run Locally

1. Clone the repository:
   ```
   git clone https://github.com/AAAc11/Exchange-rates.git
   ```
  

2. Set up the environment variable:
   Create `.env` file:
   ```
   POSTGRES_USER=your_user
   POSTGRES_PASSWORD=your_password
   POSTGRES_DB=exchange_rates
   ```
    
4. Start the database:
   ```
   docker compose up db -d
   ```

5. Run the ETL pipeline:
   ```
   docker compose up etl --build
   ```

## Roadmap (V 2.0)

~~Migration from local SQLite to a Cloud/Dockerized PostgreSQL database.~~

~~Containerization of the application using Docker.~~

Orchestration and scheduling using Apache Airflow or Prefect.

Storing raw extracted data in a Cloud Data Lake (e.g., AWS S3).
