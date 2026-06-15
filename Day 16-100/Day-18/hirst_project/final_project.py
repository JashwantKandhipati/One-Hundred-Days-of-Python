import turtle as t
import random
# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# 10 X 10 spots
# 20 in size, space of 50 paces

def dot_loop():
    for _ in range(10):
        hurst.dot(20, random.choice(color_list))
        hurst.penup()
        hurst.forward(50)
        hurst.pendown()
        hurst.dot(20, random.choice(color_list))

t.colormode(255)
hurst = t.Turtle()
hurst.hideturtle()
hurst.speed("fastest")
color_list = [(222, 232, 225), (208, 161, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (45, 55, 104), (158, 46, 83), (168, 160, 39), (128, 189, 143), (83, 20, 44), (38, 42, 67), (186, 93, 106), (187, 140, 170), (84, 122, 181), (59, 39, 31), (79, 153, 165), (88, 157, 91), (194, 79, 72), (161, 202, 220), (45, 74, 77), (80, 73, 44), (58, 130, 122), (217, 176, 187), (220, 182, 167), (166, 207, 164)]
hurst.penup()
hurst.goto(-250, -200)
hurst.penup()
dot_loop()
for _ in range(4):
    hurst.setheading(90)
    hurst.penup()
    hurst.forward(50)
    hurst.setheading(180)
    dot_loop()

    hurst.setheading(90)
    hurst.penup()
    hurst.forward(50)
    hurst.setheading(360)
    dot_loop()

hurst.setheading(90)
hurst.penup()
hurst.forward(50)
hurst.setheading(180)
dot_loop()






screen = t.Screen()
screen.exitonclick()