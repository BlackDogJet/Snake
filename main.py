import sys
import pygame

from game import Game
from pygame.math import Vector2

from constants import (
    WIDTH,
    HEIGHT,
)


def main():
    pygame.init()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Background graphics
    background = pygame.image.load("graphics/background.png").convert_alpha()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Fruit graphics
    apple = pygame.image.load("graphics/apple.png").convert_alpha()
        
    # Snakes graphics
    head_up = pygame.image.load("graphics/head_up.png").convert_alpha()
    head_down = pygame.image.load("graphics/head_down.png").convert_alpha()
    head_left = pygame.image.load("graphics/head_left.png").convert_alpha()
    head_right = pygame.image.load("graphics/head_right.png").convert_alpha()

    tail_up = pygame.image.load("graphics/tail_up.png").convert_alpha()
    tail_down = pygame.image.load("graphics/tail_down.png").convert_alpha()
    tail_left = pygame.image.load("graphics/tail_left.png").convert_alpha()
    tail_right = pygame.image.load("graphics/tail_right.png").convert_alpha()

    body_vertical = pygame.image.load("graphics/body_vertical.png").convert_alpha()
    body_horizontal = pygame.image.load("graphics/body_horizontal.png").convert_alpha()

    body_bottom_left = pygame.image.load("graphics/body_bottom_left.png").convert_alpha()
    body_bottom_right = pygame.image.load("graphics/body_bottom_right.png").convert_alpha()
    body_top_left = pygame.image.load("graphics/body_top_left.png").convert_alpha()
    body_top_right = pygame.image.load("graphics/body_top_right.png").convert_alpha()

    game = Game(apple, head_up, head_down, head_left, head_right,
                tail_up, tail_down, tail_left, tail_right,
                body_vertical, body_horizontal, body_bottom_left,
                body_bottom_right, body_top_left, body_top_right)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                game.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if game.snake.direction != Vector2(0, 1):
                        game.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if game.snake.direction != Vector2(0, -1):
                        game.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if game.snake.direction != Vector2(1, 0):
                        game.snake.direction = Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if game.snake.direction != Vector2(-1, 0):
                        game.snake.direction = Vector2(1, 0)

        screen.blit(background, (0, 0))
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()        