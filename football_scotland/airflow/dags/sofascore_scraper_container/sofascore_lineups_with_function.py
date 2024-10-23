import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd


def lineups_each_game(game_id_param):
    dict_lineups_each_game = dict()
    try:
        
        url_lineups_first = "https://www.sofascore.com/api/v1/event/"
        url_lineups_second = "/lineups"
        url_lineups = url_lineups_first + str(game_id_param) + url_lineups_second

        home_players_list = []
        away_players_list = []

        for repeat_index in range(11):

            payload = {}
            headers = {
        'authority' : 'www.sofascore.com' ,
        'accept': '*/*' ,
        'accept-language': 'el-GR,el;q=0.9,de;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0' ,
        'cookie': '_gcl_au=1.1.468311363.1720620111; _ga=GA1.1.1629986250.1720620112; FCCDCF=^%^5Bnull^%^2Cnull^%^2Cnull^%^2C^%^5B^%^22CQBihYAQBihYAEsACBELA7EoAP_gAEPgAA6II3gB5C5ETSFBYH51KIsEYAEHwAAAIsAgAAYBAQABQBKQAIQCAGAAEAhAhCACgAAAIEYBIAEACAAQAAAAAAAAIAAEIAAQAAAIICAAAAAAAABIAAAIAAAAEAAAwCAABAAA0AgEAJIISNgAAAAAAAAAAgAAAAAAAgAAAEhAAAEIAAAAACgAEABAEAAAAAEIABBII3gB5C5ETSFBYHhVIIMEIAERQAAAIsAgAAQBAQAAQBKQAIQCEGAAAAgAACAAAAAAIEQBIAEAAAgAAAAAAAAAIAAEAAAAAAAIICAAAAAAAABAAAAIAAAAAAAAwCAABAAAwQhEAJIASFgAAAAgAAAAAoAAAAAAAgAAAEhAAAEAAAAAAAAAEAAAEAAAAAAAABBIAAA.dnAACAgAAAA^%^22^%^2C^%^222~70.89.108.149.211.313.358.415.486.540.621.981.1029.1046.1092.1097.1126.1205.1301.1516.1558.1584.1598.1651.1697.1716.1753.1810.1832.1985.2328.2373.2440.2571.2572.2575.2577.2628.2642.2677.2767.2860.2878.2887.2922.3182.3190.3234.3290.3292.3331.10631~dv.^%^22^%^2C^%^22E40555D6-D565-42CE-B57C-E02328DFD472^%^22^%^5D^%^5D; _lr_env_src_ats=false; __browsiUID=c7d29faa-32b0-47db-a158-4d28e107c355; __browsiSessionID=a4edb7f0-6070-4294-817d-a8f24a0d4eb3&true&DEFAULT&de&desktop-4.27.14&false; _lr_retry_request=true; gcid_first=44a36dfc-59b5-4ba3-8419-33357b14d1a6; __gads=ID=fac686349d767848:T=1720620117:RT=1723643439:S=ALNI_MaAoHojfBDt-T66REpp95zwlnIY6Q; __gpi=UID=00000e7926227a4d:T=1720620117:RT=1723643439:S=ALNI_MbrL9MbKb6RX_evmqbuDVyhf0MtuA; __eoi=ID=1e9dbcf311fbbba4:T=1720620117:RT=1723643439:S=AA-AfjbwF8cU5e-qVkxB3YzNcPEW; FCNEC=^%^5B^%^5B^%^22AKsRol92IvRXOG1mdcPWrU1ldMu0qEvlp2ZNzgZR2f4rbOBdrPcxVTNAHSSS3WDoQGmuYWCRQyT_0-TNJWbFz4663mYo_hwVCr8r-RvxQ4DJINUINEi6F0iQtmtj4GA5TZRPMU6e45NLXcbGJr3TCQkMdtP8T1S5JA^%^3D^%^3D^%^22^%^5D^%^5D; _ga_QH2YGS7BB4=GS1.1.1723629578.22.1.1723643644.0.0.0; _ga_3KF4XTPHC4=GS1.1.1723629578.22.1.1723643644.59.0.0; _ga_HNQ9P9MGZR=GS1.1.1723629582.11.1.1723643659.44.0.0^',
        'if-none-match': 'W/^\^"3d5f1e62a2^\^"^',
        'priority': 'u=1, i',
        'referer': 'https://www.sofascore.com/football/match/atletico-madrid-inter/XdbsLgb',
        'sec-ch-ua': '^\^"Not)A;Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"127^\^", ^\^"Chromium^\^";v=^\^"127^\^"^',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '^\^"Windows^\^"^',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'x-requested-with': '8c2739'}
            

            response = requests.request("GET" , url_lineups , headers=headers , data = payload)
            lineups_api = json.loads(response.text)

            try:
                home_formation = lineups_api["home"]["formation"]
            except:home_formation = None

            #print(home_formation)

            try:
                away_formation = lineups_api["away"]["formation"]
            except:away_formation = None



            #all_players_of_hometeam   
            for player_home in  lineups_api["home"]["players"]:
                dict_single_home_player = dict()

                try:
                    player_name_home = player_home["player"]["name"]
                except:player_name_home = None
                
                try:
                    player_slug_home = player_home["player"]["slug"]
                except:player_slug_home=None


                try:
                    player_position_home = player_home["player"]["position"]
                except:player_position_home=None
                

                try:
                    if len(player_home["statistics"]) != 0:
                        player_has_played_home = 1
                        player_rating_home = player_home["statistics"]["ratingVersions"]["original"]
                    else:
                        player_has_played_home = 0
                        player_rating_home = None
                except:
                        player_has_played_home = None
                        player_rating_home = None


                
                
                try:
                    player_id_home = player_home["player"]["id"]
                except:player_id_home=None


                try:
                    player_country_alpha_two_home = player_home["player"]["country"]["alpha2"]
                except:player_country_alpha_two_home=None


                try:
                    player_country_home= player_home["player"]["country"]["name"]
                except:player_country_home =None


                
                #for dictionary
                dict_single_home_player["player_name"] = player_name_home
                dict_single_home_player["player_slug"] = player_slug_home
                dict_single_home_player["player_position"] = player_position_home
                dict_single_home_player["player_has_played"] = player_has_played_home
                dict_single_home_player["player_rating"] = player_rating_home
                dict_single_home_player["player_id"] = player_id_home
                dict_single_home_player["player_country_alpha_two"] = player_country_alpha_two_home
                dict_single_home_player["player_country"] = player_country_home

                if dict_single_home_player not in home_players_list:
                    home_players_list.append(dict_single_home_player)

            #all_players_of_away_team
        
            for player_away in  lineups_api["away"]["players"]:
                dict_single_away_player = dict()

                try:
                    player_name_away = player_away["player"]["name"]
                except:player_name_away = None
                
                try:
                    player_slug_away = player_away["player"]["slug"]
                except:player_slug_away=None


                try:
                    player_position_away = player_away["player"]["position"]
                except:player_position_away=None
                

                try:
                    if len(player_away["statistics"]) != 0:
                        player_has_played_away = 1
                        player_rating_away = player_away["statistics"]["ratingVersions"]["original"]
                    else:
                        player_has_played_away = 0
                        player_rating_away = None
                except:
                        player_has_played_away = None
                        player_rating_away = None


                
                
                try:
                    player_id_away = player_away["player"]["id"]
                except:player_id_away=None


                try:
                    player_country_alpha_two_away = player_away["player"]["country"]["alpha2"]
                except:player_country_alpha_two_away=None


                try:
                    player_country_away= player_away["player"]["country"]["name"]
                except:player_country_away =None


                
                #for dictionary
                dict_single_away_player["player_name"] = player_name_away
                dict_single_away_player["player_slug"] = player_slug_away
                dict_single_away_player["player_position"] = player_position_away
                dict_single_away_player["player_has_played"] = player_has_played_away
                dict_single_away_player["player_rating"] = player_rating_away
                dict_single_away_player["player_id"] = player_id_away
                dict_single_away_player["player_country_alpha_two"] = player_country_alpha_two_away
                dict_single_away_player["player_country"] = player_country_away

                if dict_single_away_player not in away_players_list:
                    away_players_list.append(dict_single_away_player)
    except:
        home_formation = None
        away_formation = None
        home_players_list = None
        away_players_list = None

    dict_lineups_each_game["home_formation"] = home_formation
    dict_lineups_each_game["away_formation"] = away_formation
    dict_lineups_each_game["home_players_list"] = home_players_list
    dict_lineups_each_game["away_players_list"] =away_players_list 
    return dict_lineups_each_game
