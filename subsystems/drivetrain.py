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


        self.frontLeftMotor = ctre.WPI_TalonSRX(channels.frontLeftChannel)
        self.rearLeftMotor = ctre.WPI_TalonSRX(channels.rearLeftChannel)
        self.frontRightMotor = ctre.WPI_TalonSRX(channels.frontRightChannel)
        self.rearRightMotor = ctre.WPI_TalonSRX(channels.rearRightChannel)

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

    def set(self, ySpeed, xSpeed, zRotation, gyroAngle):
        self.drive.driveCartesian(ySpeed, xSpeed, zRotation, gyroAngle)