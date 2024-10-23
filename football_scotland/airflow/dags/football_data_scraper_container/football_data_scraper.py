import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
import pandas as pd
import requests
from io import StringIO
from keeps_to_column_scraper import columns_to_keep
import os
from datetime import datetime,date, timedelta
def football_data_scraper():
    football_data_url = 'https://www.football-data.co.uk/scotlandm.php'
    response_football_data = requests.get(football_data_url)
    time.sleep(20)
    soup_football_data = BeautifulSoup(response_football_data.text, 'html.parser')

    # Find all <a> tags
    links_football_data = soup_football_data.find_all('a')

    # List to store Premier League hrefs
    premier_league_hrefs = []

    # Iterate through the <a> tags and filter for Premier League
    for link in links_football_data:
        if "Premier League" in link.get_text():
            href = link.get('href')
            premier_league_hrefs.append(href)

    start_date_str = os.getenv("DATE_ENV")  # Use os.getenv instead of os.environ.get
    #start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()

    # Extract the last two digits of the year
    last_two_digits_of_year = start_date_str[2:4]

    print(last_two_digits_of_year)  # Output: '24'ontas date

    # Print the extracted hrefs
    update_premier_league_hrefs = []
    for href in premier_league_hrefs:
        if last_two_digits_of_year in href:
            update_premier_league_hrefs.append(href)

    football_data_url_part_one = 'https://www.football-data.co.uk/'


    for href_idx in range(len(update_premier_league_hrefs)):
        update_premier_league_hrefs[href_idx] = football_data_url_part_one + update_premier_league_hrefs[href_idx]


    # List to hold DataFrames
    data_frames = []

    for url in update_premier_league_hrefs:
        response = requests.get(url)
        time.sleep(20)  # Adjust as necessary
        if response.status_code == 200:
            # Load the CSV content into a DataFrame
            df = pd.read_csv(StringIO(response.text))
            df= columns_to_keep(df)
            data_frames.append(df)  # Add the DataFrame to the list
            print(f"Loaded data from {url}")
        else:
            print(f"Failed to fetch data from {url}")

    # Concatenate all DataFrames into a single DataFrame
    if data_frames:  # Check if the list is not empty
        combined_df = pd.concat(data_frames, ignore_index=True)
        print("DataFrames concatenated successfully.")
    else:
        combined_df = pd.DataFrame()  # Create an empty DataFrame if no data was loaded

    combined_df['Date'] = pd.to_datetime(combined_df['Date'], format='%d/%m/%Y')
    for value in combined_df['Date']:
        print(value)

    #kratao mono ta pio epikaira
    condition_date_dt = pd.to_datetime(start_date_str)

    # Example condition: Filter rows where the date is equal to the testing date
    aktuell_df = combined_df[combined_df['Date'] >= condition_date_dt]

    aktuell_df = aktuell_df.map(lambda x: x.strip() if isinstance(x, str) else x)
    # Get the latest date
    #latest_date = aktuell_df['Date'].max()

    start_date_str = start_date_str.replace("-","_")
    #end_date_str = latest_date.strftime('%Y-%m-%d').replace("-","_")

    output_csv_file = f"/app/csv/football_data_{start_date_str}.csv"

    if not os.path.isfile(output_csv_file):
        aktuell_df.to_csv(output_csv_file, index= False)
    else: 
        aktuell_df.to_csv(output_csv_file, mode='a', index=False, header=False)

if __name__ == "__main__":
    football_data_scraper()