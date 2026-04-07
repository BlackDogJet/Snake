import os
import json

from constants import (
    SETTINGS_PATH,
    DIFFICULTY_DEFAULT,
    SNAKE_COLOR_DEFAULT,
)


class Settings:
    def __init__(self):
        self.high_score = 0
        self.difficulty = DIFFICULTY_DEFAULT
        self.snake_color = SNAKE_COLOR_DEFAULT

        self.load_settings()
                        

    def load_settings(self):
        if os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, "r") as file:
                data = json.load(file)
                self.difficulty = data.get("difficulty", DIFFICULTY_DEFAULT)
                self.snake_color = data.get("snake_color", SNAKE_COLOR_DEFAULT)
                self.high_score = data.get("high_score", 0)
        else:
            self.save_settings()


    def save_settings(self):
        if not os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, "w") as file:
                json.dump({"difficulty": self.difficulty, "snake_color": self.snake_color, "high_score": self.high_score}, file)
        else:
            with open(SETTINGS_PATH, "r") as file:
                data = json.load(file)
                data["difficulty"] = self.difficulty
                data["snake_color"] = self.snake_color
                data["high_score"] = self.high_score

                with open(SETTINGS_PATH, "w") as file:
                    json.dump(data, file)
        

