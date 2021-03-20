import sys
import time

from adafruit_motorkit import MotorKit  # type: ignore

from robot_fridge import RobotFridge


def main(argv):
    kit = MotorKit()
    bot = RobotFridge.from_kit(kit)

    try:
        while True:
            bot.move_forward()
            time.sleep(1)
            bot.move_backward()
            time.sleep(1)
            bot.rotate_left()
            time.sleep(1)
            bot.rotate_right()
            time.sleep(1)
    finally:
        bot.halt()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
