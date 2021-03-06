import pygame
from pygame.draw import *
import math
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800,600))



#Цвета:
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
darkgreen=(0,151,0)
blue = (0,0,255)
brown = (100,100,100)
yellow = (255,255,0)
darkblue = (50,50,255)
red = (255,0,0)



#Полянка и небо
polygon(screen,blue,[(0,0),(800,0),(800,300),(0,300)])
polygon(screen,green,[(0,300),(800,300),(800,600),(0,600)])



#Рисуем дерево
tree = [6, darkgreen, 50, 600, 200]
def derevo(tree,dx,dy):
    number, color, rad, x,y = tree
    polygon(screen,brown,[(x+10,y+90),(x+10,y+300),(x-10,y+300),(x-10,y+90)])
    circle(screen, color, (x,y),rad)
    circle(screen, (0,0,0), (x,y),rad,2)
    for i in range(number):
            circle(screen, color, (x+dx/2,y+dy),rad)
            circle(screen, (0,0,0), (x+dx/2,y+dy),rad,2)
            x = x + dx*(-1)**(i+1)
            y = y + dy*(1+(-1)**(i+1))
derevo(tree,60,30)

        
#Рисуем облако
cloud = [7,white ,50,100,100]
def oblaka(cloud,dx,dy):
      number, color, rad,x,y = cloud
      for k in range(number):
        circle(screen, color, (x,y),rad)
        circle(screen, (0,0,0), (x,y),rad,2)
        y = y + dy*((-1)**k)
        x = x + dx*(1+(-1)**(k+1))
oblaka(cloud,30,60)

#Рисуем дом
home = [brown,red,darkblue,200, 500,175]
def dom(home):
        color1, color2, color3, x, y, size = home
        polygon(screen,color1,[(x,y),(x-size,y),(x-size,y-size),(x,y-size)])
        polygon(screen,black,[(x,y),(x-size,y),(x-size,y-size),(x,y-size)],2)
        polygon(screen, color3,[(x-size/4,y-size/4),(x-3*size/4,y-size/4),(x-3*size/4,y-3*size/4),(x-size/4,y-3*size/4)])
        polygon(screen, black,[(x-size/4,y-size/4),(x-3*size/4,y-size/4),(x-3*size/4,y-3*size/4),(x-size/4,y-3*size/4)],2)
        polygon(screen, color2,[(x,y-size),(x-size/2,y-3*size/2),(x-size,y-size)])
        polygon(screen, black,[(x,y-size),(x-size/2,y-3*size/2),(x-size,y-size)],2)
dom(home)



#Рисуем солнце
sun = [yellow, 500,150, 50]
def solnce(sun):
        fi = 0
        color, x,y, rad = sun
        dx = 0
        dy = 0
        for i in range(20):
                x1=x-rad*math.sin(fi)
                y1=y-rad+rad*math.cos(fi)
                x2=x-rad*math.cos(fi+3.14/6)
                y2=y-rad - rad*math.sin(fi+3.14/6)
                x3=x-rad*math.cos(fi+5*3.14/6)
                y3=y-rad - rad*math.sin(fi+5*3.14/6)
                polygon(screen,color,[(x1,y1),(x2,y2),(x3,y3)])
                fi+=3.14/10
solnce(sun)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
