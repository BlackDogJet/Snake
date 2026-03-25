from turtle import Screen

import pygame
import random

from pygame.math import Vector2

from constants import (
    RED,
    CELL_SIZE,
    CELL_NUMBER,
)


class Fruit:
    def __init__(self):
        self.randomize()


    def draw(self, screen):
        fruit = pygame.Rect(
            int(self.position.x * CELL_SIZE),
            int(self.position.y * CELL_SIZE),
            int(CELL_SIZE),
            int(CELL_SIZE)
        )

        pygame.draw.rect(screen, RED, fruit)


    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.position = Vector2(self.x, self.y)