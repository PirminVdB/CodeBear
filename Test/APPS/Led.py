__author__ = 'PirminVDB'

from unittest import TestCase
from APPS.Led import RGBLed

class TestRGBLed(TestCase):
    def test_contruction_of_led(self):
        led = RGBLed()
        self.assertFalse(led.get_red())
        self.assertFalse(led.get_green())
        self.assertFalse(led.get_blue())