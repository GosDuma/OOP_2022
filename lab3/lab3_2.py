import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((700, 700))
screen.fill((105, 105, 105))
polygon(screen, (0, 0, 0), [(100, 350), (300, 350), (300, 150), (100, 150)])
polygon(screen, (0, 209, 79), [(70, 260), (330, 260), (330, 240), (70, 240)])
polygon(screen, (0, 209, 80), [(70, 250), (70, 220), (80, 220), (80, 250)])  # 80, 220
polygon(screen, (0, 210, 80), [(80, 220), (320, 220), (320, 210), (80, 210)])
polygon(screen, (0, 210, 80), [(320, 240), (330, 240), (330, 220), (320, 220)])
for i in range(10):
    if i % 2 == 1:
        polygon(screen, (0, 210, 80), [(90 + 20 * i, 240), (100 + 20 * i, 240), (100 + 20 * i, 220), (90 + 20 * i, 220)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
