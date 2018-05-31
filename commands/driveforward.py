import wpilib

from wpilib.command import CommandGroup
import subsystems
import math
import robotmap
from commands.mecdrivetimed import MecDriveTimed

class DriveForward(CommandGroup):
    def __init__(self):
        super().__init__('DriveForward')

        self.addSequential(MecDriveTimed(ySpeed=.5, xSpeed=.4, zRotation=1, gyroAngle=0, tlen = 5))
        self.addSequential(MecDriveTimed(ySpeed=1, xSpeed=.1, zRotation=.8, gyroAngle=0, tlen = 5))