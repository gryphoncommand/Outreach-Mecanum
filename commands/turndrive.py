from wpilib.command import Command
import subsystems
import oi
import math
import wpilib

def inputNoise(input): 
    if(abs(input) < 0.02):
        input = 0
    return input

class TurnDrive(Command):
    '''
    This command will read the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.
    '''

    def __init__(self):
        super().__init__('Turn Drive')
        self.requires(subsystems.drivetrain)

    def execute(self):
        wpilib.SmartDashboard.putNumber(
            'velocity', subsystems.drivetrain.rearLeftMotor.getSelectedSensorVelocity(0) 
        )
        print("Velocity: ", subsystems.drivetrain.rearLeftMotor.getSelectedSensorVelocity(0))
        # print('X:' + str(oi.joystick.getX()), 
        #     'Y:' + str(inputNoise(oi.joystick.getY())),
        #     'Z:' + str(inputNoise(oi.joystick.getZ())))
      #  self.getRobot().motor.setSpeed(self.getRobot().joystick.getY())
      
    subsystems.drivetrain.driveCartesian(
        inputNoise(oi.joystick.getX()),
        inputNoise(oi.joystick.getY()),
        inputNoise(oi.joystick.getZ()), 0)
      # 0 is for the gyro

