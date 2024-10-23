def columns_to_keep(dataframe):
    columns_to_keep = [ 'Date', 'Time', 'HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','Referee','HS','AS','HST','AST','HF','AF',
                    'HC','AC','HY','AY','HR','AR','B365H','B365D','B365A','BWH','BWD','BWA']
        # Keep only the specified columns
    filtered_dataframe = dataframe[columns_to_keep]
    
    return filtered_dataframe

if __name__ == "__main__":
    columns_to_keep()