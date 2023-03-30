import pygame
from pygame.draw import *

screen = pygame.display.set_mode((300, 200))

pygame.display.update()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        clock.tick(30)
        if event.type == pygame.QUIT:
            pygame.quit()
