__author__ = 'Pirmin'

MAX_BRIGHTNESS = 255
MIN_BRIGHTNESS = 0

class Led(object):

    def __init__(self):
        self.brightness = MIN_BRIGHTNESS

    def set_color(self, red, green, blue):
        self.set_red(red)
        self.set_green(green)
        self.set_blue(blue)

    def set_brightness(self, brightness):
        assert MIN_BRIGHTNESS <= brightness <= MAX_BRIGHTNESS  , "brightness of led %s is invalid, brightness must be between %s and %s with borders" % (brightness, MIN_BRIGHTNESS, MAX_BRIGHTNESS)
        self.brightness = brightness

    def get_brightness(self):
        return self.red

    def turn_off(self):
        self.set_brightness(MIN_BRIGHTNESS)

    def turn_on(self):
        self.set_brightness(MAX_BRIGHTNESS)