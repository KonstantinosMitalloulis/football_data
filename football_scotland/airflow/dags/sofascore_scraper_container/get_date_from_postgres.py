from airflow.providers.postgres.hooks.postgres import PostgresHook
def get_date_from_postgres(**kwargs):
    # Get the PostgreSQL hook
    pg_hook = PostgresHook(postgres_conn_id='football_scotland_connection')

    # Define your SQL query
    sql = "SELECT game_date, fd_time, hometeam FROM scottish_premiership.dim_general_info ORDER BY game_date DESC, fd_time DESC LIMIT 1;" 
    connection = pg_hook.get_conn()
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    # Extract the date (assuming it's the first column)
    date_value = result[0]
    print(date_value)
    return date_value

if __name__ == "__main__":
    get_date_from_postgres()
