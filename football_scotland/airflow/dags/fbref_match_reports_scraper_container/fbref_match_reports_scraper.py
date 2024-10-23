import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
from datetime import datetime,date, timedelta
import os

from matches_info import matches_info
from check_forbidden_and_correction import check_forbidden_and_correction
from check_starting_elevens_and_correction import check_starting_elevens_and_correction


def fbref_match_reports_scraper():
    all_match_reports_for_updating = []
    website_url_part = "https://fbref.com/en/matches/"
    #last_game = ('2024-10-05', '15:00:00', 'Ross County')
    
    # Define the start date as April 1, 2024
    start_date_str = os.getenv("DATE_ENV")  # Use os.getenv instead of os.environ.get
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    print(start_date)

    #start_date = datetime.strptime(last_game[0], '%Y-%m-%d').date()
    #print(start_date)

    # Extract the month
    #month_from_start_date = start_date.month
    #print(month_from_start_date)

    end_date = date.today()
    date_iterator = start_date

    while date_iterator <= end_date:
        day_url_part = str(date_iterator)
        day_match_reports = website_url_part + day_url_part

        data = requests.get(day_match_reports)
        time.sleep(20)
        soup = BeautifulSoup(data.text)
        links = soup.find_all('a')
        links = [l.get("href") for l in links]
        links = [l for l in links if l and '/matches/' in l and '-Scottish-Premiership' in l]
        links = set(links)
        links = list(links)
        all_match_reports_for_updating.extend(links)
        date_iterator += timedelta(days=1)

    for match_report_idx in range(len(all_match_reports_for_updating)):
        all_match_reports_for_updating[match_report_idx] = "https://fbref.com/" +  all_match_reports_for_updating[match_report_idx]

    df_init = matches_info(all_match_reports_for_updating)
    final_df=check_forbidden_and_correction(df_init)
    final_df=check_starting_elevens_and_correction(final_df)
    final_df = final_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    start_date_str = start_date.strftime('%Y-%m-%d').replace("-","_")
    end_date_str = end_date.strftime('%Y-%m-%d').replace("-","_")

    csv_name = f"/app/csv/fbref_match_reports_{start_date_str}_{end_date_str}.csv"
    final_df.to_csv(csv_name, index=False)

if __name__ == "__main__":
    fbref_match_reports_scraper()








































