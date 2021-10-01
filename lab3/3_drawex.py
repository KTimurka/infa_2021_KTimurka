import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

# задаем цвета
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
darkgreen = (0, 151, 0)
blue = (0, 0, 255)
brown = (100, 100, 100)
yellow = (255, 255, 0)
darkblue = (50, 50, 255)
red = (255, 0, 0)


# задаем функцию облака
def oblaka(cloud, dx, dy, rad):
    '''
    cloud - лист переменных, задан в main()
            в листе:количество кружков, цвет облака, координаты центра левого кружка
    dx, dy - смещение очередного кружка в облаке вправо и вверх
    rad - радиус кружков
    '''
    number, color, x, y = cloud
    for k in range(number):
        circle(screen, color, (x, y), rad)
        y = y + dy * ((-1) ** k)
        x = x + dx * (1 + (-1) ** (k + 1))


# задаем функцию дерева
def derevo(tree, dx, dy, rad):
    '''
    tree - лист данных о дереве, задан в main() ниже
           в листе: количество шариков, их цвет, координаты 
    dx, dy - смещение следующего шарика
    rad - размеры шарика
    '''
    number, color, x, y = tree
    polygon(screen, brown,
            [(x + 10, y + 9 * rad / 5), (x + 10, y + 6 * rad), (x - 10, y + 6 * rad), (x - 10, y + 9 * rad / 5)])
    circle(screen, color, (x, y), rad)
    circle(screen, (0, 0, 0), (x, y), rad, 2)
    for i in range(number):
        circle(screen, color, (x + dx / 2, y + dy), rad)
        circle(screen, (0, 0, 0), (x + dx / 2, y + dy), rad, 2)
        x = x + dx * (-1) ** (i + 1)
        y = y + dy * (1 + (-1) ** (i + 1))


# задаем функцию дома
def dom(home):
    '''
    параметр - лист home, задан в main() ниже
               в листе: цвета стены, крыши, окна
    в функции рисуем
      1 - стену
      2 - окно
      3 - крышу
    '''
    color1, color2, color3, x, y, size = home
    polygon(screen, color1, [(x, y), (x - size, y), (x - size, y - size), (x, y - size)])
    polygon(screen, black, [(x, y), (x - size, y), (x - size, y - size), (x, y - size)], 2)
    polygon(screen, color3,
            [(x - size / 4, y - size / 4), (x - 3 * size / 4, y - size / 4), (x - 3 * size / 4, y - 3 * size / 4),
             (x - size / 4, y - 3 * size / 4)])
    polygon(screen, black,
            [(x - size / 4, y - size / 4), (x - 3 * size / 4, y - size / 4), (x - 3 * size / 4, y - 3 * size / 4),
             (x - size / 4, y - 3 * size / 4)], 2)
    polygon(screen, color2, [(x, y - size), (x - size / 2, y - 3 * size / 2), (x - size, y - size)])
    polygon(screen, black, [(x, y - size), (x - size / 2, y - 3 * size / 2), (x - size, y - size)], 2)


# задаем функцию солнца
def solnce(sun):
    '''
    параметр - лист sun
               в листе: цвет, координаты центра, радиус
    в функции рисуем
      1 - задаем 20 правильных треугольников
      2 - поворачиваем их каждый раз на 18 градусов
      3 - центры треугольников имеюют координаты Х, У
    '''
    fi = 0
    color, x, y, rad = sun
    dx = 0
    dy = 0
    for i in range(20):
        x1 = x - rad * math.sin(fi)
        y1 = y - rad + rad * math.cos(fi)
        x2 = x - rad * math.cos(fi + 3.14 / 6)
        y2 = y - rad - rad * math.sin(fi + 3.14 / 6)
        x3 = x - rad * math.cos(fi + 5 * 3.14 / 6)
        y3 = y - rad - rad * math.sin(fi + 5 * 3.14 / 6)
        polygon(screen, color, [(x1, y1), (x2, y2), (x3, y3)])
        fi += 3.14 / 10


#Рисуем всё
def main():
    '''
    Рисуем прямоугольники - небо и землю
    '''
    polygon(screen, blue, [(0, 0), (800, 0), (800, 300), (0, 300)])
    polygon(screen, green, [(0, 300), (800, 300), (800, 600), (0, 600)])
    #Основные параметры:
    '''
    Листы-параметры для функций:
    1 - солнце
    2 - два дома
    3 - три дерева
    4 - три облака
    '''
    sun = [yellow, 730, 120, 50]
    home = [brown, red, darkblue, 200, 500, 175]
    home1 = [brown, red, darkblue, 600, 400, 100]
    tree = [6, darkgreen, 700, 200]
    tree1 = [6, darkgreen, 450, 250]
    tree2 = [6, darkgreen, 350, 170]
    cloud = [7, white, 100, 100]
    cloud1 = [7, white, 350, 130]
    cloud2 = [7, white, 550, 50]
    '''
    Далее вызываем сами функции для рисования
      и добавляем к ним желаемые координаты и размеры
    '''
    #Рисуем облака
    oblaka(cloud, 24, 48, 40)
    oblaka(cloud1, 18, 36, 30)
    oblaka(cloud2, 12, 24, 20)
    #Рисуем деревья
    derevo(tree, 48, 24, 40)
    derevo(tree1, 24, 12, 20)
    derevo(tree2, 36, 18, 30)
    #Рисуем дома
    dom(home)
    dom(home1)
    #Рисуем солнце
    solnce(sun)
main()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
