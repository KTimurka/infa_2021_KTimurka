import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800,600))

#Цвета:
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)
brown = (100,100,100)
yellow = (255,255,0)
darkblue = (50,50,255)


#Рисуем дерево
tree = [6, green, 50, 600, 200]
dx = 60
dy = 30
number, color, rad, x,y = tree
polygon(screen,brown,[(x+10,y+90),(x+10,y+300),(x-10,y+300),(x-10,y+90)])
circle(screen, color, (x,y),rad)
circle(screen, (0,0,0), (x,y),rad,2)
for i in range(number):
        circle(screen, color, (x+dx/2,y+dy),rad)
        circle(screen, (0,0,0), (x+dx/2,y+dy),rad,2)
        x = x + dx*(-1)**(i+1)
        y = y + dy*(1+(-1)**(i+1))

#Рисуем облако
cloud = [7,white ,50,100,100]
dx1 = 30
dy1 = 60
number1, color1, rad1,x1,y1 = cloud
for k in range(number1):
        circle(screen, color1, (x1,y1),rad1)
        circle(screen, (0,0,0), (x1,y1),rad1,2)
        y1 = y1 + dy1*((-1)**k)
        x1 = x1 + dx1*(1+(-1)**(k+1))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
