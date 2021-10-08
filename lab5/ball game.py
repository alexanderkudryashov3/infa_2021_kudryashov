import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

points, num_balls = 0, 10

pygame.display.update()
clock = pygame.time.Clock()
finished = False


def new_ball(x1, y1, r1, color):

    circle(screen, color, (x1, y1), r1)


def draw_balls(x, y, r, colors):
    for i in range(num_balls):
        new_ball(x[i], y[i], r[i], colors[i])


def click_handler(event):
    global points
    x1, y1 = event.pos
    click_inside_ball = [r[i]**2>(x[i]-x1)**2+(y[i]-y1)**2 for i in range(num_balls)]
    for i in range(num_balls):
        if(click_inside_ball[i]):
            x[i] = randint(100, 700)
            y[i] = randint(100, 500)
            r[i] = randint(30, 50)
            v_x[i] = randint(-10, +10)
            v_y[i] = randint(-10, +10)
            colors[i] = COLORS[randint(0, 5)]

    points += sum(click_inside_ball)


def check_wall():
    global x, y, r, v_x, v_y, num_balls
    hit_right_wall = [1200 - x[i] + r[i] <= v_x[i] and v_x[i] > 0 for i in range(num_balls)]
    hit_left_wall = [x[i] - r[i] <= abs(v_x[i]) and v_x[i] < 0 for i in range(num_balls)]
    hit_upper_wall = [y[i] - r[i] <= abs(v_y[i]) and v_y[i] < 0 for i in range(num_balls)]
    hit_lower_wall = [900 - y[i] - r[i] <= v_y[i] and v_y[i] > 0 for i in range(num_balls)]
    for i in range(num_balls):
        if hit_right_wall[i] or hit_left_wall[i]:
            v_x[i] *= -1
        if hit_upper_wall[i] or hit_lower_wall[i]:
            v_y[i] *= -1


def display_points():
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 150)
    textsurface = myfont.render(str(points), False, (200, 200, 200))
    screen.blit(textsurface, (50, 0))


colors = [COLORS[randint(0, 5)] for i in range(num_balls)]
x = [randint(100, 700) for i in range(num_balls)]
y = [randint(100, 500) for i in range(num_balls)]
r = [randint(30, 50) for i in range(num_balls)]
v_x = [randint(-10, +10) for i in range(num_balls)]
v_y = [randint(-10, +10) for i in range(num_balls)]
while not finished:
    clock.tick(FPS)
    x[1] += 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_handler(event)
    check_wall()
    x = [x[i] + v_x[i] for i in range(num_balls)]
    y = [y[i] + v_y[i] for i in range(num_balls)]
    screen.fill(BLACK)
    display_points()
    draw_balls(x, y, r, colors)
    pygame.display.update()

pygame.quit()
