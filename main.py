import sys
import pygame

from constants import (
    Screen,
    Surface,
    Colors,
)

pygame.init()

x_position = Surface.X.value
y_position = Surface.Y.value
x_velocity = 5
y_velocity = 5

screen = pygame.display.set_mode((Screen.WIDTH.value, Screen.HEIGHT.value))
clock = pygame.time.Clock()
test_surface = pygame.Surface((Surface.WIDTH.value, Surface.HEIGHT.value))
test_surface.fill(Colors.LIGHT_SKY_BLUE.value)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    x_position += x_velocity
    y_position += y_velocity
    
    if x_position + Surface.WIDTH.value > Screen.WIDTH.value or x_position < 0:
        x_velocity = -x_velocity
    
    if y_position + Surface.HEIGHT.value > Screen.HEIGHT.value or y_position < 0:
        y_velocity = -y_velocity

    screen.fill(Colors.LIME.value)
    screen.blit(test_surface, (x_position, y_position))
    pygame.display.update()
    clock.tick(60)