__author__ = 'Pirmin'

from MCP23017 import MCP23017
from Led import RGBLed

class Table(object):
    def __init__(self):
        self.grid = []
        for address in [0x20, 0x21, 0x22, 0x24]:
            row = []
            mcp = MCP23017(address)
            row.append(RGBLed(mcp, 2,3,4))
            row.append(RGBLed(mcp, 5,6,7))
            row.append(RGBLed(mcp, 8,9,10))
            row.append(RGBLed(mcp, 11,12,13))
            self.grid.append(row)

    def set_led(self, x, y, r, g, b):
        self.grid[x][y].set_color(r,g,b)

    def reset(self):
        for x in range(0,len(self.grid)):
            for y in range(0, len(self.grid[x])):
                self.grid[x][y].turn_off()

if __name__ == '__main__':
    table = Table()
    table.set_led(0,0,1,0,0)