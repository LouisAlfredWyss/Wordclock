# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:13:58 2023

@author: laugi
"""

import requests
from datetime import datetime
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np


payload={}
headers = {}

def get_temperature(path):
    # Define the URL of the temperature sensor API
    IP_MYSTROM_OFFICE = '192.168.0.10'
    IP_MYSTROM_GAME_ROOM = '192.168.0.11'
    IP_MYSTROM_LIVING_ROOM = '192.168.0.12'
    urls = ['http://' + IP_MYSTROM_OFFICE + '/api/v1/temperature',\
           'http://' + IP_MYSTROM_LIVING_ROOM + '/api/v1/temperature',\
           'http://' + IP_MYSTROM_GAME_ROOM + '/api/v1/temperature']
    
    
    temp = []
    for url in urls:
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            temp.append(pd.json_normalize(response.json()).drop('offset', axis=1).values)
        else:
            pass
    time_ser = pd.Series(datetime.now()).repeat(temp[0].shape[1])
    
    temperature_df = pd.concat([pd.DataFrame(np.array(temp).reshape((len(temp)), temp[0].shape[1]).T).reset_index(drop=True),  time_ser.reset_index(drop=True)], axis=1, ignore_index=True)
    temperature_df.to_csv(path, index=False, mode = 'a', header = False)

