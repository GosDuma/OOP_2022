import pygame
from pygame.draw import *

pygame.init()
FPS = 30
i = 0
screen = pygame.display.set_mode((700, 700))
screen.fill((105, 105, 105))
circle(screen, (255, 255, 255), (310, 60), 50)  # Луна
# Облака
ellipse(screen, (51, 51, 51), (300, 10, 600, 100))
ellipse(screen, (26, 26, 26), (100, 50, 300, 100))
ellipse(screen, (77, 77, 77), (300, 100, 400, 100))

polygon(screen, (0, 0, 0), [(0, 200), (700, 200), (700, 700), (0, 700)])


def house(x, y):
    polygon(screen, (43, 34, 0), [(x - 100, y + 150), (x + 100, y + 150), (x + 100, y - 50), (x - 100, y - 50)])
    # Окна верхние
    for i in range(0, 8, 2):
        polygon(screen, (72, 62, 55),
                [(x - 80 + i * 25, y + 40), (x - 60 + i * 25, y + 40), (x - 60 + i * 25, y - 50),
                 (x - 80 + i * 25, y - 50)])
    # Ограда
    polygon(screen, (26, 26, 26), [(x - 130, y + 60), (x + 130, y + 60), (x + 130, y + 40), (x - 130, y + 40)])
    polygon(screen, (26, 26, 26), [(x - 130, y + 50), (x - 130, y + 20), (x - 120, y + 20), (x - 120, y + 50)])
    polygon(screen, (26, 26, 26), [(x - 120, y + 20), (x + 120, y + 20), (x + 120, y + 10), (x - 120, y + 10)])
    polygon(screen, (26, 26, 26), [(x + 120, y + 40), (x + 130, y + 40), (x + 130, y + 20), (x + 120, y + 20)])
    for i in range(0, 11, 2):
        polygon(screen, (26, 26, 26),
                [(x - 110 + 20 * i, y + 40), (x - 100 + 20 * i, y + 40), (x - 100 + 20 * i, y + 20),
                 (x - 110 + 20 * i, y + 20)])
    polygon(screen, (0, 0, 0), [(x - 130, y - 50), (x - 120, y - 70), (x + 120, y - 70), (x + 130, y - 50)])  # Крыша
    polygon(screen, (51, 51, 51), [(x - 80, y - 65), (x - 75, y - 65), (x - 75, y - 80), (x - 80, y - 80)])  # Труба
    # Нижние окна
    for i in range(0, 5, 2):
        polygon(screen, (139, 69, 19),
                [(x - 80 + i * 25, y + 120), (x - 40 + i * 25, y + 120), (x - 40 + i * 25, y + 90),
                 (x - 80 + i * 25, y + 90)])
    polygon(screen, (212, 170, 0), [(x - 80 + i * 25, y + 120), (x - 40 + i * 25, y + 120), (x - 40 + i * 25, y + 90),
                                    (x - 80 + i * 25, y + 90)])


def ghost(x, y):
    circle(screen, (179, 179, 179), (x, y), 20)
    circle(screen, (135, 205, 222), (x - 10, y), 5)
    circle(screen, (0, 0, 0), (x - 10, y), 2)
    circle(screen, (135, 205, 222), (x + 5, y), 5)
    circle(screen, (0, 0, 0), (x + 5, y), 2)
    ellipse(screen, (179, 179, 179), (x - 30, y + 10, 75, 40))
    ellipse(screen, (179, 179, 179), (x - 35, y + 10, 40, 70))
    polygon(screen, (179, 179, 179),
            [(x - 20, y + 80), (x, y + 70), (x + 20, y + 80), (x + 30, y + 50), (x + 40, y + 70), (x + 45, y + 60),
             (x + 45, y + 20), (x + 20, y + 10)])


ghost(250, 581)
ghost(358, 582)
ghost(223, 426)
ghost(520, 500)
house(150, 200)
house(500, 180)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
