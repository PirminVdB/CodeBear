__author__ = 'Pirmin'
from DOM.Led import Led
from TECH import Enum

class RGBLed(object):

    def __init__(self, mcp, red_pin, green_pin, blue_pin):
        self.mcp = mcp
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        self.turn_off()

    def set_color(self, red, green, blue):
        self.mcp.output(self.red_pin, red)
        self.mcp.output(self.green_pin, green)
        self.mcp.output(self.blue_pin, blue)

    def turn_off(self):
        self.set_color(False, False, False)
'''
    def __set_red(self, value):
        assert value == True or value == False , "red led value should be a boolean"
        if value:
            self.red.turn_on()
        else:
            self.red.turn_off()

    def __set_green(self, value):
        assert value == True or value == False , "green led value should be a boolean"
        if value:
            self.green.turn_on()
        else:
            self.green.turn_off()

    def __set_blue(self, value):
        assert value == True or value == False , "blue led value should be a boolean"
        if value:
            self.blue.turn_on()
        else:
            self.blue.turn_off()

    def get_red(self):
        return self.red.get_brightness()>0

    def get_green(self):
        return self.green.get_brightness()>0

    def get_blue(self):
        return self.blue.get_brightness()>0'''