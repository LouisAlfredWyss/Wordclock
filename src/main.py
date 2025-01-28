# coding=utf-8
import argparse
from datetime import datetime
import numpy as np 
from rpi_ws281x import PixelStrip, Color
from led import set_color, clear_color, set_minute, wipe_color
from constants import LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,\
                        LED_BRIGHTNESS, LED_INVERT, LED_CHANNEL
from constants import VEC_1, VEC_2, VEC_3, VEC_4, VEC_5, VEC_6, VEC_7,\
                        VEC_8, VEC_9, VEC_10, VEC_11, VEC_12, VEC_ES_ISCH

if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
 
    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
        # "Es isch" anzeigen lassen, ist immer an.
        set_color(strip, VEC_ES_ISCH)
        
        while True:
            # time.sleep(1000/1000.0)
            
            # Abfragen der aktuellen Zeit und auf Stunden und Minuten aufteilen
            now_method = datetime.now()   
            hours = int(now_method.strftime("%H")) % 12
            minute = int(now_method.strftime("%M"))
            seconds = int(now_method.strftime("%S"))
            
            # Stunde um eines erhöhen wenn Minute grösser gleich 30
            if minute >= 30 and minute < 60:
                hours = hours +1

            # Abfragen, welche Stunde aktuell ist aktuelle Zeit anzeigen lassen
            if hours == 1:
                clear_color(strip, VEC_12)
                set_color(strip, VEC_1)
                set_minute(strip, minute)
                
            elif hours ==2:
                clear_color(strip, VEC_1)
                set_color(strip, VEC_2)
                set_minute(strip, minute)

            elif hours == 3:
                clear_color(strip, VEC_2)
                set_color(strip, VEC_3)
                set_minute(strip, minute)
                
            elif hours == 4:
                clear_color(strip, VEC_3)
                set_color(strip, VEC_4)
                set_minute(strip, minute)
                
            elif hours == 5:
                clear_color(strip, VEC_4)
                set_color(strip, VEC_5)
                set_minute(strip, minute)
                
            elif hours == 6:
                clear_color(strip, VEC_5)
                set_color(strip, VEC_6)
                set_minute(strip, minute)
                
            elif hours == 7:
                clear_color(strip, VEC_6)
                set_color(strip, VEC_7)
                set_minute(strip, minute)
                
            elif hours == 8:
                clear_color(strip, VEC_7)
                set_color(strip, VEC_8)
                set_minute(strip, minute)
                
            elif hours == 9:
                clear_color(strip, VEC_8)
                set_color(strip, VEC_9)
                set_minute(strip, minute)
                
            elif hours == 10:
                clear_color(strip, VEC_9)
                set_color(strip, VEC_10)
                set_minute(strip, minute)
                
            elif hours == 11:
                clear_color(strip, VEC_10)
                set_color(strip, VEC_11)
                set_minute(strip, minute)
                
            else:
                clear_color(strip, VEC_11)
                set_color(strip, VEC_12)
                set_minute(strip, minute)
            
 
    except KeyboardInterrupt:
        if args.clear:
            wipe_color(strip, Color(0,0,0), 0)
            
