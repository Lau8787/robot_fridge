#!/usr/bin/env python3

import time
import typing as t

import adafruit_ads1x15.ads1015 as ADS
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn

from read_adc import p0 as y_axis
from read_adc import p1 as x_axis


class Point(t.NamedTuple):
    x: int
    y: int


class Joystick:
    @property
    def value(self):
        return Point(
            self.x_axis.value - self.x_offset,
            self.y_axis.value - self.y_offset,
        )

    def __init__(
        self,
        x_axis,
        y_axis,
    ) -> None:
        self.x_axis = x_axis
        self.y_axis = y_axis

        # X-axis: 13232; Y-axis: 12992
        self.x_offset = x_axis.value
        self.y_offset = y_axis.value


def main() -> None:

    my_joystick = Joystick(x_axis, y_axis)

    while True:
        # print("{:>5}\t{:>5.3f}".format(x_axis.value, x_axis.voltage))
        # print("{:>5}\t{:>5.3f}".format(y_axis.value, y_axis.voltage))

        # print(f"X-axis: {x_axis.value}; Y-axis: {y_axis.value}")
        print(my_joystick.value)

        time.sleep(0.005)
