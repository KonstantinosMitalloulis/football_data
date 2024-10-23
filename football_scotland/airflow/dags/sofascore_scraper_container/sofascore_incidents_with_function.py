import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd


def incidents_game_each_game(game_id_param):
    dict_incidents_each_game = dict()
    periods = None
    homescore_ht= None
    awayscore_ht= None
    homescore_ft= None
    awayscore_ft= None
    total_goals_ht= None
    total_goals_ft= None
    extra_time= None
    penalties= None
    incident_type_card= None
    incident_type_goal= None
    incident_type_substitution= None
    incident_type_period = None 
    incidents = None

    try:
        url_incidents_first = "https://www.sofascore.com/api/v1/event/"
        url_incidents_second = "/incidents"
        url_incidents = url_incidents_first + str(game_id_param) + url_incidents_second

        payload = {}
        headers = {
        'authority' : 'www.sofascore.com' ,
        'accept' : '*/*' ,
        'accept-language': 'el-GR,el;q=0.9,de;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': '_gcl_au=1.1.468311363.1720620111; _ga=GA1.1.1629986250.1720620112; FCCDCF=^%^5Bnull^%^2Cnull^%^2Cnull^%^2C^%^5B^%^22CQBihYAQBihYAEsACBELA7EoAP_gAEPgAA6II3gB5C5ETSFBYH51KIsEYAEHwAAAIsAgAAYBAQABQBKQAIQCAGAAEAhAhCACgAAAIEYBIAEACAAQAAAAAAAAIAAEIAAQAAAIICAAAAAAAABIAAAIAAAAEAAAwCAABAAA0AgEAJIISNgAAAAAAAAAAgAAAAAAAgAAAEhAAAEIAAAAACgAEABAEAAAAAEIABBII3gB5C5ETSFBYHhVIIMEIAERQAAAIsAgAAQBAQAAQBKQAIQCEGAAAAgAACAAAAAAIEQBIAEAAAgAAAAAAAAAIAAEAAAAAAAIICAAAAAAAABAAAAIAAAAAAAAwCAABAAAwQhEAJIASFgAAAAgAAAAAoAAAAAAAgAAAEhAAAEAAAAAAAAAEAAAEAAAAAAAABBIAAA.dnAACAgAAAA^%^22^%^2C^%^222~70.89.108.149.211.313.358.415.486.540.621.981.1029.1046.1092.1097.1126.1205.1301.1516.1558.1584.1598.1651.1697.1716.1753.1810.1832.1985.2328.2373.2440.2571.2572.2575.2577.2628.2642.2677.2767.2860.2878.2887.2922.3182.3190.3234.3290.3292.3331.10631~dv.^%^22^%^2C^%^22E40555D6-D565-42CE-B57C-E02328DFD472^%^22^%^5D^%^5D; _lr_env_src_ats=false; __browsiUID=c7d29faa-32b0-47db-a158-4d28e107c355; __browsiSessionID=a4edb7f0-6070-4294-817d-a8f24a0d4eb3&true&DEFAULT&de&desktop-4.27.14&false; _lr_retry_request=true; gcid_first=c31343d7-de2c-44b8-96db-c156c29ee6c8; __gads=ID=fac686349d767848:T=1720620117:RT=1723661411:S=ALNI_MaAoHojfBDt-T66REpp95zwlnIY6Q; __gpi=UID=00000e7926227a4d:T=1720620117:RT=1723661411:S=ALNI_MbrL9MbKb6RX_evmqbuDVyhf0MtuA; __eoi=ID=1e9dbcf311fbbba4:T=1720620117:RT=1723661411:S=AA-AfjbwF8cU5e-qVkxB3YzNcPEW; FCNEC=^%^5B^%^5B^%^22AKsRol9wcdUyoZOp-8qQnVnAQKZlTlfEh-Tb445XMqzsR8JJ9TIRwwBKKJfeS8oC3agjE6BjgR3yf1dbABzPOLfPnyNv-ytT80Dvz6AlODMC0rviTn0VQXZLBcinbh8BHIHxxqnMbGItzCQBDnqtSIVPqb58bdTzRw^%^3D^%^3D^%^22^%^5D^%^5D; _ga_3KF4XTPHC4=GS1.1.1723629578.22.1.1723661522.20.0.0; _ga_QH2YGS7BB4=GS1.1.1723629578.22.1.1723661522.0.0.0; _ga_HNQ9P9MGZR=GS1.1.1723629582.11.1.1723661522.20.0.0^',
        'if-none-match': 'W/^\^"d6fa5bc240^\^"^' ,
        'priority': 'u=1, i',
        'referer': 'https://www.sofascore.com/football/match/spain-france/GObsYTb' ,
        'sec-ch-ua': '^\^"Not)A;Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"127^\^", ^\^"Chromium^\^";v=^\^"127^\^"^" ',
        'sec-ch-ua-mobile': '?0' ,
        'sec-ch-ua-platform': '^\^"Windows^\^"^" ',
        'sec-fetch-dest': 'empty' ,
        'sec-fetch-mode': 'cors' ,
        'sec-fetch-site': 'same-origin' ,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' ,
        'x-requested-with': '6af25f' }

        response = requests.request("GET" , url_incidents , headers=headers , data = payload)
        incidents_api = json.loads(response.text)
        incidents = incidents_api["incidents"]
        incidents.reverse()

        for i in range(len(incidents)):
            try:
                if incidents[i]["text"] == 'HT':
                    time_kriterium = i
            except:pass

        for fact_idx in range(len(incidents)):
            fact_rank = dict()
            fact_rank["rank"] = str(fact_idx) 
            incidents[fact_idx].update(fact_rank)

        for fact_categorize_idx in range(len(incidents)):
            fact_categorize_rank = dict()
            if int(incidents[fact_categorize_idx]["rank"]) < time_kriterium:
                fact_categorize_rank["time_part"] = "first_half"
            else:
                fact_categorize_rank["time_part"] = "second_half"
            incidents[fact_categorize_idx].update(fact_categorize_rank)

        # Sleep for 1.5 seconds
        #time.sleep(1.5)


        incident_type_period = []
        initial_incident_type_substitution = []
        incident_type_goal = []
        incident_type_injurytime = []
        incident_type_card = []



        for single_incident in incidents:
            incident = dict()
            if single_incident["incidentType"] == "period":
                incident_type_period.append(single_incident)



            if single_incident["incidentType"] == "substitution":
                initial_incident_type_substitution.append(single_incident)


        #Goals, Assists,time ok,time_part ok
            if single_incident["incidentType"] == "goal":
                try:
                    incident["scorer_name"] = single_incident["player"]["name"]
                except:  incident["name"] = None
                try:
                    incident["scorer_name_slug"] = single_incident["player"]["slug"]
                except:  incident["scorer_name_slug"] = None

                try:
                    incident["scorer_name_shortname"] = single_incident["player"]["shortName"]
                except:  incident["scorer_name_shortname"] = None

                try:
                    incident["scorer_name_id"] = single_incident["player"]["id"]
                except:  incident["scorer_name_id"] = None

                try:
                    incident["assist_player_name"] = single_incident["assist1"]["name"]
                except:  incident["assist_player_name"] = None
                
                try:
                    incident["assist_player_name_slug"] = single_incident["assist1"]["slug"]
                except:  incident["assist_player_name_slug"] = None
                
                try:
                    incident["assist_player_name_shortName"] = single_incident["assist1"]["shortName"]
                except:  incident["assist_player_name_shortName"] = None

                try:
                    incident["assist_player_id"] = single_incident["assist1"]["id"]
                except:  incident["assist_player_id"] = None       
                
                try:
                    incident["homeScore_after_goal"] = single_incident["homeScore"]
                except:  incident["homeScore_after_goal"] = None
                try:
                    incident["awayScore_after_goal"] = single_incident["awayScore"]
                except:  incident["awayScore_after_goal"] = None
                try:
                    incident["time"] = single_incident["time"]
                except:  incident["time"] = None
                try:
                    incident["time_part"] = single_incident["time_part"]
                except:  incident["time_part"] = None
                incident_type_goal.append(incident)

        #Injuries
            if single_incident["incidentType"] == "injuryTime":
                incident_type_injurytime.append(single_incident)

        #Cards,time ok,time part ok
            if single_incident["incidentType"] == "card":
                try:
                    incident["card_player_name"] = single_incident["player"]["name"]
                except:  incident["card_player_name"] = None
                try:
                    incident["card_player_name_slug"] = single_incident["player"]["slug"]
                except:  incident["card_player_name_slug"] = None
                try:
                    incident["card_player_name_shortName"] = single_incident["player"]["shortName"]
                except:  incident["card_player_name_shortName"] = None
                
                try:
                    incident["card_player_id"] = single_incident["player"]["id"]
                except:  incident["card_player_id"] = None

                try:
                    incident["card_reason"] = single_incident["reason"]
                except:  incident["card_reason"] = None
                try:
                    incident["card_colour"] = single_incident["incidentClass"]
                except:  incident["card_colour"] = None
                try:
                    incident["time"] = single_incident["time"]
                except:  incident["time"] = None
                try:
                    incident["time_part"] = single_incident["time_part"]
                except:  incident["time_part"] = None

                incident_type_card.append(incident)






        #Substitutions,time ok,time_part ok 
        incident_type_substitution = []
        for player in initial_incident_type_substitution:
            player_dict_substitutions= dict()
            player_in = dict()
            player_out = dict()
            try:
                player_in["playerIn_name"] = player["playerIn"]["name"]
            except:player_in["playerIn_name"] = None
            try:
                player_in["playerIn_name_slug"] = player["playerIn"]["slug"]
            except:player_in["playerIn_name_slug"] = None
            try:
                player_in["playerIn_name_shortname"] = player["playerIn"]["shortName"]
            except:player_in["playerIn_name_shortname"] = None
            try:
                player_in["playerIn_player_id"] = player["playerIn"]["id"]
            except:player_in["playerIn_player_id"] = None


            try:
                player_out["playerOut_name"]=player["playerOut"]["name"]
            except:player_out["playerOut_name"] = None
            try:
                player_out["playerOut_name_slug"]=player["playerOut"]["slug"]
            except:player_out["playerOut_name_slug"] = None
            try:
                player_out["playerOut_name_shortname"]=player["playerOut"]["shortName"]
            except:player_out["playerOut_name_shortname"] = None
            try:
                player_out["playerOut_player_id"]=player["playerOut"]["id"]
            except:player_out["playerOut_player_id"] = None
            try:
                time_sub= player["time"]
            except:  time_sub = None
            try:
                time_sub_part= player["time_part"]
            except:  time_sub_part = None


            player_dict_substitutions["in"]=player_in
            player_dict_substitutions["out"]=player_out
            player_dict_substitutions["time"] = time_sub
            player_dict_substitutions["time_part"] = time_sub_part
            incident_type_substitution.append(player_dict_substitutions)



        #Scores,time ok
        extra_time = False
        penalties = False
        for single_imixrono in incident_type_period:
            if 'HT' in single_imixrono.values():
                homescore_ht = single_imixrono["homeScore"]
                awayscore_ht = single_imixrono["awayScore"]
            if 'FT' in single_imixrono.values():
                homescore_ft = single_imixrono["homeScore"]
                awayscore_ft = single_imixrono["awayScore"]
            if 'ET' in  single_imixrono.values():
                extra_time = True
            if 'PEN' in  single_imixrono.values():
                penalties = True


        periods = []

        for period in incident_type_period:
            periods.append(period["text"])
            
        total_goals_ht = int(homescore_ht) + int(awayscore_ht)
        total_goals_ft = int(homescore_ft) + int(awayscore_ft)

    except:pass
        #periods = None
        #homescore_ht= None
        #awayscore_ht= None
        #homescore_ft= None
        #awayscore_ft= None
        #total_goals_ht= None
        #total_goals_ft= None
        #extra_time= None
        #penalties= None
        #incident_type_card= None
        #incident_type_goal= None
        #incident_type_substitution= None
        #incident_type_period = None 
        #incidents = None


    dict_incidents_each_game["periods_of_match"] = periods
    dict_incidents_each_game["homescore_ht"] = homescore_ht
    dict_incidents_each_game["awayscore_ht"] = awayscore_ht
    dict_incidents_each_game["homescore_ft"] = homescore_ft
    dict_incidents_each_game["awayscore_ft"] = awayscore_ft
    dict_incidents_each_game["total_goals_ht"] = total_goals_ht
    dict_incidents_each_game["total_goals_ft"] = total_goals_ft
    dict_incidents_each_game["extra_time"] = extra_time
    dict_incidents_each_game["penalties"] = penalties
    dict_incidents_each_game["incident_type_card"] = incident_type_card
    dict_incidents_each_game["incident_type_goal"] = incident_type_goal
    dict_incidents_each_game["incident_type_substitution"] = incident_type_substitution
    dict_incidents_each_game["incident_type_period"] = incident_type_period
    dict_incidents_each_game["incidents"] = incidents
    return dict_incidents_each_game
