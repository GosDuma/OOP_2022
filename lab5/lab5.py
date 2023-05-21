import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 70
# Размер экрана
screen = pygame.display.set_mode((900, 600))
# Задаём цвета и картеж из цветов
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
# Координаты x и y, радиус 1ого шара
x1 = randint(100, 700)
y1 = randint(100, 500)
r1 = randint(30, 50)
# Координаты x и y, радиус 2ого шара
x2 = randint(100, 700)
y2 = randint(100, 500)
r2 = randint(30, 50)
# Координаты x и y, радиус 3ого шара
x3 = randint(100, 700)
y3 = randint(100, 500)
r3 = randint(30, 50)
# Координаты x и y, радиус 4ого шара
x4 = randint(100, 700)
y4 = randint(100, 500)
z4 = randint(30, 50)
# Выбор цвета каждого из шаров
color_1 = COLORS[randint(0, 5)]
color_2 = COLORS[randint(0, 5)]
color_3 = COLORS[randint(0, 5)]
color_4 = COLORS[randint(0, 5)]


def mouse_pos():
    """
    Функция считывания позиции мыши
    Возвращает картеж из координат x, y
    """
    return pygame.mouse.get_pos()


def new_ball():
    """
    Функция создания нового шара
    """
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


class Ball:
    def __init__(self, x, y, radius):
        self.radius = radius
        self.x = x
        self.y = y
        self.velocity_y = 10
        self.velocity_x = 10
        self.counter = 0

    def draw(self, color1):
        """
        Метод рисования шарика
        Подаем значение color1 - переменная хранящая картеж
        """
        circle(screen, color1, (self.x, self.y), self.radius)

    def move(self):
        """
        Движение шара
        """
        self.velocity_y += 0.01
        self.velocity_x += 0.01
        self.y += self.velocity_y
        self.x += self.velocity_x
        if self.y + self.radius >= 600 or self.y - self.radius <= 0:
            self.velocity_y = -self.velocity_y
        if self.x + self.radius >= 900 or self.x - self.radius <= 0:
            self.velocity_x = -self.velocity_x

    def click(self, mouse_posit, counter):
        """
        Функция определения попадания курсора мыши по шарику
        На вход подаём счет и позицию мыши
        """
        if self.radius >= 30 and (
                self.radius > ((mouse_posit[0] - self.x) ** 2 + (mouse_posit[1] - self.y) ** 2) ** 0.5):
            self.counter += 3
        counter += self.counter
        return counter


pygame.display.update()
clock = pygame.time.Clock()
finished = False
game_score = 0
ball_one = Ball(x1, y1, r1)
ball_two = Ball(x2, y2, r2)
ball_three = Ball(x3, y3, r3)
ball_four = Ball(x4, y4, r3)
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            a = mouse_pos()
            count_1 = ball_one.click(a, game_score)
            count_2 = ball_two.click(a, game_score)
            count_3 = ball_three.click(a, game_score)
            count_4 = ball_four.click(a, game_score)
            print("Your score is", count_1 + count_2 + count_3 + count_4)
            print("________________________________")

    ball_one.move()
    ball_two.move()
    ball_three.move()
    ball_four.move()
    screen.fill((32, 32, 32))
    ball_one.draw(color_1)
    ball_two.draw(color_2)
    ball_three.draw(color_3)
    ball_four.draw(color_4)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
