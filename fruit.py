import pygame
import random

from pygame.math import Vector2

from constants import (
    Screen,
    Colors
)


class Fruit:
    def __init__(self):
        self.randomize()

    def draw(self, screen):
        fruit = pygame.Rect(
            int(self.position.x * Screen.CELL_SIZE.value),
            int(self.position.y * Screen.CELL_SIZE.value),
            int(Screen.CELL_SIZE.value),
            int(Screen.CELL_SIZE.value)
        )

        pygame.draw.rect(screen, Colors.RED.value, fruit)


    def randomize(self):
        self.x = random.randint(0, Screen.CELL_NUMBER.value - 1)
        self.y = random.randint(0, Screen.CELL_NUMBER.value - 1)
        self.position = Vector2(self.x, self.y)