# coding=utf-8
import argparse
import time
import numpy as np 
from datetime import datetime
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
        is_awake = True
        # "Es isch" anzeigen lassen, ist immer an.
        set_color(strip, VEC_ES_ISCH)
        
        while True:
            time.sleep(1.0)
            
            # Abfragen der aktuellen Zeit und auf Stunden und Minuten aufteilen
            now_method = datetime.now()   
            real_hours = now_method.hour
            hours = real_hours % 12
            minute = now_method.minute
            seconds = now_method.second
            
            # Sleep mode logic: between midnight (0) and 6:00
            if 0 <= real_hours < 6:
                if is_awake:
                    wipe_color(strip, Color(0,0,0), 0)
                    is_awake = False
                time.sleep(5.0)  # Sleep longer to save CPU during night
                continue
            else:
                if not is_awake:
                    # Wake up: restore "Es isch"
                    wipe_color(strip, Color(0,0,0), 0)
                    set_color(strip, VEC_ES_ISCH)
                    is_awake = True

                # Brightness logic: reduce from 21:00 towards 24:00 (which is 00:00)
                if 21 <= real_hours < 24:
                    minutes_past_21 = (real_hours - 21) * 60 + minute
                    # Decrease linearly over 180 minutes (3 hours)
                    fraction = 1.0 - (minutes_past_21 / 180.0)
                    # Don't let brightness hit 0 to avoid turning off prematurely
                    current_brightness = max(1, int(LED_BRIGHTNESS * fraction))
                else:
                    current_brightness = LED_BRIGHTNESS
                
                strip.setBrightness(current_brightness)
            
            # Stunde um eines erhöhen wenn Minute grösser gleich 25
            if minute >= 25 and minute < 60:
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
        wipe_color(strip, Color(0,0,0), 0)
