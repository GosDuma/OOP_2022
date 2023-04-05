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
polygon(screen, (43, 34, 0), [(100, 350), (300, 350), (300, 150), (100, 150)])
# Окна верхние
for i in range(0, 8, 2):
    polygon(screen, (72, 62, 55), [(120 + i * 25, 240), (140 + i * 25, 240), (140 + i * 25, 150), (120 + i * 25, 150)])
# Ограда
polygon(screen, (26, 26, 26), [(70, 260), (330, 260), (330, 240), (70, 240)])
polygon(screen, (26, 26, 26), [(70, 250), (70, 220), (80, 220), (80, 250)])  # 80, 220
polygon(screen, (26, 26, 26), [(80, 220), (320, 220), (320, 210), (80, 210)])
polygon(screen, (26, 26, 26), [(320, 240), (330, 240), (330, 220), (320, 220)])
for i in range(0, 11, 2):
    polygon(screen, (26, 26, 26), [(90 + 20 * i, 240), (100 + 20 * i, 240), (100 + 20 * i, 220), (90 + 20 * i, 220)])
polygon(screen, (0, 0, 0), [(70, 150), (80, 130), (320, 130), (330, 150)])  # Крыша
polygon(screen, (51, 51, 51), [(120, 135), (125, 135), (125, 120), (120, 120)])  # Труба
# Нижние окна
for i in range(0, 5, 2):
    polygon(screen, (139, 69, 19), [(120 + i * 25, 320), (160 + i * 25, 320), (160 + i * 25, 290), (120 + i * 25, 290)])
polygon(screen, (212, 170, 0), [(120 + i * 25, 320), (160 + i * 25, 320), (160 + i * 25, 290), (120 + i * 25, 290)])
# Призрак
x = 400
y = 400
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

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
