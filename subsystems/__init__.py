
import wpilib

from .drivetrain import DriveTrain

import robotmap

drivetrain = None

is_init = False


def init():
    """

    instansiates all subsystems. Needs to be a method so it isn't ran on import

    """
    global drivetrain; global is_init
    drivetrain = DriveTrain()
