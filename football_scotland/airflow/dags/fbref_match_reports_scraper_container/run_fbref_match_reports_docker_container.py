import docker

def run_fbref_match_reports_scraper_container(**kwargs):
    # Get the date from the previous task
    date_value = kwargs['ti'].xcom_pull(task_ids='get_date_from_postgres')

    # Initialize the Docker client
    client = docker.from_env()

    # Specify the Docker image to pull
    image = "kostasmitalloulis/fbref_match_reports_scraper_image"
    
    # Pull the image from Docker Hub
    client.images.pull(image)

    # Define the path on the host and the path inside the container
    host_directory = "C:/Users/efsta/Desktop/Kostas/Data/football_scotland/airflow/dags/fbref_match_reports_scraper_container/csv"  # Adjust this to your local directory
    container_directory = "/app/csv"  # This should match where the container writes data

    # Set up the volume (bind mount)
    volumes = {
        host_directory: {'bind': container_directory, 'mode': 'rw'}  # rw = read-write
    }

    # Set a custom container name
    container_name = "fbref_match_reports_scraper_container"

    # Run the container with the bind mount, environment variable, and custom name
    container = client.containers.run(
        image,
        environment={"DATE_ENV": str(date_value)},  # Pass the date as an environment variable
        volumes=volumes,  # Add the bind mount
        name=container_name,  # Custom container name
        detach=False  # Detach to run in the background
    )

    # Optional: Log the container's output or ID
    print(f"Container '{container_name}' is running with DATE_ENV={date_value} and bind mount {host_directory} -> {container_directory}")


if __name__ == "__main__":
    run_fbref_match_reports_scraper_container()