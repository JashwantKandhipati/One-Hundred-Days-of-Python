import turtle as t
import random

tim = t.Turtle()

tim.speed('fastest')
tim.pensize(1)
t.colormode(255)

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

def spirograph(size_gap):
    for _ in range(360 // size_gap):
        tim.color(rand_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)

spirograph(5)






screen = t.Screen()
screen.exitonclick()
