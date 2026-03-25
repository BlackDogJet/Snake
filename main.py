import sys
import pygame

from game import Game
from pygame.math import Vector2

from constants import (
    Screen,
    Colors,
)


def main():
    pygame.init()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Screen.WIDTH.value, Screen.HEIGHT.value))

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                game.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    game.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    game.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    game.snake.direction = Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    game.snake.direction = Vector2(1, 0)

        screen.fill(Colors.LIME.value)
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()        