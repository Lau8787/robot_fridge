from adafruit_motor.motor import DCMotor  # type: ignore
from adafruit_motor.stepper import StepperMotor  # type: ignore
from adafruit_motorkit import MotorKit  # type: ignore


class RobotFridge:
    _front_left: DCMotor
    _rear_left: DCMotor
    _front_right: DCMotor
    _rear_right: DCMotor

    @classmethod
    def from_kit(cls, kit: MotorKit) -> 'RobotFridge':
        return cls(kit.motor1, kit.motor2, kit.motor3, kit.motor4) 

    def __init__(
        self, 
        front_left: DCMotor,
        front_right: DCMotor,
        rear_left: DCMotor,
        rear_right: DCMotor,
    ) -> None:
        self._front_left = front_left
        self._front_right = front_right
        self._rear_left = rear_left
        self._rear_right = rear_right

    def _set_left(self, throttle: float = 1) -> None:
        self._front_left.throttle = throttle
        self._front_right.throttle = throttle

    def _set_right(self, throttle: float = 1) -> None:
        self._rear_left.throttle = throttle
        self._rear_right.throttle = throttle

    def move_forward(self, throttle: float = 1) -> None:
        self._set_left(throttle)
        self._set_right(throttle)

    def move_backward(self, throttle: float = 1) -> None:
        self.move_forward(-throttle)

    def rotate_left(self, throttle: float = 1) -> None:
        self._set_left(throttle)
        self._set_right(-throttle)

    def rotate_right(self, throttle: float = 1) -> None:
        self.rotate_left(-throttle)

    def halt(self) -> None:
        self._set_left(0)
        self._set_right(0)


class RobotFridgeArm:
    _base_front: StepperMotor
    _base_back: StepperMotor
    # _front_right: StepperMotor
    # _rear_right: StepperMotor

    def __init__(
        self,
        base_front: StepperMotor,
        base_back: StepperMotor,
    ) -> None:
        self._base_front = base_front
        self._base_back = base_back
        # self._rear_left = self._kit.motor3
        # self._rear_right = self._kit.motor4
