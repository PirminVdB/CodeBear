__author__ = 'Pirmin'

class RGBLed(object):

    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def set_color(self, red, green, blue):
        self.set_red(red)
        self.set_green(green)
        self.set_blue(blue)

    def set_red(self, value):
        assert 0 <= value , "state of red %s is invalid, state must be an integer larger than or equal to 0" % value
        self.red = value

    def set_green(self, value):
        assert 0 <= value , "state of green %s is invalid, state must be an integer larger than or equal to 0" % value
        self.green = value

    def set_blue(self, value):
        assert 0 <= value , "state of blue %s is invalid, state must be an integer larger than or equal to 0" % value
        self.blue = value

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue