# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 19:35:54 2023

@author: laugi
"""
import time
from rpi_ws281x import Color
import numpy as np
from constants import VEC_5_10, VEC_10_15,VEC_15_20, VEC_20_25,VEC_25_30,\
                        VEC_30_35, VEC_35_40, VEC_40_45, VEC_45_50,\
                        VEC_50_55, VEC_55_60, VEC_VOR, VEC_VIERTEL, VEC_UEBER,\
                        VEC_HALBI, VEC_AB, VEC_FUEF, VEC_ZAEH, VEC_ZWAENZG


def wipe_color(strip, color, wait_ms=0):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        
def clear_color(strip, delete_vec):
    for i in range(0, len(delete_vec)):
        strip.setPixelColor(int(delete_vec[i]), Color(0, 0, 0))
        strip.show()

def set_color(strip, set_vec):        
    for i in range(0, len(set_vec)):
        strip.setPixelColor(int(set_vec[i]), Color(255, 255, 255))
    strip.show()
    
def set_minute(strip, minute):
    
    if  minute >= 5 and minute < 10:
        set_color(strip, VEC_5_10)
        strip.show()

    elif minute >= 10 and minute < 15:
        set_color(strip, VEC_10_15)
        clear_color(strip, VEC_FUEF)

    elif minute >= 15 and minute < 20:
        set_color(strip, VEC_15_20)
        clear_color(strip, VEC_ZAEH)        

    elif minute >= 20 and minute < 25:
        set_color(strip, VEC_20_25)
        clear_color(strip, VEC_VIERTEL)

    elif minute >= 25 and minute < 30:
        set_color(strip, VEC_25_30)
        clear_color(strip, np.concatenate([VEC_ZWAENZG, VEC_AB]))

    elif minute >= 30 and minute < 35:
        set_color(strip, VEC_30_35)
        clear_color(strip, np.concatenate([VEC_FUEF, VEC_VOR]))

    elif minute >= 35 and minute < 40:
        set_color(strip, VEC_35_40)
        
    elif minute >= 40 and minute < 45:
        set_color(strip, VEC_40_45)
        clear_color(strip, np.concatenate([VEC_FUEF, VEC_UEBER, VEC_HALBI]))

    elif minute >= 45 and minute < 50:
        set_color(strip, VEC_45_50)
        clear_color(strip, VEC_ZWAENZG)
        
    elif minute >= 50 and minute < 55:
        set_color(strip, VEC_50_55)
        clear_color(strip, VEC_VIERTEL)

    elif minute >= 55 and minute < 60:
        set_color(strip, VEC_55_60)
        clear_color(strip, VEC_ZAEH)
        
    else:
        clear_color(strip, np.concatenate([VEC_FUEF, VEC_VOR]))
