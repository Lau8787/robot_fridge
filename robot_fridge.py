from adafruit_motorkit import MotorKit  # type: ignore


def move_forward(kit: MotorKit, throttle: float = 1) -> None:
    kit.motor1.throttle = throttle
    kit.motor2.throttle = throttle
    kit.motor3.throttle = throttle
    kit.motor4.throttle = throttle


def move_backward(kit: MotorKit, throttle: float = 1) -> None:
    move_forward(kit, -throttle)


def rotate_left(kit: MotorKit, throttle: float = 1) -> None:
    kit.motor1.throttle = throttle
    kit.motor2.throttle = throttle
    kit.motor3.throttle = -throttle
    kit.motor4.throttle = -throttle


def rotate_right(kit: MotorKit, throttle: float = 1) -> None:
    rotate_left(kit, -throttle)
