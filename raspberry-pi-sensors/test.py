#!/usr/bin/env python3

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
line_tracker_pin = 23  # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(line_tracker_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        line_tracker_action = GPIO.input(line_tracker_pin)
        if line_tracker_action:
            print(f"Line tracker active: {line_tracker_action}")
        else:
            print(f"Line tracker not active: {line_tracker_action}")
        # print(line_tracker_action, end="")
        time.sleep(0.075)

except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup()  # cleanup all GPIO
