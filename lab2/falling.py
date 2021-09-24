import turtle
import math

angle_0 = 70.0
v_0 = 100
dt = 0.1
x = -500.0
y = 0.0
g = 9.81
dt = 0.1


t1 = turtle.Turtle("turtle")
t1.shape('turtle')
t1.penup()
t1.goto(x, y)
t1.pendown()


for i in range(100):
    v_0*=0.8
    v_x = math.cos(math.pi * angle_0 / 180.0) * v_0
    v_y = math.sin(math.pi * angle_0 / 180.0) * v_0
    while(not(v_y<0 and y<1)):
        x += v_x*dt
        y += v_y*dt - g*dt**2/2
        v_y -= g*dt
        t1.goto(x, y)
