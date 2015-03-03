__author__ = 'Pirmin'

from Led import RGBLed

grid_width = 4
grid_heigth = 4

class Table(object):

    def __init__(self):
        self.grid = []
        for x in range(0,grid_width):
            row = []
            for y in range(0,grid_heigth):
                row.append(RGBLed())
            self.grid.append(row)