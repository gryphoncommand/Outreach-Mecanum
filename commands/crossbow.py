import wpilib

from wpilib.command import Command
import subsystems
import math
import robotmap
from commands.mecdrivetimed import MecDriveTimed

class CrossBow(Command):
    def __init__(self, setting):
        super().__init__('CrossBow')
        self.setting = setting

    def execute(self):
        subsystems.drivetrain.set_crossbow(self.setting)