import wpilib

from wpilib.command import Command
import subsystems
import math
import robotmap
from commands.mecdrivetimed import MecDriveTimed

class CrossBow(Command):
    def __init__(self):
        super().__init__('CrossBow')
        self.default = False
        subsystems.drivetrain.set_crossbow(wpilib.DoubleSolenoid.Value.kOff)

    def execute(self):
        print('In Crossbow::execute()')
        print(self.default)
        if self.default:
            subsystems.drivetrain.set_crossbow(wpilib.DoubleSolenoid.Value.kForward)
        else:
            subsystems.drivetrain.set_crossbow(wpilib.DoubleSolenoid.Value.kReverse)
        self.default = not self.default
        self.isDone = True
    
    def isFinished(self):
        return self.isDone