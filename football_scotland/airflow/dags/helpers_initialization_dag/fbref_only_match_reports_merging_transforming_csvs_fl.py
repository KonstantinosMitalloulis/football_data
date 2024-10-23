import os
import pandas as pd

#Merging the fbref_match_reports

def fbref_only_match_reports_merging_transforming_csvs_fl():

    # Define the path where your CSV files are located
    path_fbref_match_reports = '/opt/airflow/dags/csvs/first_load_csvs/fbref_csvs/all_match_reports/'

    # Get all CSV files from the directory
    fbref_match_reports_csv_files = [f for f in os.listdir(path_fbref_match_reports) if f.endswith('.csv')]

    # List to hold DataFrames
    dataframes_fbref_match_reports= []

    # Loop through all CSV files and read them into a DataFrame
    for fbref_match_reports_file in fbref_match_reports_csv_files:
        fbref_match_reports_file_path = os.path.join(path_fbref_match_reports, fbref_match_reports_file)
        df = pd.read_csv(fbref_match_reports_file_path)
        dataframes_fbref_match_reports.append(df)

    # Concatenate all DataFrames into one
    fbref_match_reports_merged_df = pd.concat(dataframes_fbref_match_reports, ignore_index=True)

    # Rename columns in-place (without reassigning)
    fbref_match_reports_merged_df.rename(columns={'fbref_rest_events_list': 'rest_events_list', 'fbref_yellow_cards_list': 'yellow_cards_list','fbref_red_cards_list': 'red_cards_list',
                    'fbref_goal_list': 'goal_list','fbref_substitutions_list': 'substitutions_list','fbref_missed_penalty_list': 'missed_penalty_list'}, inplace=True)


    # Split by '(', take the second part, and remove the closing ')'
    fbref_match_reports_merged_df['hometeam_formation'] = fbref_match_reports_merged_df['hometeam_formation'].str.split('(').str[1].str.rstrip(')')

    # Split by '(', take the second part, and remove the closing ')'
    fbref_match_reports_merged_df['awayteam_formation'] = fbref_match_reports_merged_df['awayteam_formation'].str.split('(').str[1].str.rstrip(')')

    fbref_match_reports_merged_df = fbref_match_reports_merged_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)


    fbref_match_reports_merged_df = fbref_match_reports_merged_df.rename(
        columns=lambda col: f'fbref_match_reports_{col}'
    )

    #fbref_match_reports_merged_df.columns = fbref_match_reports_merged_df.columns.str.lower()

    csv_fbref_match_reports_merged_name = "/opt/airflow/dags/csvs/first_load_csvs/fbref_match_reports_merged_transformed.csv"


    fbref_match_reports_merged_df.to_csv(csv_fbref_match_reports_merged_name, index=False)


if __name__ == "__main__":
    fbref_only_match_reports_merging_transforming_csvs_fl()