from enum import Enum


class Tile(Enum):
    SAND = 0
    AIR = 1
    SOURCE = 2
    ROCK = 3

    def __str__(self):
        if self.value == 0:
            return "o"
        elif self.value == 1:
            return "."
        elif self.value == 2:
            return "+"
        else:
            return "#"
