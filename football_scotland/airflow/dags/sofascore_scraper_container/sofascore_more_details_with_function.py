import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date, timedelta
import time

def more_details_each_game(game_id_param):
    dict_more_details_each_game = dict()
    try:
        url_more_details_first_part   = "https://www.sofascore.com/api/v1/event/"
        url_more_details = url_more_details_first_part + str(game_id_param)



        payload = {}
        headers = {
            'authority' : 'www.sofascore.com' ,
            'accept' : '*/*' ,
            'accept-language': 'el-GR,el;q=0.9,de;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'cookie': '_gcl_au=1.1.468311363.1720620111; _ga=GA1.1.1629986250.1720620112; FCCDCF=^%^5Bnull^%^2Cnull^%^2Cnull^%^2C^%^5B^%^22CQBihYAQBihYAEsACBELA7EoAP_gAEPgAA6II3gB5C5ETSFBYH51KIsEYAEHwAAAIsAgAAYBAQABQBKQAIQCAGAAEAhAhCACgAAAIEYBIAEACAAQAAAAAAAAIAAEIAAQAAAIICAAAAAAAABIAAAIAAAAEAAAwCAABAAA0AgEAJIISNgAAAAAAAAAAgAAAAAAAgAAAEhAAAEIAAAAACgAEABAEAAAAAEIABBII3gB5C5ETSFBYHhVIIMEIAERQAAAIsAgAAQBAQAAQBKQAIQCEGAAAAgAACAAAAAAIEQBIAEAAAgAAAAAAAAAIAAEAAAAAAAIICAAAAAAAABAAAAIAAAAAAAAwCAABAAAwQhEAJIASFgAAAAgAAAAAoAAAAAAAgAAAEhAAAEAAAAAAAAAEAAAEAAAAAAAABBIAAA.dnAACAgAAAA^%^22^%^2C^%^222~70.89.108.149.211.313.358.415.486.540.621.981.1029.1046.1092.1097.1126.1205.1301.1516.1558.1584.1598.1651.1697.1716.1753.1810.1832.1985.2328.2373.2440.2571.2572.2575.2577.2628.2642.2677.2767.2860.2878.2887.2922.3182.3190.3234.3290.3292.3331.10631~dv.^%^22^%^2C^%^22E40555D6-D565-42CE-B57C-E02328DFD472^%^22^%^5D^%^5D; _lr_env_src_ats=false; __browsiUID=c7d29faa-32b0-47db-a158-4d28e107c355; _lr_retry_request=true; gcid_first=28b4e8aa-d914-45ad-8207-d8cdc9360b86; FCNEC=^%^5B^%^5B^%^22AKsRol9X5kkEGUEWN_BYisIA69rehTHwjdlU5QKiFIOv9qm1QVtfBY7OQt2Re70nJfjJ9T9kZ-6xI1eWgqwdzrlswp5kCNwjAaM3oE07Bh35BjjlmvQ3YBY3M-0inMlRU6hRIIlaFiOXs7Hqp-sM4df6ZkaB0yAlmQ^%^3D^%^3D^%^22^%^5D^%^5D; __gads=ID=fac686349d767848:T=1720620117:RT=1723992774:S=ALNI_MaAoHojfBDt-T66REpp95zwlnIY6Q; __gpi=UID=00000e7926227a4d:T=1720620117:RT=1723992774:S=ALNI_MbrL9MbKb6RX_evmqbuDVyhf0MtuA; __eoi=ID=1e9dbcf311fbbba4:T=1720620117:RT=1723992774:S=AA-AfjbwF8cU5e-qVkxB3YzNcPEW; _ga_QH2YGS7BB4=GS1.1.1723980723.24.1.1723992930.0.0.0; _ga_3KF4XTPHC4=GS1.1.1723980723.24.1.1723992930.41.0.0; _ga_HNQ9P9MGZR=GS1.1.1723980725.13.1.1723992933.38.0.0^',
            'if-none-match': 'W/^\^"eb45fbe85a^\^"^' ,
            'priority': 'u=1, i',
            'referer': 'https://www.sofascore.com/football/match/spain-france/GObsYTb' ,
            'sec-ch-ua': '^\^"Not)A;Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"127^\^", ^\^"Chromium^\^";v=^\^"127^\^"^" ',
            'sec-ch-ua-mobile': '?0' ,
            'sec-ch-ua-platform': '^\^"Windows^\^"^" ',
            'sec-fetch-dest': 'empty' ,
            'sec-fetch-mode': 'cors' ,
            'sec-fetch-site': 'same-origin' ,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' ,
            'x-requested-with': 'f971d8' }

        response = requests.request("GET" , url_more_details , headers=headers , data = payload)
        more_details_api = json.loads(response.text)

            #details_for_referee
        try:
            referee_name =  more_details_api["event"]["referee"]["name"]
        except:referee_name = None

        try:
            referee_yellow_cards =  more_details_api["event"]["referee"]["yellowCards"]
        except:referee_yellow_cards = None

        try:
            referee_redCards =  more_details_api["event"]["referee"]["redCards"]
        except:referee_redCards = None

        try:
            referee_yellowRedCards =  more_details_api["event"]["referee"]["yellowRedCards"]
        except:referee_yellowRedCards = None

        try:
            referee_games =  more_details_api["event"]["referee"]["games"]
        except:referee_games = None

        try:
            referee_id =  more_details_api["event"]["referee"]["id"]
        except:referee_id = None

        try:
            referee_country =  more_details_api["event"]["referee"]["country"]["name"]
        except:referee_country = None
            #stadium the game took plaxe

        try:
            city_game_took_place = more_details_api["event"]["venue"]["city"]["name"]
        except:city_game_took_place = None

        try:
            stadium_game_took_place = more_details_api["event"]["venue"]["stadium"]["name"]
        except:stadium_game_took_place = None

        try:
            stadium_id_game_took_place = more_details_api["event"]["venue"]["id"]
        except:stadium_id_game_took_place = None

        try:
            country_game_took_place = more_details_api["event"]["venue"]["country"]["name"]
        except:country_game_took_place = None

    except:
        referee_name = None
        referee_yellow_cards = None
        referee_redCards = None
        referee_games = None
        referee_id = None
        referee_country = None
        city_game_took_place = None
        stadium_game_took_place = None
        stadium_id_game_took_place = None
        country_game_took_place = None


    dict_more_details_each_game["referee_name"] = referee_name
    dict_more_details_each_game["referee_yellow_cards"] = referee_yellow_cards
    dict_more_details_each_game["referee_redCards"] = referee_redCards
    dict_more_details_each_game["referee_yellowRedCards"] = referee_yellowRedCards
    dict_more_details_each_game["referee_games"] = referee_games
    dict_more_details_each_game["referee_id"] = referee_id
    dict_more_details_each_game["referee_country"] = referee_country
    dict_more_details_each_game["city_game_took_place"] = city_game_took_place
    dict_more_details_each_game["stadium_game_took_place"] = stadium_game_took_place
    dict_more_details_each_game["stadium_id_game_took_place"] = stadium_id_game_took_place
    dict_more_details_each_game["country_game_took_place"] = country_game_took_place
    return dict_more_details_each_game