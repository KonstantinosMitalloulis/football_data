import os
import pandas as pd

def fbref_only_general_stats_of_each_match_merging_transforming_fl():
    # Initialize an empty list to store DataFrames
    dataframes = []

    # Path where CSV files are located
    path_for_all_csvs_only_general_stats = "/opt/airflow/dags/csvs/first_load_csvs/fbref_csvs/only_general_stats_of_each_match/"

    # Get a list of all CSV files in the folder
    csv_files_only_general_stats = [file for file in os.listdir(path_for_all_csvs_only_general_stats) if file.endswith('.csv')]

    # Loop through the list of CSV files and read each one into a DataFrame
    for file_only_general_stats in csv_files_only_general_stats:
        file_path_only_general_stats  = os.path.join(path_for_all_csvs_only_general_stats, file_only_general_stats )  # Construct the full file path
        try:
            df = pd.read_csv(file_path_only_general_stats )
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file_path_only_general_stats }: {e}")

    # Concatenate all DataFrames into one
    merged_transformed_df_only_general_stats  = pd.concat(dataframes, ignore_index=True)
    # Remove duplicates based on all columns (keep the first occurrence)
    #merged_df = merged_df.drop_duplicates()
    merged_transformed_df_only_general_stats = merged_transformed_df_only_general_stats.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    merged_transformed_df_only_general_stats = merged_transformed_df_only_general_stats.rename(
        columns=lambda col: col.replace('fbref_', 'fbref_only_general_stats_')
    )

    #merged_transformed_df_only_general_stats.columns = merged_transformed_df_only_general_stats.columns.str.lower()

    # Save the merged DataFrame to a new CSV file
    csv_file_name_only_general_stats = '/opt/airflow/dags/csvs/first_load_csvs/fbref_only_general_stats_merged_transformed.csv'
    merged_transformed_df_only_general_stats.to_csv(csv_file_name_only_general_stats, index=False)

    print(f"All CSVs have been merged into {csv_file_name_only_general_stats}")

if __name__ == "__main__":
    fbref_only_general_stats_of_each_match_merging_transforming_fl()