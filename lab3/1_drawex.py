import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode((400,400))

face = [(200,200), 150]
yellow = (204, 255, 0)
circle(screen, yellow, *face)
circle(screen, (255,0,0), (125,175),40)
circle(screen, (0,0,0), (125,175),15)
circle(screen, (255,0,0), (275,175),30)
circle(screen, (0,0,0), (275,175),10)
polygon(screen, (0,0,0),[(100,275),(300,275),(300,305),(100,305)],0)
polygon(screen, (0,0,0),[(100,80),(200,100),(195,125),(95,105)],0)
polygon(screen, (0,0,0),[(240,130),(340,110),(345,95),(245,115)],0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while finished is False:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished == True

pygame.quit()
