import wpilib
from ctre import WPI_TalonSRX
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


        self.frontLeftMotor = WPI_TalonSRX(channels.frontLeftChannel)
        self.rearLeftMotor = WPI_TalonSRX(channels.rearLeftChannel)
        self.frontRightMotor = WPI_TalonSRX(channels.frontRightChannel)
        self.rearRightMotor = WPI_TalonSRX(channels.rearRightChannel)
        
        self.crossbow = wpilib.DoubleSolenoid(0, 1)
        self.crossbow.set(wpilib.DoubleSolenoid.Value.kOff)
        self.frontLeftMotor.setInverted(False)

        # self.rearLeftMotor.configSelectedFeedbackSensor(WPI_TalonSRX.FeedbackDevice.CTRE_MagEncoder_Relative, 0, 30)

        # you may need to change or remove this to match your robot
        self.rearLeftMotor.setInverted(False)

        self.drive = MecanumDrive(self.frontLeftMotor,
                                         self.rearLeftMotor,
                                         self.frontRightMotor,
                                         self.rearRightMotor)

        self.drive.setExpiration(0.1)

        self.drive.setSafetyEnabled(True)
     #   self.motor = wpilib.Talon(1)

    def driveCartesian(self, ySpeed, xSpeed, zRotation, gyroAngle=0.0):
        self.drive.driveCartesian(ySpeed, xSpeed, zRotation, gyroAngle)


    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())

    def set_crossbow(self, setting):
        if setting:
            self.crossbow.set(wpilib.DoubleSolenoid.Value.kForward)
        else:
            self.crossbow.set(wpilib.DoubleSolenoid.Value.kReverse)

    def set(self, ySpeed, xSpeed, zRotation, gyroAngle):
        self.drive.driveCartesian(ySpeed, xSpeed, zRotation, gyroAngle)