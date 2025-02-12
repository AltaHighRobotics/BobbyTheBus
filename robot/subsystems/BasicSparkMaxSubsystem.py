from constants import FRONT_RIGHT_TURN_ID, SWERVE_TURN_GEAR_RATIO

from rev import SparkMax, SparkLowLevel
from commands2 import Subsystem
from math import tau, pi

class BasicSparkMaxSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()

        # We are going to use front right motor controller
        self.turn = SparkMax(FRONT_RIGHT_TURN_ID, SparkLowLevel.MotorType.kBrushless)

    def testTurn(self) -> None:
        turnOutput = self.turningPIDController.calculate(
            self.turnEncoder.getPosition() * tau * SWERVE_TURN_GEAR_RATIO, pi # used to use state.angle and not pi
        )
        self.turn.setVoltage(turnOutput)
