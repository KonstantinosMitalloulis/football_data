from getting_the_missing_match_reports import getting_the_missing_match_reports
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
from datetime import datetime,date, timedelta
def check_starting_elevens_and_correction(dataframe_param):
    if dataframe_param["hometeam_starting_eleven"].str.contains(r'\[\]').any() or dataframe_param["awayteam_starting_eleven"].str.contains(r'\[\]').any():
        print("lista exists")
        # Filter the DataFrame for rows where 'hometeam_name' is 'Forbidden'
        missing_starting_eleven_troubleshooting_df = dataframe_param[(dataframe_param["hometeam_starting_eleven"] == '[]') | (dataframe_param["awayteam_starting_eleven"] == '[]')]

        # Create a list from the 'match_report_url' column of the filtered DataFrame
        missing_starting_eleven_troubleshooting_df_list_urls = missing_starting_eleven_troubleshooting_df['match_report_url'].tolist()
        missing_starting_eleven_match_reports = getting_the_missing_match_reports(missing_starting_eleven_troubleshooting_df_list_urls)

        initial_df_without_missing_starting_elevens = dataframe_param[(dataframe_param["hometeam_starting_eleven"] != '[]') & (dataframe_param["awayteam_starting_eleven"] != '[]')].reset_index(drop=True)

        final_corrected_starting_elevens_df = pd.concat([initial_df_without_missing_starting_elevens, missing_starting_eleven_match_reports], ignore_index=True)
        return final_corrected_starting_elevens_df
    else:return dataframe_param

