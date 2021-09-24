from random import *
import turtle
from math import sqrt


number_of_turtles = 10
steps_of_time_number = 1000

v = 50.0
eps = 20
border = 200
dt = 0.2
x = [random()*2*border-border for i in range(number_of_turtles)]
y = [random()*2*border-border for i in range(number_of_turtles)]
v_x = [random()*2*v-v for i in range(number_of_turtles)]
v_y = [sqrt(v**2-v_x[i]**2)*(1-(random() > 0.5)*2) for i in range(number_of_turtles)]

t = turtle.Turtle()
t.penup()
t.goto(-border, -border)
t.pendown()
t.goto(border, -border)
t.goto(border, border)
t.goto(-border, border)
t.goto(-border, -border)
pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for time in range(steps_of_time_number):
    for i in range(number_of_turtles):
        for j in range(number_of_turtles):
            if x != j and abs(x[i] - x[j]) < 20 and abs(y[i] - y[j]) < 20:
                temp = v_x[i]
                v_x[i] = v_x[j]
                v_x[j] = temp
                temp = v_y[i]
                v_y[i] = v_y[j]
                v_y[j] = temp

        if abs(abs(x[i])-border) < eps and x[i]*v_x[i] > 0:
            v_x[i] *= (-1)
        if abs(abs(y[i])-border) < eps and y[i]*v_y[i] > 0:
            v_y[i] *= (-1)
        pool[i].penup()
        pool[i].speed(v)
        x[i] += v_x[i]*dt
        y[i] += v_y[i]*dt
    for i in range(number_of_turtles):
        pool[i].goto(x[i], y[i])


