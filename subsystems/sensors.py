import wpilib

from wpilib.command.subsystem import Subsystem 
#from hardware.navx import NavX
import robotmap

'''
A class for the various sensors on the robot. 
Currently includes Kauai Labs NavX.abs

Created on 1-20-2018 by Tyler Duckworth
'''

class Sensors(Subsystem):
    
    def __init__(self):
        super().__init__("Sensors")
        #self.navx = NavX(navx_type)
        # self.navx = None
        wpilib.LiveWindow.addSensor("Sensors", "PDP", wpilib.PowerDistributionPanel(0)) 
        self.ultrasonic = wpilib.AnalogInput(0)


    def get_pressure_sensor_voltage(self):
        return self.pressure_sensor.getVoltage()

    def get_pressure(self):
        # in PSI
        reading = self.pressure_sensor.getVoltage()
        #return 250*(reading/robotmap.solenoids.supply_voltage) - 25

    def get_distance(self):
        reading = self.ultrasonic.getVoltage()
        print(reading)
        return reading
