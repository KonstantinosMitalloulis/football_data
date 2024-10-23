import os
import pandas as pd

def postponed_matches(postpone_value):
    if  postpone_value == "[]": 
        return "postponed"
    else:return "not_postponed"

def finished_matches(finished_value):
    if  finished_value == "['HT', 'FT']": 
        return "yes"
    else:return "no"

#ftiaxno tin stili postponed me true h false kai apomakrino duplicates
def transformation(dataframe): 
    dataframe =dataframe[(dataframe["tournament_name"] == "Premiership") | (dataframe["tournament_name"] == "Premiership, Championship Round") | (dataframe["tournament_name"] == "Premiership, Relegation Round")]
    # Remove duplicate rows
    dataframe = dataframe.drop_duplicates()    
    dataframe['postponed'] = dataframe['periods_of_match'].apply(postponed_matches)
    dataframe['match_finished'] = dataframe['periods_of_match'].apply(finished_matches)
    dataframe = dataframe[dataframe["match_finished"] == 'yes'].reset_index(drop=True)
    dataframe = dataframe[dataframe["postponed"] == 'not_postponed'].reset_index(drop=True)
    #Renaming the columns
    dataframe.columns = ['sofascore_' + col for col in dataframe.columns]
    #Drop some columns i do not need
    # Remove single or multiple columns by name
    dataframe = dataframe.drop(['sofascore_postponed','sofascore_extra_time','sofascore_penalties','sofascore_home_manager_id',
                                'sofascore_away_manager_id','sofascore_referee_id',
                                'sofascore_stadium_id_game_took_place','sofascore_country_game_took_place'], axis=1)
    dataframe= dataframe.reset_index(drop=True)
    # Replace 'St. Mirren' with 'St Mirren' in all columns
    dataframe.replace('Dundee FC', 'Dundee', inplace=True)
    dataframe.replace('Hamilton Academical', 'Hamilton', inplace=True)
    dataframe.replace('Heart of Midlothian', 'Hearts', inplace=True)
    dataframe.replace('St. Johnstone', 'St Johnstone', inplace=True)
    dataframe.replace('St. Mirren', 'St Mirren', inplace=True)
    dataframe.replace('Inverness Caledonian Thistle', 'Inverness CT', inplace=True)
    dataframe = dataframe.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    # Remove duplicates based on all columns (keep the first occurrence)
    finalised_dataframe = dataframe.drop_duplicates()
    return finalised_dataframe
    
