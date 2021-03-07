#!/usr/bin/env python3

# External module imports
import RPi.GPIO as GPIO
import typing as t
import time


class RGB(t.NamedTuple):
    red: int
    green: int
    blue: int


# rgb = collections.namedtuple(
#     "rgb",
#     [
#         "red",
#         "green",
#         "blue",
#     ],
# )


def init_pin(pin: int, duty_cycle=50) -> GPIO.PWM:
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, duty_cycle)
    pwm.start(0)
    return pwm


def set_rgb(rgb_values: RGB, pwms: t.Dict[str, GPIO.PWM]) -> None:

    print("Turning RGB LED on!")
    pwms["red"].ChangeDutyCycle(rgb_values.red)
    pwms["green"].ChangeDutyCycle(rgb_values.green)
    pwms["blue"].ChangeDutyCycle(rgb_values.blue)


def main() -> None:

    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BroadOUT

    # Pin Definitons:
    pwms = {
        "red": init_pin(17),
        "green": init_pin(27),
        "blue": init_pin(22),
    }

    set_rgb(
        RGB(
            0,
            100,
            0,
        ),
        pwms,
    )

    time.sleep(5)


if __name__ == "__main__":
    try:
        main()
    finally:
        GPIO.cleanup()  # cleanup all GPIO
