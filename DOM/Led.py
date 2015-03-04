__author__ = 'Pirmin'

MAX_BRIGHTNESS = 256

class Led(object):

    def __init__(self):
        self.brightness = 0

    def set_color(self, red, green, blue):
        self.set_red(red)
        self.set_green(green)
        self.set_blue(blue)

    def set_brightness(self, brightness):
        assert 0 <= brightness <= MAX_BRIGHTNESS  , "brightness of led %s is invalid, brightness must be between 0 and 256 with borders" % brightness
        self.brightness = brightness

    def get_brightness(self):
        return self.red

    def turn_off(self):
        self.set_brightness(0)

    def turn_on(self):
        self.set_brightness(MAX_BRIGHTNESS)