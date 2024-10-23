from getting_the_missing_match_reports import getting_the_missing_match_reports
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
from datetime import datetime,date, timedelta
def check_forbidden_and_correction(dataframe_param):
    if dataframe_param["awayteam_name"].isna().any():
        print("NaN values in awyteam_name")
        # Filter the DataFrame for rows where 'hometeam_name' is 'Forbidden'
        forbidden_troubleshooting_df = dataframe_param[dataframe_param["awayteam_name"].isna()]

        # Create a list from the 'match_report_url' column of the filtered DataFrame
        forbidden_match_report_url_list = forbidden_troubleshooting_df['match_report_url'].tolist()
        forbidden_match_reports = getting_the_missing_match_reports(forbidden_match_report_url_list)
        initial_df_without_forbidden = dataframe_param[dataframe_param["awayteam_name"].notna()].reset_index(drop=True)
        final_corrected_df = pd.concat([initial_df_without_forbidden, forbidden_match_reports], ignore_index=True)
        return final_corrected_df
    else:return dataframe_param

