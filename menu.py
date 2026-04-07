import os
import json
import sys
import pygame_menu as pm

from settings import Settings

from constants import (
    RED,
    EASY,
    HARD,
    BLACK,
    GRASS,
    WIDTH,
    HEIGHT,
    NORMAL,
    SNAKE_BLUE,
    SNAKE_BLACK,
    SNAKE_ORANGE,
    SNAKE_PURPLE,
    SNAKE_YELLOW,
    OVER_THE_HILL,
)


class Menu(Settings):
    def __init__(self, screen, font):
        super().__init__()

        self.font = font
        self.screen = screen
        self.main_menu = True

        self.load_settings()
        self.settings_menu()
        
        self.menu = pm.Menu("Main Menu", WIDTH, HEIGHT, theme=pm.themes.THEME_GREEN)
        self.menu._theme.widget_font_size = 50
        self.menu.add.button("Play", self.start_game)
        self.menu.add.button("Settings", self.settings)
        self.menu.add.button("Quit", self.quit)

        menu_text = self.font.render("Main Menu", True, RED)
        menu_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(menu_text, menu_rect)

        play_button = self.font.render("Play", True, GRASS)
        play_rect = play_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        screen.blit(play_button, play_rect)

        settings_button = self.font.render("Settings", True, GRASS)
        settings_rect = settings_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
        screen.blit(settings_button, settings_rect)

        quit_button = self.font.render("Quit", True, RED)
        quit_rect = quit_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140))
        screen.blit(quit_button, quit_rect)

        self.menu.mainloop(self.screen)


    def start_game(self):
        self.main_menu = False
        self.menu.disable()


    def settings_menu(self):
        if self.difficulty == 250:
            difficulty_index = 0
        elif self.difficulty == 200:
            difficulty_index = 1
        elif self.difficulty == 150:
            difficulty_index = 2
        elif self.difficulty == 100:
            difficulty_index = 3

        if self.snake_color == SNAKE_YELLOW:
            snake_color_index = 0
        elif self.snake_color == SNAKE_ORANGE:
            snake_color_index = 1
        elif self.snake_color == SNAKE_BLUE:
            snake_color_index = 2
        elif self.snake_color == SNAKE_BLACK:
            snake_color_index = 3
        elif self.snake_color == SNAKE_PURPLE:
            snake_color_index = 4

        difficulty_options = [("Over the hill", OVER_THE_HILL),
                              ("Easy", EASY),
                              ("Normal", NORMAL),
                              ("Hard", HARD)]
        
        snake_color_options = [(SNAKE_YELLOW, SNAKE_YELLOW),
                               (SNAKE_ORANGE, SNAKE_ORANGE),
                               (SNAKE_BLUE, SNAKE_BLUE),
                               (SNAKE_BLACK, SNAKE_BLACK),
                               (SNAKE_PURPLE, SNAKE_PURPLE)]

        # Create the settings menu
        self.settings = pm.Menu("Settings", WIDTH, HEIGHT, theme=pm.themes.THEME_GREEN)
        self.settings._theme.widget_font_size = 50
        self.settings._theme.widget_font_color = BLACK
        self.settings._theme.widget_alignment = pm.locals.ALIGN_CENTER

        # Add difficulty selector
        self.settings.add.selector(title="Difficulty: ",
                              items=difficulty_options,
                              selector_id="difficulty",
                              default=difficulty_index,
                              onchange=self.set_difficulty)
        
        # Add snake color selector
        self.settings.add.selector(title="Snake Color: ",
                              items=snake_color_options,
                              selector_id="snake_color",
                              default=snake_color_index,
                              onchange=self.set_snake_color)
        
        # Add buttons
        self.settings.add.button(title="Save Settings",
                            action=self.save,
                            align=pm.locals.ALIGN_CENTER)

        self.settings.add.button(title="Return To Main Menu",
                            action=pm.events.BACK,
                            align=pm.locals.ALIGN_CENTER)


    def set_difficulty(self, selected, value):
        self.difficulty = value


    def set_snake_color(self, selected, value):        
        self.snake_color = value


    def save(self):
        self.save_settings()
        self.settings._back()


    def quit(self):
        sys.exit()
