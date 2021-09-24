import turtle
from math import sqrt


def go1(digit, t1):
    angle = digit[0]
    length = digit[1]
    for i in range(len(angle)):
        t1.left(angle[i])
        t1.forward(length[i])


def next_number(n, t1):
    t1.penup()
    t1.sety(0)
    t1.setx(a*1.5*n-300)
    t1.pendown()

a = 50
leng = [a, a*2, a*sqrt(2)]
t1 = turtle.Turtle("turtle")
t1.shape('turtle')
t1.pencolor('blue')


file = open(file_directory, 'r')
A = file.readlines()
A = [line.rstrip().split() for line in A]
angles = [[int(i) for i in j[::2]] for j in A]
lengths = [[leng[int(i)-1] for i in j[1::2]] for j in A]
digits = [(angles[i], lengths[i]) for i in range(len(angles))]
number = input()
for i in range(len(number)):
    next_number(i+1, t1)
    go1(digits[int(number[i])], t1)
    t1.setheading(0)


