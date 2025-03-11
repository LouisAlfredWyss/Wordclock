# File containing all constants to run the wordclock

import numpy as np

# LED strip configuration:
LED_COUNT      = 121      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Vektoren mit LED-Positionen zur jeweiligen Stunde
VEC_1 = [92, 104, 113]
VEC_2 = [5, 16, 27, 38]
VEC_3 = [3, 18, 25]
VEC_4 = [19, 24, 41, 46, 63]
VEC_5 = [1, 20, 23, 42]
VEC_6 = [60, 71, 82, 93, 103, 114]
VEC_7 = [0, 21, 22, 43, 44, 65]
VEC_8 = [66, 87, 88, 108, 109]
VEC_9 = [85, 90, 106, 111]
VEC_10 = [47, 62, 69, 84, 91]
VEC_11 = [17, 26, 39, 48]
VEC_12 = [64, 67, 86, 89, 107, 110]

# Vektor mit LED-Positionen zu den uebrigen Worten
VEC_ES_ISCH = [33, 54, 55, 76, 98, 119]
VEC_VOR = [14, 29, 36]
VEC_VIERTEL = [9, 12, 31, 34, 53, 56, 75]
VEC_UEBER = [58, 73, 80, 95]
VEC_HALBI = [15, 28, 37, 50, 59]
VEC_AB = [94 ,102]
VEC_FUEF = [97, 99, 118]
VEC_ZAEH = [96, 100, 117]
VEC_ZWAENZG = [13, 30, 35, 52, 57,74]

# Vekoren mit LED-Positionen zur jeweiligen Minute
VEC_5_10 = np.concatenate([VEC_FUEF, VEC_AB])
VEC_10_15 = np.concatenate([VEC_ZAEH, VEC_AB])
VEC_15_20 = np.concatenate([VEC_VIERTEL, VEC_AB])
VEC_20_25 = np.concatenate([VEC_ZWAENZG, VEC_AB])
VEC_25_30 = np.concatenate([VEC_FUEF, VEC_VOR, VEC_HALBI])
VEC_30_35 = VEC_HALBI
VEC_35_40 = np.concatenate([VEC_FUEF, VEC_UEBER, VEC_HALBI])
VEC_40_45 = np.concatenate([VEC_ZWAENZG, VEC_VOR])
VEC_45_50 = np.concatenate([VEC_VIERTEL, VEC_VOR])
VEC_50_55 = np.concatenate([VEC_ZAEH, VEC_VOR])
VEC_55_60 = np.concatenate([VEC_FUEF, VEC_VOR])
