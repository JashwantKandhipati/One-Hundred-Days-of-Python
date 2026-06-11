import turtle as t
import random

# increase thickness of line  ✅
# increase the speed of drawing ✅
# make the lines go in random directions a random amount of times 🕛
# use random colors for each line drawn


tim = t.Turtle()
tim.speed('fastest')
tim.pensize(15)
# tim.width(10)
colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple", "medium slate blue", "spring green", "light salmon"]
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.forward(50)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))







screen = t.Screen()
screen.exitonclick()
