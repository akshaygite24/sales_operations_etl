from airflow import DAG
from airflow.operators.python import PythonOperator
from etl_pipeline import run_pipeline
from datetime import datetime, timedelta
import sys
import os


PROJECT_PATH = "/home/akshay/projects/sales_operations_etl"

sys.path.append(PROJECT_PATH)


default_args = {
    "owner": "akshay",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id= "sales_operations_etl",
    default_args=default_args,
    description="Daily ETL for Sales and Operations data",
    schedule_interval="@daily",
    start_date=datetime(2025,11,9),
    catchup=False,
    tags=["etl", "sales", "operations"]
) as dag:
    
    run_sales_etl = PythonOperator(
        task_id="run_sales_etl",
        python_callable=run_pipeline,
    )

    run_sales_etl
