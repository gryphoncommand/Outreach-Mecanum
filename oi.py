from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
from commands.crossbow import CrossBow

#from commands.crash import Crash
joystick = None

def init():
    global joystick
    joystick = Joystick(0)

    crossbow_open = JoystickButton(joystick, 1)

    
    crossbow_open.whenPressed(CrossBow())



# from mechanum drive - self.stick = wpilib.Joystick(self.joystickChannel)
