# coding=utf-8
import time
from rpi_ws281x import *
import argparse
from datetime import datetime
import numpy as np 


# LED strip configuration:
LED_COUNT      = 121      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def colorWipe(strip, color, wait_ms=0):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        
def colorClear(strip, delVec):
    for i in range(0, len(delVec)):
        strip.setPixelColor(delVec[i], Color(0, 0, 0))
        strip.show()

def colorSet(strip, ledVec):        
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

if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Vektoren mit LED-Positionen zur jeweiligen Stunde
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
    
    # Vektor mit LED-Positionen zu den übrigen Worten
    vecEsIsch = [33, 54, 55, 76, 98, 119]
    vecVor = [14, 29, 36]
    vecViertel = [9, 12, 31, 34, 53, 56, 75]
    vecUeber = [58, 73, 80, 95]
    vecHalbi = [15, 28, 37, 50, 59]
    vecAb = [94 ,102]
    vecFuef = [97, 99, 118]
    vecZaeh = [96, 100, 117]
    vecZwaenzg = [13, 30, 35, 52, 57,74]
    
    # Vekoren mit LED-Positionen zur jeweiligen Minute
    vec5_10 = np.concatenate([vecFuef, vecAb])
    vec10_15 = np.concatenate([vecZaeh, vecAb])
    vec15_20 = np.concatenate([vecViertel, vecAb])
    vec20_25 = np.concatenate([vecZwaenzg, vecAb])
    vec25_30 = np.concatenate([vecFuef, vecVor, vecHalbi])
    vec30_35 = vecHalbi
    vec35_40 = np.concatenate([vecFuef, vecUeber, vecHalbi])
    vec40_45 = np.concatenate([vecZwaenzg, vecVor])
    vec45_50 = np.concatenate([vecViertel, vecVor])
    vec50_55 = np.concatenate([vecZaeh, vecVor])
    vec55_60 = np.concatenate([vecFuef, vecVor])
                
    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
 
    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
        # Es isch anzeigen lassen, ist immer an.
        colorSet(strip, vecEsIsch)
        
        while True:
            # time.sleep(1000/1000.0)
            
            # Abfragen der aktuellen Zeit und auf Stunden und Minuten aufteilen
            now_method = datetime.now()   
            hours = int(now_method.strftime("%H")) % 12
            minutes = int(now_method.strftime("%M"))
            seconds = int(now_method.strftime("%S"))
            
            # Stunde um eines erhöhen wenn Minute grösser gleich 30
            if minutes >= 30 and minutes < 60:
                hours = hours +1

            # Abfragen, welche Stunde aktuell ist aktuelle Zeit anzeigen lassen
            if hours == 1:
                colorClear(strip, vec12)
                colorSet(strip, vec1)
                minuteSet(strip, minutes)
                
            elif hours ==2:
                colorClear(strip, vec1)
                colorSet(strip, vec2)
                minuteSet(strip, minutes)

            elif hours == 3:
                colorClear(strip, vec2)
                colorSet(strip, vec3)
                minuteSet(strip, minutes)
                
            elif hours == 4:
                colorClear(strip, vec3)
                colorSet(strip, vec4)
                minuteSet(strip, minutes)
                
            elif hours == 5:
                colorClear(strip, vec4)
                colorSet(strip, vec5)
                minuteSet(strip, minutes)
                
            elif hours == 6:
                colorClear(strip, vec5)
                colorSet(strip, vec6)
                minuteSet(strip, minutes)
                
            elif hours == 7:
                colorClear(strip, vec6)
                colorSet(strip, vec7)
                minuteSet(strip, minutes)
                
            elif hours == 8:
                colorClear(strip, vec7)
                colorSet(strip, vec8)
                minuteSet(strip, minutes)
                
            elif hours == 9:
                colorClear(strip, vec8)
                colorSet(strip, vec9)
                minuteSet(strip, minutes)
                
            elif hours == 10:
                colorClear(strip, vec9)
                colorSet(strip, vec10)
                minuteSet(strip, minutes)
                
            elif hours == 11:
                colorClear(strip, vec10)
                colorSet(strip, vec11)
                minuteSet(strip, minutes)
                
            else:
                colorClear(strip, vec11)
                colorSet(strip, vec12)
                minuteSet(strip, minutes)
            
 
    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 0)
            
