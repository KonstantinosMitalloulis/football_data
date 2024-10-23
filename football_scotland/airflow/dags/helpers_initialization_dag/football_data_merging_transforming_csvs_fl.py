import os
import pandas as pd
import numpy as np


from .helpers_football_data_merging_transforming_csvs_fl import ensure_columns,fix_date_format,fix_date_format_after_nineties

def football_data_merging_transforming_csvs_fl():
    # List of columns to keep
    columns_to_keep = ['Div', 'Date', 'Time', 'HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','Referee','HS','AS','HST','AST','HF','AF',
                    'HC','AC','HY','AY','HR','AR','B365H','B365D','B365A','BWH','BWD','BWA',]

    # Initialize an empty list to store DataFrames
    dataframes = []

    # Specify the folder where the CSV files are located
    path_for_all_csvs = "/opt/airflow/dags/csvs/first_load_csvs/football_data_csvs/"


    # Get a list of all CSV files in the folder
    #csv_files = [file for file in os.listdir(path_for_all_csvs) if file.endswith('.csv')]
    csv_files = ['football_data_23_24.csv','football_data_22_23.csv','football_data_21_22.csv','football_data_20_21.csv',
                'football_data_19_20.csv','football_data_18_19.csv','football_data_17_18.csv','football_data_16_17.csv','football_data_15_16.csv','football_data_14_15.csv','football_data_13_14.csv','football_data_12_13.csv',
                'football_data_11_12.csv','football_data_10_11.csv','football_data_09_10.csv','football_data_08_09.csv','football_data_07_08.csv','football_data_06_07.csv','football_data_05_06.csv','football_data_04_05.csv',
                'football_data_03_04.csv','football_data_02_03.csv','football_data_01_02.csv','football_data_00_01.csv']
    df = None

    # Loop through the list of CSV files and read each one into a DataFrame
    for file in csv_files:
        file_path = os.path.join(path_for_all_csvs, file)
        try:
            df = pd.read_csv(file_path)
            # Ensure columns and keep only the specified ones
            df = ensure_columns(df, columns_to_keep)
            # Remove the .csv extension
            file_without_extension = file.split('.')[0]
            df["tournament_season"] = file_without_extension[-5:].replace('_', '/') 
        except:pass
        dataframes.append(df)

    # Concatenate all DataFrames into one
    df_after_nineties = pd.concat(dataframes, ignore_index=True)
    df_after_nineties['Date'] = df_after_nineties['Date'].astype(str)
    # Apply the function to the 'date' column
    df_after_nineties['Date'] = df_after_nineties['Date'].apply(fix_date_format_after_nineties)




    # Initialize an empty list to store DataFrames
    dataframes = []

    # Get a list of all CSV files in the folder
    csv_files = ['football_data_98_99.csv','football_data_97_98.csv','football_data_96_97.csv',
                'football_data_95_96.csv','football_data_94_95.csv']

    df = None
    # Loop through the list of CSV files and read each one into a DataFrame
    for file in csv_files:
        file_path = os.path.join(path_for_all_csvs, file)
        try:
            df = pd.read_csv(file_path)
            # Ensure columns and keep only the specified ones
            df = ensure_columns(df, columns_to_keep)
            file_without_extension = file.split('.')[0]
            df["tournament_season"] = file_without_extension[-5:].replace('_', '/') 
        except:pass
        dataframes.append(df)

    # Concatenate all DataFrames into one
    df_nineties = pd.concat(dataframes, ignore_index=True)
    df_nineties = df_nineties.dropna(subset=['Div', 'Date','HomeTeam','AwayTeam'])
    df_nineties['Date'] = df_nineties['Date'].astype(str)
    df_nineties['Date'] = df_nineties['Date'].apply(fix_date_format)
    #df_nineties = df_nineties.dropna(subset=['Div', 'Date','HomeTeam','AwayTeam'])





    #99_00
    csv_file_99_00 = '/opt/airflow/dags/csvs/first_load_csvs/football_data_csvs/football_data_99_00.csv'
    df_99_00 = pd.read_csv(csv_file_99_00)
    # Ensure columns and keep only the specified ones
    df_99_00 = ensure_columns(df_99_00, columns_to_keep)
    file_without_extension_99_00 = csv_file_99_00.split('.')[0]
    df_99_00["tournament_season"] = file_without_extension_99_00[-5:].replace('_', '/')
    df_99_00 = df_99_00.dropna(subset=['Div', 'Date','HomeTeam','AwayTeam'])
    df_99_00['Date'] = df_99_00['Date'].astype(str)


    # Create a DataFrame containing rows with '00' in the 'season_column'
    df_99_00_00 = df_99_00[df_99_00['Date'].str.contains('00')]
    df_99_00_00['Date'] = df_99_00_00['Date'].apply(fix_date_format_after_nineties)
    df_99_00_00.to_csv('/opt/airflow/dags/csvs/first_load_csvs/football_data_csvs/df_99_00_00.csv', index=False)

    # Create a DataFrame containing rows with '99' in the 'season_column'
    df_99_00_99 = df_99_00[df_99_00['Date'].str.contains('99')]
    df_99_00_99['Date'] = df_99_00_99['Date'].apply(fix_date_format)




    # Concatenate the DataFrames row-wise
    df_concatenated = pd.concat([df_after_nineties, df_nineties,df_99_00_00,df_99_00_99], ignore_index=True)
    df_concatenated=df_concatenated.drop('Div', axis=1)
    df_concatenated.columns = ['football_data_' + col for col in df_concatenated.columns]
    df_concatenated.replace('Partick', 'Partick Thistle', inplace=True)
    df_concatenated.replace('Inverness C', 'Inverness CT', inplace=True)
    # Remove duplicates based on all columns (keep the first occurrence)
    df_concatenated = df_concatenated.drop_duplicates()
    #df_concatenated = df_concatenated.map(lambda x: x.strip() if isinstance(x, str) else x)
    df_concatenated = df_concatenated.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    #df_concatenated.columns = df_concatenated.columns.str.lower()

    df_concatenated.to_csv('/opt/airflow/dags/csvs/first_load_csvs/football_data_merged_transformed_football_data.csv', index=False)



    # Path to your CSV file
    file_path_to_be_deleted = "/opt/airflow/dags/csvs/first_load_csvs/football_data_csvs/df_99_00_00.csv"

    # Deleting the file
    if os.path.exists(file_path_to_be_deleted):
        os.remove(file_path_to_be_deleted)
        print(f"File {file_path_to_be_deleted} has been deleted.")
    else:
        print(f"The file {file_path_to_be_deleted} does not exist.")



if __name__ == "__main__":
    football_data_merging_transforming_csvs_fl()