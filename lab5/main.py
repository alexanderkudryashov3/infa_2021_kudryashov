import pygame
from pygame.draw import *
from random import random
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 800))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

points, num_balls, num_squares = 0, 10, 1
x, y, r, v_x, v_y, colors = [0] * num_balls, [0] * num_balls, [0] * num_balls,\
                            [0] * num_balls, [0] * num_balls, [0] * num_balls

x2, y2, r2, v_x2, v_y2, colors2 = [0] * num_balls, [0] * num_balls, [0] * num_balls,\
                            [0] * num_balls, [0] * num_balls, [0] * num_balls

def generate_new_ball(i):
    '''
    Создает новый шарик, i-й по номеру
    '''
    global x, y, r, v_x, v_y, colors
    x[i] = randint(100, 700)
    y[i] = randint(100, 500)
    r[i] = randint(30, 50)
    v_x[i] = randint(-10, +10)
    v_y[i] = randint(-10, +10)
    colors[i] = COLORS[randint(0, 3)]


def generate_new_square(i):
    global x2, y2, r2, v_x2, v_y2, colors2
    x2[i] = randint(0, 1200)
    y2[i] = randint(0, 800)
    r2[i] = randint(50, 150)
    v_x2[i] = randint(-10, +10)
    v_y2[i] = randint(-10, +10)
    colors2[i] = COLORS[randint(4, 6)]


def draw_balls(x, y, r, colors):
    for i in range(num_balls):
        circle(screen, colors[i], (x[i], y[i]), r[i])


def draw_squares(x2, y2, r2, colors2):
    for i in range(num_squares):
        rect(screen, colors2[i], (x2[i], y2[i], r2[i], r2[i]))


def click_handler(event):
    global points
    x1, y1 = event.pos
    click_inside_ball = [r[i]**2>(x[i]-x1)**2+(y[i]-y1)**2 for i in range(num_balls)]
    click_inside_square = [r2[i] + x2[i] > x1 > x2[i] and r2[i] + y2[i] > y1 > y2[i] for i in range(num_squares)]
    for i in range(num_balls):
        if click_inside_ball[i]:
            generate_new_ball(i)
    for i in range(num_squares):
        if click_inside_square[i]:
            generate_new_square(i)
    points += sum(click_inside_ball)+5*sum(click_inside_square)





def check_wall():
    global x, y, r, v_x, v_y, num_balls
    global x2, y2, r2, v_x2, v_y2, num_squares
    hit_right_wall = [1200 - x[i] - r[i] <= v_x[i] and v_x[i] > 0 for i in range(num_balls)]
    hit_left_wall = [x[i] - r[i] <= abs(v_x[i]) and v_x[i] < 0 for i in range(num_balls)]
    hit_upper_wall = [y[i] - r[i] <= abs(v_y[i]) and v_y[i] < 0 for i in range(num_balls)]
    hit_lower_wall = [800 - y[i] - r[i] <= v_y[i] and v_y[i] > 0 for i in range(num_balls)]

    hit_right_wall2 = [1200 - x2[i] - r2[i] <= 2*v_x2[i] and v_x2[i] > 0 for i in range(num_squares)]
    hit_left_wall2 = [x2[i] <= 2*abs(v_x2[i]) and v_x2[i] < 0 for i in range(num_squares)]
    hit_upper_wall2 = [y2[i] <= 2*abs(v_y2[i]) and v_y2[i] < 0 for i in range(num_squares)]
    hit_lower_wall2 = [800 - y2[i] - r2[i] <= 2*v_y2[i] and v_y2[i] > 0 for i in range(num_squares)]

    for i in range(num_balls):
        if hit_right_wall[i] or hit_left_wall[i]:
            v_x[i] *= -1
        if hit_upper_wall[i] or hit_lower_wall[i]:
            v_y[i] *= -1

    for i in range(num_squares):
        if hit_right_wall2[i] or hit_left_wall2[i]:
            v_x2[i] *= -1
        if hit_upper_wall2[i] or hit_lower_wall2[i]:
            v_y2[i] *= -1




def display_points():
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 150)
    textsurface = myfont.render(str(points), False, (200, 200, 200))
    screen.blit(textsurface, (50, 0))


def balls_position_update():
    global x, y, v_x, v_y
    x = [x[i] + v_x[i] for i in range(num_balls)]
    y = [y[i] + v_y[i] for i in range(num_balls)]


def squares_position_update():
    global x2, y2, v_x2, v_y2
    for i in range(num_squares):
        if v_x2[i] > 30:
            v_x2[i] = 5
        if v_y2[i] > 30:
            v_y2[i] = 5
    v_x2 = [v_x2[i]*(randint(499, 503)/500) for i in range(num_squares)]
    v_y2 = [v_y2[i]+(randint(-1, 1)) for i in range(num_squares)]

    x2 = [x2[i] + v_x2[i] for i in range(num_squares)]
    y2 = [y2[i] + v_y2[i] for i in range(num_squares)]


for i in range(num_balls):
    generate_new_ball(i)
for i in range(num_squares):
    generate_new_square(i)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_handler(event)

    check_wall()
    balls_position_update()
    squares_position_update()
    screen.fill(BLACK)
    display_points()
    draw_balls(x, y, r, colors)
    draw_squares(x2, y2, r2, colors2)
    pygame.display.update()

pygame.quit()
