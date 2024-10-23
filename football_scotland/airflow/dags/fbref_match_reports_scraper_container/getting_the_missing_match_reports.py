import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
from datetime import datetime,date, timedelta

def getting_the_missing_match_reports(missing_url_list):
    missing_match_reports_single_season = []
    #Title
    for match_rpt_idx in range(len(missing_url_list)):
        hometeam_possesion = np.nan
        hometeam_name= np.nan
        awayteam_name= np.nan
        hometeam_manager= np.nan
        awayteam_manager= np.nan
        hometeam_form= np.nan
        awayteam_form		= np.nan								
        game_venue_date= np.nan
        game_venue_epoch= np.nan
        game_venue_time= np.nan
        stadium_name= np.nan
        game_officials= np.nan
        game_attendance= np.nan
        referee= np.nan
        ar1= np.nan
        ar2= np.nan
        fourth_official= np.nan
        hometeam_fouls	= np.nan							
        awayteam_fouls= np.nan
        hometeam_crosses= np.nan
        awayteam_crosses= np.nan
        hometeam_interceptions= np.nan
        awayteam_interceptions= np.nan
        hometeam_offsides= np.nan
        awayteam_offsides= np.nan
        hometeam_possesion= np.nan
        awayteam_possesion	= np.nan					
        hometeam_shots_on_target_percentage= np.nan
        awayteam_shots_on_target_percentage= np.nan
        hometean_shots_not_percentages= np.nan
        awayteam_shots_not_percentages= np.nan
        hometeam_saves_percentage= np.nan
        awayteam_saves_not_percentages= np.nan
        hometean_saves_not_percentages	= 	np.nan											
        awayteam_saves_percentage= 	np.nan	
        fbref_rest_events_list= 	np.nan	
        fbref_yellow_cards_list= 	np.nan	
        fbref_red_cards_list= 	np.nan	
        fbref_goal_list= 	np.nan	
        fbref_substitutions_list= 	np.nan	
        fbref_missed_penalty_list= 	np.nan	
        hometeam_starting_eleven= 	np.nan	
        hometeam_bench= 	np.nan	
        hometeam_formation= 	np.nan	
        awayteam_starting_eleven= 	np.nan	
        awayteam_bench= 	np.nan	
        awayteam_formation= 	np.nan	
        # URL to scrape
        #single_match_url = 'https://fbref.com/en/matches/65358e6f/St-Mirren-Celtic-March-5-2023-Scottish-Premiership'


        single_match_dict = dict()
        # Fetch the HTML content
        response_single_match = requests.get(missing_url_list[match_rpt_idx])
        time.sleep(20)
        soup_single_match = BeautifulSoup(response_single_match.text, 'html.parser')
        #print(all_match_reports_of_the_season[match_rpt_idx])
        single_match_dict["match_report_url"] = missing_url_list[match_rpt_idx]


        #if all_match_reports_of_the_season[match_rpt_idx] in not_duplicates:
        #    continue
        #else:not_duplicates.append(all_match_reports_of_the_season[match_rpt_idx] )
        #Title

        try:
            title_infos = soup_single_match.find_all('h1')
            title = title_infos[0].get_text(strip=True)
            try:
                hometeam_name = title.split('vs.')[0].strip()
            except:hometeam_name =np.nan
            try:
                awayteam_name =title.split('vs.')[1].strip()
                awayteam_name = awayteam_name.split('Match Report')[0].strip()
            except:awayteam_name = np.nan
        except:
            hometeam_name = np.nan
            awayteam_name= np.nan

        hometeam_name = assign_change_team_name(hometeam_name)
        awayteam_name = assign_change_team_name(awayteam_name)

        single_match_dict["hometeam_name"] =hometeam_name
        single_match_dict["awayteam_name"] =awayteam_name


        #Top_of_webpage
        #Managers
        try:
            managers_part = soup_single_match.find_all('div', class_='datapoint')
            teams_managers = []
            for managering in managers_part:
                if 'Manager' in managering.get_text(strip=True):
                    teams_managers.append(managering.get_text(strip=True))

            try:
                hometeam_manager = teams_managers[0].split(':')[1].strip().replace("\xa0",' ')
            except:hometeam_manager = np.nan
            try:
                awayteam_manager = teams_managers[1].split(':')[1].strip().replace("\xa0",' ')
            except:awayteam_manager =np.nan
        except:
            hometeam_manager = np.nan
            awayteam_manager = np.nan


        single_match_dict["hometeam_manager"] =hometeam_manager
        single_match_dict["awayteam_manager"] =awayteam_manager

        #team_results at this point
        # Find the divs that contain the records after the scores
        try:
            team_forms = soup_single_match.find_all('div', class_='scores')

            # Extract the values following the score divs
            team_records = [record.find_next_sibling('div').get_text(strip=True) for record in team_forms]
            try:
                hometeam_form = team_records[0]
            except:hometeam_form= np.nan
            try:
                awayteam_form = team_records[1]
            except:awayteam_form= np.nan
        except:
            hometeam_form = np.nan
            awayteam_form = np.nan

        single_match_dict["hometeam_form"] =hometeam_form
        single_match_dict["awayteam_form"] =awayteam_form

        #game_venue_time
        try:

            game_times =soup_single_match.find('span', class_='venuetime')
            # Extract the attributes
            try:
                game_venue_date = game_times.get('data-venue-date')
            except:game_venue_date =np.nan
            try:
                game_venue_epoch = game_times.get('data-venue-epoch')
            except:game_venue_epoch =np.nan
            try:
                game_venue_time = game_times.get('data-venue-time')
            except:game_venue_time =np.nan
        except:
            game_times = np.nan
            game_venue_date = np.nan
            game_venue_epoch = np.nan
            game_venue_time = np.nan

        single_match_dict["game_venue_date"] =game_venue_date
        single_match_dict["game_venue_epoch"] =game_venue_epoch
        single_match_dict["game_venue_time"] =game_venue_time


        #stadium,attendance,officials
        try:
            stadium_attendance_officials = soup_single_match.find_all('small')
            stadium_name = np.nan
            game_officials= np.nan
            game_attendance= np.nan

            for st_idx in range(len(stadium_attendance_officials)):
                if stadium_attendance_officials[st_idx].get_text(strip=True) == "Venue":
                    try:
                        stadium_name = stadium_attendance_officials[st_idx+1].get_text(strip=True)
                    except:stadium_name =np.nan
                if stadium_attendance_officials[st_idx].get_text(strip=True) == "Officials":
                    try:
                        game_officials = stadium_attendance_officials[st_idx+1].get_text(strip=True)
                    except:game_officials = np.nan
                    try:
                        officials_list = game_officials.split('·')
                    except:officials_list = np.nan
                    # Now extract the required data from each part of the list
                    try:
                        referee = officials_list[0].split(' (')[0].replace("\xa0"," ") 
                    except:referee= np.nan
                    try: # Extract referee's name
                        ar1 = officials_list[1].split(' (')[0].replace("\xa0"," ")
                    except:ar1= np.nan
                    try:       # Extract AR1's name
                        ar2 = officials_list[2].split(' (')[0].replace("\xa0"," ") 
                    except:ar2= np.nan
                    try:      # Extract AR2's name
                        fourth_official = officials_list[3].split(' (')[0].replace("\xa0"," ") 
                    except:fourth_official= np.nan
                    # Extract 4th official's nam

                if stadium_attendance_officials[st_idx].get_text(strip=True) == "Attendance":
                    game_attendance = stadium_attendance_officials[st_idx+1].get_text(strip=True)
        except:
            stadium_name= np.nan
            game_officials= np.nan
            game_attendance= np.nan
            referee= np.nan
            ar1= np.nan
            ar2= np.nan
            fourth_official= np.nan

        single_match_dict["stadium_name"] =stadium_name
        single_match_dict["game_officials"] =game_officials
        single_match_dict["game_attendance"] =game_attendance
        single_match_dict["referee"] =referee
        single_match_dict["ar1"] =ar1
        single_match_dict["ar2"] =ar2
        single_match_dict["fourth_official"] =fourth_official


        #fouls
        try:
            fouls_div_prev = soup_single_match.find_all('div', text='Fouls')[0].find_previous_siblings()
            fouls_div_next = soup_single_match.find_all('div', text='Fouls')[0].find_next_siblings()
            try:
                hometeam_fouls = fouls_div_prev[0].get_text(strip=True)
            except:hometeam_fouls= np.nan
            try:
                awayteam_fouls = fouls_div_next[0].get_text(strip=True)
            except:awayteam_fouls= np.nan
        except:
            hometeam_fouls = np.nan
            awayteam_fouls = np.nan

        #crosses
        try:
            crosses_div_prev = soup_single_match.find_all('div', text='Crosses')[0].find_previous_siblings()
            crosses_div_next = soup_single_match.find_all('div', text='Crosses')[0].find_next_siblings()
            try:
                hometeam_crosses = crosses_div_prev[0].get_text(strip=True)
            except:hometeam_crosses= np.nan
            try:
                awayteam_crosses = crosses_div_next[0].get_text(strip=True)
            except:awayteam_crosses= np.nan
        except:
            hometeam_crosses = np.nan
            awayteam_crosses = np.nan


        #interceptons
        try:
            interceptions_div_prev = soup_single_match.find_all('div', text='Interceptions')[0].find_previous_siblings()
            interceptions_div_next = soup_single_match.find_all('div', text='Interceptions')[0].find_next_siblings()
            try:
                hometeam_interceptions = interceptions_div_prev[0].get_text(strip=True)
            except:hometeam_interceptions= np.nan
            try:
                awayteam_interceptions = interceptions_div_next[0].get_text(strip=True)
            except:awayteam_interceptions= np.nan
        except:
            hometeam_interceptions = np.nan
            awayteam_interceptions= np.nan

        #offsides
        try:
            offsides_div_prev = soup_single_match.find_all('div', text='Offsides')[0].find_previous_siblings()
            offsides_div_next = soup_single_match.find_all('div', text='Offsides')[0].find_next_siblings()
            # Extract the offsides for each team
            try:
                hometeam_offsides = offsides_div_prev[0].get_text(strip=True)
            except:hometeam_offsides= np.nan
            try:
                awayteam_offsides = offsides_div_next[0].get_text(strip=True)
            except:awayteam_offsides= np.nan
        except:
            hometeam_offsides = np.nan
            awayteam_offsides = np.nan


        single_match_dict["hometeam_fouls"] =hometeam_fouls
        single_match_dict["awayteam_fouls"] =awayteam_fouls
        single_match_dict["hometeam_crosses"] =hometeam_crosses
        single_match_dict["awayteam_crosses"] =awayteam_crosses
        single_match_dict["hometeam_interceptions"] =hometeam_interceptions
        single_match_dict["awayteam_interceptions"] =awayteam_interceptions
        single_match_dict["hometeam_offsides"] =hometeam_offsides
        single_match_dict["awayteam_offsides"] =awayteam_offsides



        #Team_Stats
        # Find the div with id "team_stats"
        try:
            team_stats_div = soup_single_match.find('div', id='team_stats')
            indexes_stats = team_stats_div.find_all('tr')
            dictionary_of_indexes = {"index_possesion":0,"index_shots_on_target":0,"index_saves":0}
            for idx in range(len(indexes_stats)):
                try:
                    if indexes_stats[idx].find('th').get_text(strip=True) == 'Possession':
                        dictionary_of_indexes["index_possesion"] = idx + 1
                    if indexes_stats[idx].find('th').get_text(strip=True) == 'Shots on Target':
                        dictionary_of_indexes["index_shots_on_target"] = idx + 1
                    if indexes_stats[idx].find('th').get_text(strip=True) == 'Saves':
                        dictionary_of_indexes["index_saves"] = idx + 1
                except:pass


            for key,value in dictionary_of_indexes.items():
                if key == 'index_possesion' and value != 0:
                    ball_possesions = indexes_stats[value].get_text(strip=True)
                    try:
                        hometeam_possesion =ball_possesions[:3]
                    except:hometeam_possesion= np.nan
                    try:
                        awayteam_possesion =ball_possesions[3:]
                    except:awayteam_possesion= np.nan
                    #print(hometeam_possesion,awayteam_possesion)
                elif key == 'index_shots_on_target' and value != 0:
                    try:
                        hometeam_shots_on_target_percentage =indexes_stats[value].find_all('strong')[0].get_text(strip=True)
                    except:hometeam_shots_on_target_percentage= np.nan
                    try:
                        awayteam_shots_on_target_percentage =indexes_stats[value].find_all('strong')[1].get_text(strip=True)
                    except:awayteam_shots_on_target_percentage= np.nan
                    shots_on_target_not_percentages = []
                    for testing in indexes_stats[4].find_all('div'):
                        if testing.get_text(strip=True) not in shots_on_target_not_percentages and testing.get_text(strip=True) != '':
                            shots_on_target_not_percentages.append(testing.get_text(strip=True))


                    # Initialize a list to store the extracted and replaced values
                    extracted_shots = []

                    for data in shots_on_target_not_percentages:
                        # Split the string by the em dash ('—')
                        parts = data.split('—')
                        
                        # Check if the first part contains the "of" pattern, which means it's the desired value
                        if "of" in parts[0]:
                            extracted_value = parts[0].strip()
                        elif len(parts) > 1 and "of" in parts[1]:  # Check the second part if the first doesn't contain "of"
                            extracted_value = parts[1].strip()
                        
                        # Replace ' of ' with '/' and add to the list
                        extracted_shots.append(extracted_value.replace(' of ', '/'))
                    try:
                        hometean_shots_not_percentages = extracted_shots[0]
                    except:hometean_shots_not_percentages= np.nan
                    try:
                        awayteam_shots_not_percentages = extracted_shots[1]
                    except:awayteam_shots_not_percentages= np.nan
                elif key == 'index_saves' and value != 0:
                    try:
                        hometeam_saves_percentage =indexes_stats[6].find_all('strong')[0].get_text(strip=True)
                    except:hometeam_saves_percentage= np.nan
                    try:
                        awayteam_saves_percentage =indexes_stats[6].find_all('strong')[1].get_text(strip=True)
                    except:awayteam_saves_percentage
                    saves_not_percentages = []
                    for testing in indexes_stats[6].find_all('div'):
                        if testing.get_text(strip=True) not in saves_not_percentages and testing.get_text(strip=True) != '':
                            saves_not_percentages.append(testing.get_text(strip=True))


                    # Initialize a list to store the extracted and replaced values
                    extracted_shots = []

                    for data in saves_not_percentages:
                        # Split the string by the em dash ('—')
                        parts = data.split('—')
                        
                        # Check if the first part contains the "of" pattern, which means it's the desired value
                        if "of" in parts[0]:
                            extracted_value = parts[0].strip()
                        elif len(parts) > 1 and "of" in parts[1]:  # Check the second part if the first doesn't contain "of"
                            extracted_value = parts[1].strip()
                        
                        # Replace ' of ' with '/' and add to the list
                        extracted_shots.append(extracted_value.replace(' of ', '/'))
                    try:
                        hometean_saves_not_percentages = extracted_shots[0]
                    except:hometean_saves_not_percentages= np.nan
                    try:
                        awayteam_saves_not_percentages = extracted_shots[1]
                    except:awayteam_saves_not_percentages= np.nan
        except:
            hometeam_possesion = np.nan
            awayteam_possesion = np.nan
            hometeam_shots_on_target_percentage = np.nan
            awayteam_shots_on_target_percentage = np.nan
            hometean_shots_not_percentages = np.nan
            awayteam_shots_not_percentages = np.nan
            hometeam_saves_percentage = np.nan
            awayteam_saves_not_percentages = np.nan
            hometean_saves_not_percentages = np.nan
            awayteam_saves_percentage = np.nan

        single_match_dict["hometeam_possesion"] =hometeam_possesion
        single_match_dict["awayteam_possesion"] =awayteam_possesion
        single_match_dict["hometeam_shots_on_target_percentage"] =hometeam_shots_on_target_percentage
        single_match_dict["awayteam_shots_on_target_percentage"] =awayteam_shots_on_target_percentage
        single_match_dict["hometean_shots_not_percentages"] =hometean_shots_not_percentages
        single_match_dict["awayteam_shots_not_percentages"] =awayteam_shots_not_percentages
        single_match_dict["hometeam_saves_percentage"] =hometeam_saves_percentage
        single_match_dict["awayteam_saves_not_percentages"] =awayteam_saves_not_percentages
        single_match_dict["hometean_saves_not_percentages"] =hometean_saves_not_percentages
        single_match_dict["awayteam_saves_percentage"] =awayteam_saves_percentage

        #Match_Summary
        # Find the div with id "events_wrap"
        try:
            events_wrap_div = soup_single_match.find('div', id='events_wrap')

            # Initialize a list to hold event dictionaries
            events_list = []

            # Check if the div was found
            if events_wrap_div:
                # Find all events
                events = events_wrap_div.find_all('div', class_='event')
                
                for event in events:
                    # Extract minute and score
                    try:
                        minute_div = event.find('div')
                        minute_text = minute_div.get_text(strip=True) if minute_div else 'Unknown'
                    except:minute_text= np.nan
                    
                    # Extract event details
                    try:
                        details_div = event.find_all('div')[1]
                        event_icon = details_div.find('div', class_='event_icon')
                        event_type = event_icon['class'][1] if event_icon and len(event_icon['class']) > 1 else 'Unknown'
                    except:event_type= np.nan
                    
                    # Extract player and additional info
                    try:
                        player_div = details_div.find('a')
                        player_name = player_div.get_text(strip=True) if player_div else 'Unknown'
                    except:player_name= np.nan
                    
                    # Extract additional info (e.g., assist or for substitution)
                    try:
                        additional_info = details_div.find('small')
                        additional_info_text = additional_info.get_text(strip=True) if additional_info else ''
                    except:additional_info_text= np.nan
                    
                    # Create a dictionary for each event
                    event_dict = {
                        'minute': minute_text,
                        'type': event_type,
                        'player': player_name,
                        'additional_info': additional_info_text
                    }
                    
                    # Append the event dictionary to the list
                    events_list.append(event_dict)
            else:
                print("Div with id 'events_wrap' not found")

            #events_list
            fbref_substitutions_list = []
            fbref_yellow_cards_list = []
            fbref_red_cards_list = []
            fbref_goal_list = []
            fbref_missed_penalty_list = []
            fbref_rest_events_list = []

            for event_index in range(len(events_list)):
                if events_list[event_index]["type"] == "substitute_in":
                    fbref_substitutions_list.append(events_list[event_index])
                elif  events_list[event_index]["type"] == "yellow_card":
                    fbref_yellow_cards_list.append(events_list[event_index])
                elif  events_list[event_index]["type"] == "red_card":
                    fbref_red_cards_list.append(events_list[event_index])
                elif  events_list[event_index]["type"] == "goal":
                    fbref_goal_list.append(events_list[event_index])
                elif  events_list[event_index]["type"] == "penalty_goal":
                    fbref_goal_list.append(events_list[event_index])
                elif  events_list[event_index]["type"] == "own_goal":
                    fbref_goal_list.append(events_list[event_index])
                elif  events_list[event_index]["type"] == "penalty_miss":
                    fbref_missed_penalty_list.append(events_list[event_index])
                else:
                    fbref_rest_events_list.append(events_list[event_index])

            #missed_penalties
            fbref_updated_missed_penalty_list = []
            for missed_penalty_event in fbref_missed_penalty_list:
                fbref_updated_missed_penalty_dict = dict()
                try:
                    missed_penalty_event_minute = missed_penalty_event['minute'].split('’')[0]
                except:missed_penalty_event_minute = np.nan

                try:
                    missed_penalty_event_score= missed_penalty_event['minute'].split('’')[1]
                except:missed_penalty_event_score= np.nan

                try:
                    missed_penalty_event_type = missed_penalty_event['type']
                except:missed_penalty_event_type= np.nan

                try:
                    missed_penalty_event_player  = missed_penalty_event['player']  
                except:missed_penalty_event_player= np.nan  

                try:
                    missed_penalty_event_additional_info = missed_penalty_event['additional_info']
                except:missed_penalty_event_additional_info= np.nan
            
                fbref_updated_missed_penalty_dict['minute'] =missed_penalty_event_minute
                fbref_updated_missed_penalty_dict['score'] =missed_penalty_event_score
                fbref_updated_missed_penalty_dict['type'] = missed_penalty_event_type
                fbref_updated_missed_penalty_dict['player'] = missed_penalty_event_player
                fbref_updated_missed_penalty_dict['additional_info'] =missed_penalty_event_additional_info
                fbref_updated_missed_penalty_list.append(fbref_updated_missed_penalty_dict)

            #substitutions
            fbref_updated_substitutions_list = []
            for substitution_event in fbref_substitutions_list:
                updated_subsitution_dict = dict()
                try:
                    updated_subsitution_dict_minute   = substitution_event['minute'].split('’')[0]
                except:updated_subsitution_dict_minute = np.nan

                try:
                    updated_subsitution_dict_score = substitution_event['minute'].split('’')[1]
                except:updated_subsitution_dict_score= np.nan

                try:
                    updated_subsitution_dict_type = substitution_event['type'].replace('substitute_in','substitution')
                except:updated_subsitution_dict_type= np.nan

                try:
                    updated_subsitution_dict_player_in = substitution_event['player']
                except:updated_subsitution_dict_player_in= np.nan

                try:
                    updated_subsitution_dict_player_out = substitution_event['additional_info'].replace('for', '', 1)
                except:updated_subsitution_dict_player_out= np.nan

                updated_subsitution_dict['minute'] =updated_subsitution_dict_minute
                updated_subsitution_dict['score'] = updated_subsitution_dict_score
                updated_subsitution_dict['type'] =updated_subsitution_dict_type
                updated_subsitution_dict['player_in'] = updated_subsitution_dict_player_in
                updated_subsitution_dict['player_out'] =updated_subsitution_dict_player_out
                fbref_updated_substitutions_list.append(updated_subsitution_dict)


            #goals
            fbref_updated_goal_list = []
            for goal_event in fbref_goal_list:
                fbref_updated_goal_dict = dict()
                try:
                    fbref_updated_goal_dict_minute = goal_event['minute'].split('’')[0]
                except:fbref_updated_goal_dict_minute= np.nan

                fbref_updated_goal_dict['minute'] = fbref_updated_goal_dict_minute

                try:
                    fbref_updated_goal_dict_score = goal_event['minute'].split('’')[1]
                except:fbref_updated_goal_dict_score= np.nan
                fbref_updated_goal_dict['score'] = fbref_updated_goal_dict_score

                # Handle 'type' field
                if goal_event['type'] == 'penalty_goal' or goal_event['type'] == 'own_goal':
                    fbref_updated_goal_dict['type'] = 'goal'  # Change type to 'goal'
                else:
                    fbref_updated_goal_dict['type'] = goal_event['type']
                fbref_updated_goal_dict['player'] = goal_event['player']
                fbref_updated_goal_dict['additional_info'] = goal_event['additional_info']
                if 'Assist' in fbref_updated_goal_dict['additional_info']:
                    assist_dict = dict()
                    try:
                        assist_dict_Assist = fbref_updated_goal_dict['additional_info'].split(':')[1]
                    except:assist_dict_Assist= np.nan
                    assist_dict["Assist"] = assist_dict_Assist
                    fbref_updated_goal_dict['additional_info'] = assist_dict
                fbref_updated_goal_list.append(fbref_updated_goal_dict)


            #Yellow Cards
            fbref_updated_yellow_cards_list = []
            for yellow_card_event in fbref_yellow_cards_list:
                fbref_updated_yellow_card_dict = dict()
                try:
                    fbref_updated_yellow_card_dict_minute = yellow_card_event['minute'].split('’')[0]
                except:fbref_updated_yellow_card_dict_minute = np.nan

                try:
                    fbref_updated_yellow_card_dict_score = yellow_card_event['minute'].split('’')[1]
                except:fbref_updated_yellow_card_dict_score= np.nan

                try:
                    fbref_updated_yellow_card_dict_type = yellow_card_event['type']
                except:fbref_updated_yellow_card_dict_type= np.nan

                try:
                    fbref_updated_yellow_card_dict_player = yellow_card_event['player']
                except:fbref_updated_yellow_card_dict_player= np.nan

                try:
                    fbref_updated_yellow_card_dict_additional_info = yellow_card_event['additional_info']
                except:fbref_updated_yellow_card_dict_additional_info= np.nan

                fbref_updated_yellow_card_dict['minute'] =fbref_updated_yellow_card_dict_minute
                fbref_updated_yellow_card_dict['score'] = fbref_updated_yellow_card_dict_score
                fbref_updated_yellow_card_dict['type'] = fbref_updated_yellow_card_dict_type
                fbref_updated_yellow_card_dict['player'] =fbref_updated_yellow_card_dict_player
                fbref_updated_yellow_card_dict['additional_info'] =fbref_updated_yellow_card_dict_additional_info
                fbref_updated_yellow_cards_list.append(fbref_updated_yellow_card_dict)


            #Red Cards
            fbref_updated_red_cards_list = []
            for red_card_event in fbref_red_cards_list:
                fbref_updated_red_card_dict = dict()
                try:
                    fbref_updated_red_card_dict_minute = red_card_event['minute'].split('’')[0]
                except:fbref_updated_red_card_dict_minute= np.nan

                try:
                    fbref_updated_red_card_dict_score = red_card_event['minute'].split('’')[1]
                except:fbref_updated_red_card_dict_score= np.nan

                try:
                    fbref_updated_red_card_dict_type = red_card_event['type']
                except:fbref_updated_red_card_dict_type= np.nan

                try:
                    fbref_updated_red_card_dict_player = red_card_event['player']
                except:fbref_updated_red_card_dict_player= np.nan

                try:
                    fbref_updated_red_card_dict_additional_info = red_card_event['additional_info']
                except:fbref_updated_red_card_dict_additional_info= np.nan


                fbref_updated_red_card_dict['minute'] = fbref_updated_red_card_dict_minute
                fbref_updated_red_card_dict['score'] = fbref_updated_red_card_dict_score
                fbref_updated_red_card_dict['type'] = fbref_updated_red_card_dict_type
                fbref_updated_red_card_dict['player'] =fbref_updated_red_card_dict_player
                fbref_updated_red_card_dict['additional_info'] = fbref_updated_red_card_dict_additional_info
                fbref_updated_red_cards_list.append(fbref_updated_red_card_dict)

            #fbref_rest_events_list
            fbref_updated_rest_events_list = []
            for rest_event in fbref_rest_events_list:
                fbref_updated_rest_event_dict = dict()
                try:
                    fbref_updated_rest_event_dict_minute = rest_event['minute'].split('’')[0]
                except:fbref_updated_rest_event_dict_minute= np.nan

                try:
                    fbref_updated_rest_event_dict_score = rest_event['minute'].split('’')[1]
                except:fbref_updated_rest_event_dict_score= np.nan

                try:
                    fbref_updated_rest_event_dict_type = rest_event['type']
                except:fbref_updated_rest_event_dict_type= np.nan

                try:
                    fbref_updated_rest_event_dict_player = rest_event['player']
                except:fbref_updated_rest_event_dict_player= np.nan

                try:
                    fbref_updated_rest_event_dict_additional_info = rest_event['additional_info']
                except:fbref_updated_rest_event_dict_additional_info= np.nan

                fbref_updated_rest_event_dict['minute'] = fbref_updated_rest_event_dict_minute
                fbref_updated_rest_event_dict['score'] = fbref_updated_rest_event_dict_score
                fbref_updated_rest_event_dict['type'] = fbref_updated_rest_event_dict_type
                fbref_updated_rest_event_dict['player'] = fbref_updated_rest_event_dict_player
                fbref_updated_rest_event_dict['additional_info'] = fbref_updated_rest_event_dict_additional_info
                fbref_updated_rest_events_list.append(fbref_updated_rest_event_dict)

            #print(fbref_rest_events_list)
            #print(fbref_updated_rest_events_list)
        except:
            fbref_updated_rest_events_list= np.nan
            fbref_updated_yellow_cards_list= np.nan
            fbref_updated_red_cards_list= np.nan
            fbref_updated_goal_list= np.nan
            fbref_updated_substitutions_list= np.nan
            fbref_updated_missed_penalty_list= np.nan

        single_match_dict["fbref_rest_events_list"] =fbref_updated_rest_events_list
        single_match_dict["fbref_yellow_cards_list"] =fbref_updated_yellow_cards_list
        single_match_dict["fbref_red_cards_list"] =fbref_updated_red_cards_list
        single_match_dict["fbref_goal_list"] =fbref_updated_goal_list
        single_match_dict["fbref_substitutions_list"] =fbref_updated_substitutions_list
        single_match_dict["fbref_missed_penalty_list"] =fbref_updated_missed_penalty_list

        #Lineups

        # Find all 'div' elements with class 'lineup'
        try:
            lineups = soup_single_match.find_all('div', class_='lineup')

            # Function to extract players and formation from a lineup div
            def extract_players_and_formation_from_lineup(lineup_div):
                try:
                    starting_eleven = []
                    bench = []
                    formation = None
                    current_section = None

                    # Find all 'tr' elements in the table within the div
                    rows = lineup_div.find_all('tr')
                    for row in rows:
                        # Check if the row contains section headers
                        th_tag = row.find('th')
                        if th_tag:
                            header_text = th_tag.text.strip()
                            if 'Bench' in header_text:
                                current_section = 'bench'
                            elif 'Starting XI' in header_text or 'Starting Eleven' in header_text:
                                current_section = 'starting'
                            elif '(' in header_text and ')' in header_text:
                                formation = header_text
                        else:
                            # Find the <a> tag within the row
                            a_tag = row.find('a')
                            td_tag = row.find('td')
                            if a_tag and td_tag:
                                player_name = a_tag.text
                                shirt_number = td_tag.text.strip()
                                player_dict = {"name_of_player": player_name, "shirt_number": shirt_number}
                                if current_section == 'bench':
                                    bench.append(player_dict)
                                else:
                                    starting_eleven.append(player_dict)
                except:
                    starting_eleven= np.nan
                    bench= np.nan
                    formation=np.nan
                return starting_eleven, bench, formation

            # Initialize lists and formations
            awayteam_starting_eleven = []
            awayteam_bench = []
            hometeam_starting_eleven = []
            hometeam_bench = []
            awayteam_formation = None
            hometeam_formation = None

            # Process each lineup div
            for lineup in lineups:
                # Check the team name in the header
                team_header = lineup.find('th')
                if team_header:
                    team_name = team_header.text.strip()
                    if awayteam_name in team_name:
                        awayteam_starting_eleven, awayteam_bench, awayteam_formation = extract_players_and_formation_from_lineup(lineup)
                    elif hometeam_name in team_name:
                        hometeam_starting_eleven, hometeam_bench, hometeam_formation = extract_players_and_formation_from_lineup(lineup)

        except:
            hometeam_starting_eleven= np.nan
            hometeam_bench= np.nan
            hometeam_formation= np.nan
            awayteam_starting_eleven= np.nan
            awayteam_bench= np.nan
            awayteam_formation= np.nan

        single_match_dict["hometeam_starting_eleven"] =hometeam_starting_eleven
        single_match_dict["hometeam_bench"] =hometeam_bench
        single_match_dict["hometeam_formation"] =hometeam_formation
        single_match_dict["awayteam_starting_eleven"] =awayteam_starting_eleven
        single_match_dict["awayteam_bench"] =awayteam_bench
        single_match_dict["awayteam_formation"] =awayteam_formation


        print(missing_url_list[match_rpt_idx])
        #print(single_match_dict)
        if single_match_dict in missing_match_reports_single_season:
            continue
        else:
            missing_match_reports_single_season.append(single_match_dict)

    missing_match_reports_df = pd.DataFrame(missing_match_reports_single_season)
    return missing_match_reports_df

