import pygame

from pygame.math import Vector2

from constants import (
    Colors,
    Screen,
)

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)


    def draw(self, screen):
        for block in self.body:
            snake = pygame.Rect(
                int(block.x * Screen.CELL_SIZE.value),
                int(block.y * Screen.CELL_SIZE.value),
                int(Screen.CELL_SIZE.value),
                int(Screen.CELL_SIZE.value)
            )

            pygame.draw.rect(screen, Colors.LIGHT_SKY_BLUE.value, snake)

    
    def move(self):
        new_body = self.body[:-1]
        new_body.insert(0, self.body[0] + self.direction)
        self.body = new_body