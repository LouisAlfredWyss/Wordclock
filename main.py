# coding=utf-8
import argparse
# import shutil
from rpi_ws281x import PixelStrip, Color
from wordclock import get_current_time, color_set, hour_set, color_wipe
from mystrom import get_temperature
# from pythonping import ping


# LED strip configuration:
LED_COUNT      = 121      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

STORE_PATH = r'/home/pi/shared/mystrom_csv/temperature.csv'
TARGET_PATH =  r'C:\\Users\\laugi\\repos\\mystrom\\data\\temperature.csv'
HOST_IP = '192.168.0.17'
# CHECK_STR = 'Reply from 192.168.0.17, 29 bytes in'

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
        # 'Es isch' anzeigen lassen, ist immer an.
        vecEsIsch = [33, 54, 55, 76, 98, 119]
        color_set(strip, vecEsIsch)
        
        while True:           
            
            # Abfragen der aktuellen Zeit und auf Stunden und Minuten aufteilen
            hours, minutes = get_current_time()
            
            # Abfragen, welche Stunde aktuell ist aktuelle Zeit anzeigen lassen
            hour_set(strip, hours, minutes)
            
            # Get temperature
            get_temperature(STORE_PATH)
            

            # if CHECK_STR == str(ping(HOST_IP, verbose=False, count=1))[:36]:
            #     shutil.copyfile(STORE_PATH, TARGET_PATH)


    except KeyboardInterrupt:
        if args.clear:
            color_wipe(strip, Color(0,0,0), 0)
            
