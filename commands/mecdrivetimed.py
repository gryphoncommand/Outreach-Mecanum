import time

from wpilib.command import Command

import subsystems
import oi
import time

class MecDriveTimed(Command):
    """

    Timed Mecaunum Drive

    """

    def __init__(self, ySpeed, xSpeed, zRotation, gyroAngle, tlen):
        super().__init__('TankDriveTimed')
        self.ySpeed, self.xSpeed, self.zRotation, self.gyroAngle, self.tlen = ySpeed, xSpeed, zRotation, gyroAngle, tlen

        self.requires(subsystems.drivetrain)
        self.stime = None

    def initialize(self):
        self.stime = time.time()

    def execute(self):
        subsystems.drivetrain.set(self.ySpeed, self.xSpeed, self.zRotation, self.gyroAngle)

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)
    
    def isFinished(self):
        return self.stime is not None and time.time() - self.stime > self.tlen

    def interrupted(self):
        self.end()
