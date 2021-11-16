import pygame
import math
from random import choice
from random import randint as rnd

FPS = 100

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
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 100

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        gdt = 1
        self.vy -= gdt
        self.x += self.vx
        self.y -= self.vy
        if self.x + self.r >= WIDTH or self.x - self.r <= 0:
            self.vx = self.vx * (-1)
        if self.y + self.r >= HEIGHT or self.y - self.r <= 0:
            self.vy *= (-1)

    def kill_balls(self):
        if self.live > 0:
            self.live -=1
        else:
            balls.remove(self)

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
        # FIXME

        return (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r+obj.r) ** 2


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)/2
        new_ball.vy = - self.f2_power * math.sin(self.an)/2
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        gun.targetting(event)

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] - 20 > 0:
                self.an = math.atan(-(event.pos[1] - 450) / (event.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # fixme
        l = 100
        x = l * math.cos(self.an)
        y = l * math.sin(self.an)
        if self.f2_on:
            x *= self.f2_power
            y *= self.f2_power
        l_0 = 100

        pygame.draw.line(self.screen, self.color, (20, 450), (20 + math.cos(self.an)*(l_0+ self.f2_power),
                          450 - math.sin(self.an) *(l_0 + self.f2_power)),
                         10)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?

    def __init__(self, screen):
        """ Инициализация новой цели. """
        self.screen = screen
        self.points = 0
        self.live = 1
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        vx = self.vx = rnd(-10, 10)
        vy = self.vy = rnd(-10, 10)
        r = self.r = rnd(20, 50)

        color = self.color = BLACK

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        if self.x + self.r >= WIDTH or self.x - self.r <= 0:
            self.vx = self.vx * (-1)
        if self.y + self.r >= HEIGHT or self.y - self.r <= 0:
            self.vy *= (-1)



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = []
num_targets = 2
clock = pygame.time.Clock()
gun = Gun(screen)

for i in range(num_targets):
    targets.append(Target(screen))
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for target in targets:
        target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        b.kill_balls()
        for target in targets:
            if b.hittest(target) and target.live:
                target.live = 0
                target.hit()
                targets.remove(target)
                targets.append(Target(screen))
        gun.power_up()
    for target in targets:
        target.move()
pygame.quit()
