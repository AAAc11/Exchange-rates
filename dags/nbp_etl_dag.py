from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='nbp_exchange_rates_pipeline',
    default_args=default_args,
    description='Codzienny pobór kursów walut z NBP o 12:15',
    schedule_interval='15 12 * * *',
    start_date=datetime(2023, 10, 1),
    catchup=False,
    tags=['ETL', 'NBP'],
) as dag:
    
    run_etl = BashOperator(
        task_id='run_main_python_script',
        bash_command='cd /opt/airflow/project && python main.py',
    )

    run_etl