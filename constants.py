from enum import Enum


class Screen(Enum):
    CELL_SIZE = 40
    CELL_NUMBER = 20
    WIDTH = CELL_SIZE * CELL_NUMBER
    HEIGHT = CELL_SIZE * CELL_NUMBER


class Surface(Enum):
    X = 200
    Y = 250
    WIDTH = 100
    HEIGHT = 200


class Colors(Enum):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    LIME = (0, 255, 0)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    LIGHT_SKY_BLUE = (135, 206, 250)