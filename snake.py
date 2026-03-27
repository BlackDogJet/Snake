import pygame

from pygame.math import Vector2

from constants import (
    OFFSET,
    CELL_SIZE,
)

class Snake:
    def __init__(self, head_up, head_down, head_left, head_right,
                 tail_up, tail_down, tail_left, tail_right,
                 body_vertical, body_horizontal, body_bottom_left,
                 body_bottom_right, body_top_left, body_top_right):        
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)

        self.head_up = head_up
        self.head_down = head_down
        self.head_left = head_left
        self.head_right = head_right

        self.tail_up = tail_up
        self.tail_down = tail_down
        self.tail_left = tail_left
        self.tail_right = tail_right

        self.body_vertical = body_vertical
        self.body_horizontal = body_horizontal

        self.body_bottom_left = body_bottom_left
        self.body_bottom_right = body_bottom_right
        self.body_top_left = body_top_left
        self.body_top_right = body_top_right


    def draw(self, screen):
        self.update_head_graphic()
        self.update_tail_graphic()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * CELL_SIZE) + OFFSET
            y_pos = int(block.y * CELL_SIZE) + OFFSET
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block

                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if ((previous_block.x == -1 and next_block.y == -1) or
                        (previous_block.y == -1 and next_block.x == -1)):
                        screen.blit(self.body_top_left, block_rect)
                    elif ((previous_block.x == -1 and next_block.y == 1) or
                          (previous_block.y == 1 and next_block.x == -1)):
                        screen.blit(self.body_bottom_left, block_rect)
                    elif ((previous_block.x == 1 and next_block.y == -1) or
                          (previous_block.y == -1 and next_block.x == 1)):
                        screen.blit(self.body_top_right, block_rect)
                    elif ((previous_block.x == 1 and next_block.y == 1) or
                          (previous_block.y == 1 and next_block.x == 1)):
                        screen.blit(self.body_bottom_right, block_rect)
                

    def slither(self):
        new_body = self.body[:-1]
        new_body.insert(0, self.body[0] + self.direction)
        self.body = new_body


    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)


    def update_head_graphic(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(0, -1):
            self.head = self.head_down
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(1, 0):
            self.head = self.head_left


    def update_tail_graphic(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(0, -1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(1, 0):
            self.tail = self.tail_left