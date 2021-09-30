import pygame
from pygame.draw import *
from math import sin
from math import cos
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 500))





rect(screen, (240,240,240), (0, 100, 800, 500))

d = 350

#body
ellipse(screen, 'Dark green', (50, 350, 350, 350))
ellipse(screen, 'Orange', (400, 350, 350, 350))


#head
ellipse(screen, (220, 213, 185), (100, 150, 250, 250))
ellipse(screen, (220, 213, 185), (450, 150, 250, 250))

#eyes
ellipse(screen, 'Grey', (160, 220, 40, 40))
ellipse(screen, 'Black', (160, 220, 40, 40), 1)
ellipse(screen, 'Black', (175, 235, 10, 10))

ellipse(screen, 'Grey', (250, 220, 40, 40))
ellipse(screen, 'Black', (250, 220, 40, 40), 1)
ellipse(screen, 'Black', (265, 235, 10, 10))


ellipse(screen, 'Light blue', (160+d, 220, 40, 40))
ellipse(screen, 'Black', (160+d, 220, 40, 40), 1)
ellipse(screen, 'Black', (175+d, 235, 10, 10))

ellipse(screen, 'Light blue', (250+d, 220, 40, 40))
ellipse(screen, 'Black', (250+d, 220, 40, 40), 1)
ellipse(screen, 'Black', (265+d, 235, 10, 10))


#hands
ellipse(screen, (220, 213, 185), (10, 80, 70, 90))
ellipse(screen, (220, 213, 185), (355, 80, 70, 90))
ellipse(screen, 'White', (10, 80, 70, 90), 1)
ellipse(screen, 'White', (355, 80, 70, 90), 1)
ellipse(screen, (220, 213, 185), (365, 80, 70, 90))
ellipse(screen, (220, 213, 185), (720, 80, 70, 90))
ellipse(screen, 'White', (365, 80, 70, 90), 1)
ellipse(screen, 'White', (720, 80, 70, 90), 1)


#banner
rect(screen, (50,205,50), (0, 0, 800, 110))
font1 = pygame.font.SysFont('chalkduster.ttf', 72)
img1 = font1.render('PYTHON is REALLY AMAZING!', True, 'Black')
screen.blit(img1, (20, 25))



#arms
line(screen, (220, 213, 185), (40, 150), (100, 400), 12)
line(screen, (220, 213, 185), (380, 150), (350, 400), 12)
line(screen, (220, 213, 185), (45+d, 150), (110+d, 400), 12)
line(screen, (220, 213, 185), (405+d, 150), (340+d, 400), 12)


#sleeves
line(screen, (220, 213, 185), (40, 150), (100, 400), 12)
line(screen, (220, 213, 185), (380, 150), (350, 400), 12)
line(screen, (220, 213, 185), (45+d, 150), (110+d, 400), 12)
line(screen, (220, 213, 185), (405+d, 150), (340+d, 400), 12)


#hair
a = 30.0
alpha = 3.14/3.0


def triangle(x1, y1, phi, color):
    x3 = x1 - a*cos(alpha+phi)
    y3 = y1 - a*sin(alpha+phi)
    x2 = x1 - a * cos(phi)
    y2 = y1 - a * sin(phi)
    polygon(screen, color, ((x1, y1), (x2, y2), (x3, y3)))
    polygon(screen, 'Black', ((x1, y1), (x2, y2), (x3, y3)), 1)
    return x2, y2


x1 = 340.0
y1 = 225.0
phi = 3.14/3
for i in range(9):
    x2, y2 = triangle(x1, y1, phi, 'Yellow')
    x1 = x2
    y1 = y2
    phi -= 2*a/250

x1 = 340.0+d
y1 = 225.0
phi = 3.14/3
for i in range(9):
    x2, y2 = triangle(x1, y1, phi, 'Purple')
    x1 = x2
    y1 = y2
    phi -= 2*a/250


#nose
polygon(screen, 'Brown', ((210, 280), (240, 280), (225, 310)))
polygon(screen, 'Brown', ((210+d, 280), (240+d, 280), (225+d, 310)))


#mouth
polygon(screen, 'Red', ((160, 330), (290, 330), (225, 350)))
polygon(screen, 'Red', ((160+d, 330), (290+d, 330), (225+d, 350)))


#sleeves
polygon(screen, 'Dark Green', ((50, 430), (120, 460), (150, 385), (110, 360), (60, 360)))
polygon(screen, 'Black', ((50, 430), (120, 460), (150, 385), (110, 360), (60, 360)), 1)

polygon(screen, 'Orange', ((50+d, 430), (120+d, 460), (150+d, 385), (110+d, 360), (60+d, 360)))
polygon(screen, 'Black', ((50+d, 430), (120+d, 460), (150+d, 385), (110+d, 360), (60+d, 360)), 1)

x = 440
polygon(screen, 'Dark Green', ((x-50, 430), (x-120, 460), (x-150, 385), (x-110, 360), (x-60, 360)))
polygon(screen, 'Black', ((x-50, 430), (x-120, 460), (x-150, 385), (x-110, 360), (x-60, 360)), 1)

polygon(screen, 'Orange', ((x-50+d, 430), (x-120+d, 460), (x-150+d, 385), (x-110+d, 360), (x-60+d, 360)))
polygon(screen, 'Black', ((x-50+d, 430), (x-120+d, 460), (x-150+d, 385), (x-110+d, 360), (x-60+d, 360)), 1)






pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()