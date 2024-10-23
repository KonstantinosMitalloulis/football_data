import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd

def pregame_form_each_game(game_id_param):
    dict_pregame_form_each_game = dict()
    hometeam_avgRating = None
    hometeam_position= None
    hometeam_value= None
    hometeam_eam_form= None
    awayTeam_avgRating= None
    awayTeam_position= None
    awayTeam_value= None
    awayTeam_form= None
    try:

        url_pregame_form_first = "https://www.sofascore.com/api/v1/event/"
        url_pregame_form_second = "/pregame-form"
        url_pregame_form = url_pregame_form_first + str(game_id_param) + url_pregame_form_second

        

        #for_referer = main_link + game_slug + '/' + custom_id

        payload = {}
        headers = {
        'authority' : 'www.sofascore.com' ,
        'accept' : '*/*' ,
        'accept-language': 'el-GR,el;q=0.9,de;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': '_gcl_au=1.1.468311363.1720620111; _ga=GA1.1.1629986250.1720620112; FCCDCF=^%^5Bnull^%^2Cnull^%^2Cnull^%^2C^%^5B^%^22CQBihYAQBihYAEsACBELA7EoAP_gAEPgAA6II3gB5C5ETSFBYH51KIsEYAEHwAAAIsAgAAYBAQABQBKQAIQCAGAAEAhAhCACgAAAIEYBIAEACAAQAAAAAAAAIAAEIAAQAAAIICAAAAAAAABIAAAIAAAAEAAAwCAABAAA0AgEAJIISNgAAAAAAAAAAgAAAAAAAgAAAEhAAAEIAAAAACgAEABAEAAAAAEIABBII3gB5C5ETSFBYHhVIIMEIAERQAAAIsAgAAQBAQAAQBKQAIQCEGAAAAgAACAAAAAAIEQBIAEAAAgAAAAAAAAAIAAEAAAAAAAIICAAAAAAAABAAAAIAAAAAAAAwCAABAAAwQhEAJIASFgAAAAgAAAAAoAAAAAAAgAAAEhAAAEAAAAAAAAAEAAAEAAAAAAAABBIAAA.dnAACAgAAAA^%^22^%^2C^%^222~70.89.108.149.211.313.358.415.486.540.621.981.1029.1046.1092.1097.1126.1205.1301.1516.1558.1584.1598.1651.1697.1716.1753.1810.1832.1985.2328.2373.2440.2571.2572.2575.2577.2628.2642.2677.2767.2860.2878.2887.2922.3182.3190.3234.3290.3292.3331.10631~dv.^%^22^%^2C^%^22E40555D6-D565-42CE-B57C-E02328DFD472^%^22^%^5D^%^5D; _lr_env_src_ats=false; __browsiUID=c7d29faa-32b0-47db-a158-4d28e107c355; __browsiSessionID=33da003e-00ac-4c30-bf54-85866ee24123&true&DEFAULT&de&desktop-4.27.14&false; __gads=ID=fac686349d767848:T=1720620117:RT=1723712155:S=ALNI_MaAoHojfBDt-T66REpp95zwlnIY6Q; __gpi=UID=00000e7926227a4d:T=1720620117:RT=1723712155:S=ALNI_MbrL9MbKb6RX_evmqbuDVyhf0MtuA; __eoi=ID=1e9dbcf311fbbba4:T=1720620117:RT=1723712155:S=AA-AfjbwF8cU5e-qVkxB3YzNcPEW; _lr_retry_request=true; gcid_first=f8eab151-a9b2-434d-858b-1ec9cce10fc4; FCNEC=^%^5B^%^5B^%^22AKsRol9XPfxzDnunn4X8lY-lmEMRZaTotNl8xLP7KMRks77XNZ1iIFwl0RUBAblSs0S2o32VxHlKF0az60njrbObBIBUKcWyMFMknGLTfXGrw0d0_aS3xbADqVoctWgs3Hk5U7i0Fs_iVqflYfPEY4U4-l-B4OoWvg^%^3D^%^3D^%^22^%^5D^%^5D; _ga_QH2YGS7BB4=GS1.1.1723708658.23.1.1723712444.0.0.0; _ga_3KF4XTPHC4=GS1.1.1723708658.23.1.1723712444.51.0.0; _ga_HNQ9P9MGZR=GS1.1.1723708661.12.1.1723712445.50.0.0^',
        'if-none-match': 'W/^\^"a0339e5ed6^\^"^' ,
        'priority': 'u=1, i',
        'referer': 'for_referer' ,
        'sec-ch-ua': '^\^"Not)A;Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"127^\^", ^\^"Chromium^\^";v=^\^"127^\^"^" ',
        'sec-ch-ua-mobile': '?0' ,
        'sec-ch-ua-platform': '^\^"Windows^\^"^" ',
        'sec-fetch-dest': 'empty' ,
        'sec-fetch-mode': 'cors' ,
        'sec-fetch-site': 'same-origin' ,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' ,
        'x-requested-with': '8755c' }

        response = requests.request("GET" , url_pregame_form , headers=headers , data = payload)
        pregame_form_api = json.loads(response.text)

        #pregame_hometeam
        try:
            hometeam_avgRating=pregame_form_api["homeTeam"]['avgRating']
        except:hometeam_avgRating = None

        try:
            hometeam_position=pregame_form_api["homeTeam"]['position']
        except:hometeam_position = None

        try:
            hometeam_value=pregame_form_api["homeTeam"]['value']
        except:hometeam_value = None

        try:
            hometeam_eam_form=pregame_form_api["homeTeam"]['form']
        except:hometeam_eam_form = None

        #pregame_awayTeam
        try:
            awayTeam_avgRating=pregame_form_api["awayTeam"]['avgRating']
        except:awayTeam_avgRating = None

        try:
            awayTeam_position=pregame_form_api["awayTeam"]['position']
        except:awayTeam_position = None

        try:
            awayTeam_value=pregame_form_api["awayTeam"]['value']
        except:awayTeam_value = None

        try:
            awayTeam_form=pregame_form_api["awayTeam"]['form']
        except:awayTeam_form = None
    except:pass
    
    dict_pregame_form_each_game["hometeam_avgRating"] = hometeam_avgRating
    dict_pregame_form_each_game["hometeam_position"] = hometeam_position
    dict_pregame_form_each_game["hometeam_value"] = hometeam_value
    dict_pregame_form_each_game["hometeam_eam_form"] = hometeam_eam_form
    dict_pregame_form_each_game["awayTeam_avgRating"] = awayTeam_avgRating
    dict_pregame_form_each_game["awayTeam_position"] = awayTeam_position
    dict_pregame_form_each_game["awayTeam_value"] = awayTeam_value
    dict_pregame_form_each_game["awayTeam_form"] = awayTeam_form
    return dict_pregame_form_each_game