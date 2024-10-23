import os
import pandas as pd

from .helpers_sofascore_merging_transforming_csvs_fl import postponed_matches,finished_matches,transformation


def sofascore_merging_transforming_csvs_fl():
    # Initialize an empty list to store DataFrames
    dataframes = []

    for single_csv in ["2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024"]:

        # Specify the folder where the CSV files are located
        #path_for_all_csvs = "C:/Users/efsta/Desktop/Kostas/Data/Betting_Project/kooperation_bill/sofascore_csvs/"
        path_for_all_csvs = "/opt/airflow/dags/csvs/first_load_csvs/sofascore_csvs/"
        folder_path = path_for_all_csvs + str(single_csv) 

    #C:\Users\efsta\Desktop\Kostas\Data\Betting_Project\kooperation_bill
    # Get a list of all CSV files in the folder
        csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]



        # Loop through the list of CSV files and read each one into a DataFrame
        for file in csv_files:
            file_path = os.path.join(folder_path, file)
            try:
                df = pd.read_csv(file_path)
            except:pass
            dataframes.append(df)

        # Concatenate all DataFrames into one
        untransformed_merged_df = pd.concat(dataframes, ignore_index=True)

    # Save the merged DataFrame to a new CSV file
    #untransformed_merged_df.to_csv('sofascore_final_untransformed_merged.csv', index=False)

    #print("All CSVs have been merged from 2017 to 2024 into sofascore_final_untransformed_merged.csv")

    sofascore_merged_transformed=transformation(untransformed_merged_df)
    #sofascore_merged_transformed.columns = sofascore_merged_transformed.columns.str.lower()
    sofascore_merged_transformed.to_csv('/opt/airflow/dags/csvs/first_load_csvs/sofascore_merged_transformed.csv', index=False)


if __name__ == "__main__":
    sofascore_merging_transforming_csvs_fl()
