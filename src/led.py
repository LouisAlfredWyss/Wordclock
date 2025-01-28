# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 19:35:54 2023

@author: laugi
"""
import time
from rpi_ws281x import Color
import numpy as np 


def color_wipe(strip, color, wait_ms=0):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        
def color_clear(strip, delVec):
    for i in range(0, len(delVec)):
        strip.setPixelColor(delVec[i], Color(0, 0, 0))
        strip.show()

def color_set(strip, ledVec):        
    for i in range(0, len(ledVec)):
        strip.setPixelColor(ledVec[i], Color(255, 255, 255))
    strip.show()
    
def minuteSet(strip, timeMinutes):
    
    if  timeMinutes >= 5 and timeMinutes < 10:
        colorSet(strip, vec5_10)
        strip.show()

    elif timeMinutes >= 10 and timeMinutes < 15:
        colorSet(strip, vec10_15)
        colorClear(strip, vecFuef)

    elif timeMinutes >= 15 and timeMinutes < 20:
        colorSet(strip, vec15_20)
        colorClear(strip, vecZaeh)        

    elif timeMinutes >= 20 and timeMinutes < 25:
        colorSet(strip, vec20_25)
        colorClear(strip, vecViertel)

    elif timeMinutes >= 25 and timeMinutes < 30:
        colorSet(strip, vec25_30)
        colorClear(strip, np.concatenate([vecZwaenzg, vecAb]))

    elif timeMinutes >= 30 and timeMinutes < 35:
        colorSet(strip, vec30_35)
        colorClear(strip, np.concatenate([vecFuef, vecVor]))

    elif timeMinutes >= 35 and timeMinutes < 40:
        colorSet(strip, vec35_40)
        
    elif timeMinutes >= 40 and timeMinutes < 45:
        colorSet(strip, vec40_45)
        colorClear(strip, np.concatenate([vecFuef, vecUeber, vecHalbi]))

    elif timeMinutes >= 45 and timeMinutes < 50:
        colorSet(strip, vec45_50)
        colorClear(strip, vecZwaenzg)
        
    elif timeMinutes >= 50 and timeMinutes < 55:
        colorSet(strip, vec50_55)
        colorClear(strip, vecViertel)

    elif timeMinutes >= 55 and timeMinutes < 60:
        colorSet(strip, vec55_60)
        colorClear(strip, vecZaeh)
        
    else:
        colorClear(strip, np.concatenate([vecFuef, vecVor]))
