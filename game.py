import os
import sys
import json
import pygame

from pygame.math import Vector2

from menu import Menu
from fruit import Fruit
from snake import Snake
from settings import Settings

from constants import (
    RED, GRASS, SNAKE_BLACK_PATH, WHITE, WIDTH, HEIGHT, OFFSET, CELL_SIZE,
    ICON_PATH, FONT_PATH, SETTINGS_PATH, APPLE_PATH, CELL_NUMBER, BACKGROUND_PATH,
    SCREEN_UPDATE, HEAD_UP_PATH, HEAD_DOWN_PATH, HEAD_LEFT_PATH, HEAD_RIGHT_PATH,
    TAIL_UP_PATH, TAIL_DOWN_PATH, TAIL_LEFT_PATH, TAIL_RIGHT_PATH, BODY_VERTICAL_PATH,
    BODY_HORIZONTAL_PATH, BODY_TOP_LEFT_PATH, BODY_TOP_RIGHT_PATH, BODY_BOTTOM_LEFT_PATH,
    BODY_BOTTOM_RIGHT_PATH, EAT_SOUND_PATH, CRASH_SOUND_PATH, SNAKE_BLUE, SNAKE_BLACK,
    SNAKE_ORANGE, SNAKE_PURPLE, SNAKE_YELLOW, SNAKE_BLUE_PATH, SNAKE_BLACK_PATH,
    SNAKE_ORANGE_PATH, SNAKE_PURPLE_PATH, SNAKE_YELLOW_PATH,
)

class Game(Settings):
    def __init__(self):
        super().__init__()

        # Load settings
        self.load_settings()

        # Sound settings
        pygame.mixer.pre_init(44100, -16, 1, 512)

        # Initialize Pygame
        pygame.init()

        self.load_assets();

        self.snake = Snake(self.head_up, self.head_down, self.head_left, self.head_right,
                           self.tail_up, self.tail_down, self.tail_left, self.tail_right,
                           self.body_vertical, self.body_horizontal, self.body_bottom_left,
                           self.body_bottom_right, self.body_top_left, self.body_top_right)
        
        self.fruit = Fruit(self.apple)


    def load_assets(self):
        # Event for updating the screen
        pygame.time.set_timer(SCREEN_UPDATE, int(self.difficulty))

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.playing = False
        self.running = True

        # Caption
        pygame.display.set_caption("Snake Game")

        # Game Icon
        self.icon = pygame.image.load(ICON_PATH).convert_alpha()
        pygame.display.set_icon(self.icon)

        # Font
        self.font = pygame.font.Font(FONT_PATH, 32)

        # Sounds
        self.crash_sound = pygame.mixer.Sound(CRASH_SOUND_PATH)
        self.eat_sound = pygame.mixer.Sound(EAT_SOUND_PATH)

        # Background graphics
        self.background = pygame.image.load(BACKGROUND_PATH).convert_alpha()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        # Fruit graphics
        self.apple = pygame.image.load(APPLE_PATH).convert_alpha()

        # Snake image path
        if self.snake_color == SNAKE_YELLOW:
            snake_color_path = SNAKE_YELLOW_PATH
        elif self.snake_color == SNAKE_ORANGE:
            snake_color_path = SNAKE_ORANGE_PATH
        elif self.snake_color == SNAKE_BLUE:
            snake_color_path = SNAKE_BLUE_PATH
        elif self.snake_color == SNAKE_BLACK:
            snake_color_path = SNAKE_BLACK_PATH
        elif self.snake_color == SNAKE_PURPLE:
            snake_color_path = SNAKE_PURPLE_PATH

        print(snake_color_path)

        # Snakes graphics
        self.head_up = pygame.image.load(os.path.join(snake_color_path, HEAD_UP_PATH)).convert_alpha()
        self.head_down = pygame.image.load(os.path.join(snake_color_path, HEAD_DOWN_PATH)).convert_alpha()
        self.head_left = pygame.image.load(os.path.join(snake_color_path, HEAD_LEFT_PATH)).convert_alpha()
        self.head_right = pygame.image.load(os.path.join(snake_color_path, HEAD_RIGHT_PATH)).convert_alpha()

        self.tail_up = pygame.image.load(os.path.join(snake_color_path, TAIL_UP_PATH)).convert_alpha()
        self.tail_down = pygame.image.load(os.path.join(snake_color_path, TAIL_DOWN_PATH)).convert_alpha()
        self.tail_left = pygame.image.load(os.path.join(snake_color_path, TAIL_LEFT_PATH)).convert_alpha()
        self.tail_right = pygame.image.load(os.path.join(snake_color_path, TAIL_RIGHT_PATH)).convert_alpha()

        self.body_vertical = pygame.image.load(os.path.join(snake_color_path, BODY_VERTICAL_PATH)).convert_alpha()
        self.body_horizontal = pygame.image.load(os.path.join(snake_color_path, BODY_HORIZONTAL_PATH)).convert_alpha()

        self.body_bottom_left = pygame.image.load(os.path.join(snake_color_path, BODY_BOTTOM_LEFT_PATH)).convert_alpha()
        self.body_bottom_right = pygame.image.load(os.path.join(snake_color_path, BODY_BOTTOM_RIGHT_PATH)).convert_alpha()
        self.body_top_left = pygame.image.load(os.path.join(snake_color_path, BODY_TOP_LEFT_PATH)).convert_alpha()
        self.body_top_right = pygame.image.load(os.path.join(snake_color_path, BODY_TOP_RIGHT_PATH)).convert_alpha()


    def loop(self):
        while self.playing:
            self.get_events()

            if self.playing:
                self.screen.blit(self.background, (0, 0))

                # Border
                border_rect = pygame.Rect(
                    OFFSET - 10,
                    OFFSET - 10,
                    CELL_SIZE * CELL_NUMBER + 20,
                    CELL_SIZE * CELL_NUMBER + 20,
                )

                pygame.draw.rect(self.screen, GRASS, border_rect, 10)

                self.draw()

                # Title
                title_text = self.font.render("Snake Game", True, WHITE)
                title_rect = title_text.get_rect(left=OFFSET, top=OFFSET - 40)
                title_rect.topleft = (OFFSET, 10)

                high_score_text = self.font.render("High Score: " + str(self.high_score), True, WHITE)
                high_score_rect = high_score_text.get_rect(center=(WIDTH // 2, 30))

                self.screen.blit(title_text, title_rect)
                self.screen.blit(high_score_text, high_score_rect)

                pygame.display.update()
                self.clock.tick(60)


    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == SCREEN_UPDATE and self.playing:
                self.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.snake.direction != Vector2(0, 1):
                        self.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.snake.direction != Vector2(0, -1):
                        self.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if self.snake.direction != Vector2(1, 0):
                        self.snake.direction = Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if self.snake.direction != Vector2(-1, 0):
                        self.snake.direction = Vector2(1, 0)
                elif event.key == pygame.K_ESCAPE and self.playing:
                    quit()


    def update(self):
        self.snake.slither()
        self.ate_fruit()

        if self.check_collision():
            self.crash_sound.play()
            self.game_over()


    def draw(self):
        self.draw_grid()
        self.fruit.draw(self.screen)
        self.snake.draw(self.screen)
        self.score()


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
    

    def draw_grid(self):
        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        x_pos = col * CELL_SIZE + OFFSET
                        y_pos = row * CELL_SIZE + OFFSET
                        grass_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.screen, GRASS, grass_rect)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        x_pos = col * CELL_SIZE + OFFSET
                        y_pos = row * CELL_SIZE + OFFSET
                        grass_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.screen, GRASS, grass_rect)


    def score(self):
        # Score text
        score_text = self.get_score()
        score_surface = self.font.render("Score: " + str(score_text), True, WHITE)
        score_rect = score_surface.get_rect(right=WIDTH - OFFSET, top=10)

        # Position the apple to the left of the score
        apple_rect = self.fruit.apple.get_rect()
        apple_rect.right = score_rect.left - 10
        apple_rect.centery = score_rect.centery

        self.screen.blit(score_surface, score_rect)
        self.screen.blit(self.fruit.apple, apple_rect)


    def game_over(self):
        game_over_text = self.font.render("Game Over", True, RED)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        score_text = self.get_score()
        if self.update_high_score():
            score_surface = self.font.render("New High Score! " + str(score_text), True, WHITE)
            score_rect = score_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        else:
            score_surface = self.font.render("Final Score: " + str(score_text), True, WHITE)
            score_rect = score_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_surface, score_rect)

        pygame.display.update()
        pygame.time.delay(2000)

        # Quit the game
        self.playing = False
        self.reset()

    
    def get_score(self):
        # Score is the length of the snake's body minus the initial length (3)
        return len(self.snake.body) - 3
    

    def update_high_score(self):
        current_score = self.get_score()
        if current_score > self.high_score:
            self.high_score = current_score
            with open(SETTINGS_PATH, "r") as file:
                data = json.load(file)
                data["high_score"] = self.high_score
            with open(SETTINGS_PATH, "w") as file:
                json.dump(data, file)
            return True
        
        return False


    def clear(self):
        self.snake.clear()
        self.fruit.clear()


    def reset(self):
        self.load_settings()
        self.load_assets()
        self.snake.update_snake_color(self.head_up, self.head_down, self.head_left, self.head_right,
                                self.tail_up, self.tail_down, self.tail_left, self.tail_right,
                                self.body_vertical, self.body_horizontal, self.body_bottom_left,
                                self.body_bottom_right, self.body_top_left, self.body_top_right)
        self.snake.reset()
        self.fruit.reset()
        self.playing = False


def quit():
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game = Game()
    while game.running:
        if not game.playing:
            menu = Menu(game.screen, game.font)
            game.reset()
            game.playing = True

        if game.playing:
            game.loop()