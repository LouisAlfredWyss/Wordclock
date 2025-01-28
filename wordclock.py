# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:13:16 2023

@author: laugi
"""


import time
from datetime import datetime
from rpi_ws281x import Color

# Define hour vectors
vec1 = [92, 104, 113]
vec2 = [5, 16, 27, 38]
vec3 = [3, 18, 25]
vec4 = [19, 24, 41, 46, 63]
vec5 = [1, 20, 23, 42]
vec6 = [60, 71, 82, 93, 103, 114]
vec7 = [0, 21, 22, 43, 44, 65]
vec8 = [66, 87, 88, 108, 109]
vec9 = [85, 90, 106, 111]
vec10 = [47, 62, 69, 84, 91]
vec11 = [17, 26, 39, 48]
vec12 = [64, 67, 86, 89, 107, 110]


# Dictionary with hour leds
hour_dict = {
    1: vec1,
    2: vec2,
    3: vec3,
    4: vec4,
    5: vec5,
    6: vec6,
    7: vec7,
    8: vec8,
    9: vec9,
    10: vec10,
    11: vec11,
    0: vec12 # When the hour is 12 or 0, use vec12
}

# Vektor mit LED-Positionen zu den Worten
vecVor = [14, 29, 36]
vecUeber = [58, 73, 80, 95]
vecAb = [94 ,102]


# Dict mit Vektor mit LED-Positionen zu den übrigen Worten
word_dict = {
    1: vecAb,
    2: vecVor,
    3: vecUeber,
    }

# Vektoren mit Minuten
vecFuef = [97, 99, 118]
vecZaeh = [96, 100, 117]
vecViertel = [9, 12, 31, 34, 53, 56, 75]
vecZwaenzg = [13, 30, 35, 52, 57,74]
vecHalbi = [15, 28, 37, 50, 59]

# Dict mit Vektoren mit Minuten
minutes_dict = {
    1: vecFuef,
    2: vecZaeh,
    3: vecViertel,
    4: vecZwaenzg,
    5: vecFuef,
    6: vecHalbi,
    7: vecFuef,
    8: vecZwaenzg,
    9: vecViertel,
    10: vecZaeh,
    11: vecFuef,
    0: [120]
    }
        
def color_wipe(strip, color, wait_ms=0):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        
def color_clear(strip, leds):
    for led in leds:
        strip.setPixelColor(led, Color(0, 0, 0))
        strip.show()

def color_set(strip, leds):
    
    for led in leds:
        strip.setPixelColor(led, Color(255, 255, 255))
    strip.show()

def get_current_time():
    time_now = datetime.now()
    hours = time_now.hour % 12
    minutes = time_now.minute
    return hours, minutes

def word_set(strip, minutes):
    # Set word ab
    if 0 < minutes // 5 <= 4:
        color_clear(strip, word_dict[2])
        color_clear(strip, word_dict[3])
        color_set(strip, word_dict[1])
    
    elif minutes // 5 == 5:
        color_clear(strip, word_dict[1])
        color_clear(strip, word_dict[3])
        color_set(strip, word_dict[2])
        color_set(strip, minutes_dict[6]) 
        
    elif minutes // 5 == 6:
        color_clear(strip, word_dict[1])
        color_clear(strip, word_dict[2])
        color_clear(strip, word_dict[3])
        color_set(strip, minutes_dict[6]) 
    
    # Set word über    
    elif minutes // 5 == 7:
        color_clear(strip, word_dict[2])
        color_clear(strip, word_dict[1])
        color_set(strip, word_dict[3])
        
    # Set word vor    
    elif 8 <= minutes // 5 < 12:
        color_clear(strip, word_dict[1])
        color_clear(strip, word_dict[3])
        color_clear(strip, minutes_dict[6])
        color_set(strip, word_dict[2])
        
def minute_set(strip, minutes):
    if 0 < minutes // 5:
        color_clear(strip, minutes_dict[minutes // 5 - 1])
        color_set(strip, minutes_dict[minutes // 5])
        
    else:
        color_clear(strip, minutes_dict[11])

def hour_set(strip, hours, minutes):
# Stunde um eines erhöhen wenn Minute grösser gleich 30 und kleiner 60
    if minutes >= 25 and minutes < 60:
        hours = hours +1
    
    if 0 < hours % 12:
        color_clear(strip, hour_dict[hours % 12-1])
        color_set(strip, hour_dict[hours % 12])
        minute_set(strip, minutes)
        word_set(strip, minutes)

    else:           
        color_clear(strip, hour_dict[11])
        color_clear(strip, word_dict[2])
        color_set(strip, hour_dict[hours % 12])
        minute_set(strip, minutes)
        word_set(strip, minutes)