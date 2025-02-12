from constants import FRONT_RIGHT_TURN_ID, SWERVE_TURN_GEAR_RATIO
from constants import MODULE_MAX_ANGULAR_VELOCITY, MODULE_MAX_ANGULAR_ACCELERATION
from constants import TURN_FRONT_RIGHT_P, TURN_FRONT_RIGHT_I, TURN_FRONT_RIGHT_D

from rev import SparkMax, SparkLowLevel
from commands2 import Subsystem
from wpimath.controller import ProfiledPIDController
from wpimath.trajectory import TrapezoidProfile
from math import tau, pi


class BasicSparkMaxSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()

        # We are going to use front right motor controller
        self.turn = SparkMax(FRONT_RIGHT_TURN_ID, SparkLowLevel.MotorType.kBrushless)

        self.turningPIDController = ProfiledPIDController(
            TURN_FRONT_RIGHT_P,
            TURN_FRONT_RIGHT_I,
            TURN_FRONT_RIGHT_D,
            TrapezoidProfile.Constraints(
                MODULE_MAX_ANGULAR_VELOCITY,
                MODULE_MAX_ANGULAR_ACCELERATION,
            ),
        )  # Turn PID controller

    def testTurn(self) -> None:
        turnOutput = self.turningPIDController.calculate(
            self.turnEncoder.getPosition() * tau * SWERVE_TURN_GEAR_RATIO,
            pi,  # used to use state.angle and not pi
        )
        self.turn.setVoltage(turnOutput)
