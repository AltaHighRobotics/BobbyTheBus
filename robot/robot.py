from commands2 import TimedCommandRobot
from RobotContainer import RobotContainer

class MyRobot(TimedCommandRobot):
    def robotInit(self) -> None:
        self.container = RobotContainer()
