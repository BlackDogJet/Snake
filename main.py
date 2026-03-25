import sys
import pygame

from fruit import Fruit
from snake import Snake
from pygame.math import Vector2

from constants import (
    Screen,
    Surface,
    Colors,
)


def main():
    pygame.init()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Screen.WIDTH.value, Screen.HEIGHT.value))

    fruit = Fruit()
    snake = Snake()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                snake.move()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.direction = Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake.direction = Vector2(1, 0)

        screen.fill(Colors.LIME.value)
        fruit.draw(screen)
        snake.draw(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()        