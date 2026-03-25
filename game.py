import sys
import pygame

from fruit import Fruit
from snake import Snake
from constants import WIDTH, HEIGHT, CELL_SIZE, CELL_NUMBER

class Game:
    def __init__(self, apple, head_up, head_down, head_left, head_right,
                 tail_up, tail_down, tail_left, tail_right,
                 body_vertical, body_horizontal, body_left,
                 body_right, body_tail_left, body_tail_right):
        
        self.snake = Snake(head_up, head_down, head_left, head_right,
                           tail_up, tail_down, tail_left, tail_right,
                           body_vertical, body_horizontal, body_left,
                           body_right, body_tail_left, body_tail_right)
        
        self.fruit = Fruit(apple)


    def update(self):
        self.snake.slither()
        self.ate_fruit()

        if self.check_collision():
            pygame.quit()
            sys.exit()


    def draw(self, screen):
        self.draw_grid(screen)
        self.fruit.draw(screen)
        self.snake.draw(screen)


    def ate_fruit(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()

            self.snake.grow()


    def check_collision(self):
        if (not 0 <= self.snake.body[0].x < CELL_NUMBER or
            not 0 <= self.snake.body[0].y < CELL_NUMBER):
            return True

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                return True

        return False
    

    def draw_grid(self, screen):
        grass = (1, 46, 11)
        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE,
                                                 CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass, grass_rect)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE,
                                                 CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass, grass_rect)
