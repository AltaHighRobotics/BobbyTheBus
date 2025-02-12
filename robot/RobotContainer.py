from constants import DRIVER_CONTROLLER_PORT

from wpilib import XboxController

class RobotContainer:
    def __init__(self) -> None:
        self.driverController = XboxController(DRIVER_CONTROLLER_PORT)
