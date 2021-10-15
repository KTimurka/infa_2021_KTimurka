import pygame
from pygame.draw import *
from random import randint
pygame.init()

rating = open("Rating",'a')
name = input()
FPS = 120
screen = pygame.display.set_mode((1000, 700))

font = pygame.font.Font(None, 50)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
number = 10

def generator():
    '''
        Функция генерирует случайные параметры шариков.
        Функция возвращает кортеж с этими значениями.
    '''
    x = randint(100, 900)
    y = randint(100, 600)
    r = randint(20, 100)
    color = COLORS[randint(0, 5)]
    dx = randint(-10, 10)
    dy = randint(-10, 10)
    shape = randint(1, 6)
    data = (x, y, r, color, dx, dy, shape)
    return data

def new_ball(data):
    '''
        Получает на вход массив информации о фигуре.
        Делает сдвиг шарика на dx,dy.
        Создает шарик или квадратик.
        Возвращает обновленный массив данных о фигуре.
    '''
    x, y, r, color, dx, dy, shape = data
    x = x + dx/5
    y = y + dy/5
    if shape == 1:
        dy+=0.1
        dx+=0.1
        rect(screen, color, (x-r,y-r,2*r,2*r),4)
    else:
        circle(screen, color, (x, y), r)
    data = (x, y, r, color, dx, dy, shape)
    return data

def click(event, data):
    '''
        Функция проверяет, было ли попадание.
        Функция получает событие и информацию о шарике в массиве(data).
        Возвращает попадание (True or False)
    '''
    x, y, r, color, dx, dy, shape = data
    click_x,click_y = event.pos
    if (click_x - x)**2 + (click_y - y)**2 <= r**2:
        shoot = True
    else:
        shoot = False
    return shoot

pool = [generator() for i in range(number)]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

# Добавим счетчик
count = 0
time = 0
lifes = 10
while not finished:
    clock.tick(FPS)
    time+=1
    if time == 7200:
        finished = True
    dubl_pool = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            for data in pool:
                if click(event,data) == True:
                    x,y,r,color,dx,dy,shape = data
                    v = dx**2 + dy**2
                    if shape == 1:
                        count+=2000/(r**2)+5*v/200
                    else:
                        count+=1000/(r**2)+5*v/200
                    data = generator()
                    dubl_pool.append(data)
                else:
                    lifes-=1
                    dubl_pool.append(data)
            lifes+=9
            pool = dubl_pool
        if lifes == 0:
            finished=True
    new_pool = []
    for data in pool:
        x, y, r, color, dx, dy, shape = data
        if x < r or x > 1000 - r:
            if shape == 100:
                dx, dy = -dy, dx
                data = (x, y, r, color, dx, dy, shape)
            else:
                dx = -dx
                data = (x, y, r, color, dx, dy, shape)
        if y < r or y > 700 - r:
            if shape == 100:
                dx , dy = dy, -dx
                data = (x, y, r, color, dx, dy, shape)
            else:
                dy = -dy
                data = (x, y, r, color, dx, dy,shape)
        data = new_ball(data)
        new_pool.append(data)
    pool = new_pool
    text = font.render("Score: " + str(count//1), True, (255,255,255))
    text_life = font.render("Lifes: " + str(lifes),True,(255,255,255))
    screen.blit(text, [100, 100])
    screen.blit(text_life,[100,50])
    pygame.display.update()
    screen.fill(BLACK)
print(count//1)
finished = False
while not finished:
    text = font.render("Game Over :(", True, (255, 255, 255))
    screen.blit(text, [400, 300]),
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
print(name + ' '+ str(count//1), file=rating)