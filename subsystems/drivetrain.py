import wpilib
from wpilib.command.subsystem import Subsystem
from robotmap import channels

from wpilib.drive import MecanumDrive
from commands.followjoystick import FollowJoystick


#from commands.followjoystick import FollowJoystick

class DriveTrain(Subsystem):
    '''
    This example subsystem controls a single Talon in PercentVBus mode.
    '''

    def __init__(self):
        '''Instantiates the motor object.'''

        super().__init__('SingleMotor')


        self.frontLeftMotor = wpilib.Talon(channels.frontLeftChannel)
        self.rearLeftMotor = wpilib.Talon(channels.rearLeftChannel)
        self.frontRightMotor = wpilib.Talon(channels.frontRightChannel)
        self.rearRightMotor = wpilib.Talon(channels.rearRightChannel)

        self.frontLeftMotor.setInverted(True)

        # you may need to change or remove this to match your robot
        self.rearLeftMotor.setInverted(True)

        self.drive = MecanumDrive(self.frontLeftMotor,
                                         self.rearLeftMotor,
                                         self.frontRightMotor,
                                         self.rearRightMotor);

        self.drive.setExpiration(0.1)

        self.drive.setSafetyEnabled(True)
     #   self.motor = wpilib.Talon(1)

    def driveCartesian(self, ySpeed, xSpeed, zRotation, gyroAngle=0.0):
        self.drive.driveCartesian(ySpeed, xSpeed, zRotation, gyroAngle)


    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())