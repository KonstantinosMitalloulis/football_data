
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
#from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
from datetime import datetime,date, timedelta
import time
import json
import os
from sqlalchemy import create_engine

from sofascore_incidents_with_function import incidents_game_each_game
from sofascore_game_details_with_function import game_details_each_game
from sofascore_lineups_with_function import lineups_each_game
from sofascore_managers_with_function import game_managers_each_game
from sofascore_more_details_with_function import more_details_each_game
from sofascore_statistics_with_function import statistics_each_game
from sofascore_starting_elevens import starting_elevens
from sofascore_pregame_form_with_function import pregame_form_each_game
#from sofascore_starting_date import get_starting_date



def sofascore_scraping_up():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # Disable GPU (if necessary for some environments)
    chrome_options.add_argument('--disable-gpu')
    # **Important**: Specify the Chrome binary location installed by the Dockerfile
    chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"
    chrome_options.set_capability(
        'goog:loggingPrefs' , {"performance" : "ALL" , "browser" : "ALL"}
    )
    # Specify the path to the ChromeDriver (use the one from the Dockerfile)
    driver_path = "/opt/chromedriver/chromedriver-linux64/chromedriver"  # Adjust to match where it's installed in Docker
    # Create the WebDriver instance with the specified path to ChromeDriver
    service = Service(executable_path=driver_path)
    # Initialize the WebDriver with the configured service and options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    total_list_at_this_period = []



    #datetime.strptime(get_starting_date()[0], '%Y-%m-%d').date()
    # Define the start date as April 1, 2024
    start_date_str = os.getenv("DATE_ENV")  # Use os.getenv instead of os.environ.get
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    print(start_date)


    # Extract the month
    month_from_start_date = start_date.month
    # Get the current date
    end_date = date.today()
    date_iterator = start_date

    url_first_part_date = "https://www.sofascore.com/football/"
    # Generate and print all dates from start_date to current_date
    date_iterator = start_date
    all_games_for_this_period = []
    all_game_ids_for_control = []
    while date_iterator <= end_date:
        # Store the current date in a variable
        date_variable = date_iterator.strftime('%Y-%m-%d')
        date_single_day =  url_first_part_date + str(date_variable)
    
        driver.set_page_load_timeout(900)
        try:
            driver.get(date_single_day)
        except:
            pass

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        logs_raw = driver.get_log("performance")
        logs = [json.loads(lr['message'])['message'] for lr in logs_raw]

        scheduled_events_first_part = "scheduled-events/"
        final_scheduled_events = scheduled_events_first_part + str(date_variable)

        for x in logs:
            if final_scheduled_events in  x['params'].get('headers',{}).get(':path',''):
                #print(x['params'].get('headers',{}).get(':path',''))
                break

        time.sleep(2)
        games = json.loads(driver.execute_cdp_cmd('Network.getResponseBody',{'requestId' : x['params']['requestId']})['body'])
        time.sleep(8)
        for i in range(len(games["events"])):
            dict_each_game = dict()
            custom_id = games["events"][i]["customId"]
            game_id = str(games["events"][i]["id"])
            game_slug =games["events"][i]["slug"]
            main_link = 'https://www.sofascore.com/'
            game_link = main_link + game_slug + '/' + custom_id + '#id:' +  game_id
            #game_link
            dict_game_link = dict()
            try: 
                dict_game_link["game_link"] = game_link
            except:dict_game_link["game_link"] = None
            #Game_date
            dict_game_date = dict()
            try:
                timestamp_of_game = games["events"][i]["startTimestamp"]
                # Convert timestamp to datetime object
                date_object = datetime.fromtimestamp(timestamp_of_game)
                # Extract the month
                month_from_single_day = date_object.month

                # Format the datetime object to "yyyy-mm-dd"
                date_of_game = date_object.strftime('%Y-%m-%d')
            except:date_of_game= None
            dict_game_date["game_date"] = date_of_game

            countries_of_interest = ["Scotland"]
            tournaments_names_of_interest =["Premiership","Premiership, Championship Round","Premiership, Championship Round"] 

            country_to_be_controlled_var  = game_details_each_game(i,games)["tournament_country"]
            tournament_to_be_controlled_var = game_details_each_game(i,games)["tournament_name"]
            
            if (game_id in all_game_ids_for_control) or (country_to_be_controlled_var not in countries_of_interest) or (tournament_to_be_controlled_var not in tournaments_names_of_interest):
                continue
            else:
                all_game_ids_for_control.append(game_id)
                #game_details
                game_details_var =  game_details_each_game(i,games)
                #incidents
                incidents_var = incidents_game_each_game(game_id)
                #lineups
                lineups_var =  lineups_each_game(game_id)
                #starting elevens
                home_player_list_variable = lineups_var["home_players_list"]
                away_player_list_variable = lineups_var["away_players_list"]
                substitutions_variable = incidents_var["incident_type_substitution"]
                starting_elevens_var = starting_elevens(home_player_list_variable,away_player_list_variable,substitutions_variable)
                #managers
                managers_var = game_managers_each_game(game_id)
                #more_details
                more_details_var = more_details_each_game(game_id)
                #statistics
                statistics_var = statistics_each_game(game_id)
                #pregame_form
                pregame_form_var = pregame_form_each_game(game_id)

                dict_each_game.update(dict_game_link)
                dict_each_game.update(dict_game_date)
                dict_each_game.update(game_details_var)
                dict_each_game.update(incidents_var)
                dict_each_game.update(lineups_var)
                dict_each_game.update(managers_var)
                dict_each_game.update(more_details_var)
                dict_each_game.update(statistics_var)
                dict_each_game.update(starting_elevens_var)
                dict_each_game.update(pregame_form_var)
                #print(dict_each_game)
                all_games_for_this_period.append(dict_each_game)
            # Move to the next day
        date_iterator += timedelta(days=1)
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(all_games_for_this_period)
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    start_date_str = start_date.strftime('%Y-%m-%d').replace("-","_")
    end_date_str = end_date.strftime('%Y-%m-%d').replace("-","_")
    output_csv_file = f"/app/csv/sofascore_{start_date_str}_to_{end_date_str}.csv"
    print(df)
    #time.sleep(100)
    if not os.path.isfile(output_csv_file):
        df.to_csv(output_csv_file, index= False)
    else: 
        df.to_csv(output_csv_file, mode='a', index=False, header=False)

if __name__ == "__main__":
    sofascore_scraping_up()