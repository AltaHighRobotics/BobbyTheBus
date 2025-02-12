from constants import DRIVER_CONTROLLER_PORT

from subsystems.BasicSparkMaxSubsystem import BasicSparkMaxSubsystem
from commands.TestSparkMaxCommand import TestSparkMaxCommand
from wpilib import XboxController
from commands2.button import JoystickButton

class RobotContainer:
    def __init__(self) -> None:
        self.driverController = XboxController(DRIVER_CONTROLLER_PORT)

        self.spark = BasicSparkMaxSubsystem()

        JoystickButton(self.driverController, 5).whileTrue(TestSparkMaxCommand(self.spark))

