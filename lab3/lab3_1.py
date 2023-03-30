import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
circle(screen, (0, 0, 0), (200, 200), 100)  # Лицо
circle(screen, (255, 255, 0), (200, 200), 98)
circle(screen, (0, 0, 0), (170, 170), 30)  # Левый
circle(screen, (255, 0, 0), (170, 170), 28)
circle(screen, (0, 0, 0), (170, 170), 20)
circle(screen, (0, 0, 0), (250, 170), 20)  # Правый
circle(screen, (255, 0, 0), (250, 170), 18)
circle(screen, (0, 0, 0), (250, 170), 13)
polygon(screen, (0, 0, 0), [(150, 250), (250, 250), (250, 270), (150, 270)])  # Рот
polygon(screen, (0, 0, 0), [(150, 100), (210, 170), (170, 100)])  # Левая бровь
polygon(screen, (0, 0, 0), [(250, 125), (220, 170), (250, 135)])  # Правая бровь
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
