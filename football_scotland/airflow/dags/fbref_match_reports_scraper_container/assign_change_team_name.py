import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
from datetime import datetime,date, timedelta

def assign_change_team_name(name_of_team_string):
    if name_of_team_string == 'Hamilton Academical':
        return 'Hamilton'
    elif name_of_team_string == 'Heart of Midlothian':
        return 'Hearts'
    elif name_of_team_string == '':
        return ''
    else:return name_of_team_string

