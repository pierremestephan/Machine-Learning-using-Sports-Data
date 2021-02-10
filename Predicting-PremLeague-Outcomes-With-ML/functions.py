import numpy as np
import pandas as pd
import requests
import json

def get(url):
    response = requests.get(url)
    return json.loads(response.content)

def build_dataframes(response):
    players = response['elements']
    teams = response['teams']
    events = response['events']

    players_df = pd.DataFrame(players)
    teams_df = pd.DataFrame(teams)
    events_df = pd.DataFrame(events)
    return players_df,teams_df,events_df