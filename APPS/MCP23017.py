#!/usr/bin/python

from APPS.Adafruit_I2C import Adafruit_I2C
import time

MCP23017_IODIRA = 0x00
MCP23017_IODIRB = 0x01
MCP23017_GPIOA  = 0x12
MCP23017_GPIOB  = 0x13
MCP23017_GPPUA  = 0x0C
MCP23017_GPPUB  = 0x0D
MCP23017_OLATA  = 0x14
MCP23017_OLATB  = 0x15

class MCP23017(object):
  def __init__(self, address, busnum=-1):
    self.i2c = Adafruit_I2C(address=address, busnum=busnum)
    self.address = address
    self.num_gpios = 16

    self.i2c.write8(MCP23017_IODIRA, 0xFF)  # all inputs on port A
    self.i2c.write8(MCP23017_IODIRB, 0xFF)  # all inputs on port B
    self.direction = self.i2c.readU8(MCP23017_IODIRA)
    self.direction |= self.i2c.readU8(MCP23017_IODIRB) << 8
    self.i2c.write8(MCP23017_GPPUA, 0x00)
    self.i2c.write8(MCP23017_GPPUB, 0x00)

  def set_pin_to_output(self, pin):
    return __config(pin, 0)

  def set_pin_to_input(self, pin):
    return __config(pin, 1)

  def __config(self, pin, mode):
    if pin < 8:
      self.direction = self._read_and_change_pin(MCP23017_IODIRA, pin, mode)
    else:
      self.direction |= self._read_and_change_pin(MCP23017_IODIRB, pin-8, mode) << 8
    return self.direction

  def output(self, pin, value):
    assert 0 <= pin < self.num_gpios, "Pin number %s is invalid, only 0-%s are valid" % (pin, self.num_gpios)
    assert self.direction & (1 << pin) == 0, "Pin %s not set to output" % pin
    if pin < 8:
      output_value = self._read_and_change_pin(MCP23017_GPIOA, pin, value, self.i2c.readU8(MCP23017_OLATA))
    else:
      output_value = self._read_and_change_pin(MCP23017_GPIOB, pin-8, value, self.i2c.readU8(MCP23017_OLATB)) << 8
    return output_value

  def input(self, pin):
    assert 0 <= pin < self.num_gpios, "Pin number %s is invalid, only 0-%s are valid" % (pin, self.num_gpios)
    assert self.direction & (1 << pin) != 0, "Pin %s not set to input" % pin
    value = self.i2c.readU8(MCP23017_GPIOA)
    value |= self.i2c.readU8(MCP23017_GPIOB) << 8
    return value & (1 << pin)

  def _read_and_change_pin(self, port, pin, value, current_value = None):
    assert 0 <= pin < self.num_gpios, "Pin number %s is invalid, only 0-%s are valid" % (pin, self.num_gpios)
    if not current_value:
      current_value = self.i2c.readU8(port)
    new_value = self._change_bit(current_value, pin, value)
    self.i2c.write8(port, new_value)
    return newvalue

  def _change_bit(self, bitmap, bit, value):
    assert value == 1 or value == 0, "Value is %s must be 1 or 0" % value
    if value == 0:
      return bitmap & ~(1 << bit)
    elif value == 1:
      return bitmap | (1 << bit)

if __name__ == '__main__':
  mcp = MCP23017(address = 0x20)
  mcp2 = MCP23017(address = 0x21)
  mcp3 = MCP23017(address = 0x22)
  mcp4 = MCP23017(address = 0x24)

  for i in range(0,15):
    mcp.config(i, 0)
    mcp2.config(i, 0)
    mcp3.config(i, 0)
    mcp4.config(i, 0)

  try:
    while True:
      for i in range(2,14):
        mcp.output(i, 1)  # Pin 0 High
        time.sleep(1)
        mcp.output(i,0)
      for i in range(2,14):
        mcp2.output(i, 1)  # Pin 0 High
        time.sleep(1)
        mcp2.output(i,0)
      for i in range(2,14):
        mcp3.output(i, 1)  # Pin 0 High
        time.sleep(1)
        mcp3.output(i,0)
      for i in range(2,14):
        mcp4.output(i, 1)  # Pin 0 High
        time.sleep(1)
        mcp4.output(i,0)

      for i in range(2,14):
        mcp.output(i, 1)  # Pin 0 High
        time.sleep(0.2)
      for i in range(2,14):
        mcp2.output(i, 1)  # Pin 0 High
        time.sleep(0.2)
      for i in range(2,14):
        mcp3.output(i, 1)  # Pin 0 High
        time.sleep(0.2)
      for i in range(2,14):
        mcp4.output(i, 1)  # Pin 0 High
        time.sleep(0.2)
  except KeyboardInterrupt:
    for i in range(2,14):
      mcp.output(i,0)
      mcp2.output(i,0)
      mcp3.output(i,0)
      mcp4.output(i,0)