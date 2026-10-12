# NBP Exchange Rates ETL Pipeline (V 2.0)
Automated ETL pipeline extracting daily exchange rates from the NBP API. After data cleansing and transformation, records are loaded into containerized PostgreSQL database. The entire process is scheduled and orchestrated using Apache Airflow.

## Architecture (ETL Process)
Project has modules, which are responsible for different stages.

- Extract: Data loaded from NBP API with *requests* library and saved as raw JSON into an **AWS S3 Data Lake**

- Transform: Parsing data with *Pandas* to DataFrame and handling Null columns, changing to correct data type

- Load: Clean data is loaded into a *PostgreSQL* database running in a *Docker* container using *SQLAlchemy*

- Infrastructure: The whole application is managed by *Docker Compose* and database changes are controlled by *Alembic*

- Orchestration: *Apache Airflow* manages the scheduling and execution of the pipeline

## Technologies Used

- Python 3.12
- Pandas
- SQLAlchemy & Alembic
- PostgreSQL
- Amazon Web Services (AWS S3) & boto3
- Docker & Docker Compose
- Apache Airflow
- Git

## Project Structure

- main.py - main file for orchestration

- load_data.py - script for getting raw data from API and uploading to AWS S3

- transform_data.py - puts data into data frame and corrects data types and puts date row

- export_to_sql.py - exports data into database

- models.py - defines database columns

- Dockerfile - containerization instructions

- docker-compose.yml - defines the environment

- dags/ - directory containing Apache Airflow DAGs

## How to Run Locally

1. Clone the repository:
   ```
   git clone https://github.com/AAAc11/Exchange-rates.git
   ```
  

2. Set up the environment variable:
   Create `.env` file:
   ```
   # Database
   POSTGRES_USER=your_user
   POSTGRES_PASSWORD=your_password
   POSTGRES_DB=exchange_rates

   # Airflow
   AIRFLOW_SECRET_KEY=your_secure_random_secret_key
   
   # AWS S3 Data Lake
   AWS_ACCESS_KEY_ID=your_aws_access_key
   AWS_SECRET_ACCESS_KEY=your_aws_secret_key
   AWS_DEFAULT_REGION=eu-north-1
   AWS_S3_BUCKET=nbp-exchange-rates-raw-data-anna-cygan
   ```
   
3. Start the infrastructure (Database and Airflow):
   ```
   docker compose up db -d
   ```

4. Access the Airflow UI:
   - Open `http://localhost:8080` in browser
   - Login: `admin` / Password: `admin`
   - Unpause the `nbp_exchange_rates_pipeline` DAG to enable daily scheduling, or click "Trigger DAG" to run it manually

## Roadmap (V 2.0) - DONE

~~Migration from local SQLite to a Cloud/Dockerized PostgreSQL database.~~

~~Containerization of the application using Docker.~~

~~Orchestration and scheduling using Apache Airflow or Prefect.~~

~~Storing raw extracted data in a Cloud Data Lake (e.g., AWS S3).~~
