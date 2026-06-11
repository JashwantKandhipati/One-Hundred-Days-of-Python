import turtle as t
import random

# increase thickness of line  ✅
# increase the speed of drawing ✅
# make the lines go in random directions a random amount of times 🕛
# use random colors for each line drawn


tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.pensize(15)
# tim.width(10)
def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.forward(50)
    tim.color(rand_color())
    tim.setheading(random.choice(directions))







screen = t.Screen()
screen.exitonclick()
