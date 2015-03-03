__author__ = 'Pirmin'
from DOM.Led import RGBLed

class RGBLed(object):

    def __init__(self):
        self.Led = RGBLed()

    def set_color(self, red, green, blue):
        self.__set_red(red)
        self.__set_green(green)
        self.__set_blue(blue)

    def __set_red(self, value):
        # TODO assert value is boolean, set DOM value accordingly
        self.Led.set_red()

    def __set_green(self):
        # TODO assert value is boolean, set DOM value accordingly
        return self.green

    def __set_blue(self):
        # TODO assert value is boolean, set DOM value accordingly
        return self.blue

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue