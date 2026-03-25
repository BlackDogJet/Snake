from fruit import Fruit
from snake import Snake


class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()


    def update(self):
        self.snake.move()
        self.check_collision()


    def draw(self, screen):
        self.fruit.draw(screen)
        self.snake.draw(screen)


    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()

            self.snake.body.append(self.snake.body[-1])
        