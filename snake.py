import pygame

from pygame.math import Vector2

from constants import (
    CELL_SIZE,
    LIGHT_SKY_BLUE,
)

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)


    def draw(self, screen):
        for block in self.body:
            snake = pygame.Rect(
                int(block.x * CELL_SIZE),
                int(block.y * CELL_SIZE),
                int(CELL_SIZE),
                int(CELL_SIZE)
            )

            pygame.draw.rect(screen, LIGHT_SKY_BLUE, snake)

    
    def move(self):
        new_body = self.body[:-1]
        new_body.insert(0, self.body[0] + self.direction)
        self.body = new_body


    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)