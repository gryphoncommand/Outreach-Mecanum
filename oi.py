from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

#from commands.crash import Crash
joystick = None

def init():
    global joystick
    joystick = Joystick(0)



# from mechanum drive - self.stick = wpilib.Joystick(self.joystickChannel)
