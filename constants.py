# Screen settings
import pygame


OFFSET = 75
CELL_SIZE = 40
CELL_NUMBER = 20
WIDTH = CELL_SIZE * CELL_NUMBER + 2 * OFFSET
HEIGHT = CELL_SIZE * CELL_NUMBER + 2 * OFFSET
SCREEN_UPDATE = pygame.USEREVENT

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRASS = (1, 46, 11)
WHITE = (255, 255, 255)

# Font
FONT_PATH = "fonts/BitcountPropDouble.ttf"

# Apple
APPLE_PATH = "graphics/apple.png"

# Background
BACKGROUND_PATH = "graphics/background.png"

# Icon
ICON_PATH = "graphics/game.ico"

# Snake body colors 
SNAKE_YELLOW = "Yellow"
SNAKE_ORANGE = "Orange"
SNAKE_BLUE = "Blue"
SNAKE_BLACK = "Black"
SNAKE_PURPLE = "Purple"

# Snake body colors path
SNAKE_YELLOW_PATH = "graphics/yellow"
SNAKE_ORANGE_PATH = "graphics/orange"
SNAKE_BLUE_PATH = "graphics/blue"
SNAKE_BLACK_PATH = "graphics/black"
SNAKE_PURPLE_PATH = "graphics/purple"

# Snake body parts
HEAD_UP_PATH = "head_up.png"
HEAD_DOWN_PATH = "head_down.png"
HEAD_LEFT_PATH = "head_left.png"
HEAD_RIGHT_PATH = "head_right.png"
TAIL_UP_PATH = "tail_up.png"
TAIL_DOWN_PATH = "tail_down.png"
TAIL_LEFT_PATH = "tail_left.png"
TAIL_RIGHT_PATH = "tail_right.png"
BODY_VERTICAL_PATH = "body_vertical.png"
BODY_HORIZONTAL_PATH = "body_horizontal.png"
BODY_BOTTOM_LEFT_PATH = "body_bottom_left.png"
BODY_BOTTOM_RIGHT_PATH = "body_bottom_right.png"
BODY_TOP_LEFT_PATH = "body_top_left.png"
BODY_TOP_RIGHT_PATH = "body_top_right.png"

# Difficulty
EASY = 200
HARD = 100
NORMAL = 150
OVER_THE_HILL = 250

# Sounds
EAT_SOUND_PATH = "sounds/eat.mp3"
CRASH_SOUND_PATH = "sounds/crash.mp3"

# Settings path
SETTINGS_PATH = "./" + "settings.json"

# Settings
DIFFICULTY_DEFAULT = NORMAL
SNAKE_COLOR_DEFAULT = SNAKE_YELLOW