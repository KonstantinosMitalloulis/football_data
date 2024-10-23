"""
Initialization DAG: Er dient zur Initialisierung der Datenbank.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator

from airflow.models import Connection
from airflow import settings
from datetime import datetime, timedelta
import pandas as pd
import psycopg2
from airflow.operators.postgres_operator import PostgresOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator


import requests
from helpers_initialization_dag.all_sources_merged_transformed_fl import all_sources_merged_transformed_fl

from helpers_initialization_dag.football_data_merging_transforming_csvs_fl import football_data_merging_transforming_csvs_fl

from helpers_initialization_dag.fbref_only_general_stats_of_each_match_merging_transforming_fl import fbref_only_general_stats_of_each_match_merging_transforming_fl

from helpers_initialization_dag.fbref_only_match_reports_merging_transforming_csvs_fl import fbref_only_match_reports_merging_transforming_csvs_fl

from helpers_initialization_dag.sofascore_merging_transforming_csvs_fl import sofascore_merging_transforming_csvs_fl

from helpers_initialization_dag.create_airflow_connection import create_airflow_connection

from helpers_initialization_dag.create_connection_football_scotland import create_football_scotland_connection

from helpers_initialization_dag.read_sql_file import read_sql_file

from helpers_initialization_dag.copy_data_to_staging_table_fl import copy_data_to_staging_table_fl



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
    'intialization_database',
    default_args=default_args,
    description='Merge csvs from after scraping,transform,load into postgres',
    schedule_interval=None,
)

#merge_transform from fbref_only_general_stats_of_each_match_merging_transforming_fl
merge_transform_fbref_only_general_stats_of_each_match_task = PythonOperator(
    task_id='merge_transform_fbref_only_general_stats_of_each_match',
    python_callable=fbref_only_general_stats_of_each_match_merging_transforming_fl,
    provide_context=True,
    dag=dag,
)

#merge_transform from football_data source
merge_transform_football_data_task = PythonOperator(
    task_id='merge_transform_football_data_task',
    python_callable=football_data_merging_transforming_csvs_fl,
    provide_context=True,
    dag=dag,
)



#merge_transform from fbref_only_match_reports_merging_transforming_csvs_fl
merge_transform_fbref_only_match_reports_task = PythonOperator(
    task_id='merge_transform_fbref_only_match_reports',
    python_callable=fbref_only_match_reports_merging_transforming_csvs_fl,
    provide_context=True,
    dag=dag,
)

#merge_transform from sofascore
merge_transform_sofascore_task = PythonOperator(
    task_id='merge_transform_sofascore',
    python_callable=sofascore_merging_transforming_csvs_fl,
    provide_context=True,
    dag=dag,
)

#merge trnasform all sources
merge_transform_all_sources_task = PythonOperator(
    task_id='merge_transform_all_sources',
    python_callable=all_sources_merged_transformed_fl,
    provide_context=True,
    dag=dag,
)

# Task to create the Airflow connection
create__football_airflow_connection_task = PythonOperator(
    task_id='create_football_airflow_connection',
    python_callable=create_airflow_connection,
)

create_database_football_scotland_task = PostgresOperator(
    task_id='create_database_football_scotland',
    postgres_conn_id='football_airflow_connection',  
    sql=read_sql_file('/opt/airflow/dags/sql_scripts_fl/create_database_schema.sql'),
    autocommit=True, 
    dag=dag,
)


# Task to create the Airflow connection
create__football_scotland_connection_task = PythonOperator(
    task_id='create_football_scotland_connection',
    python_callable=create_football_scotland_connection,
)


create_schema_task = PostgresOperator(
    task_id='create_schema_in_football_scotland',
    postgres_conn_id='football_scotland_connection',  # This connection points to the 'football_data' database
    sql="""
        CREATE SCHEMA IF NOT EXISTS scottish_premiership;
    """,
    dag=dag
)

create_staging_table_fl_task = PostgresOperator(
    task_id='create_staging_table_fl',
    postgres_conn_id='football_scotland_connection',  
    sql=read_sql_file('/opt/airflow/dags/sql_scripts_fl/create_staging_table_fl.sql'),
    autocommit=True, 
    dag=dag,
)


copy_data_to_staging_table_fl_task = PythonOperator(
    task_id='copy_data_to_staging_table_fl',
    python_callable=copy_data_to_staging_table_fl,
    provide_context=True,
    dag=dag
)

create_dimension_tables_fl_task = PostgresOperator(
    task_id='create_dimension_tables_fl',
    postgres_conn_id='football_scotland_connection',  
    sql=read_sql_file('/opt/airflow/dags/sql_scripts_fl/create_dimension_tables_fl.sql'),
    autocommit=True, 
    dag=dag,
)


data_insert_dim_tables_fl_task = PostgresOperator(
    task_id='data_insert_dim_tables_fl',
    postgres_conn_id='football_scotland_connection',  
    sql=read_sql_file('/opt/airflow/dags/sql_scripts_fl/data_insert_dim_tables_fl.sql'),
    autocommit=True, 
    dag=dag,
)






merge_transform_fbref_only_general_stats_of_each_match_task >> \
merge_transform_football_data_task >> \
merge_transform_fbref_only_match_reports_task >> \
merge_transform_sofascore_task >> \
merge_transform_all_sources_task >> \
create__football_airflow_connection_task >> \
create_database_football_scotland_task >> \
create__football_scotland_connection_task >> \
create_schema_task >> \
create_staging_table_fl_task >> \
copy_data_to_staging_table_fl_task >> \
create_dimension_tables_fl_task >> \
data_insert_dim_tables_fl_task