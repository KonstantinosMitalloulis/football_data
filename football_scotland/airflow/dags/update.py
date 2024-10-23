"""
Update DAG: Er dient zum Aktualisieren der Datenbank.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.models import Connection
from airflow import settings
from datetime import datetime, timedelta
import pandas as pd
import psycopg2
from airflow.providers.postgres.hooks.postgres import PostgresHook
import docker
from sofascore_scraper_container.get_date_from_postgres import get_date_from_postgres
from sofascore_scraper_container.run_docker_container import run_docker_container
from football_data_scraper_container.run_football_data_docker_container import run_football_data_docker_container
from fbref_match_reports_scraper_container.run_fbref_match_reports_docker_container import run_fbref_match_reports_scraper_container


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 20),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'update_database',
    default_args=default_args,
    description='Update of scottish_premiership databse',
    schedule_interval=None,
)

get_date_from_postgres_task = PythonOperator(
    task_id='get_date_from_postgres',
    python_callable=get_date_from_postgres,
    provide_context=True,
    dag=dag,
)

#fbref_match_reports
run_fbref_match_reports_scraper_container_task = PythonOperator(
    task_id='run_fbref_match_reports_scraper_container',
    python_callable=run_fbref_match_reports_scraper_container,
    provide_context=True,
    dag=dag,
)

run_football_data_docker_container_task = PythonOperator(
    task_id='run_football_data_docker_container',
    python_callable=run_football_data_docker_container,
    provide_context=True,
    dag=dag,
)


#sofascore
#run_docker_container_task = PythonOperator(
#    task_id='run_docker_container',
#    python_callable=run_docker_container,
#    provide_context=True,
#    dag=dag,
#)







get_date_from_postgres_task >>run_fbref_match_reports_scraper_container_task >>run_football_data_docker_container_task #>> run_docker_container_task 



