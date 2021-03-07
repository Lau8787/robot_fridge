#!/usr/bin/env python3

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


def init_adc(
    i2c: busio.I2C = busio.I2C(board.SCL, board.SDA),
) -> ADS.ADS1015:

    # Create the ADC object using the I2C bus
    return ADS.ADS1015(i2c)


ads = init_adc()

# Create single-ended input on channel 0
p0 = AnalogIn(ads, ADS.P0)
p1 = AnalogIn(ads, ADS.P1)
p2 = AnalogIn(ads, ADS.P2)
p3 = AnalogIn(ads, ADS.P3)


def main() -> None:

    print("{:>5}\t{:>5}".format("raw", "v"))

    while True:
        # print("{:>5}\t{:>5.3f}".format(x_axis.value, x_axis.voltage))
        # print("{:>5}\t{:>5.3f}".format(y_axis.value, y_axis.voltage))

        print(f"P0: {p0.value}; P1-axis: {p1.value}; P2-axis: {p12value}; P3-axis: {p3.value}")

        time.sleep(0.005)


if __name__ == "__main__":
    main()
