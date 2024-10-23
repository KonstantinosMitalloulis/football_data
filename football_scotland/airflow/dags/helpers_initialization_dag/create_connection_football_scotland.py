from airflow.models import Connection
from airflow import settings
# Define your connection parameters
CONN_ID = 'football_scotland_connection'
CONN_TYPE = 'postgres'
HOST = 'postgres'  # Change this to your actual host
SCHEMA = 'football_scotland'
LOGIN = 'airflow'
PASSWORD = 'airflow'
PORT = '5432'

def create_football_scotland_connection():
    conn = Connection(
        conn_id=CONN_ID,
        conn_type=CONN_TYPE,
        host=HOST,
        schema=SCHEMA,
        login=LOGIN,
        password=PASSWORD,
        port=PORT
    )
    session = settings.Session()
    session.add(conn)
    session.commit()

if __name__ == "__main__":
    create_football_scotland_connection()