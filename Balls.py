import pygame
from pygame.draw import *
from random import randint
pygame.init()

rating = open("Rating",'a')
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

# создаем массив информации о мишенях
pool = [generator() for i in range(number)]

#Просьба ввести имя
text = font.render("Please, enter your name: ",True,(255,255,255))
screen.blit(text, [200, 300])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

name = input() # вводим имя

# Добавим счетчики
count = 0 # счетчик очков
time = 0 # счетчик времени
lifes = 10 # счетчик жизней

# Основной цикл
while not finished:
    clock.tick(FPS)
    time+=1
    if time == 7200:
        finished = True
    dubl_pool = [] # резервный pool, сюда записываются изменения происходящие при обработке клика
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            # Проверим, попал ли наш клик в мишень. Вызывая функцию click для каждого объекта в pool
            for data in pool:
                if click(event,data) == True:
                    x,y,r,color,dx,dy,shape = data
                    v = dx**2 + dy**2 # скорость мишени
                    # реализуем пересчет очков за попадание в зависимости от: r, v, shape
                    if shape == 1: # shape == 1 соответствует квадратику
                        count+=2000/(r**2)+5*v/200
                    else:
                        count+=1000/(r**2)+5*v/200
                    data = generator()
                    dubl_pool.append(data)
                # снимаем жизнь за промах
                else:
                    lifes-=1
                    dubl_pool.append(data)
            lifes+=9 # даже если мы попали в один шарик, мы не попали в 9 остальных. Чтобы компенсировать это прибавляем 9
            pool = dubl_pool
        if lifes == 0:
            finished=True
    # создадим еще один резервный pool, чтобы записывать туда отражения (если они будут)
    new_pool = []
    # проверка каждого элемента из pool на столкновение со стенкой
    for data in pool:
        x, y, r, color, dx, dy, shape = data
        if x < r or x > 1000 - r:
            dx = -dx
            data = (x, y, r, color, dx, dy, shape)
        if y < r or y > 700 - r:
            dy = -dy
            data = (x, y, r, color, dx, dy,shape)
        data = new_ball(data)
        new_pool.append(data)
    # обновляем массив
    pool = new_pool
    # выводим количество очков и жизней на экран
    text = font.render("Score: " + str(count//1), True, (255,255,255))
    text_life = font.render("Lifes: " + str(lifes),True,(255,255,255))
    screen.blit(text, [100, 100])
    screen.blit(text_life,[100,50])
    pygame.display.update()
    screen.fill(BLACK)
print(count//1)
finished = False

# Игра завершилась по истечении времени или жизней. Ожидаем команды о выходе.
while not finished:
    text = font.render("Game Over :(", True, (255, 255, 255))
    screen.blit(text, [400, 300]),
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

# запишем результат в файл
print(name + ' '+ str(count//1), file=rating)