import pandas as pd
from sqlalchemy import create_engine

def copy_data_to_staging_table_fl():
    # Create a connection to your PostgreSQL database using the details from your YAML file
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/football_scotland')

    # Load the CSV file into a DataFrame
    df = pd.read_csv('/opt/airflow/dags/csvs/first_load_csvs/all_sources_merged_transformed.csv')

    # Write the DataFrame to a SQL table
    df.to_sql('staging_table_fl',schema='scottish_premiership', con=engine, if_exists='append', index=False)

if __name__ == "__main__":
    copy_data_to_staging_table_fl()
