__author__ = 'Pirmin'

class RGBLed(object):

    def __init__(self):
        self.red = False
        self.green = False
        self.blue = False

    def set_color(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue