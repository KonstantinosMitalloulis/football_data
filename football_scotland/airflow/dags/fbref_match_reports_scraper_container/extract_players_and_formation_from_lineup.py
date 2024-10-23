import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
from datetime import datetime,date, timedelta

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

