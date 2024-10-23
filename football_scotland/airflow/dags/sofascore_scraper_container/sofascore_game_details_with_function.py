import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date, timedelta
from datetime import datetime
import time
import datetime

def game_details_each_game(game_index,games_of_day):
    dict_game_details_each_game = dict()
    try:
        tournament_name = games_of_day["events"][game_index]["tournament"]["name"]
    except:tournament_name= None


    try:
        tournament_country = games_of_day["events"][game_index]["tournament"]["category"]["name"]
    except:tournament_country= None


    try:
        tournament_name_season = games_of_day["events"][game_index]["season"]["name"]
    except:tournament_name_season= None


    try:
        tournament_season = games_of_day["events"][game_index]["season"]["year"]
    except:tournament_season= None


    try:
        tournament_round = games_of_day["events"][game_index]["roundInfo"]["round"]
    except:
        tournament_round = None


    try:
        hometeam_name = games_of_day["events"][game_index]["homeTeam"]["name"]
    except:hometeam_name= None
    try:
        awayteam_name=games_of_day["events"][game_index]["awayTeam"]["name"]
    except:awayteam_name= None
    try:
        hometeam_country = games_of_day["events"][game_index]["homeTeam"]["country"]["name"]
    except:hometeam_country= None
    try:
        awayteam_country = games_of_day["events"][game_index]["awayTeam"]["country"]["name"]
    except:awayteam_country= None
    try:
        game_id = games_of_day["events"][game_index]["id"]
    except:game_id= None


    #for the dictionary
    
    dict_game_details_each_game["game_id"] = game_id
    dict_game_details_each_game["tournament_name"] = tournament_name
    dict_game_details_each_game["tournament_country"] = tournament_country
    dict_game_details_each_game["tournament_name_season"] = tournament_name_season
    dict_game_details_each_game["tournament_season"] = tournament_season
    dict_game_details_each_game["tournament_round"] = tournament_round
    dict_game_details_each_game["hometeam_name"] = hometeam_name
    dict_game_details_each_game["awayteam_name"] = awayteam_name
    dict_game_details_each_game["hometeam_country"] = hometeam_country
    dict_game_details_each_game["awayteam_country"] = awayteam_country
    return dict_game_details_each_game