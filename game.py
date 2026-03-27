import sys
import pygame

from fruit import Fruit
from snake import Snake

from constants import (
    GRASS,
    WHITE,
    OFFSET,
    WIDTH,
    HEIGHT,
    CELL_SIZE,
    CELL_NUMBER,
)

class Game:
    def __init__(self, font, crash_sound, eat_sound, apple,
                 head_up, head_down, head_left, head_right,
                 tail_up, tail_down, tail_left, tail_right,
                 body_vertical, body_horizontal, body_left,
                 body_right, body_tail_left, body_tail_right):
        
        self.font = font
        self.eat_sound = eat_sound
        self.crash_sound = crash_sound
        
        self.snake = Snake(head_up, head_down, head_left, head_right,
                           tail_up, tail_down, tail_left, tail_right,
                           body_vertical, body_horizontal, body_left,
                           body_right, body_tail_left, body_tail_right)
        
        self.fruit = Fruit(apple)


    def update(self, screen):
        self.snake.slither()
        self.ate_fruit()

        if self.check_collision():
            self.crash_sound.play()
            self.game_over(screen)


    def draw(self, screen):
        self.draw_grid(screen)
        self.fruit.draw(screen)
        self.snake.draw(screen)
        self.score(screen)


    def ate_fruit(self):
        if self.fruit.position == self.snake.body[0]:
            self.eat_sound.play()
            self.fruit.randomize()
            self.snake.grow()

        for block in self.snake.body[1:]:
            if block == self.fruit.position:
                self.fruit.randomize()


    def check_collision(self):
        if (not 0 <= self.snake.body[0].x < CELL_NUMBER or
            not 0 <= self.snake.body[0].y < CELL_NUMBER):
            return True

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                return True

        return False
    

    def draw_grid(self, screen):
        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        x_pos = col * CELL_SIZE + OFFSET
                        y_pos = row * CELL_SIZE + OFFSET
                        grass_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, GRASS, grass_rect)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        x_pos = col * CELL_SIZE + OFFSET
                        y_pos = row * CELL_SIZE + OFFSET
                        grass_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, GRASS, grass_rect)


    def score(self, screen):
        # Score is the length of the snake's body minus the initial length (3)
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.font.render("Score: " + score_text, True, WHITE)
        score_rect = score_surface.get_rect(right=WIDTH - OFFSET, top=OFFSET - 40)

        # Position the apple to the left of the score
        apple_rect = self.fruit.apple.get_rect()
        apple_rect.right = score_rect.left - 10
        apple_rect.centery = score_rect.centery

        screen.blit(score_surface, score_rect)
        screen.blit(self.fruit.apple, apple_rect)


    def game_over(self, screen):
        game_over_text = self.font.render("Game Over", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)
        pygame.display.update()
        pygame.time.delay(2000)

        # Quit the game
        pygame.quit()
        sys.exit()