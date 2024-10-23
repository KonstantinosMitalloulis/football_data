import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date, timedelta
import time

def statistics_each_game(game_id_param):
    dict_statistics_each_game = dict()
    try:
        url_statistics_first = "https://www.sofascore.com/api/v1/event/"
        url_statistics_second = "/statistics"
        url_statistics = url_statistics_first + str(game_id_param) + url_statistics_second

        #print(game_link)
        #print(url_statistics)
        #print(for_referer)
        payload = {}
        headers = {
        'authority' : 'www.sofascore.com' ,
        'accept' : '*/*' ,
        'accept-language': 'el-GR,el;q=0.9,de;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': '_gcl_au=1.1.468311363.1720620111; _ga=GA1.1.1629986250.1720620112; FCCDCF=^%^5Bnull^%^2Cnull^%^2Cnull^%^2C^%^5B^%^22CQBihYAQBihYAEsACBELA7EoAP_gAEPgAA6II3gB5C5ETSFBYH51KIsEYAEHwAAAIsAgAAYBAQABQBKQAIQCAGAAEAhAhCACgAAAIEYBIAEACAAQAAAAAAAAIAAEIAAQAAAIICAAAAAAAABIAAAIAAAAEAAAwCAABAAA0AgEAJIISNgAAAAAAAAAAgAAAAAAAgAAAEhAAAEIAAAAACgAEABAEAAAAAEIABBII3gB5C5ETSFBYHhVIIMEIAERQAAAIsAgAAQBAQAAQBKQAIQCEGAAAAgAACAAAAAAIEQBIAEAAAgAAAAAAAAAIAAEAAAAAAAIICAAAAAAAABAAAAIAAAAAAAAwCAABAAAwQhEAJIASFgAAAAgAAAAAoAAAAAAAgAAAEhAAAEAAAAAAAAAEAAAEAAAAAAAABBIAAA.dnAACAgAAAA^%^22^%^2C^%^222~70.89.108.149.211.313.358.415.486.540.621.981.1029.1046.1092.1097.1126.1205.1301.1516.1558.1584.1598.1651.1697.1716.1753.1810.1832.1985.2328.2373.2440.2571.2572.2575.2577.2628.2642.2677.2767.2860.2878.2887.2922.3182.3190.3234.3290.3292.3331.10631~dv.^%^22^%^2C^%^22E40555D6-D565-42CE-B57C-E02328DFD472^%^22^%^5D^%^5D; _lr_env_src_ats=false; __browsiUID=c7d29faa-32b0-47db-a158-4d28e107c355; _lr_retry_request=true; __browsiSessionID=181b30b4-e355-41ee-b63d-f19c474c3a7b&true&DEFAULT&de&desktop-4.27.14&false; __gads=ID=fac686349d767848:T=1720620117:RT=1723629581:S=ALNI_MaAoHojfBDt-T66REpp95zwlnIY6Q; __gpi=UID=00000e7926227a4d:T=1720620117:RT=1723629581:S=ALNI_MbrL9MbKb6RX_evmqbuDVyhf0MtuA; __eoi=ID=1e9dbcf311fbbba4:T=1720620117:RT=1723629581:S=AA-AfjbwF8cU5e-qVkxB3YzNcPEW; gcid_first=381b90a9-f5c4-4271-8340-ee61cf67e631; _ga_QH2YGS7BB4=GS1.1.1723629578.22.0.1723629582.0.0.0; _ga_3KF4XTPHC4=GS1.1.1723629578.22.0.1723629582.56.0.0; FCNEC=^%^5B^%^5B^%^22AKsRol8jISeuAILq7hgtu2WEFS8yDqwo93FcEbaEsPWpmZ8etA-AXdI99JTZuwclpgrDEXeRok8Tx0A7aCvqrP-_GJiVHUWS3hOeqFhpHn62WVuNXZ4XkKsmSMWwOiucLZQq6k-nfGtB_25zKQ6zwpiWiyvLHfQfWA^%^3D^%^3D^%^22^%^5D^%^5D; _ga_HNQ9P9MGZR=GS1.1.1723629582.11.0.1723629584.58.0.0^',
        'if-none-match': 'W/^\^"108a00ed97^\^"^' ,
        'priority': 'u=1, i',
        'referer': 'https://www.sofascore.com/football/match/spain-france/GObsYTb',
        'sec-ch-ua': '^\^"Not)A;Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"127^\^", ^\^"Chromium^\^";v=^\^"127^\^"^" ',
        'sec-ch-ua-mobile': '?0' ,
        'sec-ch-ua-platform': '^\^"Windows^\^"^" ',
        'sec-fetch-dest': 'empty' ,
        'sec-fetch-mode': 'cors' ,
        'sec-fetch-site': 'same-origin' ,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' ,
        'x-requested-with': '81f213' }

        response = requests.request("GET" , url_statistics , headers=headers , data = payload)
        statistics_api = json.loads(response.text)
        #dict_each_game = dict()

        all_home_ball_possession = None
        all_away_ball_possession = None
        all_home_expected_goals = None
        all_away_expected_goals = None
        all_home_big_chances = None
        all_away_big_chances= None
        all_home_total_shots= None
        all_away_total_shots= None
        all_home_goalkeeper_saves= None
        all_away_goalkeeper_saves= None
        all_home_corner_kicks= None
        all_away_corner_kicks= None
        all_home_fouls= None
        all_away_fouls= None
        all_home_passes= None
        all_away_passes= None
        all_home_tackles= None
        all_away_tackles= None
        all_home_free_kicks= None
        all_away_free_kicks= None
        all_home_yellow_cards= None
        all_away_yellow_cards= None
        all_home_total_shots= None
        all_away_total_shots= None
        all_home_shots_on_target= None
        all_away_shots_on_target= None
        all_home_hit_woodwork= None
        all_away_hit_woodwork= None
        all_home_shots_off_target= None
        all_away_shots_off_target= None
        all_home_blocked_shots= None
        all_away_blocked_shots= None
        all_home_shots_inside_box= None
        all_away_shots_inside_box= None
        all_home_shots_outside_box= None
        all_away_shots_outside_box= None
        all_home_big_chances_scored= None
        all_away_big_chances_scored= None
        all_home_big_chances_missed= None
        all_away_big_chances_missed= None
        all_home_through_balls= None
        all_away_through_balls= None
        all_home_fouled_in_final_third= None
        all_away_fouled_in_final_third= None
        all_home_offsides= None
        all_away_offsides= None
        all_home_accurate_passes= None
        all_away_accurate_passes= None
        all_home_throw_ins= None
        all_away_throw_ins= None
        all_home_final_third_entries= None
        all_away_final_third_entries= None
        all_home_long_balls= None
        all_away_long_balls= None
        all_home_crosses= None
        all_away_crosses= None
        all_home_duels= None
        all_away_duels= None
        all_home_dispossessed= None
        all_away_dispossessed= None
        all_home_ground_duels= None
        all_away_ground_duels= None
        all_home_aerial_duels= None
        all_away_aerial_duels= None
        all_home_dribbles= None
        all_away_dribbles= None
        all_home_tackles_won= None
        all_away_tackles_won= None
        all_home_total_tackles= None
        all_away_total_tackles= None
        all_home_interceptions= None
        all_away_interceptions= None
        all_home_recoveries= None
        all_away_recoveries= None
        all_home_clearances= None
        all_away_clearances= None
        all_home_total_saves= None
        all_away_total_saves= None
        all_home_goals_prevented= None
        all_away_goals_prevented= None
        all_home_goal_kicks= None
        all_away_goal_kicks= None
        #first_half
        first_half_home_ball_possession= None
        first_half_away_ball_possession= None
        first_half_home_expected_goals= None
        first_half_away_expected_goals= None
        first_half_home_big_chances= None
        first_half_away_big_chances= None
        first_half_home_total_shots= None
        first_half_away_total_shots= None
        first_half_home_goalkeeper_saves= None
        first_half_away_goalkeeper_saves= None
        first_half_home_corner_kicks= None
        first_half_away_corner_kicks= None
        first_half_home_fouls= None
        first_half_away_fouls= None
        first_half_home_passes= None
        first_half_away_passes= None
        first_half_home_tackles= None
        first_half_away_tackles= None
        first_half_home_free_kicks= None
        first_half_away_free_kicks= None
        first_half_home_yellow_cards= None
        first_half_away_yellow_cards= None
        first_half_home_total_shots= None
        first_half_away_total_shots= None
        first_half_home_shots_on_target= None
        first_half_away_shots_on_target= None
        first_half_home_hit_woodwork= None
        first_half_away_hit_woodwork= None
        first_half_home_shots_off_target= None
        first_half_away_shots_off_target= None
        first_half_home_blocked_shots= None
        first_half_away_blocked_shots= None
        first_half_home_shots_inside_box= None
        first_half_away_shots_inside_box= None
        first_half_home_shots_outside_box= None
        first_half_away_shots_outside_box= None
        first_half_home_big_chances_scored= None
        first_half_away_big_chances_scored= None
        first_half_home_big_chances_missed= None
        first_half_away_big_chances_missed= None
        first_half_home_through_balls= None
        first_half_away_through_balls= None
        first_half_home_fouled_in_final_third= None
        first_half_away_fouled_in_final_third= None
        first_half_home_offsides= None
        first_half_away_offsides= None
        first_half_home_accurate_passes= None
        first_half_away_accurate_passes= None
        first_half_home_throw_ins= None
        first_half_away_throw_ins= None
        first_half_home_final_third_entries= None
        first_half_away_final_third_entries= None
        first_half_home_long_balls= None
        first_half_away_long_balls= None
        first_half_home_crosses= None
        first_half_away_crosses= None
        first_half_home_duels= None
        first_half_away_duels= None
        first_half_home_dispossessed= None
        first_half_away_dispossessed= None
        first_half_home_ground_duels= None
        first_half_away_ground_duels= None
        first_half_home_aerial_duels= None
        first_half_away_aerial_duels= None
        first_half_home_dribbles= None
        first_half_away_dribbles= None
        first_half_home_tackles_won= None
        first_half_away_tackles_won= None
        first_half_home_total_tackles= None
        first_half_away_total_tackles= None
        first_half_home_interceptions= None
        first_half_away_interceptions= None
        first_half_home_recoveries= None
        first_half_away_recoveries= None
        first_half_home_clearances= None
        first_half_away_clearances= None
        first_half_home_total_saves= None
        first_half_away_total_saves= None
        first_half_home_goals_prevented= None
        first_half_away_goals_prevented= None
        first_half_home_goal_kicks= None
        first_half_away_goal_kicks= None
        #second half
        second_half_home_ball_possession= None
        second_half_away_ball_possession= None
        second_half_home_expected_goals= None
        second_half_away_expected_goals= None
        second_half_home_big_chances= None
        second_half_away_big_chances= None
        second_half_home_total_shots= None
        second_half_away_total_shots= None
        second_half_home_goalkeeper_saves= None
        second_half_away_goalkeeper_saves= None
        second_half_home_corner_kicks= None
        second_half_away_corner_kicks= None
        second_half_home_fouls= None
        second_half_away_fouls= None
        second_half_home_passes= None
        second_half_away_passes= None
        second_half_home_tackles= None
        second_half_away_tackles= None
        second_half_home_free_kicks= None
        second_half_away_free_kicks= None
        second_half_home_yellow_cards= None
        second_half_away_yellow_cards= None
        second_half_home_total_shots= None
        second_half_away_total_shots= None
        second_half_home_shots_on_target= None
        second_half_away_shots_on_target= None
        second_half_home_hit_woodwork= None
        second_half_away_hit_woodwork= None
        second_half_home_shots_off_target= None
        second_half_away_shots_off_target= None
        second_half_home_blocked_shots= None
        second_half_away_blocked_shots= None
        second_half_home_shots_inside_box= None
        second_half_away_shots_inside_box= None
        second_half_home_shots_outside_box= None
        second_half_away_shots_outside_box= None
        second_half_home_big_chances_scored= None
        second_half_away_big_chances_scored= None
        second_half_home_big_chances_missed= None
        second_half_away_big_chances_missed= None
        second_half_home_through_balls= None
        second_half_away_through_balls= None
        second_half_home_fouled_in_final_third= None
        second_half_away_fouled_in_final_third= None
        second_half_home_offsides= None
        second_half_away_offsides= None
        second_half_home_accurate_passes= None
        second_half_away_accurate_passes= None
        second_half_home_throw_ins= None
        second_half_away_throw_ins= None
        second_half_home_final_third_entries= None
        second_half_away_final_third_entries= None
        second_half_home_long_balls= None
        second_half_away_long_balls= None
        second_half_home_crosses= None
        second_half_away_crosses= None
        second_half_home_duels= None
        second_half_away_duels= None
        second_half_home_dispossessed= None
        second_half_away_dispossessed= None
        second_half_home_ground_duels= None
        second_half_away_ground_duels= None
        second_half_home_aerial_duels= None
        second_half_away_aerial_duels= None
        second_half_home_dribbles= None
        second_half_away_dribbles= None
        second_half_home_tackles_won= None
        second_half_away_tackles_won= None
        second_half_home_total_tackles= None
        second_half_away_total_tackles= None
        second_half_home_interceptions= None
        second_half_away_interceptions= None
        second_half_home_recoveries= None
        second_half_away_recoveries= None
        second_half_home_clearances= None
        second_half_away_clearances= None
        second_half_home_total_saves= None
        second_half_away_total_saves= None
        second_half_home_goals_prevented= None
        second_half_away_goals_prevented= None
        second_half_home_goal_kicks= None
        second_half_away_goal_kicks = None

        for period_index in statistics_api['statistics']:#
            yoyo = period_index["groups"][2]['statisticsItems']
            if period_index['period'] == 'ALL':
                #Match_overview
                for merkmal_ball_possession in period_index["groups"][0]['statisticsItems']:
                    if merkmal_ball_possession["name"] == "Ball possession":
                        all_home_ball_possession = merkmal_ball_possession['home']
                        all_away_ball_possession = merkmal_ball_possession['away']
                        break
                    else:
                        all_home_ball_possession = None
                        all_away_ball_possession = None

                for merkmal_expected_goals in period_index["groups"][0]['statisticsItems']:
                    if merkmal_expected_goals["name"] == "Expected goals":
                        all_home_expected_goals = merkmal_expected_goals['home']
                        all_away_expected_goals = merkmal_expected_goals['away']
                        break
                    else:
                        all_home_expected_goals = None
                        all_away_expected_goals = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Big chances":
                        all_home_big_chances = merkmal_match_overview['home']
                        all_away_big_chances = merkmal_match_overview['away']
                        break
                    else:
                        all_home_big_chances = None
                        all_away_big_chances = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Total shots":
                        all_home_total_shots = merkmal_match_overview['home']
                        all_away_total_shots = merkmal_match_overview['away']
                        break
                    else:
                        all_home_total_shots = None
                        all_away_total_shots = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Goalkeeper saves":
                        all_home_goalkeeper_saves = merkmal_match_overview['home']
                        all_away_goalkeeper_saves = merkmal_match_overview['away']
                        break
                    else:
                        all_home_goalkeeper_saves = None
                        all_away_goalkeeper_saves = None
            
                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Corner kicks":
                        all_home_corner_kicks = merkmal_match_overview['home']
                        all_away_corner_kicks = merkmal_match_overview['away']
                        break
                    else:
                        all_home_corner_kicks = None
                        all_away_corner_kicks = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Fouls":
                        all_home_fouls = merkmal_match_overview['home']
                        all_away_fouls = merkmal_match_overview['away']
                        break
                    else:
                        all_home_fouls = None
                        all_away_fouls = None
                    

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Passes":
                        all_home_passes = merkmal_match_overview['home']
                        all_away_passes = merkmal_match_overview['away']
                        break
                    else:
                        all_home_passes = None
                        all_away_passes = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Tackles":
                        all_home_tackles = merkmal_match_overview['home']
                        all_away_tackles = merkmal_match_overview['away']
                        break
                    else:
                        all_home_tackles = None
                        all_away_tackles = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Free kicks":
                        all_home_free_kicks = merkmal_match_overview['home']
                        all_away_free_kicks = merkmal_match_overview['away']
                        break
                    else:
                        all_home_free_kicks = None
                        all_away_free_kicks = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Yellow cards":
                        all_home_yellow_cards = merkmal_match_overview['home']
                        all_away_yellow_cards = merkmal_match_overview['away']
                        break
                    else:
                        all_home_yellow_cards = None
                        all_away_yellow_cards = None



                    #Shots
                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Total shots":
                        all_home_total_shots = merkmal_match_overview['home']
                        all_away_total_shots = merkmal_match_overview['away']
                        break
                    else:
                        all_home_total_shots = None
                        all_away_total_shots = None

                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Shots on target":
                        all_home_shots_on_target = merkmal_match_overview['home']
                        all_away_shots_on_target = merkmal_match_overview['away']
                        break
                    else:
                        all_home_shots_on_target = None
                        all_away_shots_on_target = None


                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Hit woodwork":
                        all_home_hit_woodwork = merkmal_match_overview['home']
                        all_away_hit_woodwork = merkmal_match_overview['away']
                        break
                    else:
                        all_home_hit_woodwork = None
                        all_away_hit_woodwork = None

                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Shots off target":
                        all_home_shots_off_target = merkmal_match_overview['home']
                        all_away_shots_off_target = merkmal_match_overview['away']
                        break
                    else:
                        all_home_shots_off_target = None
                        all_away_shots_off_target = None

                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Blocked shots":
                        all_home_blocked_shots = merkmal_match_overview['home']
                        all_away_blocked_shots = merkmal_match_overview['away']
                        break
                    else:
                        all_home_blocked_shots = None
                        all_away_blocked_shots = None

                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Shots inside box":
                        all_home_shots_inside_box = merkmal_match_overview['home']
                        all_away_shots_inside_box = merkmal_match_overview['away']
                        break
                    else:
                        all_home_shots_inside_box = None
                        all_away_shots_inside_box = None

                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Shots outside box":
                        all_home_shots_outside_box = merkmal_match_overview['home']
                        all_away_shots_outside_box = merkmal_match_overview['away']
                        break
                    else:
                        all_home_shots_outside_box = None
                        all_away_shots_outside_box = None


                    #Attack
                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == "Big chances scored":
                            all_home_big_chances_scored = merkmal['home']
                            all_away_big_chances_scored = merkmal['away']
                            break
                        else:
                            all_home_big_chances_scored = None
                            all_away_big_chances_scored = None

                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == "Big chances missed":
                            all_home_big_chances_missed = merkmal['home']
                            all_away_big_chances_missed = merkmal['away']
                            break
                        else:
                            all_home_big_chances_missed = None
                            all_away_big_chances_missed = None

                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == 'Through balls':
                            all_home_through_balls = merkmal['home']
                            all_away_through_balls = merkmal['away']
                            break
                        else:
                            all_home_through_balls = None
                            all_away_through_balls = None

                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == 'Touches in penalty area':
                            all_home_touches_in_penalty_area = merkmal['home']
                            all_away_touches_in_penalty_area = merkmal['away']
                            break
                        else:
                            all_home_touches_in_penalty_area = None
                            all_away_touches_in_penalty_area = None

                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == 'Fouled in final third':
                            all_home_fouled_in_final_third = merkmal['home']
                            all_away_fouled_in_final_third = merkmal['away']
                            break
                        else:
                            all_home_fouled_in_final_third = None
                            all_away_fouled_in_final_third = None


                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == 'Offsides':
                            all_home_offsides = merkmal['home']
                            all_away_offsides = merkmal['away']
                            break
                        else:
                            all_home_offsides = None
                            all_away_offsides = None


                    #Passes

                    for merkmal in period_index["groups"][3]['statisticsItems']:
                        if merkmal["name"] == 'Accurate passes':
                            all_home_accurate_passes = merkmal['home']
                            all_away_accurate_passes = merkmal['away']
                            break
                        else:
                            all_home_accurate_passes = None
                            all_away_accurate_passes = None

                    for merkmal in period_index["groups"][3]['statisticsItems']:
                        if merkmal["name"] == 'Throw-ins':
                            all_home_throw_ins = merkmal['home']
                            all_away_throw_ins = merkmal['away']
                            break
                        else:
                            all_home_throw_ins = None
                            all_away_throw_ins = None  

                    for merkmal in period_index["groups"][3]['statisticsItems']:
                        if merkmal["name"] == 'Final third entries':
                            all_home_final_third_entries = merkmal['home']
                            all_away_final_third_entries = merkmal['away']
                            break
                        else:
                            all_home_final_third_entries = None
                            all_away_final_third_entries = None

                    for merkmal in period_index["groups"][3]['statisticsItems']:
                        if merkmal["name"] == 'Long balls':
                            all_home_long_balls = merkmal['home']
                            all_away_long_balls = merkmal['away']
                            break
                        else:
                            all_home_long_balls = None
                            all_away_long_balls = None      

                    for merkmal in period_index["groups"][3]['statisticsItems']:
                        if merkmal["name"] == 'Crosses':
                            all_home_crosses = merkmal['home']
                            all_away_crosses = merkmal['away']
                            break
                        else:
                            all_home_crosses = None
                            all_away_crosses = None                   



                    #Duels
                    for merkmal in period_index["groups"][4]['statisticsItems']:
                        if merkmal["name"] == 'Duels':
                            all_home_duels = merkmal['home']
                            all_away_duels = merkmal['away']
                            break
                        else:
                            all_home_duels = None
                            all_away_duels = None    

                    for merkmal in period_index["groups"][4]['statisticsItems']:
                        if merkmal["name"] == 'Dispossessed':
                            all_home_dispossessed = merkmal['home']
                            all_away_dispossessed = merkmal['away']
                            break
                        else:
                            all_home_dispossessed = None
                            all_away_dispossessed = None    


                    for merkmal in period_index["groups"][4]['statisticsItems']:
                        if merkmal["name"] == 'Ground duels':
                            all_home_ground_duels = merkmal['home']
                            all_away_ground_duels = merkmal['away']
                            break
                        else:
                            all_home_ground_duels = None
                            all_away_ground_duels = None    


                    for merkmal in period_index["groups"][4]['statisticsItems']:
                        if merkmal["name"] == 'Aerial duels':
                            all_home_aerial_duels = merkmal['home']
                            all_away_aerial_duels = merkmal['away']
                            break
                        else:
                            all_home_aerial_duels = None
                            all_away_aerial_duels = None    

                    for merkmal in period_index["groups"][4]['statisticsItems']:
                        if merkmal["name"] == 'Dribbles':
                            all_home_dribbles = merkmal['home']
                            all_away_dribbles = merkmal['away']
                            break
                        else:
                            all_home_dribbles = None
                            all_away_dribbles = None    


                    #Defendung
                    for merkmal in period_index["groups"][5]['statisticsItems']:
                        if merkmal["name"] == 'Tackles won':
                            all_home_tackles_won = merkmal['home']
                            all_away_tackles_won = merkmal['away']
                            break
                        else:
                            all_home_tackles_won = None
                            all_away_tackles_won = None   

                    for merkmal in period_index["groups"][5]['statisticsItems']:
                        if merkmal["name"] == 'Total tackles':
                            all_home_total_tackles = merkmal['home']
                            all_away_total_tackles = merkmal['away']
                            break
                        else:
                            all_home_total_tackles = None
                            all_away_total_tackles = None   

                    for merkmal in period_index["groups"][5]['statisticsItems']:
                        if merkmal["name"] == 'Interceptions':
                            all_home_interceptions = merkmal['home']
                            all_away_interceptions = merkmal['away']
                            break
                        else:
                            all_home_interceptions = None
                            all_away_interceptions = None   


                    for merkmal in period_index["groups"][5]['statisticsItems']:
                        if merkmal["name"] == 'Recoveries':
                            all_home_recoveries = merkmal['home']
                            all_away_recoveries = merkmal['away']
                            break
                        else:
                            all_home_recoveries = None
                            all_away_recoveries = None   


                    for merkmal in period_index["groups"][5]['statisticsItems']:
                        if merkmal["name"] == 'Clearances':
                            all_home_clearances = merkmal['home']
                            all_away_clearances = merkmal['away']
                            break
                        else:
                            all_home_clearances = None
                            all_away_clearances = None   

                    #Goalkeeping
                    for merkmal in period_index["groups"][6]['statisticsItems']:
                        if merkmal["name"] == 'Goalkeeper saves':
                            all_home_total_saves = merkmal['home']
                            all_away_total_saves = merkmal['away']
                            break
                        else:
                            all_home_total_saves = None
                            all_away_total_saves = None 

                    for merkmal in period_index["groups"][6]['statisticsItems']:
                        if merkmal["name"] == 'Goals prevented':
                            all_home_goals_prevented = merkmal['home']
                            all_away_goals_prevented = merkmal['away']
                            break
                        else:
                            all_home_goals_prevented = None
                            all_away_goals_prevented = None 

                    for merkmal in period_index["groups"][6]['statisticsItems']:
                        if merkmal["name"] == 'Goal kicks':
                            all_home_goal_kicks = merkmal['home']
                            all_away_goal_kicks = merkmal['away']
                            break
                        else:
                            all_home_goal_kicks = None
                            all_away_goal_kicks = None 






            elif period_index['period'] == "1ST" :
                #Match_overview
                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Ball possession":
                        first_half_home_ball_possession = merkmal_match_overview['home']
                        first_half_away_ball_possession = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_ball_possession = None
                        first_half_away_ball_possession = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Expected goals":
                        first_half_home_expected_goals = merkmal_match_overview['home']
                        first_half_away_expected_goals = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_expected_goals = None
                        first_half_away_expected_goals = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Big chances":
                        first_half_home_big_chances = merkmal_match_overview['home']
                        first_half_away_big_chances = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_big_chances = None
                        first_half_away_big_chances = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Total shots":
                        first_half_home_total_shots = merkmal_match_overview['home']
                        first_half_away_total_shots = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_total_shots = None
                        first_half_away_total_shots = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Goalkeeper saves":
                        first_half_home_goalkeeper_saves = merkmal_match_overview['home']
                        first_half_away_goalkeeper_saves = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_goalkeeper_saves = None
                        first_half_away_goalkeeper_saves = None
            
                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Corner kicks":
                        first_half_home_corner_kicks = merkmal_match_overview['home']
                        first_half_away_corner_kicks = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_corner_kicks = None
                        first_half_away_corner_kicks = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Fouls":
                        first_half_home_fouls = merkmal_match_overview['home']
                        first_half_away_fouls = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_fouls = None
                        first_half_away_fouls = None
                    

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Passes":
                        first_half_home_passes = merkmal_match_overview['home']
                        first_half_away_passes = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_passes = None
                        first_half_away_passes = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Tackles":
                        first_half_home_tackles = merkmal_match_overview['home']
                        first_half_away_tackles = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_tackles = None
                        first_half_away_tackles = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Free kicks":
                        first_half_home_free_kicks = merkmal_match_overview['home']
                        first_half_away_free_kicks = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_free_kicks = None
                        first_half_away_free_kicks = None

                for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Yellow cards":
                        first_half_home_yellow_cards = merkmal_match_overview['home']
                        first_half_away_yellow_cards = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_yellow_cards = None
                        first_half_away_yellow_cards = None



                    #Shots
                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Total shots":
                        first_half_home_total_shots = merkmal_match_overview['home']
                        first_half_away_total_shots = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_total_shots = None
                        first_half_away_total_shots = None

                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Shots on target":
                        first_half_home_shots_on_target = merkmal_match_overview['home']
                        first_half_away_shots_on_target = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_shots_on_target = None
                        first_half_away_shots_on_target = None


                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Hit woodwork":
                        first_half_home_hit_woodwork = merkmal_match_overview['home']
                        first_half_away_hit_woodwork = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_hit_woodwork = None
                        first_half_away_hit_woodwork = None

                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Shots off target":
                        first_half_home_shots_off_target = merkmal_match_overview['home']
                        first_half_away_shots_off_target = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_shots_off_target = None
                        first_half_away_shots_off_target = None

                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Blocked shots":
                        first_half_home_blocked_shots = merkmal_match_overview['home']
                        first_half_away_blocked_shots = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_blocked_shots = None
                        first_half_away_blocked_shots = None

                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Shots inside box":
                        first_half_home_shots_inside_box = merkmal_match_overview['home']
                        first_half_away_shots_inside_box = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_shots_inside_box = None
                        first_half_away_shots_inside_box = None

                for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                    if merkmal_match_overview["name"] == "Shots outside box":
                        first_half_home_shots_outside_box = merkmal_match_overview['home']
                        first_half_away_shots_outside_box = merkmal_match_overview['away']
                        break
                    else:
                        first_half_home_shots_outside_box = None
                        first_half_away_shots_outside_box = None


                    #Attack
                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == "Big chances scored":
                            first_half_home_big_chances_scored = merkmal['home']
                            first_half_away_big_chances_scored = merkmal['away']
                            break
                        else:
                            first_half_home_big_chances_scored = None
                            first_half_away_big_chances_scored = None

                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == "Big chances missed":
                            first_half_home_big_chances_missed = merkmal['home']
                            first_half_away_big_chances_missed = merkmal['away']
                            break
                        else:
                            first_half_home_big_chances_missed = None
                            first_half_away_big_chances_missed = None

                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == 'Through balls':
                            first_half_home_through_balls = merkmal['home']
                            first_half_away_through_balls = merkmal['away']
                            break
                        else:
                            first_half_home_through_balls = None
                            first_half_away_through_balls = None

                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == 'Touches in penalty area':
                            first_half_home_touches_in_penalty_area = merkmal['home']
                            first_half_away_touches_in_penalty_area = merkmal['away']
                            break
                        else:
                            first_half_home_touches_in_penalty_area = None
                            first_half_away_touches_in_penalty_area = None

                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == 'Fouled in final third':
                            first_half_home_fouled_in_final_third = merkmal['home']
                            first_half_away_fouled_in_final_third = merkmal['away']
                            break
                        else:
                            first_half_home_fouled_in_final_third = None
                            first_half_away_fouled_in_final_third = None


                    for merkmal in period_index["groups"][2]['statisticsItems']:
                        if merkmal["name"] == 'Offsides':
                            first_half_home_offsides = merkmal['home']
                            first_half_away_offsides = merkmal['away']
                            break
                        else:
                            first_half_home_offsides = None
                            first_half_away_offsides = None


                    #Passes

                    for merkmal in period_index["groups"][3]['statisticsItems']:
                        if merkmal["name"] == 'Accurate passes':
                            first_half_home_accurate_passes = merkmal['home']
                            first_half_away_accurate_passes = merkmal['away']
                            break
                        else:
                            first_half_home_accurate_passes = None
                            first_half_away_accurate_passes = None

                    for merkmal in period_index["groups"][3]['statisticsItems']:
                        if merkmal["name"] == 'Throw-ins':
                            first_half_home_throw_ins = merkmal['home']
                            first_half_away_throw_ins = merkmal['away']
                            break
                        else:
                            first_half_home_throw_ins = None
                            first_half_away_throw_ins = None  

                    for merkmal in period_index["groups"][3]['statisticsItems']:
                        if merkmal["name"] == 'Final third entries':
                            first_half_home_final_third_entries = merkmal['home']
                            first_half_away_final_third_entries = merkmal['away']
                            break
                        else:
                            first_half_home_final_third_entries = None
                            first_half_away_final_third_entries = None

                    for merkmal in period_index["groups"][3]['statisticsItems']:
                        if merkmal["name"] == 'Long balls':
                            first_half_home_long_balls = merkmal['home']
                            first_half_away_long_balls = merkmal['away']
                            break
                        else:
                            first_half_home_long_balls = None
                            first_half_away_long_balls = None      

                    for merkmal in period_index["groups"][3]['statisticsItems']:
                        if merkmal["name"] == 'Crosses':
                            first_half_home_crosses = merkmal['home']
                            first_half_away_crosses = merkmal['away']
                            break
                        else:
                            first_half_home_crosses = None
                            first_half_away_crosses = None                   



                    #Duels
                    for merkmal in period_index["groups"][4]['statisticsItems']:
                        if merkmal["name"] == 'Duels':
                            first_half_home_duels = merkmal['home']
                            first_half_away_duels = merkmal['away']
                            break
                        else:
                            first_half_home_duels = None
                            first_half_away_duels = None    

                    for merkmal in period_index["groups"][4]['statisticsItems']:
                        if merkmal["name"] == 'Dispossessed':
                            first_half_home_dispossessed = merkmal['home']
                            first_half_away_dispossessed = merkmal['away']
                            break
                        else:
                            first_half_home_dispossessed = None
                            first_half_away_dispossessed = None    


                    for merkmal in period_index["groups"][4]['statisticsItems']:
                        if merkmal["name"] == 'Ground duels':
                            first_half_home_ground_duels = merkmal['home']
                            first_half_away_ground_duels = merkmal['away']
                            break
                        else:
                            first_half_home_ground_duels = None
                            first_half_away_ground_duels = None    


                    for merkmal in period_index["groups"][4]['statisticsItems']:
                        if merkmal["name"] == 'Aerial duels':
                            first_half_home_aerial_duels = merkmal['home']
                            first_half_away_aerial_duels = merkmal['away']
                            break
                        else:
                            first_half_home_aerial_duels = None
                            first_half_away_aerial_duels = None    

                    for merkmal in period_index["groups"][4]['statisticsItems']:
                        if merkmal["name"] == 'Dribbles':
                            first_half_home_dribbles = merkmal['home']
                            first_half_away_dribbles = merkmal['away']
                            break
                        else:
                            first_half_home_dribbles = None
                            first_half_away_dribbles = None    


                    #Defendung
                    for merkmal in period_index["groups"][5]['statisticsItems']:
                        if merkmal["name"] == 'Tackles won':
                            first_half_home_tackles_won = merkmal['home']
                            first_half_away_tackles_won = merkmal['away']
                            break
                        else:
                            first_half_home_tackles_won = None
                            first_half_away_tackles_won = None   

                    for merkmal in period_index["groups"][5]['statisticsItems']:
                        if merkmal["name"] == 'Total tackles':
                            first_half_home_total_tackles = merkmal['home']
                            first_half_away_total_tackles = merkmal['away']
                            break
                        else:
                            first_half_home_total_tackles = None
                            first_half_away_total_tackles = None   

                    for merkmal in period_index["groups"][5]['statisticsItems']:
                        if merkmal["name"] == 'Interceptions':
                            first_half_home_interceptions = merkmal['home']
                            first_half_away_interceptions = merkmal['away']
                            break
                        else:
                            first_half_home_interceptions = None
                            first_half_away_interceptions = None   


                    for merkmal in period_index["groups"][5]['statisticsItems']:
                        if merkmal["name"] == 'Recoveries':
                            first_half_home_recoveries = merkmal['home']
                            first_half_away_recoveries = merkmal['away']
                            break
                        else:
                            first_half_home_recoveries = None
                            first_half_away_recoveries = None   


                    for merkmal in period_index["groups"][5]['statisticsItems']:
                        if merkmal["name"] == 'Clearances':
                            first_half_home_clearances = merkmal['home']
                            first_half_away_clearances = merkmal['away']
                            break
                        else:
                            first_half_home_clearances = None
                            first_half_away_clearances = None   

                    #Goalkeeping
                    for merkmal in period_index["groups"][6]['statisticsItems']:
                        if merkmal["name"] == 'Goalkeeper saves':
                            first_half_home_total_saves = merkmal['home']
                            first_half_away_total_saves = merkmal['away']
                            break
                        else:
                            first_half_home_total_saves = None
                            first_half_away_total_saves = None 

                    for merkmal in period_index["groups"][6]['statisticsItems']:
                        if merkmal["name"] == 'Goals prevented':
                            first_half_home_goals_prevented = merkmal['home']
                            first_half_away_goals_prevented = merkmal['away']
                            break
                        else:
                            first_half_home_goals_prevented = None
                            first_half_away_goals_prevented = None 

                    for merkmal in period_index["groups"][6]['statisticsItems']:
                        if merkmal["name"] == 'Goal kicks':
                            first_half_home_goal_kicks = merkmal['home']
                            first_half_away_goal_kicks = merkmal['away']
                            break
                        else:
                            first_half_home_goal_kicks = None
                            first_half_away_goal_kicks = None 

            elif period_index['period'] == "2ND" :
                #Match_overview
                    for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Ball possession":
                            second_half_home_ball_possession = merkmal_match_overview['home']
                            second_half_away_ball_possession = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_ball_possession = None
                            second_half_away_ball_possession = None

                    for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Expected goals":
                            second_half_home_expected_goals = merkmal_match_overview['home']
                            second_half_away_expected_goals = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_expected_goals = None
                            second_half_away_expected_goals = None

                    for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Big chances":
                            second_half_home_big_chances = merkmal_match_overview['home']
                            second_half_away_big_chances = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_big_chances = None
                            second_half_away_big_chances = None

                    for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Total shots":
                            second_half_home_total_shots = merkmal_match_overview['home']
                            second_half_away_total_shots = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_total_shots = None
                            second_half_away_total_shots = None

                    for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Goalkeeper saves":
                            second_half_home_goalkeeper_saves = merkmal_match_overview['home']
                            second_half_away_goalkeeper_saves = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_goalkeeper_saves = None
                            second_half_away_goalkeeper_saves = None
                
                    for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Corner kicks":
                            second_half_home_corner_kicks = merkmal_match_overview['home']
                            second_half_away_corner_kicks = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_corner_kicks = None
                            second_half_away_corner_kicks = None

                    for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Fouls":
                            second_half_home_fouls = merkmal_match_overview['home']
                            second_half_away_fouls = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_fouls = None
                            second_half_away_fouls = None
                        

                    for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Passes":
                            second_half_home_passes = merkmal_match_overview['home']
                            second_half_away_passes = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_passes = None
                            second_half_away_passes = None

                    for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Tackles":
                            second_half_home_tackles = merkmal_match_overview['home']
                            second_half_away_tackles = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_tackles = None
                            second_half_away_tackles = None

                    for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Free kicks":
                            second_half_home_free_kicks = merkmal_match_overview['home']
                            second_half_away_free_kicks = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_free_kicks = None
                            second_half_away_free_kicks = None

                    for merkmal_match_overview in period_index["groups"][0]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Yellow cards":
                            second_half_home_yellow_cards = merkmal_match_overview['home']
                            second_half_away_yellow_cards = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_yellow_cards = None
                            second_half_away_yellow_cards = None



                        #Shots
                    for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Total shots":
                            second_half_home_total_shots = merkmal_match_overview['home']
                            second_half_away_total_shots = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_total_shots = None
                            second_half_away_total_shots = None

                    for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Shots on target":
                            second_half_home_shots_on_target = merkmal_match_overview['home']
                            second_half_away_shots_on_target = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_shots_on_target = None
                            second_half_away_shots_on_target = None


                    for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Hit woodwork":
                            second_half_home_hit_woodwork = merkmal_match_overview['home']
                            second_half_away_hit_woodwork = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_hit_woodwork = None
                            second_half_away_hit_woodwork = None

                    for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Shots off target":
                            second_half_home_shots_off_target = merkmal_match_overview['home']
                            second_half_away_shots_off_target = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_shots_off_target = None
                            second_half_away_shots_off_target = None

                    for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Blocked shots":
                            second_half_home_blocked_shots = merkmal_match_overview['home']
                            second_half_away_blocked_shots = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_blocked_shots = None
                            second_half_away_blocked_shots = None

                    for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Shots inside box":
                            second_half_home_shots_inside_box = merkmal_match_overview['home']
                            second_half_away_shots_inside_box = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_shots_inside_box = None
                            second_half_away_shots_inside_box = None

                    for merkmal_match_overview in period_index["groups"][1]['statisticsItems']:
                        if merkmal_match_overview["name"] == "Shots outside box":
                            second_half_home_shots_outside_box = merkmal_match_overview['home']
                            second_half_away_shots_outside_box = merkmal_match_overview['away']
                            break
                        else:
                            second_half_home_shots_outside_box = None
                            second_half_away_shots_outside_box = None


                        #Attack
                        for merkmal in period_index["groups"][2]['statisticsItems']:
                            if merkmal["name"] == "Big chances scored":
                                second_half_home_big_chances_scored = merkmal['home']
                                second_half_away_big_chances_scored = merkmal['away']
                                break
                            else:
                                second_half_home_big_chances_scored = None
                                second_half_away_big_chances_scored = None

                        for merkmal in period_index["groups"][2]['statisticsItems']:
                            if merkmal["name"] == "Big chances missed":
                                second_half_home_big_chances_missed = merkmal['home']
                                second_half_away_big_chances_missed = merkmal['away']
                                break
                            else:
                                second_half_home_big_chances_missed = None
                                second_half_away_big_chances_missed = None

                        for merkmal in period_index["groups"][2]['statisticsItems']:
                            if merkmal["name"] == 'Through balls':
                                second_half_home_through_balls = merkmal['home']
                                second_half_away_through_balls = merkmal['away']
                                break
                            else:
                                second_half_home_through_balls = None
                                second_half_away_through_balls = None

                        for merkmal in period_index["groups"][2]['statisticsItems']:
                            if merkmal["name"] == 'Touches in penalty area':
                                second_half_home_touches_in_penalty_area = merkmal['home']
                                second_half_away_touches_in_penalty_area = merkmal['away']
                                break
                            else:
                                second_half_home_touches_in_penalty_area = None
                                second_half_away_touches_in_penalty_area = None

                        for merkmal in period_index["groups"][2]['statisticsItems']:
                            if merkmal["name"] == 'Fouled in final third':
                                second_half_home_fouled_in_final_third = merkmal['home']
                                second_half_away_fouled_in_final_third = merkmal['away']
                                break
                            else:
                                second_half_home_fouled_in_final_third = None
                                second_half_away_fouled_in_final_third = None


                        for merkmal in period_index["groups"][2]['statisticsItems']:
                            if merkmal["name"] == 'Offsides':
                                second_half_home_offsides = merkmal['home']
                                second_half_away_offsides = merkmal['away']
                                break
                            else:
                                second_half_home_offsides = None
                                second_half_away_offsides = None


                        #Passes

                        for merkmal in period_index["groups"][3]['statisticsItems']:
                            if merkmal["name"] == 'Accurate passes':
                                second_half_home_accurate_passes = merkmal['home']
                                second_half_away_accurate_passes = merkmal['away']
                                break
                            else:
                                second_half_home_accurate_passes = None
                                second_half_away_accurate_passes = None

                        for merkmal in period_index["groups"][3]['statisticsItems']:
                            if merkmal["name"] == 'Throw-ins':
                                second_half_home_throw_ins = merkmal['home']
                                second_half_away_throw_ins = merkmal['away']
                                break
                            else:
                                second_half_home_throw_ins = None
                                second_half_away_throw_ins = None  

                        for merkmal in period_index["groups"][3]['statisticsItems']:
                            if merkmal["name"] == 'Final third entries':
                                second_half_home_final_third_entries = merkmal['home']
                                second_half_away_final_third_entries = merkmal['away']
                                break
                            else:
                                second_half_home_final_third_entries = None
                                second_half_away_final_third_entries = None

                        for merkmal in period_index["groups"][3]['statisticsItems']:
                            if merkmal["name"] == 'Long balls':
                                second_half_home_long_balls = merkmal['home']
                                second_half_away_long_balls = merkmal['away']
                                break
                            else:
                                second_half_home_long_balls = None
                                second_half_away_long_balls = None      

                        for merkmal in period_index["groups"][3]['statisticsItems']:
                            if merkmal["name"] == 'Crosses':
                                second_half_home_crosses = merkmal['home']
                                second_half_away_crosses = merkmal['away']
                                break
                            else:
                                second_half_home_crosses = None
                                second_half_away_crosses = None                   



                        #Duels
                        for merkmal in period_index["groups"][4]['statisticsItems']:
                            if merkmal["name"] == 'Duels':
                                second_half_home_duels = merkmal['home']
                                second_half_away_duels = merkmal['away']
                                break
                            else:
                                second_half_home_duels = None
                                second_half_away_duels = None    

                        for merkmal in period_index["groups"][4]['statisticsItems']:
                            if merkmal["name"] == 'Dispossessed':
                                second_half_home_dispossessed = merkmal['home']
                                second_half_away_dispossessed = merkmal['away']
                                break
                            else:
                                second_half_home_dispossessed = None
                                second_half_away_dispossessed = None    


                        for merkmal in period_index["groups"][4]['statisticsItems']:
                            if merkmal["name"] == 'Ground duels':
                                second_half_home_ground_duels = merkmal['home']
                                second_half_away_ground_duels = merkmal['away']
                                break
                            else:
                                second_half_home_ground_duels = None
                                second_half_away_ground_duels = None    


                        for merkmal in period_index["groups"][4]['statisticsItems']:
                            if merkmal["name"] == 'Aerial duels':
                                second_half_home_aerial_duels = merkmal['home']
                                second_half_away_aerial_duels = merkmal['away']
                                break
                            else:
                                second_half_home_aerial_duels = None
                                second_half_away_aerial_duels = None    

                        for merkmal in period_index["groups"][4]['statisticsItems']:
                            if merkmal["name"] == 'Dribbles':
                                second_half_home_dribbles = merkmal['home']
                                second_half_away_dribbles = merkmal['away']
                                break
                            else:
                                second_half_home_dribbles = None
                                second_half_away_dribbles = None    


                        #Defendung
                        for merkmal in period_index["groups"][5]['statisticsItems']:
                            if merkmal["name"] == 'Tackles won':
                                second_half_home_tackles_won = merkmal['home']
                                second_half_away_tackles_won = merkmal['away']
                                break
                            else:
                                second_half_home_tackles_won = None
                                second_half_away_tackles_won = None   

                        for merkmal in period_index["groups"][5]['statisticsItems']:
                            if merkmal["name"] == 'Total tackles':
                                second_half_home_total_tackles = merkmal['home']
                                second_half_away_total_tackles = merkmal['away']
                                break
                            else:
                                second_half_home_total_tackles = None
                                second_half_away_total_tackles = None   

                        for merkmal in period_index["groups"][5]['statisticsItems']:
                            if merkmal["name"] == 'Interceptions':
                                second_half_home_interceptions = merkmal['home']
                                second_half_away_interceptions = merkmal['away']
                                break
                            else:
                                second_half_home_interceptions = None
                                second_half_away_interceptions = None   


                        for merkmal in period_index["groups"][5]['statisticsItems']:
                            if merkmal["name"] == 'Recoveries':
                                second_half_home_recoveries = merkmal['home']
                                second_half_away_recoveries = merkmal['away']
                                break
                            else:
                                second_half_home_recoveries = None
                                second_half_away_recoveries = None   


                        for merkmal in period_index["groups"][5]['statisticsItems']:
                            if merkmal["name"] == 'Clearances':
                                second_half_home_clearances = merkmal['home']
                                second_half_away_clearances = merkmal['away']
                                break
                            else:
                                second_half_home_clearances = None
                                second_half_away_clearances = None   

                        #Goalkeeping
                        for merkmal in period_index["groups"][6]['statisticsItems']:
                            if merkmal["name"] == 'Goalkeeper saves':
                                second_half_home_total_saves = merkmal['home']
                                second_half_away_total_saves = merkmal['away']
                                break
                            else:
                                second_half_home_total_saves = None
                                second_half_away_total_saves = None 

                        for merkmal in period_index["groups"][6]['statisticsItems']:
                            if merkmal["name"] == 'Goals prevented':
                                second_half_home_goals_prevented = merkmal['home']
                                second_half_away_goals_prevented = merkmal['away']
                                break
                            else:
                                second_half_home_goals_prevented = None
                                second_half_away_goals_prevented = None 

                        for merkmal in period_index["groups"][6]['statisticsItems']:
                            if merkmal["name"] == 'Goal kicks':
                                second_half_home_goal_kicksme_goal_kicks = merkmal['home']
                                second_half_away_goal_kicks = merkmal['away']
                                break
                            else:
                                second_half_home_goal_kicks = None
                                second_half_away_goal_kicks = None



    except:
        all_home_ball_possession = None
        all_away_ball_possession = None
        all_home_expected_goals = None
        all_away_expected_goals = None
        all_home_big_chances = None
        all_away_big_chances= None
        all_home_total_shots= None
        all_away_total_shots= None
        all_home_goalkeeper_saves= None
        all_away_goalkeeper_saves= None
        all_home_corner_kicks= None
        all_away_corner_kicks= None
        all_home_fouls= None
        all_away_fouls= None
        all_home_passes= None
        all_away_passes= None
        all_home_tackles= None
        all_away_tackles= None
        all_home_free_kicks= None
        all_away_free_kicks= None
        all_home_yellow_cards= None
        all_away_yellow_cards= None
        all_home_total_shots= None
        all_away_total_shots= None
        all_home_shots_on_target= None
        all_away_shots_on_target= None
        all_home_hit_woodwork= None
        all_away_hit_woodwork= None
        all_home_shots_off_target= None
        all_away_shots_off_target= None
        all_home_blocked_shots= None
        all_away_blocked_shots= None
        all_home_shots_inside_box= None
        all_away_shots_inside_box= None
        all_home_shots_outside_box= None
        all_away_shots_outside_box= None
        all_home_big_chances_scored= None
        all_away_big_chances_scored= None
        all_home_big_chances_missed= None
        all_away_big_chances_missed= None
        all_home_through_balls= None
        all_away_through_balls= None
        all_home_fouled_in_final_third= None
        all_away_fouled_in_final_third= None
        all_home_offsides= None
        all_away_offsides= None
        all_home_accurate_passes= None
        all_away_accurate_passes= None
        all_home_throw_ins= None
        all_away_throw_ins= None
        all_home_final_third_entries= None
        all_away_final_third_entries= None
        all_home_long_balls= None
        all_away_long_balls= None
        all_home_crosses= None
        all_away_crosses= None
        all_home_duels= None
        all_away_duels= None
        all_home_dispossessed= None
        all_away_dispossessed= None
        all_home_ground_duels= None
        all_away_ground_duels= None
        all_home_aerial_duels= None
        all_away_aerial_duels= None
        all_home_dribbles= None
        all_away_dribbles= None
        all_home_tackles_won= None
        all_away_tackles_won= None
        all_home_total_tackles= None
        all_away_total_tackles= None
        all_home_interceptions= None
        all_away_interceptions= None
        all_home_recoveries= None
        all_away_recoveries= None
        all_home_clearances= None
        all_away_clearances= None
        all_home_total_saves= None
        all_away_total_saves= None
        all_home_goals_prevented= None
        all_away_goals_prevented= None
        all_home_goal_kicks= None
        all_away_goal_kicks= None
        #first_half
        first_half_home_ball_possession= None
        first_half_away_ball_possession= None
        first_half_home_expected_goals= None
        first_half_away_expected_goals= None
        first_half_home_big_chances= None
        first_half_away_big_chances= None
        first_half_home_total_shots= None
        first_half_away_total_shots= None
        first_half_home_goalkeeper_saves= None
        first_half_away_goalkeeper_saves= None
        first_half_home_corner_kicks= None
        first_half_away_corner_kicks= None
        first_half_home_fouls= None
        first_half_away_fouls= None
        first_half_home_passes= None
        first_half_away_passes= None
        first_half_home_tackles= None
        first_half_away_tackles= None
        first_half_home_free_kicks= None
        first_half_away_free_kicks= None
        first_half_home_yellow_cards= None
        first_half_away_yellow_cards= None
        first_half_home_total_shots= None
        first_half_away_total_shots= None
        first_half_home_shots_on_target= None
        first_half_away_shots_on_target= None
        first_half_home_hit_woodwork= None
        first_half_away_hit_woodwork= None
        first_half_home_shots_off_target= None
        first_half_away_shots_off_target= None
        first_half_home_blocked_shots= None
        first_half_away_blocked_shots= None
        first_half_home_shots_inside_box= None
        first_half_away_shots_inside_box= None
        first_half_home_shots_outside_box= None
        first_half_away_shots_outside_box= None
        first_half_home_big_chances_scored= None
        first_half_away_big_chances_scored= None
        first_half_home_big_chances_missed= None
        first_half_away_big_chances_missed= None
        first_half_home_through_balls= None
        first_half_away_through_balls= None
        first_half_home_fouled_in_final_third= None
        first_half_away_fouled_in_final_third= None
        first_half_home_offsides= None
        first_half_away_offsides= None
        first_half_home_accurate_passes= None
        first_half_away_accurate_passes= None
        first_half_home_throw_ins= None
        first_half_away_throw_ins= None
        first_half_home_final_third_entries= None
        first_half_away_final_third_entries= None
        first_half_home_long_balls= None
        first_half_away_long_balls= None
        first_half_home_crosses= None
        first_half_away_crosses= None
        first_half_home_duels= None
        first_half_away_duels= None
        first_half_home_dispossessed= None
        first_half_away_dispossessed= None
        first_half_home_ground_duels= None
        first_half_away_ground_duels= None
        first_half_home_aerial_duels= None
        first_half_away_aerial_duels= None
        first_half_home_dribbles= None
        first_half_away_dribbles= None
        first_half_home_tackles_won= None
        first_half_away_tackles_won= None
        first_half_home_total_tackles= None
        first_half_away_total_tackles= None
        first_half_home_interceptions= None
        first_half_away_interceptions= None
        first_half_home_recoveries= None
        first_half_away_recoveries= None
        first_half_home_clearances= None
        first_half_away_clearances= None
        first_half_home_total_saves= None
        first_half_away_total_saves= None
        first_half_home_goals_prevented= None
        first_half_away_goals_prevented= None
        first_half_home_goal_kicks= None
        first_half_away_goal_kicks= None
        #second half
        second_half_home_ball_possession= None
        second_half_away_ball_possession= None
        second_half_home_expected_goals= None
        second_half_away_expected_goals= None
        second_half_home_big_chances= None
        second_half_away_big_chances= None
        second_half_home_total_shots= None
        second_half_away_total_shots= None
        second_half_home_goalkeeper_saves= None
        second_half_away_goalkeeper_saves= None
        second_half_home_corner_kicks= None
        second_half_away_corner_kicks= None
        second_half_home_fouls= None
        second_half_away_fouls= None
        second_half_home_passes= None
        second_half_away_passes= None
        second_half_home_tackles= None
        second_half_away_tackles= None
        second_half_home_free_kicks= None
        second_half_away_free_kicks= None
        second_half_home_yellow_cards= None
        second_half_away_yellow_cards= None
        second_half_home_total_shots= None
        second_half_away_total_shots= None
        second_half_home_shots_on_target= None
        second_half_away_shots_on_target= None
        second_half_home_hit_woodwork= None
        second_half_away_hit_woodwork= None
        second_half_home_shots_off_target= None
        second_half_away_shots_off_target= None
        second_half_home_blocked_shots= None
        second_half_away_blocked_shots= None
        second_half_home_shots_inside_box= None
        second_half_away_shots_inside_box= None
        second_half_home_shots_outside_box= None
        second_half_away_shots_outside_box= None
        second_half_home_big_chances_scored= None
        second_half_away_big_chances_scored= None
        second_half_home_big_chances_missed= None
        second_half_away_big_chances_missed= None
        second_half_home_through_balls= None
        second_half_away_through_balls= None
        second_half_home_fouled_in_final_third= None
        second_half_away_fouled_in_final_third= None
        second_half_home_offsides= None
        second_half_away_offsides= None
        second_half_home_accurate_passes= None
        second_half_away_accurate_passes= None
        second_half_home_throw_ins= None
        second_half_away_throw_ins= None
        second_half_home_final_third_entries= None
        second_half_away_final_third_entries= None
        second_half_home_long_balls= None
        second_half_away_long_balls= None
        second_half_home_crosses= None
        second_half_away_crosses= None
        second_half_home_duels= None
        second_half_away_duels= None
        second_half_home_dispossessed= None
        second_half_away_dispossessed= None
        second_half_home_ground_duels= None
        second_half_away_ground_duels= None
        second_half_home_aerial_duels= None
        second_half_away_aerial_duels= None
        second_half_home_dribbles= None
        second_half_away_dribbles= None
        second_half_home_tackles_won= None
        second_half_away_tackles_won= None
        second_half_home_total_tackles= None
        second_half_away_total_tackles= None
        second_half_home_interceptions= None
        second_half_away_interceptions= None
        second_half_home_recoveries= None
        second_half_away_recoveries= None
        second_half_home_clearances= None
        second_half_away_clearances= None
        second_half_home_total_saves= None
        second_half_away_total_saves= None
        second_half_home_goals_prevented= None
        second_half_away_goals_prevented= None
        second_half_home_goal_kicks= None
        second_half_away_goal_kicks = None








    dict_statistics_each_game["all_home_ball_possession"] =all_home_ball_possession
    dict_statistics_each_game["all_away_ball_possession"] =all_away_ball_possession
    dict_statistics_each_game["all_home_expected_goals"] =all_home_expected_goals
    dict_statistics_each_game["all_away_expected_goals"] =all_away_expected_goals
    dict_statistics_each_game["all_home_big_chances"] =all_home_big_chances
    dict_statistics_each_game["all_away_big_chances"] =all_away_big_chances
    dict_statistics_each_game["all_home_total_shots"] =all_home_total_shots
    dict_statistics_each_game["all_away_total_shots"] =all_away_total_shots
    dict_statistics_each_game["all_home_goalkeeper_saves"] =all_home_goalkeeper_saves
    dict_statistics_each_game["all_away_goalkeeper_saves"] =all_away_goalkeeper_saves
    dict_statistics_each_game["all_home_corner_kicks"] =all_home_corner_kicks
    dict_statistics_each_game["all_away_corner_kicks"] =all_away_corner_kicks
    dict_statistics_each_game["all_home_fouls"] =all_home_fouls
    dict_statistics_each_game["all_away_fouls"] =all_away_fouls
    dict_statistics_each_game["all_home_passes"] =all_home_passes
    dict_statistics_each_game["all_away_passes"] =all_away_passes
    dict_statistics_each_game["all_home_tackles"] =all_home_tackles
    dict_statistics_each_game["all_away_tackles"] =all_away_tackles
    dict_statistics_each_game["all_home_free_kicks"] =all_home_free_kicks
    dict_statistics_each_game["all_away_free_kicks"] =all_away_free_kicks
    dict_statistics_each_game["all_home_yellow_cards"] =all_home_yellow_cards
    dict_statistics_each_game["all_away_yellow_cards"] =all_away_yellow_cards
    dict_statistics_each_game["all_home_total_shots"] =all_home_total_shots
    dict_statistics_each_game["all_away_total_shots"] =all_away_total_shots
    dict_statistics_each_game["all_home_shots_on_target"] =all_home_shots_on_target
    dict_statistics_each_game["all_away_shots_on_target"] =all_away_shots_on_target
    dict_statistics_each_game["all_home_hit_woodwork"] =all_home_hit_woodwork
    dict_statistics_each_game["all_away_hit_woodwork"] =all_away_hit_woodwork
    dict_statistics_each_game["all_home_shots_off_target"] =all_home_shots_off_target
    dict_statistics_each_game["all_away_shots_off_target"] =all_away_shots_off_target
    dict_statistics_each_game["all_home_blocked_shots"] =all_home_blocked_shots
    dict_statistics_each_game["all_away_blocked_shots"] =all_away_blocked_shots
    dict_statistics_each_game["all_home_shots_inside_box"] =all_home_shots_inside_box
    dict_statistics_each_game["all_away_shots_inside_box"] =all_away_shots_inside_box
    dict_statistics_each_game["all_home_shots_outside_box"] =all_home_shots_outside_box
    dict_statistics_each_game["all_away_shots_outside_box"] =all_away_shots_outside_box
    dict_statistics_each_game["all_home_big_chances_scored"] =all_home_big_chances_scored
    dict_statistics_each_game["all_away_big_chances_scored"] =all_away_big_chances_scored
    dict_statistics_each_game["all_home_big_chances_missed"] =all_home_big_chances_missed
    dict_statistics_each_game["all_away_big_chances_missed"] =all_away_big_chances_missed
    dict_statistics_each_game["all_home_through_balls"] =all_home_through_balls
    dict_statistics_each_game["all_away_through_balls"] =all_away_through_balls
    dict_statistics_each_game["all_home_fouled_in_final_third"] =all_home_fouled_in_final_third
    dict_statistics_each_game["all_away_fouled_in_final_third"] =all_away_fouled_in_final_third
    dict_statistics_each_game["all_home_offsides"] =all_home_offsides
    dict_statistics_each_game["all_away_offsides"] =all_away_offsides
    dict_statistics_each_game["all_home_accurate_passes"] =all_home_accurate_passes
    dict_statistics_each_game["all_away_accurate_passes"] =all_away_accurate_passes
    dict_statistics_each_game["all_home_throw_ins"] =all_home_throw_ins
    dict_statistics_each_game["all_away_throw_ins"] =all_away_throw_ins
    dict_statistics_each_game["all_home_final_third_entries"] =all_home_final_third_entries
    dict_statistics_each_game["all_away_final_third_entries"] =all_away_final_third_entries
    dict_statistics_each_game["all_home_long_balls"] =all_home_long_balls
    dict_statistics_each_game["all_away_long_balls"] =all_away_long_balls
    dict_statistics_each_game["all_home_crosses"] =all_home_crosses
    dict_statistics_each_game["all_away_crosses"] =all_away_crosses
    dict_statistics_each_game["all_home_duels"] =all_home_duels
    dict_statistics_each_game["all_away_duels"] =all_away_duels
    dict_statistics_each_game["all_home_dispossessed"] =all_home_dispossessed
    dict_statistics_each_game["all_away_dispossessed"] =all_away_dispossessed
    dict_statistics_each_game["all_home_ground_duels"] =all_home_ground_duels
    dict_statistics_each_game["all_away_ground_duels"] =all_away_ground_duels
    dict_statistics_each_game["all_home_aerial_duels"] =all_home_aerial_duels
    dict_statistics_each_game["all_away_aerial_duels"] =all_away_aerial_duels
    dict_statistics_each_game["all_home_dribbles"] =all_home_dribbles
    dict_statistics_each_game["all_away_dribbles"] =all_away_dribbles
    dict_statistics_each_game["all_home_tackles_won"] =all_home_tackles_won
    dict_statistics_each_game["all_away_tackles_won"] =all_away_tackles_won
    dict_statistics_each_game["all_home_total_tackles"] =all_home_total_tackles
    dict_statistics_each_game["all_away_total_tackles"] =all_away_total_tackles
    dict_statistics_each_game["all_home_interceptions"] =all_home_interceptions
    dict_statistics_each_game["all_away_interceptions"] =all_away_interceptions
    dict_statistics_each_game["all_home_recoveries"] =all_home_recoveries
    dict_statistics_each_game["all_away_recoveries"] =all_away_recoveries
    dict_statistics_each_game["all_home_clearances"] =all_home_clearances
    dict_statistics_each_game["all_away_clearances"] =all_away_clearances
    dict_statistics_each_game["all_home_total_saves"] =all_home_total_saves
    dict_statistics_each_game["all_away_total_saves"] =all_away_total_saves
    dict_statistics_each_game["all_home_goals_prevented"] =all_home_goals_prevented
    dict_statistics_each_game["all_away_goals_prevented"] =all_away_goals_prevented
    dict_statistics_each_game["all_home_goal_kicks"] =all_home_goal_kicks
    dict_statistics_each_game["all_away_goal_kicks"] =all_away_goal_kicks
    #first_half,statitstics
    dict_statistics_each_game["first_half_home_ball_possession"] =first_half_home_ball_possession
    dict_statistics_each_game["first_half_away_ball_possession"] =first_half_away_ball_possession
    dict_statistics_each_game["first_half_home_expected_goals"] =first_half_home_expected_goals
    dict_statistics_each_game["first_half_away_expected_goals"] =first_half_away_expected_goals
    dict_statistics_each_game["first_half_home_big_chances"] =first_half_home_big_chances
    dict_statistics_each_game["first_half_away_big_chances"] =first_half_away_big_chances
    dict_statistics_each_game["first_half_home_total_shots"] =first_half_home_total_shots
    dict_statistics_each_game["first_half_away_total_shots"] =first_half_away_total_shots
    dict_statistics_each_game["first_half_home_goalkeeper_saves"] =first_half_home_goalkeeper_saves
    dict_statistics_each_game["first_half_away_goalkeeper_saves"] =first_half_away_goalkeeper_saves
    dict_statistics_each_game["first_half_home_corner_kicks"] =first_half_home_corner_kicks
    dict_statistics_each_game["first_half_away_corner_kicks"] =first_half_away_corner_kicks
    dict_statistics_each_game["first_half_home_fouls"] =first_half_home_fouls
    dict_statistics_each_game["first_half_away_fouls"] =first_half_away_fouls
    dict_statistics_each_game["first_half_home_passes"] =first_half_home_passes
    dict_statistics_each_game["first_half_away_passes"] =first_half_away_passes
    dict_statistics_each_game["first_half_home_tackles"] =first_half_home_tackles
    dict_statistics_each_game["first_half_away_tackles"] =first_half_away_tackles
    dict_statistics_each_game["first_half_home_free_kicks"] =first_half_home_free_kicks
    dict_statistics_each_game["first_half_away_free_kicks"] =first_half_away_free_kicks
    dict_statistics_each_game["first_half_home_yellow_cards"] =first_half_home_yellow_cards
    dict_statistics_each_game["first_half_away_yellow_cards"] =first_half_away_yellow_cards
    dict_statistics_each_game["first_half_home_total_shots"] =first_half_home_total_shots
    dict_statistics_each_game["first_half_away_total_shots"] =first_half_away_total_shots
    dict_statistics_each_game["first_half_home_shots_on_target"] =first_half_home_shots_on_target
    dict_statistics_each_game["first_half_away_shots_on_target"] =first_half_away_shots_on_target
    dict_statistics_each_game["first_half_home_hit_woodwork"] =first_half_home_hit_woodwork
    dict_statistics_each_game["first_half_away_hit_woodwork"] =first_half_away_hit_woodwork
    dict_statistics_each_game["first_half_home_shots_off_target"] =first_half_home_shots_off_target
    dict_statistics_each_game["first_half_away_shots_off_target"] =first_half_away_shots_off_target
    dict_statistics_each_game["first_half_home_blocked_shots"] =first_half_home_blocked_shots
    dict_statistics_each_game["first_half_away_blocked_shots"] =first_half_away_blocked_shots
    dict_statistics_each_game["first_half_home_shots_inside_box"] =first_half_home_shots_inside_box
    dict_statistics_each_game["first_half_away_shots_inside_box"] =first_half_away_shots_inside_box
    dict_statistics_each_game["first_half_home_shots_outside_box"] =first_half_home_shots_outside_box
    dict_statistics_each_game["first_half_away_shots_outside_box"] =first_half_away_shots_outside_box
    dict_statistics_each_game["first_half_home_big_chances_scored"] =first_half_home_big_chances_scored
    dict_statistics_each_game["first_half_away_big_chances_scored"] =first_half_away_big_chances_scored
    dict_statistics_each_game["first_half_home_big_chances_missed"] =first_half_home_big_chances_missed
    dict_statistics_each_game["first_half_away_big_chances_missed"] =first_half_away_big_chances_missed
    dict_statistics_each_game["first_half_home_through_balls"] =first_half_home_through_balls
    dict_statistics_each_game["first_half_away_through_balls"] =first_half_away_through_balls
    dict_statistics_each_game["first_half_home_fouled_in_final_third"] =first_half_home_fouled_in_final_third
    dict_statistics_each_game["first_half_away_fouled_in_final_third"] =first_half_away_fouled_in_final_third
    dict_statistics_each_game["first_half_home_offsides"] =first_half_home_offsides
    dict_statistics_each_game["first_half_away_offsides"] =first_half_away_offsides
    dict_statistics_each_game["first_half_home_accurate_passes"] =first_half_home_accurate_passes
    dict_statistics_each_game["first_half_away_accurate_passes"] =first_half_away_accurate_passes
    dict_statistics_each_game["first_half_home_throw_ins"] =first_half_home_throw_ins
    dict_statistics_each_game["first_half_away_throw_ins"] =first_half_away_throw_ins
    dict_statistics_each_game["first_half_home_final_third_entries"] =first_half_home_final_third_entries
    dict_statistics_each_game["first_half_away_final_third_entries"] =first_half_away_final_third_entries
    dict_statistics_each_game["first_half_home_long_balls"] =first_half_home_long_balls
    dict_statistics_each_game["first_half_away_long_balls"] =first_half_away_long_balls
    dict_statistics_each_game["first_half_home_crosses"] =first_half_home_crosses
    dict_statistics_each_game["first_half_away_crosses"] =first_half_away_crosses
    dict_statistics_each_game["first_half_home_duels"] =first_half_home_duels
    dict_statistics_each_game["first_half_away_duels"] =first_half_away_duels
    dict_statistics_each_game["first_half_home_dispossessed"] =first_half_home_dispossessed
    dict_statistics_each_game["first_half_away_dispossessed"] =first_half_away_dispossessed
    dict_statistics_each_game["first_half_home_ground_duels"] =first_half_home_ground_duels
    dict_statistics_each_game["first_half_away_ground_duels"] =first_half_away_ground_duels
    dict_statistics_each_game["first_half_home_aerial_duels"] =first_half_home_aerial_duels
    dict_statistics_each_game["first_half_away_aerial_duels"] =first_half_away_aerial_duels
    dict_statistics_each_game["first_half_home_dribbles"] =first_half_home_dribbles
    dict_statistics_each_game["first_half_away_dribbles"] =first_half_away_dribbles
    dict_statistics_each_game["first_half_home_tackles_won"] =first_half_home_tackles_won
    dict_statistics_each_game["first_half_away_tackles_won"] =first_half_away_tackles_won
    dict_statistics_each_game["first_half_home_total_tackles"] =first_half_home_total_tackles
    dict_statistics_each_game["first_half_away_total_tackles"] =first_half_away_total_tackles
    dict_statistics_each_game["first_half_home_interceptions"] =first_half_home_interceptions
    dict_statistics_each_game["first_half_away_interceptions"] =first_half_away_interceptions
    dict_statistics_each_game["first_half_home_recoveries"] =first_half_home_recoveries
    dict_statistics_each_game["first_half_away_recoveries"] =first_half_away_recoveries
    dict_statistics_each_game["first_half_home_clearances"] =first_half_home_clearances
    dict_statistics_each_game["first_half_away_clearances"] =first_half_away_clearances
    dict_statistics_each_game["first_half_home_total_saves"] =first_half_home_total_saves
    dict_statistics_each_game["first_half_away_total_saves"] =first_half_away_total_saves
    dict_statistics_each_game["first_half_home_goals_prevented"] =first_half_home_goals_prevented
    dict_statistics_each_game["first_half_away_goals_prevented"] =first_half_away_goals_prevented
    dict_statistics_each_game["first_half_home_goal_kicks"] =first_half_home_goal_kicks
    dict_statistics_each_game["first_half_away_goal_kicks"] =first_half_away_goal_kicks
    #second half,statistics
    dict_statistics_each_game["second_half_home_ball_possession"] =second_half_home_ball_possession
    dict_statistics_each_game["second_half_away_ball_possession"] =second_half_away_ball_possession
    dict_statistics_each_game["second_half_home_expected_goals"] =second_half_home_expected_goals
    dict_statistics_each_game["second_half_away_expected_goals"] =second_half_away_expected_goals
    dict_statistics_each_game["second_half_home_big_chances"] =second_half_home_big_chances
    dict_statistics_each_game["second_half_away_big_chances"] =second_half_away_big_chances
    dict_statistics_each_game["second_half_home_total_shots"] =second_half_home_total_shots
    dict_statistics_each_game["second_half_away_total_shots"] =second_half_away_total_shots
    dict_statistics_each_game["second_half_home_goalkeeper_saves"] =second_half_home_goalkeeper_saves
    dict_statistics_each_game["second_half_away_goalkeeper_saves"] =second_half_away_goalkeeper_saves
    dict_statistics_each_game["second_half_home_corner_kicks"] =second_half_home_corner_kicks
    dict_statistics_each_game["second_half_away_corner_kicks"] =second_half_away_corner_kicks
    dict_statistics_each_game["second_half_home_fouls"] =second_half_home_fouls
    dict_statistics_each_game["second_half_away_fouls"] =second_half_away_fouls
    dict_statistics_each_game["second_half_home_passes"] =second_half_home_passes
    dict_statistics_each_game["second_half_away_passes"] =second_half_away_passes
    dict_statistics_each_game["second_half_home_tackles"] =second_half_home_tackles
    dict_statistics_each_game["second_half_away_tackles"] =second_half_away_tackles
    dict_statistics_each_game["second_half_home_free_kicks"] =second_half_home_free_kicks
    dict_statistics_each_game["second_half_away_free_kicks"] =second_half_away_free_kicks
    dict_statistics_each_game["second_half_home_yellow_cards"] =second_half_home_yellow_cards
    dict_statistics_each_game["second_half_away_yellow_cards"] =second_half_away_yellow_cards
    dict_statistics_each_game["second_half_home_total_shots"] =second_half_home_total_shots
    dict_statistics_each_game["second_half_away_total_shots"] =second_half_away_total_shots
    dict_statistics_each_game["second_half_home_shots_on_target"] =second_half_home_shots_on_target
    dict_statistics_each_game["second_half_away_shots_on_target"] =second_half_away_shots_on_target
    dict_statistics_each_game["second_half_home_hit_woodwork"] =second_half_home_hit_woodwork
    dict_statistics_each_game["second_half_away_hit_woodwork"] =second_half_away_hit_woodwork
    dict_statistics_each_game["second_half_home_shots_off_target"] =second_half_home_shots_off_target
    dict_statistics_each_game["second_half_away_shots_off_target"] =second_half_away_shots_off_target
    dict_statistics_each_game["second_half_home_blocked_shots"] =second_half_home_blocked_shots
    dict_statistics_each_game["second_half_away_blocked_shots"] =second_half_away_blocked_shots
    dict_statistics_each_game["second_half_home_shots_inside_box"] =second_half_home_shots_inside_box
    dict_statistics_each_game["second_half_away_shots_inside_box"] =second_half_away_shots_inside_box
    dict_statistics_each_game["second_half_home_shots_outside_box"] =second_half_home_shots_outside_box
    dict_statistics_each_game["second_half_away_shots_outside_box"] =second_half_away_shots_outside_box
    dict_statistics_each_game["second_half_home_big_chances_scored"] =second_half_home_big_chances_scored
    dict_statistics_each_game["second_half_away_big_chances_scored"] =second_half_away_big_chances_scored
    dict_statistics_each_game["second_half_home_big_chances_missed"] =second_half_home_big_chances_missed
    dict_statistics_each_game["second_half_away_big_chances_missed"] =second_half_away_big_chances_missed
    dict_statistics_each_game["second_half_home_through_balls"] =second_half_home_through_balls
    dict_statistics_each_game["second_half_away_through_balls"] =second_half_away_through_balls
    dict_statistics_each_game["second_half_home_fouled_in_final_third"] =second_half_home_fouled_in_final_third
    dict_statistics_each_game["second_half_away_fouled_in_final_third"] =second_half_away_fouled_in_final_third
    dict_statistics_each_game["second_half_home_offsides"] =second_half_home_offsides
    dict_statistics_each_game["second_half_away_offsides"] =second_half_away_offsides
    dict_statistics_each_game["second_half_home_accurate_passes"] =second_half_home_accurate_passes
    dict_statistics_each_game["second_half_away_accurate_passes"] =second_half_away_accurate_passes
    dict_statistics_each_game["second_half_home_throw_ins"] =second_half_home_throw_ins
    dict_statistics_each_game["second_half_away_throw_ins"] =second_half_away_throw_ins
    dict_statistics_each_game["second_half_home_final_third_entries"] =second_half_home_final_third_entries
    dict_statistics_each_game["second_half_away_final_third_entries"] =second_half_away_final_third_entries
    dict_statistics_each_game["second_half_home_long_balls"] =second_half_home_long_balls
    dict_statistics_each_game["second_half_away_long_balls"] =second_half_away_long_balls
    dict_statistics_each_game["second_half_home_crosses"] =second_half_home_crosses
    dict_statistics_each_game["second_half_away_crosses"] =second_half_away_crosses
    dict_statistics_each_game["second_half_home_duels"] =second_half_home_duels
    dict_statistics_each_game["second_half_away_duels"] =second_half_away_duels
    dict_statistics_each_game["second_half_home_dispossessed"] =second_half_home_dispossessed
    dict_statistics_each_game["second_half_away_dispossessed"] =second_half_away_dispossessed
    dict_statistics_each_game["second_half_home_ground_duels"] =second_half_home_ground_duels
    dict_statistics_each_game["second_half_away_ground_duels"] =second_half_away_ground_duels
    dict_statistics_each_game["second_half_home_aerial_duels"] =second_half_home_aerial_duels
    dict_statistics_each_game["second_half_away_aerial_duels"] =second_half_away_aerial_duels
    dict_statistics_each_game["second_half_home_dribbles"] =second_half_home_dribbles
    dict_statistics_each_game["second_half_away_dribbles"] =second_half_away_dribbles
    dict_statistics_each_game["second_half_home_tackles_won"] =second_half_home_tackles_won
    dict_statistics_each_game["second_half_away_tackles_won"] =second_half_away_tackles_won
    dict_statistics_each_game["second_half_home_total_tackles"] =second_half_home_total_tackles
    dict_statistics_each_game["second_half_away_total_tackles"] =second_half_away_total_tackles
    dict_statistics_each_game["second_half_home_interceptions"] =second_half_home_interceptions
    dict_statistics_each_game["second_half_away_interceptions"] =second_half_away_interceptions
    dict_statistics_each_game["second_half_home_recoveries"] =second_half_home_recoveries
    dict_statistics_each_game["second_half_away_recoveries"] =second_half_away_recoveries
    dict_statistics_each_game["second_half_home_clearances"] =second_half_home_clearances
    dict_statistics_each_game["second_half_away_clearances"] =second_half_away_clearances
    dict_statistics_each_game["second_half_home_total_saves"] =second_half_home_total_saves
    dict_statistics_each_game["second_half_away_total_saves"] =second_half_away_total_saves
    dict_statistics_each_game["second_half_home_goals_prevented"] =second_half_home_goals_prevented
    dict_statistics_each_game["second_half_away_goals_prevented"] =second_half_away_goals_prevented
    dict_statistics_each_game["second_half_home_goal_kicks"] =second_half_home_goal_kicks
    dict_statistics_each_game["second_half_away_goal_kicks"] =second_half_away_goal_kicks
    return dict_statistics_each_game