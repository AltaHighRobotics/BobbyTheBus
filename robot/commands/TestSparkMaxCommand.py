from commands2.command import Command
from subsystems.BasicSparkMaxSubsystem import BasicSparkMaxSubsystem

class TestSparkMaxCommand(Command):
    def __init__(self, sparkmaxSubsystem: BasicSparkMaxSubsystem) -> None:
        super().__init__()
        self.turn = sparkmaxSubsystem

    def execute(self) -> None:
        self.turn.testTurn()
