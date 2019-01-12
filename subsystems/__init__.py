
import wpilib

from .drivetrain import DriveTrain
from .sensors import Sensors

from networktables import NetworkTables

import oi
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

def inputNoise(input): 
    if(abs(input) < 0.02):
        input = 0
    return input

def dump_info():
    smartdashboard.putNumber("Distance Sensor", sensors.get_distance())
    smartdashboard.putNumber("Joystick-X", oi.joystick.getX())
    smartdashboard.putNumber("Joystick-Y", oi.joystick.getY())
    smartdashboard.putNumber("Joystick-Z", oi.joystick.getZ())

    smartdashboard.putNumber("Trunc-Joystick-X", inputNoise(oi.joystick.getX()))
    smartdashboard.putNumber("Trunc-Joystick-Y", inputNoise(oi.joystick.getY()))
    smartdashboard.putNumber("Trunc-Joystick-Z", inputNoise(oi.joystick.getZ()))
    #wpilib.LiveWindow.run()
