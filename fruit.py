import pygame
import random

from pygame.math import Vector2

from constants import (
    OFFSET,
    CELL_SIZE,
    CELL_NUMBER,
)


class Fruit:
    def __init__(self, apple):
        self.apple = apple
        self.randomize()


    def draw(self, screen):
        x_pos = int(self.position.x * CELL_SIZE) + OFFSET
        y_pos = int(self.position.y * CELL_SIZE) + OFFSET
        fruit = pygame.Rect(
            x_pos,
            y_pos,
            CELL_SIZE,
            CELL_SIZE,
        )

        screen.blit(self.apple, fruit)


    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.position = Vector2(self.x, self.y)