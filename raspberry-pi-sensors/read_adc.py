#!/usr/bin/env python3

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
x_axis = AnalogIn(ads, ADS.P1)
y_axis = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format("raw", "v"))

while True:
    # print("{:>5}\t{:>5.3f}".format(x_axis.value, x_axis.voltage))
    # print("{:>5}\t{:>5.3f}".format(y_axis.value, y_axis.voltage))

    print(f"X-axis: {x_axis.value}; Y-axis: {y_axis.value}")

    time.sleep(0.005)