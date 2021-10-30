import math
import random
from random import choice
import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = 40
        self.y = 450
        self.r = 0
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.time = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        if self.x > 780:
            self.x -= self.vx
            self.vx = -0.5*self.vx
            self.vy = 0.5*self.vx
        if self.y > 580:
            self.y += self.vy
            self.vy = -0.5*self.vy
            self.vx = 0.5*self.vx
        if self.time == 60:
            balls.remove(b)
        self.vy -= 1
        self.time += 1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        x0 = obj.x
        y0 = obj.y
        distance = (self.x - x0)**2 + (self.y - y0)**2
        if distance < (obj.r + self.r)**2:
            return True
        else:
            return False

class Explorer(Ball):
    def __init__(self):
        Ball.__init__(self,screen)
    def explosion(self):
        x = self.x
        y = self.y
        balls.remove(b)
        for i in range(100):
            new_ball = Ball(self.screen)
            new_ball.r += 2
            new_ball.x = x
            new_ball.y = y
            new_ball.vx = random.randint(-15,15)
            new_ball.vy = random.randint(-55,15)
            balls.append(new_ball)



class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 30

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event, gun_type):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, count
        count += 1
        if gun_type:
            new_ball = Explorer()
        else:
            new_ball = Ball(self.screen)
        new_ball.r += 15
        new_ball.x += self.x - 20
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        newx1 = self.x + 1.5*self.f2_power*math.cos(self.an)
        newy1 = 450 + 1.5*self.f2_power*math.sin(self.an)
        newx2 = newx1 - 10*math.sin(self.an)
        newy2 = newy1 + 10*math.cos(self.an)
        newx3 = self.x - 10*math.sin(self.an)
        newy3 = 450 + 10*math.cos(self.an)
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(newx1,newy1),(newx2,newy2),(newx3,newy3),(self.x,450)]
        )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

class Tank:
    def __init__(self):
        self.screen = screen
        self.x = 20
        self.y = 450
        self.vx = 0.5
        self.color = GREY
    def move(self):
        if self.x + self.vx < 200 and self.x + self.vx > 0:
            self.x += self.vx
            gun.x +=self.vx
    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,(self.x,self.y, 40,20)
        )



class Target:
    def __init__(self):
        self.screen = screen
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 550)
        self.r = random.randint(20, 50)
        self.color = RED
        self.vy = random.randint(1, 10)
        self.target_type = random.randint(0, 5)
        self.live = 1
        self.x0 = self.x
        self.points = 0

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.randint(600, 700)
        self.y = random.randint(150, 550)
        self.r = random.randint(10, 50)
        self.vy = random.randint(1,10)
        self.target_type = random.randint(0,1)
        self.color = RED
        self.x0 = self.x

    def move (self):
        if self.target_type > 0:
            self.y +=self.vy
            if self.y > 550:
                self.vy = -self.vy
            if self.y < 50:
                self.vy = -self.vy
        else:
            self.x =self.x0 + 50*math.cos(6.28*(self.y)/200)
            self.y += self.vy
            if self.y > 550:
                self.vy = -self.vy
            if self.y < 50:
                self.vy = -self.vy

    def draw(self):
        if self.live==1:
            if self.target_type == 0:
                pygame.draw.rect(
                    self.screen,
                    self.color,
                    (self.x-self.r/2, self.y-self.r/2, self.r, self.r), 4
                )
            else:
                pygame.draw.circle(
                    self.screen,
                    self.color,
                    (self.x, self.y),
                    self.r
                )
        else:
            text = font.render("Вы попали по шарику. Затраченное число попыток: " + str(count), True, (0, 0, 0))
            screen.blit(text, [100, 250])
            pygame.display.update()

pygame.init()

font = pygame.font.Font(None, 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
count = 0
balls = []
pool = []

clock = pygame.time.Clock()
gun = Gun(screen)
tank = Tank()
# создание массива из целей
for i in range(2):
    target = Target()
    pool.append(target)
finished = False
stop = 0
score = 0
gun_type = False

while not finished:
    screen.fill(WHITE)
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        tank.vx=-1
        tank.move()
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        tank.vx=1
        tank.move()
    tank.draw()
    gun.draw()
    # сдвиг и отрисовка целей. В случае попадания, откат до появления новой
    for target in pool:
        target.move()
        target.draw()
        if target.live == 0:
            stop +=1
            if stop == 60:
                target.live = 1
                stop = 0
                count = 0
    for b in balls:
        b.draw()
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, [10, 10])
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event, gun_type)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gun_type = not(gun_type)
    # отрисовка шариков с проверкой на тип (взрывание подрывников)
    for b in balls:
        if type(b)==Explorer and b.time == 30:
            b.explosion()
        b.move()
        for target in pool:
            if b.hittest(target) and target.live:
                target.live = 0
                target.new_target()
                score+=1
    gun.power_up()

pygame.quit()
print(score)
print(gun_type)