from turtle import Turtle, Screen
import random

screen = Screen()
race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
speed = ["fastest", "fast", "normal", "slow", "slowest"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-230, y=y_pos[turtle])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle wins!")
                race_on = False
            else:
                print(f"You lose! the {winning_color} turtle wins!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
