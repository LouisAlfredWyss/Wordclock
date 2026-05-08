# Wordclock

Description and code of my Swiss-German Wordclock.

This project uses a Raspberry Pi to control a matrix of 121 WS281x LEDs (NeoPixels). It displays the current time using illuminated words in Swiss-German dialect (e.g., "Es isch viertel vor drüü").

The repository contains the Python code required to drive the LED matrix, as well as the mechanical and electrical files needed to physically build the clock (PCB layouts and laser cutting templates in the `mechanics/` folder).

## Hardware
* Raspberry Pi
* WS281x LED Strip (121 LEDs)
* Custom PCB and laser-cut casing

## Requirements
The project relies on the `rpi_ws281x` and `numpy` Python libraries.

```bash
sudo pip3 install rpi_ws281x numpy
```

## Running the Application
The `rpi_ws281x` library uses PWM via GPIO pin 18 by default, which requires root privileges.

To run the clock, execute the script in the `src/` folder:

```bash
sudo python3 src/main.py
```

### Options
* `-c` or `--clear`: Clears the LED display when the script exits (e.g., via Ctrl+C).

```bash
sudo python3 src/main.py -c
```
