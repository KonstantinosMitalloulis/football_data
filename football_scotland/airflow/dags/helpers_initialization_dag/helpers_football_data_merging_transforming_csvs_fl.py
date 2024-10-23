import os
import pandas as pd
import numpy as np

# Define a function to fix the date format
def fix_date_format_after_nineties(date_str):
    # Check if the year is 2 digits, assume it's in the format 'DD/MM/YY'
    if len(date_str.split('/')[-1]) == 2:
        # Prepend '20' to the year to make it 'YYYY'
        date_str = date_str[:-2] + '20' + date_str[-2:]
    
    # Convert the date string from 'DD/MM/YYYY' to 'YYYY-MM-DD'
    return pd.to_datetime(date_str, format='%d/%m/%Y').strftime('%Y-%m-%d')

def fix_date_format(date_str):
    # Check if the year is 2 digits, assume it's in the format 'DD/MM/YY'
    if len(date_str.split('/')[-1]) == 2:
        # Prepend '20' to the year to make it 'YYYY'
        date_str = date_str[:-2] + '19' + date_str[-2:]
    
    # Convert the date string from 'DD/MM/YYYY' to 'YYYY-MM-DD'
    return pd.to_datetime(date_str, format='%d/%m/%Y').strftime('%Y-%m-%d')


def ensure_columns(df, columns_to_keep):
    for column in columns_to_keep:
        if column not in df.columns:
            df[column] = np.nan  # Initialize missing columns with NaN
    return df[columns_to_keep]  # Return DataFrame with only the required columns