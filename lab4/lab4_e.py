# Данный код является измененным кодом Линника Егора под редакторством Воронова Николая
import pygame
from pygame.draw import *

pygame.init()


def draw_mose(surface, x, y):
    """
    Рисует рот зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    """
    polygon(surface, (0, 0, 0), [(x - 10, y + 8), (x + 10, y + 8), (x + 10, y + 5), (x - 10, y + 5)])


def draw_body(surface, x, y, width, height, color):
    """
    Рисует тело зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))
    ellipse(surface, (0, 0, 0), (x - width // 2 + 25, y - height // 2 + 55, width // 2, height // 2))


def draw_head(surface, x, y, size, color):
    """
    Рисует голову зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - диаметр головы
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    circle(surface, color, (x, y), size // 2)


def draw_eye(surface, x, y, width, height, color):
    """
    Рисует глаз и бровь зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    ellipse(surface, (110, 0, 110), (x - width // 2, y - height // 2, width, height))
    ellipse(surface, (0, 0, 0), (x - width // 2 + 10, y - height // 2 + 10, width * 0.5, height * 0.5))


def draw_ear(surface, x, y, width, height, color):
    """
    Рисует ухо зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_leg(surface, x, y, width, height, color):
    """
    Рисует ногу зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_hare(surface, x, y, width, height, color):
    """
    Рисует зайца на экране.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    body_width = width // 2  # Ширина, высота и координата y тела зайца
    body_height = height // 2
    body_y = y + body_height // 2
    head_size = height // 4  # Размер головы
    ear_height = height // 3  # Высота и координата y уха зайца
    ear_y = y - height // 2 + ear_height // 2
    leg_height = height // 16  # Высота и координата y ноги зайца
    leg_y = y + height // 2 - leg_height // 2
    eye_height = height // 10  # Высота и координата y глаза зайца
    eye_y = y + height // 2 - eye_height * 6.4
    draw_body(surface, x, body_y, body_width, body_height, color)  # Тело зайца
    for ear_x in (x - head_size // 4, x + head_size // 4):  # Уши зайца
        draw_ear(surface, ear_x, ear_y, width // 8, ear_height, color)
    draw_head(surface, x, y - head_size // 2, head_size, color)  # Голова и рот зайца
    draw_mose(screen, x, y - 30)
    for eye_x in (x - width // 8, x + width // 8):  # Глаза зайца
        draw_eye(surface, eye_x, eye_y, width // 5, eye_height, (255, 240, 69))
    for leg_x in (x - width // 4, x + width // 4):  # Ноги зайца
        draw_leg(surface, leg_x, leg_y, width // 4, leg_height, color)


FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
draw_hare(screen, 200, 200, 200, 400, (200, 200, 200))  # Рисуем зайца
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
