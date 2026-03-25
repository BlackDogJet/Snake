import sys
import pygame

from fruit import Fruit
from snake import Snake
from constants import CELL_NUMBER

class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()


    def update(self):
        self.snake.move()
        self.ate_fruit()

        if self.check_collision():
            pygame.quit()
            sys.exit()


    def draw(self, screen):
        self.fruit.draw(screen)
        self.snake.draw(screen)


    def ate_fruit(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()

            self.snake.grow()


    def check_collision(self):
        if (
            not 0 <= self.snake.body[0].x < CELL_NUMBER or
            not 0 <= self.snake.body[0].y < CELL_NUMBER
        ):
            return True

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                return True

        return False
        