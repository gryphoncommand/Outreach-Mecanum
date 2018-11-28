
import wpilib

from .drivetrain import DriveTrain
from .sensors import Sensors

from networktables import NetworkTables

import robotmap

drivetrain = None
sensors = None
smartdashboard = None

is_init = False


def init():
    """

    instansiates all subsystems. Needs to be a method so it isn't ran on import

    """
    global drivetrain; global is_init; global sensors; global smartdashboard
    drivetrain = DriveTrain()
    sensors = Sensors()
    smartdashboard = NetworkTables.getTable('SmartDashboard')


def dump_info():
    smartdashboard.putNumber("Distance Sensor", sensors.get_distance())

    wpilib.LiveWindow.run()
