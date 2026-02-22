from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def wait_for_data():
    # Simple check si des données Kafka sont disponibles
    subprocess.run(["python", "/opt/airflow/consumer_to_postgres.py", "--check-only"])

def process_data():
    subprocess.run(["python", "/opt/airflow/ml/clean_data.py"])

def train_model():
    subprocess.run(["python", "/opt/airflow/ml/train_model.py"])

def validate_model():
    subprocess.run(["python", "/opt/airflow/ml/validate_model.py"])

with DAG(
    'daily_irrigation_pipeline',
    start_date=datetime(2026,2,15),
    schedule_interval='@daily',
    catchup=False
) as dag:

    t1 = PythonOperator(task_id='wait_for_data', python_callable=wait_for_data)
    t2 = PythonOperator(task_id='process_data', python_callable=process_data)
    t3 = PythonOperator(task_id='train_model', python_callable=train_model)
    t4 = PythonOperator(task_id='validate_model', python_callable=validate_model)

    t1 >> t2 >> t3 >> t4
